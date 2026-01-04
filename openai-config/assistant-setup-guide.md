# OpenAI Assistant Setup Guide
## Zoho Assistant für aboutwater GmbH

### Schritt 1: OpenAI Account erstellen

1. Gehe zu [platform.openai.com](https://platform.openai.com)
2. Erstelle einen Account oder melde dich an
3. Füge eine Zahlungsmethode hinzu unter **Settings > Billing**
4. Generiere einen API-Schlüssel unter **API Keys > Create new secret key**
   - Name: `aboutwater-zoho-assistant`
   - Speichere den Schlüssel sicher (wird nur einmal angezeigt!)

### Schritt 2: Assistant erstellen

1. Gehe zu [platform.openai.com/assistants](https://platform.openai.com/assistants)
2. Klicke auf **Create**
3. Konfiguriere den Assistant mit folgenden Einstellungen:

#### Grundeinstellungen

```
Name: aboutwater_Zoho_Assistant
Model: gpt-4o (oder gpt-4o-mini für niedrigere Kosten)
```

#### Instructions (System Prompt)

Kopiere den gesamten Inhalt aus der Datei `system-prompt.txt` in das Instructions-Feld.

#### Tools aktivieren

- ✅ **File Search** (aktivieren für RAG-Funktionalität)
- ❌ Code Interpreter (nicht benötigt)
- ❌ Function Calling (nicht benötigt für diese Implementierung)

#### File Search Konfiguration

1. Erstelle einen neuen **Vector Store**:
   - Name: `zoho-knowledge-base`
   - Beschreibung: `Zoho documentation for aboutwater employees`

2. Lade die Wissensdateien hoch (siehe Schritt 3)

### Schritt 3: Wissensdateien hochladen

#### Vorbereitete Dateien aus dem Crawler

Nach Ausführung des Crawlers findest du folgende Dateien im Ordner `knowledge-base/`:

```
zoho-crm.md
zoho-books.md
zoho-inventory.md
zoho-sign.md
zoho-salesiq.md
zoho-desk.md
zoho-people.md
```

#### Upload-Prozess

1. Im Assistant Editor, unter **Tools > File Search**
2. Klicke auf **Add files to vector store**
3. Wähle den Vector Store `zoho-knowledge-base` aus
4. Lade alle `.md` Dateien gleichzeitig hoch
5. Warte bis die Verarbeitung abgeschlossen ist (Status: ✅ Completed)

#### aboutwater-spezifische Dokumente hinzufügen

Wenn aboutwater interne SOPs oder Workflows hat:

1. Erstelle Markdown-Dateien für interne Prozesse:
   ```
   aboutwater-crm-workflows.md
   aboutwater-rechnungsstellung.md
   aboutwater-lagerbestand-prozesse.md
   ```

2. Lade diese zusätzlich in den Vector Store hoch

### Schritt 4: Assistant testen

1. Klicke auf **Test** im Assistant Editor
2. Teste mit deutschen Beispielfragen:

```
Wie lege ich einen neuen Kontakt in Zoho CRM an?
Wie erstelle ich eine Rechnung in Zoho Books?
Wie tracke ich eine Bestellung in Zoho Inventory?
```

3. Überprüfe:
   - ✅ Antworten sind auf Deutsch
   - ✅ Schritt-für-Schritt Format wird eingehalten
   - ✅ Relevante Informationen aus den Wissensdateien werden zitiert
   - ✅ "Kann ich dir noch anders helfen?" erscheint am Ende

### Schritt 5: Assistant ID kopieren

1. Nach erfolgreicher Erstellung findest du oben die **Assistant ID**
   - Format: `asst_xxxxxxxxxxxxxxxxxxxxx`
2. Kopiere diese ID - wird für die SalesIQ Integration benötigt
3. Speichere sie in der Datei `assistant-id.txt` (siehe unten)

### Schritt 6: Konfigurationsdaten speichern

Erstelle eine Datei `config.json` mit folgenden Informationen:

```json
{
  "openai": {
    "api_key": "sk-proj-xxxxx",
    "assistant_id": "asst_xxxxx",
    "model": "gpt-4o"
  },
  "vector_store": {
    "id": "vs_xxxxx",
    "name": "zoho-knowledge-base"
  },
  "created_at": "2026-01-04",
  "version": "1.0"
}
```

**⚠️ WICHTIG: Füge `config.json` zur `.gitignore` hinzu! Niemals API-Schlüssel in Git committen!**

---

## Erweiterte Konfiguration

### Modell-Auswahl Überlegungen

| Modell | Kosten | Geschwindigkeit | Qualität | Empfehlung |
|--------|--------|-----------------|----------|------------|
| gpt-4o | Mittel | Schnell | Sehr hoch | ✅ Empfohlen für Produktion |
| gpt-4o-mini | Niedrig | Sehr schnell | Hoch | ✅ Gut für Test/Budget |
| gpt-4-turbo | Höher | Mittel | Sehr hoch | Optional für komplexe Fälle |

### Geschätzte Kosten (gpt-4o)

Basis: 10.000 Nachrichten/Monat, durchschnittlich 500 Input Tokens, 300 Output Tokens

```
Input:  10.000 × 500 tokens × $2.50/1M = $12.50
Output: 10.000 × 300 tokens × $10.00/1M = $30.00
Total: ~$42.50/Monat
```

### File Search Besonderheiten

- OpenAI chunked automatisch die hochgeladenen Dokumente
- Chunk Size: ~800 Tokens
- Embedding Modell: text-embedding-3-large
- Kosten: $0.13 pro 1M Tokens (einmalig beim Upload)

### Assistant Updates

Um den System Prompt zu aktualisieren:

1. Gehe zu [platform.openai.com/assistants](https://platform.openai.com/assistants)
2. Wähle deinen Assistant aus
3. Bearbeite das **Instructions** Feld
4. Klicke **Save**
5. Änderungen sind sofort wirksam (kein Re-Deploy nötig)

Um Wissensdateien zu aktualisieren:

1. Lösche alte Dateien aus dem Vector Store
2. Lade neue Versionen hoch
3. Warte auf Verarbeitung
4. Teste die Änderungen im Playground

---

## Troubleshooting

### Problem: Assistant antwortet nicht auf Deutsch

**Lösung:**
- Überprüfe, dass "Antworte IMMER auf Deutsch" in den Instructions steht
- Teste mit explizit deutscher Frage
- Füge am Anfang der Instructions hinzu: `SPRACHE: Deutsch (DE)`

### Problem: Antworten enthalten keine Quellen aus den Dateien

**Lösung:**
- Überprüfe, ob File Search aktiviert ist
- Stelle sicher, dass Dateien erfolgreich hochgeladen wurden (Status: Completed)
- Teste, ob die Frage wirklich in den Dokumenten abgedeckt ist

### Problem: Antworten sind zu lang/zu kurz

**Lösung:**
Passe die Instructions an:
```
Halte Antworten präzise und fokussiert. Maximal 5-7 Schritte pro Anleitung.
```

### Problem: Assistant spekuliert oder erfindet Informationen

**Lösung:**
Verstärke die Einschränkungen in den Instructions:
```
KRITISCH: Beziehe dich AUSSCHLIESSLICH auf die hochgeladenen Dokumente.
Wenn eine Information nicht in den Dateien vorhanden ist, sage klar:
"Diese Information habe ich nicht in meiner Wissensdatenbank."
```

---

## Best Practices

### 1. Regelmäßige Updates der Wissensbasis

- **Monatlich:** Prüfe, ob Zoho neue Features veröffentlicht hat
- **Bei Bedarf:** Crawle relevante Updates und aktualisiere den Vector Store

### 2. Monitoring

Überwache in der OpenAI Console:
- **Usage:** API-Kosten und Token-Verbrauch
- **Logs:** Fehlerhafte Anfragen
- **Performance:** Antwortzeiten

### 3. Version Control

Speichere verschiedene Versionen des System Prompts:
```
system-prompt-v1.0.txt
system-prompt-v1.1.txt
system-prompt-v2.0.txt
```

### 4. A/B Testing

Erstelle zwei Assistants zum Testen:
- `aboutwater_Zoho_Assistant_Production`
- `aboutwater_Zoho_Assistant_Beta`

Teste neue Prompts im Beta-Assistant vor dem Rollout.

---

## Nächste Schritte

Nach erfolgreichem Setup:

✅ OpenAI Assistant erstellt und konfiguriert
⏭️ **Weiter zu:** SalesIQ Integration (siehe `../salesiq-bot/integration-guide.md`)

---

**Erstellt:** Januar 2026
**Version:** 1.0
**Projekt:** aboutwater Zoho AI Chatbot
