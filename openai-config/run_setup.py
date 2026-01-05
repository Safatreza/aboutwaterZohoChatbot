#!/usr/bin/env python3
"""
Quick setup script with embedded API key
"""
import os

# Set API key
os.environ['OPENAI_API_KEY'] = 'YOUR_API_KEY_HERE'

# Import and run main setup
from create_assistant import ZohoAssistantCreator

print("Starting OpenAI Assistant setup with API key...")
print("="*60)

# Create assistant creator
creator = ZohoAssistantCreator()

# Use gpt-4o for best quality
print("\nUsing model: gpt-4o (best quality)")

# Run full setup without interactive prompts
config = creator.create_full_setup(model="gpt-4o", test=False)

if config:
    print("\n" + "="*60)
    print("SUCCESS! OpenAI Assistant is ready!")
    print("="*60)
    print(f"\nAssistant ID: {config['assistant_id']}")
    print(f"Vector Store ID: {config['vector_store_id']}")
    print(f"Model: {config['model']}")
    print("\nConfiguration saved to: assistant-config.json")
    print("Assistant ID saved to: assistant-id.txt")
    print("\nNext: Configure this Assistant ID in Zoho SalesIQ")
    print("="*60)
else:
    print("\nSetup failed!")
