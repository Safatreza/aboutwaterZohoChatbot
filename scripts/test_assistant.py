"""
Assistant Testing Script
Interactive testing tool for the OpenAI Assistant
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
            "Please run create_assistant.py first."
        )

    with open(config_file, 'r') as f:
        return json.load(f)


class AssistantTester:
    """Interactive assistant testing"""

    def __init__(self, assistant_id: str, client: OpenAI):
        self.assistant_id = assistant_id
        self.client = client
        self.thread_id = None

    def create_thread(self):
        """Create new conversation thread"""
        thread = self.client.beta.threads.create()
        self.thread_id = thread.id
        print(f"✅ New thread created: {self.thread_id}\n")

    def ask_question(self, question: str) -> str:
        """Ask a question and get response"""

        if not self.thread_id:
            self.create_thread()

        print(f"\n{'─'*60}")
        print(f"Frage: {question}")
        print('─'*60)

        try:
            # Add message to thread
            self.client.beta.threads.messages.create(
                thread_id=self.thread_id,
                role="user",
                content=question
            )

            # Run assistant
            print("⏳ Assistant denkt nach...")
            start_time = time.time()

            run = self.client.beta.threads.runs.create_and_poll(
                thread_id=self.thread_id,
                assistant_id=self.assistant_id,
                timeout=60  # 60 second timeout
            )

            elapsed_time = time.time() - start_time

            if run.status == 'completed':
                # Get response
                messages = self.client.beta.threads.messages.list(
                    thread_id=self.thread_id
                )

                response = messages.data[0].content[0].text.value

                print(f"\n✅ Antwort (in {elapsed_time:.1f}s):\n")
                print(response)
                print("\n" + "─"*60)

                return response

            elif run.status == 'failed':
                print(f"\n❌ Run failed: {run.last_error if hasattr(run, 'last_error') else 'Unknown error'}")
                return None
            else:
                print(f"\n❌ Run ended with status: {run.status}")
                return None

        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            return None

    def run_test_suite(self):
        """Run predefined test questions"""

        test_questions = [
            {
                "category": "Einfache CRM Frage",
                "question": "Wie lege ich einen neuen Kontakt in Zoho CRM an?"
            },
            {
                "category": "Komplexe Books Frage",
                "question": "Wie erstelle ich eine Rechnung in Zoho Books und sende sie per E-Mail?"
            },
            {
                "category": "Inventory Frage",
                "question": "Wie tracke ich Lagerbestände in Zoho Inventory?"
            },
            {
                "category": "Allgemeine Frage",
                "question": "Was ist der Unterschied zwischen einem Lead und einem Kontakt?"
            },
            {
                "category": "Sign Frage",
                "question": "Wie sende ich ein Dokument zur Unterschrift mit Zoho Sign?"
            }
        ]

        print("\n" + "="*60)
        print("Running Test Suite")
        print("="*60)

        results = []

        for i, test in enumerate(test_questions, 1):
            print(f"\n\n{'='*60}")
            print(f"Test {i}/{len(test_questions)}: {test['category']}")
            print("="*60)

            response = self.ask_question(test['question'])

            # Basic validation
            passed = True
            issues = []

            if not response:
                passed = False
                issues.append("Keine Antwort erhalten")
            else:
                # Check for German language
                if any(word in response.lower() for word in ['the', 'how to', 'please', 'step by step']):
                    if not any(word in response for word in ['Schritt', 'wie', 'klicke', 'öffne']):
                        issues.append("Antwort scheint nicht auf Deutsch zu sein")
                        passed = False

                # Check for step-by-step format
                if '1.' not in response and '1)' not in response:
                    issues.append("Keine Schritt-für-Schritt Nummerierung gefunden")
                    passed = False

                # Check for follow-up question
                if 'kann ich' not in response.lower() and 'helfen' not in response.lower():
                    issues.append("Keine Rückfrage am Ende")

            results.append({
                'category': test['category'],
                'passed': passed,
                'issues': issues
            })

            # Pause between tests
            if i < len(test_questions):
                time.sleep(2)

        # Print summary
        print("\n\n" + "="*60)
        print("Test Summary")
        print("="*60)

        passed_count = sum(1 for r in results if r['passed'])
        total_count = len(results)

        print(f"\nPassed: {passed_count}/{total_count}")

        for i, result in enumerate(results, 1):
            status = "✅ PASS" if result['passed'] else "❌ FAIL"
            print(f"\n{i}. {result['category']}: {status}")
            if result['issues']:
                for issue in result['issues']:
                    print(f"   ⚠️  {issue}")

        print("\n" + "="*60 + "\n")

    def interactive_mode(self):
        """Interactive Q&A mode"""

        print("\n" + "="*60)
        print("Interactive Testing Mode")
        print("="*60)
        print("\nGib deine Fragen ein (oder 'exit' zum Beenden)")
        print("Befehle:")
        print("  'exit' - Beenden")
        print("  'new' - Neuen Thread starten")
        print("  'test' - Test Suite ausführen")
        print("\n")

        while True:
            try:
                question = input("Frage: ").strip()

                if not question:
                    continue

                if question.lower() == 'exit':
                    print("\n👋 Auf Wiedersehen!")
                    break

                elif question.lower() == 'new':
                    self.create_thread()
                    continue

                elif question.lower() == 'test':
                    self.run_test_suite()
                    continue

                self.ask_question(question)

            except KeyboardInterrupt:
                print("\n\n👋 Auf Wiedersehen!")
                break


def main():
    """Main execution"""

    print("\n" + "="*60)
    print("OpenAI Assistant Testing Tool")
    print("="*60)

    # Load configuration
    try:
        config = load_config()
        assistant_id = config['openai']['assistant_id']
        print(f"\n✅ Configuration loaded")
        print(f"   Assistant ID: {assistant_id}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return

    # Initialize OpenAI client
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("\n❌ OPENAI_API_KEY environment variable not set")
        return

    client = OpenAI(api_key=api_key)

    # Create tester
    tester = AssistantTester(assistant_id, client)

    # Menu
    print("\nSelect mode:")
    print("1. Interactive mode (ask questions freely)")
    print("2. Run test suite (predefined questions)")
    print("3. Both (test suite first, then interactive)")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        tester.interactive_mode()

    elif choice == "2":
        tester.run_test_suite()

    elif choice == "3":
        tester.run_test_suite()
        print("\nStarting interactive mode...\n")
        time.sleep(2)
        tester.interactive_mode()

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
