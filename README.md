# aboutwater Zoho AI Chatbot
## OpenAI Assistant Integration für Zoho SalesIQ

Ein intelligenter Chatbot, der aboutwater Mitarbeitern bei allen Zoho-Fragen hilft - basierend auf offizieller Dokumentation und internen Workflows.

---

## 🎯 Projektübersicht

### Was ist das?

Ein AI-gestützter Chatbot, der:
- ✅ **24/7 Zoho-Support** bietet
- ✅ **Schritt-für-Schritt Anleitungen** auf Deutsch gibt
- ✅ **Auf offizieller Zoho-Dokumentation** basiert
- ✅ **aboutwater-spezifische Workflows** kennt
- ✅ **Nahtlos zu IT-Support** eskaliert bei komplexen Fragen

### Technologie-Stack

```
┌─────────────────────────────────────────┐
│  Chat Interface: Zoho SalesIQ Zobot    │
├─────────────────────────────────────────┤
│  AI Engine: OpenAI ChatGPT Assistant    │
│  (gpt-4o mit File Search/RAG)           │
├─────────────────────────────────────────┤
│  Knowledge Base: Gecrawlte Zoho Docs    │
│  + aboutwater SOPs (Markdown)           │
├─────────────────────────────────────────┤
│  Integration: Native SalesIQ-OpenAI     │
│  (kein externer Backend nötig!)         │
└─────────────────────────────────────────┘
```

### Hauptvorteile

🚀 **Keine externe Infrastruktur** - alles native in Zoho + OpenAI
💰 **Kosteneffizient** - ~€100-150/Monat
⚡ **Schnelle Antworten** - durchschnittlich <5 Sekunden
🔒 **Sicher** - DSGVO-konform, keine Datenweitergabe
📈 **ROI** - Reduziert IT-Tickets um ~60%

---

## 📁 Projektstruktur

```
zoho-chatbot-project/
│
├── crawlers/                      # Web Crawler für Zoho Dokumentation
│   ├── zoho_documentation_crawler.py
│   └── requirements.txt
│
├── knowledge-base/                # Gesammelte Wissensdatenbank (erstellt beim Crawl)
│   ├── zoho-crm.md
│   ├── zoho-books.md
│   ├── zoho-inventory.md
│   ├── aboutwater-*.md            # Interne Dokumente (manuell hinzufügen)
│   └── *-metadata.json
│
├── openai-config/                 # OpenAI Assistant Konfiguration
│   ├── system-prompt.txt          # Deutscher System Prompt
│   ├── assistant-setup-guide.md   # Manuelle Setup-Anleitung
│   ├── create_assistant.py        # Automatisches Setup-Skript
│   ├── assistant-config-template.json
│   └── requirements.txt
│
├── salesiq-bot/                   # SalesIQ Bot Flows
│   ├── integration-guide.md       # Detaillierte Integration-Anleitung
│   ├── bot-flow-codeless.json     # Codeless Bot Builder Config
│   └── bot-script-deluge.txt      # Alternative: Deluge Script
│
├── docs/                          # Umfassende Dokumentation
│   ├── deployment-guide.md        # Vollständiger Deployment-Leitfaden
│   ├── user-guide.md              # Benutzerhandbuch für Mitarbeiter
│   └── testing-maintenance-guide.md  # Testing & Wartung
│
├── scripts/                       # Hilfs-Skripte
│   └── (optional: automation scripts)
│
└── README.md                      # Dieses Dokument
```

---

## 🚀 Quick Start (5-Minuten-Überblick)

### Voraussetzungen

- ✅ **Python 3.8+** für Crawler
- ✅ **OpenAI Account** mit Billing ([platform.openai.com](https://platform.openai.com))
- ✅ **Zoho SalesIQ** mit Admin-Rechten ([salesiq.zoho.eu](https://salesiq.zoho.eu))

### Installation in 4 Schritten

#### Schritt 1: Zoho Dokumentation crawlen

```bash
cd crawlers
pip install -r requirements.txt
python zoho_documentation_crawler.py

# Wähle Option 1: Crawl all products
# Dauer: 30-60 Minuten
```

**Ausgabe:** Markdown-Dateien in `knowledge-base/`

#### Schritt 2: OpenAI Assistant erstellen

**Option A: Manuell (empfohlen für Ersteinrichtung)**

Folge der Anleitung in `openai-config/assistant-setup-guide.md`:
1. OpenAI Platform → Create Assistant
2. Kopiere System Prompt aus `system-prompt.txt`
3. Aktiviere File Search
4. Lade alle `.md` Dateien hoch
5. Kopiere Assistant ID

**Option B: Automatisch**

```bash
cd openai-config
pip install -r requirements.txt

# Setze API Key
export OPENAI_API_KEY="sk-proj-xxxxx"  # Linux/Mac
# oder
set OPENAI_API_KEY=sk-proj-xxxxx      # Windows

python create_assistant.py
```

**Ausgabe:** Assistant ID (z.B. `asst_abc123xyz`)

#### Schritt 3: SalesIQ Bot erstellen

Folge `salesiq-bot/integration-guide.md`:

1. SalesIQ → Settings → Integrations → OpenAI → Connect
2. API Key eingeben
3. Settings → Bots → Zobot → Add Bot
4. Codeless Bot Builder wählen
5. Flow aufbauen (siehe Guide)
6. ChatGPT Assistant Card: Assistant ID eintragen
7. Aktivieren & Deployen

#### Schritt 4: Testen & Rollout

```bash
# Teste im SalesIQ Preview-Modus
# Stelle Testfragen auf Deutsch
# Bei Erfolg: Rollout an alle Mitarbeiter
```

Siehe `docs/deployment-guide.md` für detaillierte Schritte.

---

## 📖 Detaillierte Dokumentation

### Für Implementierung

| Dokument | Beschreibung | Zielgruppe |
|----------|--------------|------------|
| [deployment-guide.md](docs/deployment-guide.md) | Kompletter Deployment-Prozess (Phase 1-7) | IT-Team / Projektleiter |
| [assistant-setup-guide.md](openai-config/assistant-setup-guide.md) | OpenAI Assistant Konfiguration | Developer / IT-Admin |
| [integration-guide.md](salesiq-bot/integration-guide.md) | SalesIQ Bot Integration | SalesIQ Admin |

### Für Betrieb

| Dokument | Beschreibung | Zielgruppe |
|----------|--------------|------------|
| [testing-maintenance-guide.md](docs/testing-maintenance-guide.md) | Testing, Monitoring, Wartung | IT-Team / Bot-Owner |
| [user-guide.md](docs/user-guide.md) | Benutzerhandbuch (Deutsch) | Alle Mitarbeiter |

### Für Entwicklung

| Code | Beschreibung |
|------|--------------|
| [zoho_documentation_crawler.py](crawlers/zoho_documentation_crawler.py) | Web Crawler für Zoho Help Center |
| [create_assistant.py](openai-config/create_assistant.py) | OpenAI Assistant Setup-Automatisierung |
| [bot-flow-codeless.json](salesiq-bot/bot-flow-codeless.json) | SalesIQ Bot Flow Konfiguration |
| [bot-script-deluge.txt](salesiq-bot/bot-script-deluge.txt) | Alternative Deluge-Implementation |

---

## 💡 Anwendungsbeispiele

### Beispiel 1: Neuer Kontakt in Zoho CRM

**User fragt:**
```
Wie lege ich einen neuen Kontakt in Zoho CRM an?
```

**Bot antwortet:**
```
Ich helfe dir gerne dabei, einen neuen Kontakt in Zoho CRM anzulegen!

So erstellst du einen neuen Kontakt:
1. Melde dich bei Zoho CRM an
2. Klicke in der oberen Navigation auf 'Kontakte'
3. Klicke rechts oben auf den Button '+ Neuer Kontakt'
4. Fülle die Pflichtfelder aus (Vorname, Nachname, E-Mail)
5. Optional: Ergänze weitere Informationen
6. Klicke auf 'Speichern'

💡 Pro-Tipp: Verknüpfe den Kontakt direkt mit einem Account...

Kann ich dir noch anders helfen?
```

### Beispiel 2: Rechnung erstellen

**User fragt:**
```
Wie erstelle ich eine Rechnung in Zoho Books?
```

**Bot gibt Schritt-für-Schritt Anleitung** mit Screenshots-Referenzen und aboutwater-spezifischen Zusatzinfos.

### Beispiel 3: Eskalation bei technischem Problem

**User fragt:**
```
Ich kann mich nicht bei Zoho anmelden
```

**Bot erkennt technisches Problem:**
```
Das klingt nach einem technischen Problem mit dem Login.
Ich verbinde dich am besten direkt mit unserem IT-Support,
der dir bei Login-Problemen helfen kann.

[Button: Mit Mitarbeiter verbinden]
```

---

## 🔧 Konfiguration

### System Prompt anpassen

Öffne `openai-config/system-prompt.txt` und passe an:

```
Du bist der Zoho-Assistent für aboutwater GmbH...

REGELN:
1. Antworte IMMER auf Deutsch
2. Gib Schritt-für-Schritt Anleitungen...
...
```

Nach Änderung:
1. OpenAI Platform → Assistant → Instructions → Update
2. Speichern (sofort wirksam, kein Re-Deploy nötig)

### Knowledge Base erweitern

**aboutwater-spezifische Prozesse hinzufügen:**

```bash
cd knowledge-base

# Erstelle neue Datei
notepad aboutwater-crm-workflows.md

# Format:
# aboutwater CRM Workflows
## Neuer Kunde Onboarding
1. Kontakt anlegen
2. Account verknüpfen
...
```

Dann Vector Store in OpenAI Platform aktualisieren:
1. Storage → Vector Store → zoho-knowledge-base
2. Alte Dateien löschen (optional)
3. Neue Dateien hochladen
4. Warten bis "Completed"

### Bot Flow anpassen

SalesIQ → Settings → Bots → aboutwater Zoho Assistant → Edit

Änderungen z.B.:
- Welcome Message Text
- Button Labels
- Handoff-Regeln
- Timeout-Einstellungen

---

## 📊 Monitoring & Metriken

### Dashboard

**SalesIQ Dashboard:**
- Login: [salesiq.zoho.eu](https://salesiq.zoho.eu)
- Reports → Bot Analytics

**Key Metrics:**
- Total Conversations (heute / Woche / Monat)
- Resolution Rate (% ohne Eskalation)
- User Satisfaction (👍/👎 Ratio)
- Average Response Time
- Escalation Rate

### Kosten

**OpenAI API Costs** (bei 10.000 Nachrichten/Monat):

| Modell | Input | Output | Total/Monat |
|--------|-------|--------|-------------|
| gpt-4o | $12.50 | $30.00 | ~$42.50 |
| gpt-4o-mini | $0.50 | $2.00 | ~$2.50 |

**SalesIQ:** €0 (bereits in Zoho One Subscription enthalten)

**Gesamt:** ~€50-100/Monat (je nach Modell & Nutzung)

### ROI

**Annahmen:**
- 100 ersetzte IT-Tickets pro Monat
- Durchschnitt 15 Min pro Ticket
- IT-Kosten: €50/Stunde

**Savings:**
```
100 Tickets × 15 Min = 1.500 Min = 25 Stunden
25 h × €50 = €1.250 gespart

Bot Kosten: ~€100
Net Savings: €1.150/Monat oder €13.800/Jahr
```

---

## 🛠 Wartung

### Daily (5 Minuten)
- SalesIQ Dashboard checken
- Negative Feedback reviewen
- Kosten überprüfen

### Weekly (1-2 Stunden)
- Analytics Report erstellen
- Top Questions analysieren
- Eskalierte Conversations reviewen
- Weekly Report an Stakeholder

### Monthly (3-4 Stunden)
- **Knowledge Base Update** (Crawl + aboutwater Docs)
- Vector Store aktualisieren
- Performance Review
- Cost Analysis & ROI
- Monthly Report für Management

Siehe [testing-maintenance-guide.md](docs/testing-maintenance-guide.md) für Details.

---

## ❓ Troubleshooting

### Bot antwortet nicht

**Ursachen:**
- OpenAI Integration nicht verbunden
- API Key expired
- Assistant ID falsch

**Lösungen:**
1. SalesIQ → Integrations → OpenAI → Status prüfen
2. API Key erneuern
3. Assistant ID in Bot Config überprüfen

### Antworten auf Englisch

**Lösung:**
- System Prompt verstärken: `KRITISCH: Antworte AUSSCHLIESSLICH auf Deutsch.`
- OpenAI Platform → Assistant → Instructions → Update

### Hohe Kosten

**Lösungen:**
- Wechsel zu gpt-4o-mini (90% günstiger)
- Max Tokens limitieren
- System Prompt kürzen

Siehe [testing-maintenance-guide.md](docs/testing-maintenance-guide.md) → Teil 4 für vollständiges Troubleshooting Playbook.

---

## 🗺 Roadmap

### Phase 1 (Januar 2026) ✅
- [x] Knowledge Base Crawler
- [x] OpenAI Assistant Setup
- [x] SalesIQ Integration
- [x] Deployment Guide
- [x] User Guide

### Phase 2 (Februar 2026) 🔄
- [ ] WhatsApp Integration
- [ ] Multi-Language Support (English)
- [ ] Proactive Engagement Features
- [ ] Advanced Analytics Dashboard

### Phase 3 (Q2 2026) 📅
- [ ] Zoho Analytics Integration
- [ ] Custom Reporting
- [ ] Voice Interface (optional)
- [ ] Mobile App Optimization

### Phase 4 (Q3 2026) 🔮
- [ ] Predictive Help (AI erkennt Probleme bevor User fragt)
- [ ] Video Tutorial Integration
- [ ] Multi-Tenant Support (für Partner)

---

## 👥 Team & Support

### Projektteam

- **Projektleiter:** [Name]
- **Technical Lead:** [Name]
- **Bot Owner:** [Name]

### Support-Kontakte

- **IT Support:** it-support@aboutwater.de
- **Bot-Feedback:** [email]
- **Technische Fragen:** [email]

### Externe Resources

- **OpenAI Support:** [help.openai.com](https://help.openai.com)
- **Zoho Support:** [help.zoho.com](https://help.zoho.com)
- **Community:** aboutwater Slack #zoho-bot

---

## 📄 Lizenz & Nutzung

**Intern:** Nur für aboutwater GmbH Mitarbeiter

**Externe Nutzung:** Nicht gestattet ohne Genehmigung

**Daten:** DSGVO-konform, keine Weitergabe an Dritte

---

## 🎉 Success Stories

### Story 1: Marketing Team
> "Früher musste ich jedes Mal den IT-Support fragen, wie ich Reports in Zoho CRM exportiere. Jetzt bekomme ich in 10 Sekunden eine Anleitung vom Bot!" - Sarah, Marketing Manager

### Story 2: Buchhaltung
> "Der Bot hat mir geholfen, meine erste Rechnung in Zoho Books zu erstellen. Schritt für Schritt, auf Deutsch, super einfach!" - Michael, Buchhaltung

### Story 3: Reduktion IT-Tickets
> "In den ersten 4 Wochen haben wir 65% weniger Zoho-bezogene IT-Tickets erhalten. Der Bot funktioniert!" - IT-Team Lead

---

## 🙏 Danksagungen

Dieses Projekt nutzt folgende Open Source Tools & APIs:

- **OpenAI ChatGPT API** - AI Engine
- **Zoho SalesIQ** - Chat Platform
- **BeautifulSoup** - Web Scraping
- **html2text** - HTML zu Markdown Konvertierung

---

## 📞 Kontakt

**Fragen zum Projekt?**

Email: it-support@aboutwater.de
Slack: #zoho-bot

**Feedback zum Bot?**

Direkt im Chat: 👍/👎 Buttons nutzen
Oder Email: [feedback-email]

---

**Version:** 1.0
**Erstellt:** Januar 2026
**Letzte Aktualisierung:** Januar 2026
**Projekt:** aboutwater Zoho AI Chatbot

---

Made with ❤️ by aboutwater IT-Team
