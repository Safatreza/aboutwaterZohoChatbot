"""
Vector Store Update Script
Automatically updates OpenAI Vector Store with latest knowledge files
"""

import os
import json
from pathlib import Path
from openai import OpenAI
import time


def load_config():
    """Load assistant configuration"""
    config_file = Path(__file__).parent.parent / 'openai-config' / 'assistant-config.json'

    if not config_file.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_file}\n"
            "Please run create_assistant.py first or create the config file manually."
        )

    with open(config_file, 'r') as f:
        config = json.load(f)

    return config


def main():
    """Update vector store with latest knowledge files"""
    print("\n" + "="*60)
    print("Vector Store Update Script")
    print("="*60 + "\n")

    # Load configuration
    try:
        config = load_config()
        vector_store_id = config['openai']['vector_store_id']
        print(f"✅ Configuration loaded")
        print(f"   Vector Store ID: {vector_store_id}")
    except Exception as e:
        print(f"❌ Error loading configuration: {e}")
        return

    # Initialize OpenAI client
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("\n❌ OPENAI_API_KEY environment variable not set")
        print("   Please set it before running this script.")
        return

    client = OpenAI(api_key=api_key)

    # Get knowledge files
    knowledge_dir = Path(__file__).parent.parent / 'knowledge-base'

    if not knowledge_dir.exists():
        print(f"❌ Knowledge base directory not found: {knowledge_dir}")
        return

    md_files = list(knowledge_dir.glob('*.md'))

    if not md_files:
        print(f"❌ No markdown files found in {knowledge_dir}")
        return

    print(f"\n📁 Found {len(md_files)} knowledge files:")
    for file in md_files:
        size_kb = file.stat().st_size / 1024
        print(f"   - {file.name} ({size_kb:.1f} KB)")

    # Confirm update
    print("\n⚠️  This will:")
    print("   1. Delete all existing files in the vector store")
    print("   2. Upload the new knowledge files")
    print("   3. Re-index everything (may take 5-15 minutes)")

    confirm = input("\nContinue? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("\n❌ Update cancelled.")
        return

    print("\n" + "="*60)
    print("Updating Vector Store")
    print("="*60)

    # Step 1: Delete old files
    print("\n[1/3] Deleting old files from vector store...")
    try:
        # List current files in vector store
        vector_store_files = client.beta.vector_stores.files.list(
            vector_store_id=vector_store_id
        )

        file_count = 0
        for vs_file in vector_store_files.data:
            client.beta.vector_stores.files.delete(
                vector_store_id=vector_store_id,
                file_id=vs_file.id
            )
            file_count += 1

        print(f"   ✅ Deleted {file_count} old files")

    except Exception as e:
        print(f"   ⚠️  Warning: Could not delete old files: {e}")
        print("   Continuing with upload...")

    # Step 2: Upload new files
    print("\n[2/3] Uploading new knowledge files...")

    file_streams = []
    try:
        for file_path in md_files:
            file_streams.append(open(file_path, 'rb'))

        # Batch upload and poll for completion
        file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store_id,
            files=file_streams
        )

        print(f"   ✅ Upload complete!")
        print(f"   Status: {file_batch.status}")
        print(f"   File counts: {file_batch.file_counts}")

    except Exception as e:
        print(f"   ❌ Error during upload: {e}")
        return

    finally:
        # Close all file streams
        for stream in file_streams:
            stream.close()

    # Step 3: Verify
    print("\n[3/3] Verifying update...")
    time.sleep(2)

    try:
        vector_store = client.beta.vector_stores.retrieve(vector_store_id)
        print(f"   ✅ Vector store status: {vector_store.status}")
        print(f"   File counts: {vector_store.file_counts}")

    except Exception as e:
        print(f"   ⚠️  Warning: Could not verify: {e}")

    # Update config with timestamp
    config['last_updated'] = time.strftime("%Y-%m-%d %H:%M:%S")

    config_file = Path(__file__).parent.parent / 'openai-config' / 'assistant-config.json'
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    print("\n" + "="*60)
    print("✅ Vector Store Update Complete!")
    print("="*60)
    print("\nNext steps:")
    print("1. Test the assistant in OpenAI Playground")
    print("2. Verify answers reference the new documentation")
    print("3. No changes needed in SalesIQ (automatically uses updated assistant)")
    print("\n")


if __name__ == "__main__":
    main()
