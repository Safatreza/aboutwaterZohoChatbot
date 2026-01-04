"""
OpenAI Assistant Creator
Automates the creation and configuration of the Zoho Assistant
"""

import os
import json
from pathlib import Path
from openai import OpenAI
from typing import List, Dict
import time


class ZohoAssistantCreator:
    """
    Creates and configures OpenAI Assistant for Zoho documentation
    """

    def __init__(self, api_key: str = None):
        """
        Initialize with OpenAI API key

        Args:
            api_key: OpenAI API key. If None, reads from environment variable OPENAI_API_KEY
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')

        if not self.api_key:
            raise ValueError(
                "OpenAI API key required. Set OPENAI_API_KEY environment variable or pass as parameter."
            )

        self.client = OpenAI(api_key=self.api_key)
        self.config_dir = Path(__file__).parent
        self.knowledge_base_dir = self.config_dir.parent / 'knowledge-base'

    def load_system_prompt(self) -> str:
        """Load system prompt from file"""
        prompt_file = self.config_dir / 'system-prompt.txt'

        if not prompt_file.exists():
            raise FileNotFoundError(f"System prompt not found: {prompt_file}")

        with open(prompt_file, 'r', encoding='utf-8') as f:
            return f.read()

    def get_knowledge_files(self) -> List[Path]:
        """Get list of knowledge base files"""
        if not self.knowledge_base_dir.exists():
            print(f"Warning: Knowledge base directory not found: {self.knowledge_base_dir}")
            return []

        markdown_files = list(self.knowledge_base_dir.glob('zoho-*.md'))

        # Also include aboutwater-specific files if they exist
        custom_files = list(self.knowledge_base_dir.glob('aboutwater-*.md'))

        all_files = markdown_files + custom_files

        print(f"\nFound {len(all_files)} knowledge files:")
        for file in all_files:
            file_size = file.stat().st_size / 1024  # KB
            print(f"  - {file.name} ({file_size:.1f} KB)")

        return all_files

    def create_vector_store(self, file_paths: List[Path]) -> str:
        """
        Create vector store and upload files

        Returns:
            vector_store_id: ID of created vector store
        """
        print("\n" + "="*60)
        print("Creating Vector Store")
        print("="*60)

        # Create vector store
        vector_store = self.client.beta.vector_stores.create(
            name="zoho-knowledge-base",
            metadata={
                "project": "aboutwater-zoho-chatbot",
                "version": "1.0"
            }
        )

        print(f"\n✅ Vector store created: {vector_store.id}")

        if not file_paths:
            print("⚠️  No files to upload")
            return vector_store.id

        # Upload files
        print(f"\nUploading {len(file_paths)} files...")

        file_streams = []
        try:
            for file_path in file_paths:
                if file_path.stat().st_size > 512 * 1024 * 1024:  # 512MB limit
                    print(f"   ⚠️  Skipping {file_path.name} (too large: {file_path.stat().st_size / 1024 / 1024:.1f}MB)")
                    continue
                file_streams.append(open(file_path, 'rb'))

            if not file_streams:
                print("   ⚠️  No valid files to upload")
                return vector_store.id

            # Batch upload with progress indication
            print(f"   Uploading {len(file_streams)} files (this may take a few minutes)...")
            file_batch = self.client.beta.vector_stores.file_batches.upload_and_poll(
                vector_store_id=vector_store.id,
                files=file_streams
            )

            print(f"\n✅ Upload complete!")
            print(f"   Status: {file_batch.status}")
            print(f"   File counts: {file_batch.file_counts}")

            if file_batch.status != 'completed':
                print(f"   ⚠️  Warning: Upload batch status is {file_batch.status}")

        except Exception as e:
            print(f"   ❌ Error during upload: {str(e)}")
            raise
        finally:
            # Close all file streams
            for stream in file_streams:
                try:
                    stream.close()
                except:
                    pass

        return vector_store.id

    def create_assistant(self, vector_store_id: str, model: str = "gpt-4o") -> Dict:
        """
        Create OpenAI Assistant with configuration

        Args:
            vector_store_id: ID of vector store with knowledge files
            model: OpenAI model to use (default: gpt-4o)

        Returns:
            dict: Assistant configuration including ID
        """
        print("\n" + "="*60)
        print("Creating OpenAI Assistant")
        print("="*60)

        # Load system prompt
        instructions = self.load_system_prompt()
        print(f"\n✅ System prompt loaded ({len(instructions)} characters)")

        # Create assistant
        assistant = self.client.beta.assistants.create(
            name="aboutwater_Zoho_Assistant",
            instructions=instructions,
            model=model,
            tools=[{"type": "file_search"}],
            tool_resources={
                "file_search": {
                    "vector_store_ids": [vector_store_id]
                }
            },
            temperature=0.3,
            metadata={
                "project": "aboutwater-zoho-chatbot",
                "version": "1.0",
                "language": "de"
            }
        )

        print(f"\n✅ Assistant created successfully!")
        print(f"\n{'='*60}")
        print("Assistant Details")
        print("="*60)
        print(f"ID:          {assistant.id}")
        print(f"Name:        {assistant.name}")
        print(f"Model:       {assistant.model}")
        print(f"Tools:       {[tool.type for tool in assistant.tools]}")
        print(f"Vector Store: {vector_store_id}")
        print("="*60)

        return {
            "assistant_id": assistant.id,
            "vector_store_id": vector_store_id,
            "model": model,
            "name": assistant.name
        }

    def save_configuration(self, config: Dict):
        """Save assistant configuration to file"""
        config_file = self.config_dir / 'assistant-config.json'

        full_config = {
            "openai": {
                "assistant_id": config["assistant_id"],
                "vector_store_id": config["vector_store_id"],
                "model": config["model"],
                "name": config["name"]
            },
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "version": "1.0",
            "project": "aboutwater-zoho-chatbot"
        }

        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(full_config, f, indent=2, ensure_ascii=False)

        print(f"\n✅ Configuration saved to: {config_file}")

        # Also save just the assistant ID for quick reference
        id_file = self.config_dir / 'assistant-id.txt'
        with open(id_file, 'w') as f:
            f.write(config["assistant_id"])

        print(f"✅ Assistant ID saved to: {id_file}")

    def test_assistant(self, assistant_id: str):
        """Test the assistant with sample questions"""
        print("\n" + "="*60)
        print("Testing Assistant")
        print("="*60)

        test_questions = [
            "Wie lege ich einen neuen Kontakt in Zoho CRM an?",
            "Wie erstelle ich eine Rechnung in Zoho Books?",
            "Was ist Zoho SalesIQ?"
        ]

        for i, question in enumerate(test_questions, 1):
            print(f"\n{'─'*60}")
            print(f"Test {i}: {question}")
            print('─'*60)

            # Create thread
            thread = self.client.beta.threads.create()

            # Add message
            self.client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=question
            )

            # Run assistant
            run = self.client.beta.threads.runs.create_and_poll(
                thread_id=thread.id,
                assistant_id=assistant_id
            )

            if run.status == 'completed':
                # Get response
                messages = self.client.beta.threads.messages.list(
                    thread_id=thread.id
                )

                response = messages.data[0].content[0].text.value
                print(f"\n{response}\n")
            else:
                print(f"❌ Run failed: {run.status}")

        print("="*60)
        print("Testing complete!")
        print("="*60)

    def create_full_setup(self, model: str = "gpt-4o", test: bool = True) -> Dict:
        """
        Complete setup: create vector store, upload files, create assistant

        Args:
            model: OpenAI model to use
            test: Whether to run test questions

        Returns:
            dict: Complete configuration
        """
        print("\n" + "🤖 " + "="*58)
        print("OpenAI Assistant Setup for aboutwater Zoho Chatbot")
        print("="*60 + "\n")

        # Step 1: Get knowledge files
        knowledge_files = self.get_knowledge_files()

        if not knowledge_files:
            print("\n⚠️  Warning: No knowledge files found!")
            print("The assistant will be created but won't have access to documentation.")
            print("Run the crawler first to generate knowledge files.\n")

            response = input("Continue anyway? (y/n): ").strip().lower()
            if response != 'y':
                print("Setup cancelled.")
                return None

        # Step 2: Create vector store and upload files
        vector_store_id = self.create_vector_store(knowledge_files)

        # Step 3: Create assistant
        config = self.create_assistant(vector_store_id, model)

        # Step 4: Save configuration
        self.save_configuration(config)

        # Step 5: Test (optional)
        if test and knowledge_files:
            test_response = input("\nRun test queries? (y/n): ").strip().lower()
            if test_response == 'y':
                self.test_assistant(config["assistant_id"])

        print("\n" + "="*60)
        print("✅ Setup Complete!")
        print("="*60)
        print("\nNext steps:")
        print("1. Copy the Assistant ID to SalesIQ configuration")
        print("2. Configure SalesIQ Zobot (see ../salesiq-bot/integration-guide.md)")
        print("3. Test the chatbot in SalesIQ")
        print("\nAssistant ID:", config["assistant_id"])
        print("="*60 + "\n")

        return config


def main():
    """Main execution"""
    print("\n" + "="*60)
    print("OpenAI Assistant Creator")
    print("="*60)

    # Check for API key
    api_key = os.getenv('OPENAI_API_KEY')

    if not api_key:
        print("\n⚠️  OpenAI API Key not found in environment!")
        print("\nPlease set your API key:")
        print("  export OPENAI_API_KEY='sk-proj-...'  (Linux/Mac)")
        print("  set OPENAI_API_KEY=sk-proj-...       (Windows CMD)")
        print("  $env:OPENAI_API_KEY='sk-proj-...'    (Windows PowerShell)")

        manual_key = input("\nOr enter your API key now: ").strip()
        if manual_key:
            api_key = manual_key
        else:
            print("\nSetup cancelled.")
            return

    # Create assistant creator
    creator = ZohoAssistantCreator(api_key=api_key)

    # Model selection
    print("\nSelect OpenAI model:")
    print("1. gpt-4o (recommended - best quality)")
    print("2. gpt-4o-mini (cheaper - good quality)")

    model_choice = input("\nEnter choice (1-2, default 1): ").strip()
    model = "gpt-4o-mini" if model_choice == "2" else "gpt-4o"

    print(f"\nSelected model: {model}")

    # Run setup
    config = creator.create_full_setup(model=model, test=True)

    if config:
        print("\n🎉 All done! Your assistant is ready to use.")


if __name__ == "__main__":
    main()
