# Zoho SalesIQ Integration Guide
## OpenAI Assistant Chatbot für aboutwater

Diese Anleitung zeigt Schritt für Schritt, wie der OpenAI Assistant in Zoho SalesIQ als Zobot integriert wird.

---

## Voraussetzungen

✅ OpenAI Assistant erstellt (siehe `../openai-config/assistant-setup-guide.md`)
✅ Assistant ID verfügbar
✅ OpenAI API-Schlüssel vorhanden
✅ Zoho SalesIQ Zugang mit Admin-Rechten

---

## Teil 1: OpenAI Integration in SalesIQ einrichten

### Schritt 1: SalesIQ Settings öffnen

1. Melde dich bei [salesiq.zoho.eu](https://salesiq.zoho.eu) an (oder .com für US)
2. Klicke auf **Settings** (Zahnrad-Symbol oben rechts)
3. Navigiere zu **Integrations** → **AI** → **OpenAI**

### Schritt 2: OpenAI API-Schlüssel hinzufügen

1. Klicke auf **Connect** oder **Add Integration**
2. Gib deinen OpenAI API-Schlüssel ein:
   ```
   sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
3. Klicke auf **Save** oder **Authorize**
4. Status sollte jetzt: ✅ **Connected** anzeigen

⚠️ **Wichtig:** Speichere den API-Schlüssel sicher. Er wird nicht erneut angezeigt.

---

## Teil 2: Zobot erstellen (Codeless Bot Builder)

### Schritt 1: Neuen Bot erstellen

1. Gehe zu **Settings** → **Bots** → **Zobot**
2. Klicke auf **Add Bot** oder **+ New Bot**
3. Wähle **Codeless Bot Builder** (empfohlen)
4. Gib dem Bot einen Namen:
   ```
   aboutwater Zoho Assistant
   ```
5. Beschreibung (optional):
   ```
   AI-gestützter Chatbot für Zoho-Hilfe basierend auf offizieller Dokumentation
   ```

### Schritt 2: Bot-Flow aufbauen

Der Bot-Flow besteht aus mehreren Karten (Cards). Hier ist die empfohlene Struktur:

#### 2.1 Welcome Message

**Card Type:** Message

**Inhalt (Deutsch):**
```
Hallo! 👋

Ich bin der Zoho-Assistent von aboutwater. Ich helfe dir bei allen Fragen rund um:

• Zoho CRM
• Zoho Books
• Zoho Inventory
• Zoho Sign
• Zoho SalesIQ
• Und mehr...

Stelle mir einfach deine Frage!
```

**Action:** Weiter zur nächsten Card

---

#### 2.2 Question Collection

**Card Type:** Question

**Prompt:**
```
Wie kann ich dir helfen?
```

**Input Type:** Text (einzeiliger oder mehrzeiliger Input)

**Variable Name:** `user_question`

**Validation:** Optional - Mindestens 5 Zeichen

---

#### 2.3 ChatGPT Assistant Call

**Card Type:** ChatGPT Assistant (unter AI/ML Kategorie)

**Konfiguration:**

```
Integration: OpenAI (bereits verbunden)
Assistant: aboutwater_Zoho_Assistant
          [Wähle deinen Assistant aus der Dropdown-Liste]

Input: ${user_question}
      [Variable aus vorheriger Question Card]

Response Variable: assistant_response
```

**Advanced Settings (optional):**
```
Timeout: 30 seconds
Max Tokens: 1000
Temperature: 0.3 (bereits im Assistant konfiguriert)
```

---

#### 2.4 Display Response

**Card Type:** Message

**Inhalt:**
```
${assistant_response}
```

**Format:** Markdown aktivieren (für bessere Formatierung)

---

#### 2.5 Action Buttons

**Card Type:** Quick Replies / Buttons

**Buttons:**

1. **Weitere Frage stellen**
   - Action: Loop zurück zu Card 2.2 (Question Collection)
   - Icon: 🔄

2. **Mit Mitarbeiter sprechen**
   - Action: Transfer to Operator
   - Department: IT Support (oder spezifisch)
   - Icon: 👤

3. **Problem gelöst** 👍
   - Action: End Conversation
   - Log: Positive feedback
   - Icon: ✅

4. **Nicht hilfreich** 👎
   - Action: Transfer to Operator
   - Log: Negative feedback
   - Message: "Verstanden. Ich verbinde dich mit einem Mitarbeiter."
   - Icon: ❌

---

### Schritt 3: Handoff-Regeln konfigurieren

**Settings → Bots → Routing Rules**

**Wann Bot zu Operator übergeben soll:**

1. **Explizite Anfrage:**
   - Wenn User schreibt: "Mitarbeiter", "Mensch", "Operator", "Support"
   - Action: Transfer to operator

2. **Bot kann nicht helfen:**
   - Wenn Assistant antwortet: "IT-Support kontaktieren"
   - Action: Auto-transfer

3. **Negative Bewertung:**
   - Nach "Nicht hilfreich" Button
   - Action: Transfer with context

**Operator-Auswahl:**
```
Department: IT Support
Round-robin: aktiviert
Fallback: Email an it-support@aboutwater.de
```

---

### Schritt 4: Bot veröffentlichen

1. **Preview & Test:**
   - Klicke auf **Preview** um den Bot zu testen
   - Teste verschiedene Fragen:
     - "Wie lege ich einen Kontakt an?"
     - "Rechnung erstellen in Zoho Books"
     - "Was ist Zoho SalesIQ?"

2. **Assign to Brand:**
   - Settings → Brand
   - Wähle die aboutwater Website/Domain

3. **Enable:**
   - Aktiviere den Bot
   - Status: ✅ Active

4. **Deploy Channels:**
   - Website: ✅ (Chat Widget)
   - Mobile App: ✅ (optional)
   - WhatsApp: ❌ (später aktivierbar)
   - Email: ❌ (optional)

---

## Teil 3: Alternative - SalesIQ Deluge Script

Für mehr Kontrolle kannst du auch Deluge Scripts verwenden:

### Deluge Script Beispiel

```deluge
// aboutwater Zoho Assistant - Deluge Implementation

// Welcome message
message = "Hallo! 👋\n\nIch bin der Zoho-Assistent von aboutwater.\nWie kann ich dir helfen?";
reply message;

// Get user question
question = input.message;

// Call OpenAI Assistant
response = open_ai
{
    assistant_id: "asst_YOUR_ASSISTANT_ID_HERE",
    message: question,
    temperature: 0.3
};

// Display response
reply response.get("content");

// Action buttons
actions = [
    {
        "label": "Weitere Frage",
        "action": "restart"
    },
    {
        "label": "Mit Mitarbeiter sprechen",
        "action": "transfer_to_operator"
    }
];

quick_reply actions;
```

**So verwendest du Deluge:**

1. Settings → Bots → Zobot
2. Wähle **Script-based Bot** statt Codeless
3. Füge das Script oben ein
4. Ersetze `asst_YOUR_ASSISTANT_ID_HERE` mit deiner Assistant ID
5. Save & Deploy

---

## Teil 4: Chat Widget anpassen

### Widget Design

**Settings → Brands → [Deine Marke] → Embed Code**

**Anpassungen:**

```javascript
$zoho.salesiq.ready = function() {
    // Widget Position
    $zoho.salesiq.floatwindow.position("bottom-right");

    // Custom Launcher
    $zoho.salesiq.floatbutton.customize({
        text: "Zoho Hilfe",
        iconcolor: "#1A73E8",
        backgroundcolor: "#FFFFFF"
    });

    // Auto-open für neue Besucher (optional)
    // $zoho.salesiq.floatwindow.visible("show");

    // Pre-fill user info wenn bekannt
    $zoho.salesiq.visitor.name("aboutwater Mitarbeiter");
    $zoho.salesiq.visitor.email("");  // Optional
};
```

### Widget nur für interne Zoho Apps

Wenn der Bot nur innerhalb der Zoho-Suite verfügbar sein soll:

**Settings → Installation → Embed Code**

Wähle: **Zoho Apps** statt Website

**Apps auswählen:**
- ✅ Zoho CRM
- ✅ Zoho Books
- ✅ Zoho Inventory
- ✅ Zoho Desk

Der Chat-Button erscheint dann in der rechten unteren Ecke dieser Apps.

---

## Teil 5: Testen & Qualitätssicherung

### Testfälle

Teste den Bot mit diesen Fragen:

#### Test 1: Einfache Frage
```
Frage: Wie lege ich einen neuen Kontakt in Zoho CRM an?
Erwartete Antwort: Schritt-für-Schritt Anleitung auf Deutsch
```

#### Test 2: Komplexe Frage
```
Frage: Wie erstelle ich eine Rechnung in Zoho Books und sende sie per E-Mail?
Erwartete Antwort: Detaillierte Anleitung, mehrere Schritte
```

#### Test 3: Unklare Frage
```
Frage: Zoho funktioniert nicht
Erwartete Antwort: Rückfrage zur Klärung oder Verweis auf IT-Support
```

#### Test 4: Außerhalb des Scope
```
Frage: Wie ist das Wetter heute?
Erwartete Antwort: Höfliche Ablehnung, Fokus auf Zoho-Themen
```

#### Test 5: Eskalation
```
Frage: Ich möchte mit einem Mitarbeiter sprechen
Erwartete Aktion: Transfer to operator
```

### Qualitätskriterien

✅ Antworten sind auf Deutsch
✅ Schritt-für-Schritt Format wird eingehalten
✅ Rückfragen am Ende jeder Antwort
✅ Handoff funktioniert reibungslos
✅ Antwortzeit < 5 Sekunden
✅ Relevante Informationen aus den Wissensdateien

---

## Teil 6: Monitoring & Analytics

### SalesIQ Dashboard

**Reports → Bot Performance**

**Wichtige Metriken:**

| Metrik | Ziel | Überwachung |
|--------|------|-------------|
| User Satisfaction (👍/👎) | > 80% positiv | Täglich |
| Resolution Rate | > 70% ohne Eskalation | Wöchentlich |
| Avg Response Time | < 5 Sekunden | Täglich |
| Escalation Rate | < 30% | Wöchentlich |
| Most Asked Questions | Top 10 | Monatlich |

### Conversation Logs

**Reports → Conversations → Filter: Bot**

Überprüfe regelmäßig:
- Fehlgeschlagene Anfragen
- Negative Bewertungen
- Eskalierte Gespräche

**Aktionen:**
- Identifiziere fehlende Themen in der Wissensbasis
- Passe System Prompt an bei wiederkehrenden Problemen
- Aktualisiere Dokumentation bei neuen Zoho Features

---

## Teil 7: Erweiterte Konfiguration

### Multi-Language Support (optional)

Wenn aboutwater auch englischsprachige Mitarbeiter hat:

**Option 1: Spracherkennung**
```deluge
// Erkenne Sprache
if (question.contains("how") || question.contains("what")) {
    language = "en";
} else {
    language = "de";
}

// Passe Prompt an
if (language == "en") {
    prompt = "Answer in English: " + question;
} else {
    prompt = question;
}
```

**Option 2: Separater Assistant**
- Erstelle zweiten OpenAI Assistant mit englischen Instructions
- Benutzer wählt Sprache zu Beginn

### WhatsApp Integration

**Settings → Channels → WhatsApp**

1. Verbinde WhatsApp Business Account
2. Aktiviere Zobot für WhatsApp
3. Gleicher Bot-Flow funktioniert auch auf WhatsApp

**Vorteil:** Mitarbeiter können Zoho-Fragen per WhatsApp stellen

### Custom Analytics mit Zapier

**SalesIQ → Zapier → Google Sheets**

Automatische Logs für:
- Alle Bot-Interaktionen
- Feedback (👍👎)
- Escalations
- Ungelöste Fragen

→ Monatliche Auswertung zur Bot-Optimierung

---

## Troubleshooting

### Problem: Bot antwortet nicht

**Ursachen & Lösungen:**

1. **OpenAI Integration nicht verbunden**
   - Settings → Integrations → OpenAI → Status prüfen
   - API-Schlüssel erneut eingeben

2. **Assistant ID falsch**
   - Überprüfe ID in Bot-Konfiguration
   - Format: `asst_xxxxxxxxxxxxxxxxxxxx`

3. **Rate Limit überschritten**
   - OpenAI API Limits überprüfen
   - Upgrade auf höheren Tier erwägen

### Problem: Antworten sind auf Englisch

**Lösung:**
- Überprüfe System Prompt im OpenAI Assistant
- Füge am Anfang hinzu: `KRITISCH: Antworte AUSSCHLIESSLICH auf Deutsch.`
- Update im Assistant → keine Änderung im Bot nötig

### Problem: Bot eskaliert zu oft

**Ursachen:**
- Wissensdatenbank unvollständig
- System Prompt zu vorsichtig

**Lösungen:**
1. Ergänze fehlende Dokumentation
2. Passe Instructions an: "Versuche immer zuerst eine hilfreiche Antwort zu geben, bevor du zum IT-Support verweist."

### Problem: Langsame Antworten (>10 Sekunden)

**Ursachen:**
- Zu große Wissensdateien
- gpt-4 statt gpt-4o verwendet

**Lösungen:**
1. Wechsel zu gpt-4o oder gpt-4o-mini
2. Reduziere File Search scope
3. Setze Timeout in Card auf 15-20 Sekunden

---

## Best Practices

### 1. Regelmäßige Updates

**Monatlich:**
- Überprüfe Top 10 unbeantwortete Fragen
- Ergänze fehlende Themen in Wissensdatenbank
- Aktualisiere bei neuen Zoho Features

**Vierteljährlich:**
- Kompletter Crawl der Zoho Dokumentation
- Review der Analytics
- A/B Test neue Prompts

### 2. User Feedback Loop

Implementiere Follow-up nach negativem Feedback:
```
"Danke für dein Feedback. Was genau hat nicht geholfen?"
[Freitext-Eingabe]
→ Sende an IT-Support für Review
```

### 3. Kontext speichern

Nutze SalesIQ Variables um Kontext zu speichern:
```deluge
set("last_topic", "Zoho CRM");
set("last_question", question);
```

→ Bei Eskalation hat Operator volle Historie

### 4. Proactive Engagement

Für spezifische Zoho-Seiten:
```javascript
// Auto-open Bot bei bestimmten CRM-Seiten
if (window.location.href.includes("/crm/")) {
    $zoho.salesiq.floatwindow.visible("show");
    $zoho.salesiq.chat.sendmessage("Brauchst du Hilfe mit Zoho CRM?");
}
```

---

## Nächste Schritte

Nach erfolgreicher Integration:

✅ SalesIQ Zobot konfiguriert und getestet
✅ OpenAI Assistant verbunden
⏭️ **Weiter zu:** User Onboarding & Schulung

**Erstelle:**
1. User Guide für Mitarbeiter (siehe `../docs/user-guide.md`)
2. Interne Ankündigung (Email-Template)
3. Video-Tutorial (optional)

---

**Erstellt:** Januar 2026
**Version:** 1.0
**Projekt:** aboutwater Zoho AI Chatbot
