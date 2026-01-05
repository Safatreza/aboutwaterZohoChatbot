#!/usr/bin/env python3
"""
Simplified OpenAI Assistant Setup
Creates assistant and uploads all knowledge base files
"""
import os
import json
from pathlib import Path
from openai import OpenAI

# Set API key
API_KEY = 'YOUR_API_KEY_HERE'
os.environ['OPENAI_API_KEY'] = API_KEY

print("="*60)
print("aboutwater Zoho AI Assistant - Simplified Setup")
print("="*60)

# Initialize client
client = OpenAI(api_key=API_KEY)
print("\n[1/5] OpenAI client initialized")

# Get knowledge base files
kb_dir = Path(__file__).parent.parent / 'knowledge-base'
manual_files = list(kb_dir.glob('*.md'))
crawled_dir = kb_dir / 'crawled'
crawled_files = list(crawled_dir.glob('*.md')) if crawled_dir.exists() else []

all_files = manual_files + crawled_files
all_files = [f for f in all_files if f.name.lower() != 'readme.md']

print(f"\n[2/5] Found {len(all_files)} knowledge files")
print(f"      Manual: {len(manual_files)}, Crawled: {len(crawled_files)}")

# Load system prompt
prompt_file = Path(__file__).parent / 'system-prompt.txt'
with open(prompt_file, 'r', encoding='utf-8') as f:
    system_prompt = f.read()

print(f"\n[3/5] System prompt loaded ({len(system_prompt)} chars)")

# Upload files to OpenAI
print(f"\n[4/5] Uploading {len(all_files)} files to OpenAI...")
print("      This may take several minutes...")

uploaded_file_ids = []
for i, file_path in enumerate(all_files, 1):
    try:
        with open(file_path, 'rb') as f:
            file_obj = client.files.create(
                file=f,
                purpose='assistants'
            )
            uploaded_file_ids.append(file_obj.id)
            if i % 10 == 0:
                print(f"      Uploaded {i}/{len(all_files)} files...")
    except Exception as e:
        print(f"      Warning: Failed to upload {file_path.name}: {e}")

print(f"\n      Successfully uploaded {len(uploaded_file_ids)} files")

# Create assistant
print(f"\n[5/5] Creating OpenAI Assistant...")

assistant = client.beta.assistants.create(
    name="aboutwater_Zoho_Assistant",
    instructions=system_prompt,
    model="gpt-4o",
    tools=[{"type": "file_search"}],
    tool_resources={
        "file_search": {
            "vector_stores": [{
                "file_ids": uploaded_file_ids
            }]
        }
    },
    temperature=0.3
)

print("\n" + "="*60)
print("SUCCESS! Assistant Created")
print("="*60)
print(f"\nAssistant ID: {assistant.id}")
print(f"Name: {assistant.name}")
print(f"Model: {assistant.model}")
print(f"Files uploaded: {len(uploaded_file_ids)}")

# Save configuration
config = {
    "openai": {
        "assistant_id": assistant.id,
        "model": assistant.model,
        "name": assistant.name,
        "files_uploaded": len(uploaded_file_ids)
    },
    "created_at": "2026-01-05",
    "version": "1.0",
    "project": "aboutwater-zoho-chatbot"
}

config_file = Path(__file__).parent / 'assistant-config.json'
with open(config_file, 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

id_file = Path(__file__).parent / 'assistant-id.txt'
with open(id_file, 'w') as f:
    f.write(assistant.id)

print(f"\nConfiguration saved to: {config_file}")
print(f"Assistant ID saved to: {id_file}")

print("\n" + "="*60)
print("NEXT STEPS:")
print("="*60)
print("1. Copy the Assistant ID above")
print("2. Open Zoho SalesIQ")
print("3. Go to: Settings → Integrations → AI → OpenAI")
print("4. Connect with your API key")
print("5. Create a Zobot and add ChatGPT Assistant card")
print("6. Paste the Assistant ID in the card")
print("7. Test and deploy!")
print("="*60)
