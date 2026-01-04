# Quick Start Guide
## aboutwater Zoho AI Chatbot - In 30 Minuten einsatzbereit

Dieser Guide bringt Sie in 30 Minuten zum laufenden Chatbot.

---

## Voraussetzungen (5 Minuten)

### ✅ Checkliste

```
☐ Python 3.8+ installiert (python --version)
☐ OpenAI Account erstellt (platform.openai.com)
☐ OpenAI API Key generiert
☐ Zahlungsmethode in OpenAI hinterlegt
☐ Zugang zu Zoho SalesIQ (Admin-Rechte)
```

### Kosten

- **Setup:** €0
- **Monatlich:** ~€50-100 (OpenAI API + SalesIQ)
- **ROI:** ~€1.150/Monat Ersparnis

---

## Schritt 1: Projekt Setup (5 Minuten)

### Windows

```powershell
# Navigiere zum Projektordner
cd "D:\AboutWater_GmbH\Zoho Chatbot\zoho-chatbot-project"

# Python Virtual Environment erstellen (optional)
python -m venv venv
.\venv\Scripts\activate

# Dependencies installieren
cd crawlers
pip install -r requirements.txt
```

### Linux/Mac

```bash
cd "/path/to/zoho-chatbot-project"
python3 -m venv venv
source venv/bin/activate
cd crawlers
pip install -r requirements.txt
```

---

## Schritt 2: Zoho Dokumentation crawlen (10 Minuten)

```bash
# Im crawlers/ Verzeichnis
python zoho_documentation_crawler.py
```

**Interaktive Eingabe:**
```
Select crawl mode:
1. Crawl all products (recommended)  ← WÄHLEN
2. Crawl specific product
3. Test crawl (10 pages per product)

Enter choice (1-3): 1

Max pages per product (default 100): 50  ← FÜR QUICK START
```

**Dauer:** ~10 Minuten (50 Seiten pro Produkt)

**Ergebnis:**
```
knowledge-base/
├── zoho-crm.md ✅
├── zoho-books.md ✅
├── zoho-inventory.md ✅
├── zoho-sign.md ✅
└── ...
```

---

## Schritt 3: OpenAI Assistant erstellen (10 Minuten)

### 3.1 API Key setzen

**Windows PowerShell:**
```powershell
$env:OPENAI_API_KEY="sk-proj-xxxxxxxxxxxxx"
```

**Windows CMD:**
```cmd
set OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY="sk-proj-xxxxxxxxxxxxx"
```

### 3.2 Assistant erstellen

```bash
cd ../openai-config
pip install -r requirements.txt
python create_assistant.py
```

**Interaktive Eingabe:**
```
Select OpenAI model:
1. gpt-4o (recommended - best quality)  ← FÜR PRODUCTION
2. gpt-4o-mini (cheaper - good quality) ← FÜR TESTING

Enter choice (1-2, default 1): 2  ← QUICK START: MINI

[... Upload läuft ...]

✅ Assistant created successfully!
Assistant ID: asst_abc123xyz  ← KOPIEREN!
```

**⚠️ WICHTIG:** Kopiere die Assistant ID! Du brauchst sie gleich.

### 3.3 Test im Playground (optional)

1. Gehe zu [platform.openai.com/playground](https://platform.openai.com/playground)
2. Wähle deinen Assistant aus
3. Stelle Testfrage: "Wie lege ich einen Kontakt in Zoho CRM an?"
4. Überprüfe: Antwort auf Deutsch ✅

---

## Schritt 4: SalesIQ Integration (5 Minuten)

### 4.1 OpenAI mit SalesIQ verbinden

1. Öffne [salesiq.zoho.eu](https://salesiq.zoho.eu)
2. **Settings** → **Integrations** → **AI** → **OpenAI**
3. Klicke **Connect**
4. API Key eingeben: `sk-proj-xxxxxxxxxxxxx`
5. **Save**
6. Status: ✅ Connected

### 4.2 Zobot erstellen (Codeless)

1. **Settings** → **Bots** → **Zobot** → **+ Add Bot**
2. **Codeless Bot Builder** wählen
3. Name: `aboutwater Zoho Assistant`

### 4.3 Bot Flow (Schnellversion)

**Card 1: Message**
```
Hallo! Ich bin der Zoho-Assistent. Wie kann ich dir helfen?
```

**Card 2: Question**
```
Prompt: Stelle deine Frage
Variable: user_question
```

**Card 3: ChatGPT Assistant**
```
Integration: OpenAI
Assistant: [Wähle deinen Assistant]
Input: ${user_question}
Response Variable: assistant_response
```

**Card 4: Message**
```
${assistant_response}
```

**Card 5: Quick Replies**
```
Buttons:
- "Weitere Frage" → Loop zu Card 2
- "Mit Mitarbeiter sprechen" → Transfer to Operator
```

### 4.4 Aktivieren

1. **Save**
2. **Preview** → Teste den Bot
3. **Activate**
4. **Assign to Brand** → aboutwater
5. **Deploy** → Website, Zoho Apps

---

## Fertig! 🎉

Der Bot ist jetzt live!

### Teste es:

1. Öffne eine Zoho App (z.B. CRM)
2. Rechts unten sollte Chat-Widget erscheinen
3. Klicke drauf
4. Stelle eine Frage: "Wie erstelle ich einen Kontakt?"

### Erwartetes Ergebnis:

```
Bot: Hallo! Ich bin der Zoho-Assistent. Wie kann ich dir helfen?

Du: Wie erstelle ich einen Kontakt?

Bot: Ich helfe dir gerne dabei, einen neuen Kontakt in Zoho CRM anzulegen!

So erstellst du einen neuen Kontakt:
1. Melde dich bei Zoho CRM an
2. Klicke in der oberen Navigation auf 'Kontakte'
3. Klicke rechts oben auf den Button '+ Neuer Kontakt'
...

Kann ich dir noch anders helfen?
```

---

## Nächste Schritte

### Sofort:

- ✅ Bot ist live
- ✅ Mitarbeiter können ihn nutzen
- ✅ Du bist fertig!

### Optional (später):

1. **Interne Dokumente hinzufügen**
   - Erstelle `knowledge-base/aboutwater-workflows.md`
   - Update Vector Store (siehe README)

2. **Rollout ankündigen**
   - Email an Team senden
   - User Guide teilen: `docs/user-guide.md`

3. **Monitoring einrichten**
   - SalesIQ Dashboard checken
   - Weekly Reports aktivieren

4. **Optimieren**
   - System Prompt anpassen
   - Bot Flow verbessern
   - Mehr Features hinzufügen

---

## Troubleshooting

### Bot antwortet nicht

**Check 1:** OpenAI Integration
```
SalesIQ → Settings → Integrations → OpenAI
Status: Connected? ✅
```

**Check 2:** Assistant ID
```
Bot Flow → Card 3 (ChatGPT)
Assistant: Richtige ID? asst_xxxxx
```

**Check 3:** API Key valid?
```
OpenAI Platform → Usage
Sieht du Requests? ✅
```

### Antworten auf Englisch

**Fix:**
1. OpenAI Platform → Assistants → Dein Assistant
2. Instructions → Ganz oben hinzufügen:
   ```
   SPRACHE: DEUTSCH
   KRITISCH: Antworte AUSSCHLIESSLICH auf Deutsch!
   ```
3. Save

### Zu hohe Kosten

**Fix:**
```bash
cd openai-config
# Bearbeite create_assistant.py
# Ändere model="gpt-4o" zu model="gpt-4o-mini"
# Erstelle neuen Assistant
python create_assistant.py
# Update Assistant ID in SalesIQ
```

---

## Support

**Fragen?**
- 📖 Lies die vollständige Dokumentation: `README.md`
- 📧 Email: it-support@aboutwater.de
- 📚 Detaillierte Guides in `docs/`

---

## Kosten-Übersicht

### Quick Start Setup (gpt-4o-mini)

```
Monat 1:
- OpenAI (100 Conversations): ~€5
- SalesIQ: €0 (in Zoho One)
Total: ~€5

Monat 2+ (normale Nutzung):
- OpenAI (1.000 Conversations): ~€25
- SalesIQ: €0
Total: ~€25/Monat

ROI:
Ersetzte IT-Tickets: ~50/Monat
Ersparnis: 50 × 15min × €50/h = €625
Net Savings: €625 - €25 = €600/Monat
```

---

## Was du jetzt hast

✅ Funktionierender AI Chatbot
✅ Integration in Zoho SalesIQ
✅ Knowledge Base mit Zoho Docs
✅ 24/7 verfügbar
✅ Deutsch optimiert
✅ Einsatzbereit für alle Mitarbeiter

**Zeit investiert:** 30 Minuten
**Monatliche Ersparnis:** ~€600-1.000

🎉 **Herzlichen Glückwunsch!**

---

**Erstellt:** Januar 2026
**Projekt:** aboutwater Zoho AI Chatbot
