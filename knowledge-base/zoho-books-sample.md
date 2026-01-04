# Zoho Books Documentation
## Buchhaltung & Rechnungswesen für aboutwater

**Source:** Zoho Books Help Center
**Last Updated:** Januar 2026

---

## Überblick: Zoho Books

Zoho Books ist eine cloudbasierte Buchhaltungssoftware für kleine und mittelständische Unternehmen.

**Hauptfunktionen:**
- Rechnungserstellung
- Ausgabenverwaltung
- Bankabgleich
- Steuerberechnungen
- Finanzberichte
- Inventarverwaltung

---

## Rechnungen erstellen

### Neue Rechnung anlegen

**Schritt-für-Schritt:**

1. **Zoho Books öffnen**
   - Navigiere zu https://books.zoho.eu
   - Melde dich an

2. **Zum Rechnungsmodul**
   - Klicke auf "Verkauf" → "Rechnungen"
   - Oder: Schnellzugriff "+ Neue Rechnung"

3. **Kundeninformationen**
   - **Kunde auswählen:** Beginne zu tippen, wähle aus Liste
   - Oder: "+ Neuer Kunde" für neuen Kunden

4. **Rechnungsdetails**
   - **Rechnungsnummer:** Auto-generiert oder manuell
   - **Rechnungsdatum:** Heute oder wählen
   - **Fälligkeitsdatum:** Standard: 30 Tage oder anpassen

5. **Positionen hinzufügen**
   - Klicke "+ Position hinzufügen"
   - **Artikel:** Wähle aus Katalog oder freie Eingabe
   - **Beschreibung:** Details zur Leistung
   - **Menge:** Anzahl
   - **Preis:** Pro Einheit
   - **Steuer:** 19% MwSt. (Deutschland Standard)

6. **Mehrere Positionen**
   - Wiederhole für alle Leistungen/Produkte
   - Zwischensumme wird automatisch berechnet

7. **Zusätzliche Optionen**
   - **Rabatt:** Optional, in % oder absolut
   - **Versandkosten:** Falls zutreffend
   - **Notizen:** Interne Hinweise
   - **Konditionen:** AGB, Zahlungsbedingungen

8. **Speichern & Versenden**
   - **"Speichern"**: Entwurf speichern
   - **"Speichern und senden"**: Sofort per E-Mail
   - **"Als PDF speichern"**: Download für manuellen Versand

**Pro-Tipps:**
- Erstelle Vorlagen für wiederkehrende Rechnungen
- Nutze automatische Nummerierung
- Hinterlege Firmenlogo in Einstellungen → Templates

---

## Rechnung per E-Mail versenden

**Nach Erstellung:**

1. Klicke auf "Senden" (in Rechnungsdetails)
2. E-Mail-Dialog öffnet sich
3. **An:** Kundenmail (vorausgefüllt)
4. **Betreff:** Anpassbar
5. **Nachricht:** Standard-Text oder individuell
6. **Anhänge:** Rechnung als PDF automatisch
7. "Senden" klicken

**Status-Tracking:**
- Versendet: E-Mail wurde gesendet
- Angesehen: Kunde hat PDF geöffnet
- Bezahlt: Nach Zahlungseingang

---

## Zahlungen buchen

### Zahlungseingang erfassen

**Wenn Kunde bezahlt hat:**

1. Öffne die entsprechende Rechnung
2. Klicke "Zahlung erfassen"
3. **Zahlungsdatum:** Datum des Geldeingangs
4. **Betrag:** Voller Betrag oder Teilzahlung
5. **Zahlungsmethode:** Banküberweisung, PayPal, etc.
6. **Konto:** Dein Bankkonto (aus Kontenliste)
7. **Referenz:** Optional: Überweisungsreferenz
8. "Speichern"

**Status ändert sich:**
- Rechnung: "Bezahlt" ✓
- Automatische Benachrichtigung an Kunde (optional)

---

## Ausgaben verwalten

### Neue Ausgabe erfassen

**Für Buchhaltung & Steuern:**

1. Klicke "Ausgaben" → "+ Neue Ausgabe"
2. **Lieferant:** Wählen oder neu anlegen
3. **Datum:** Ausgabedatum
4. **Kategorie:** z.B. "Büromaterial", "Software", "Reisekosten"
5. **Betrag:** Bruttobetrag
6. **Steuer:** 19% Vorsteuer (wenn berechtigt)
7. **Zahlungsmethode:** Firmenkonto, Kreditkarte, Bar
8. **Beleg:** Datei hochladen (Foto oder PDF)
9. **Beschreibung:** Details
10. "Speichern"

**Beleg-Upload:**
- Klicke "Anhang hinzufügen"
- Wähle Datei (JPG, PNG, PDF)
- Wird mit Ausgabe verknüpft

---

## Berichte generieren

### Umsatzsteuer-Voranmeldung (UStVA)

**Deutschland-spezifisch:**

1. Gehe zu "Berichte" → "Steuerberichte"
2. Wähle "Umsatzsteuer-Voranmeldung"
3. **Zeitraum:** Monat oder Quartal wählen
4. Bericht wird generiert:
   - Umsatzsteuer aus Verkäufen (19%, 7%)
   - Vorsteuer aus Einkäufen
   - Zahllast oder Erstattung
5. "Exportieren" als PDF oder ELSTER-Format

**ELSTER-Export:**
- Settings → Taxes → Enable ELSTER integration
- Export-Funktion wird verfügbar

### Gewinn & Verlust (GuV)

1. "Berichte" → "Gewinn & Verlust"
2. Zeitraum wählen
3. Zeigt:
   - Einnahmen (nach Kategorie)
   - Ausgaben (nach Kategorie)
   - Nettogewinn/-verlust

**Export:** PDF, Excel, CSV

---

## Wiederkehrende Rechnungen

### Automatische Rechnungen einrichten

**Für Abo-Kunden oder Dauerleistungen:**

1. "Verkauf" → "Wiederkehrende Rechnungen"
2. "+ Neue wiederkehrende Rechnung"
3. **Kunde:** Auswählen
4. **Profil-Name:** z.B. "Monatliche Wartung Kunde X"
5. **Wiederholungsintervall:**
   - Monatlich, vierteljährlich, jährlich, etc.
   - Startdatum
   - Enddatum (optional) oder unbegrenzt
6. **Positionen:** Wie bei normaler Rechnung
7. **Automatischer Versand:** Aktivieren
8. "Erstellen"

**Automatischer Ablauf:**
- Zoho Books erstellt Rechnung zum definierten Datum
- Sendet E-Mail automatisch an Kunden
- Status-Tracking wie bei normalen Rechnungen

---

## Integration mit Zoho CRM

### Rechnungen aus CRM erstellen

**Wenn Integration aktiv:**

1. Öffne Account oder Deal in Zoho CRM
2. Klicke "Rechnung erstellen" (Zoho Books Button)
3. Weiterleitung zu Zoho Books
4. **Auto-Ausfüllung:**
   - Kundenname
   - Adresse
   - Kontaktdaten
   - Deal-Wert (optional als Rechnungsbetrag)
5. Ergänze Positionen
6. Speichern & Senden

**Sync zurück zu CRM:**
- Rechnungsstatus wird in CRM angezeigt
- Zahlungseingang aktualisiert Deal

---

## Bankkonto-Abgleich

### Transaktionen importieren

**Für automatischen Abgleich:**

1. "Banking" → "Bank Feeds"
2. Verbinde Bankkonto (via API oder CSV-Upload)
3. Transaktionen werden importiert
4. **Abgleich:**
   - Automatische Zuordnung zu Rechnungen/Ausgaben
   - Manuelle Zuordnung für unbekannte Transaktionen
5. "Bestätigen" für jede Transaktion

**Manuelle CSV-Upload:**
- Exportiere Kontoauszug als CSV
- "Transaktionen importieren"
- Mappe Spalten (Datum, Betrag, Beschreibung)
- Import

---

## Häufige Fragen

### Wie korrigiere ich eine versendete Rechnung?

**Option 1: Gutschrift**
- Erstelle Gutschrift für falsche Rechnung
- Erstelle korrigierte neue Rechnung

**Option 2: Stornieren (wenn noch nicht bezahlt)**
- Öffne Rechnung → "Mehr" → "Stornieren"
- Erstelle neue korrekte Rechnung

### Wie erstelle ich ein Angebot?

Fast identisch zu Rechnung:
1. "Verkauf" → "Angebote"
2. "+ Neues Angebot"
3. Fülle wie Rechnung aus
4. "Senden"
5. **Bei Annahme:** "In Rechnung umwandeln"

### Wie exportiere ich Daten für Steuerberater?

1. "Berichte" → "Kontenplan"
2. Zeitraum wählen
3. "Export" → DATEV-Format oder Excel
4. An Steuerberater senden

---

## aboutwater-spezifische Prozesse

### Projektrechnungen erstellen

**Für Projekte aus Zoho Projects:**

1. Gehe zu "Projekte" (wenn Zoho Projects integriert)
2. Wähle abgeschlossenes Projekt
3. "Rechnung aus Projekt" erstellen
4. Zeiteinträge werden automatisch übernommen
5. Stundennachweis wird angehängt

**Manuelle Methode:**
- Erfasse Stunden als separate Rechnungspositionen
- Nutze "Zeitbasierte Abrechnung"

---

## Tipps & Best Practices

### Nummerierungssystem

Empfohlenes Format: `YYYY-XXXX`
- 2026-0001, 2026-0002, etc.
- Settings → Preferences → Invoice Settings

### Vorlagen anpassen

- Settings → Templates → Invoice Templates
- Lade aboutwater-Logo hoch
- Passe Farben an Corporate Design an
- Füge Firmenslogan hinzu

### Backup & Export

- Monatlich: Export aller Daten
- Berichte → "Datenexport"
- Speichere sicher (Cloud-Backup)

---

## Wichtige Einstellungen für Deutschland

### Steuern konfigurieren

Settings → Taxes
- **Umsatzsteuer:** 19% (Standard)
- **Ermäßigte USt:** 7% (Bücher, Lebensmittel)
- **Steuer-ID:** Eintragen unter Organization Settings

### Sprache & Währung

Settings → Preferences
- **Sprache:** Deutsch
- **Währung:** EUR (€)
- **Datumsformat:** TT.MM.JJJJ
- **Zeitzone:** Europe/Berlin

---

**Hinweis:** Dieses Dokument ist ein Sample-Template. Ergänzen Sie spezifische Zoho Books-Dokumentation und aboutwater-Prozesse.

**Offizielle Dokumentation:** https://www.zoho.com/books/help/
