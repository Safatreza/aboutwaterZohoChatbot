# aboutwater GmbH - Interne Zoho Workflows
## Firmenspezifische Prozesse und Best Practices

**Für:** aboutwater Mitarbeiter
**Version:** 1.0
**Letzte Aktualisierung:** Januar 2026

---

## 🎯 Überblick

Dieses Dokument beschreibt, wie aboutwater GmbH Zoho-Tools intern nutzt und welche spezifischen Prozesse etabliert sind.

**Wichtig:** Diese Workflows ergänzen die Standard-Zoho-Dokumentation und enthalten firmeninterne Besonderheiten.

---

## Neukunden-Onboarding

### Kompletter Prozess vom Lead zum ersten Projekt

**Phase 1: Lead-Erfassung (Marketing/Vertrieb)**

1. **Lead-Quelle dokumentieren**
   - Website-Formular → Tag: "Website"
   - Messe-Kontakt → Tag: "Messe-2026"
   - Empfehlung → Tag: "Referral"

2. **Erstqualifizierung (innerhalb 24h)**
   - Anruf oder E-Mail
   - BANT-Kriterien prüfen:
     - Budget vorhanden?
     - Authority (Entscheidungsbefugnis)?
     - Need (konkreter Bedarf)?
     - Timeline (Zeitrahmen)?

3. **Lead-Status aktualisieren**
   - Zoho CRM → Lead → Status ändern
   - Optionen:
     - "Qualifiziert" → weiter zu Phase 2
     - "Nicht qualifiziert" → Reason dokumentieren
     - "Follow-up" → Task für nächsten Kontakt erstellen

**Phase 2: Lead-Konvertierung (Vertrieb)**

4. **Lead in Kontakt/Account konvertieren**
   - CRM → Lead öffnen → "Konvertieren"
   - ✅ Kontakt erstellen
   - ✅ Account erstellen (Firma)
   - ✅ Deal erstellen
   - Deal-Name Format: `[Firmenname] - [Projekttyp]`
   - Beispiel: "aboutwater - Website Redesign"

5. **Deal-Details ergänzen**
   - **Betrag:** Geschätzter Projektwert (EUR)
   - **Abschlussdatum:** Erwartetes Vertragsabschluss-Datum
   - **Stage:** "Qualifizierung"
   - **Priorität:** Hoch/Mittel/Niedrig
   - **Notizen:** Besonderheiten, Anforderungen

**Phase 3: Angebot erstellen (Vertrieb + Projektleitung)**

6. **Erstgespräch dokumentieren**
   - CRM → Deal → Notes → Meeting-Zusammenfassung
   - Requirements erfassen
   - Nächste Schritte festhalten

7. **Angebot erstellen in Zoho Books**
   - Zoho Books → Verkauf → Neues Angebot
   - Kunde auswählen (synchronisiert aus CRM)
   - Positionen basierend auf Projektumfang:
     - Konzeption (Stunden × Stundensatz)
     - Design (Stunden × Stundensatz)
     - Entwicklung (Stunden × Stundensatz)
     - Testing & QA
     - Projektmanagement (10% Aufschlag)
   - **aboutwater-Standard-Konditionen:**
     - Zahlungsziel: 30 Tage netto
     - Anzahlung: 30% bei Auftragserteilung
     - Gültigkeitsdauer: 14 Tage

8. **Angebot versenden**
   - Zoho Books → "Speichern und senden"
   - CC an Projektleiter
   - Follow-up Task in CRM erstellen (7 Tage)

**Phase 4: Vertragsabschluss (Vertrieb)**

9. **Nach Annahme: Deal-Stage aktualisieren**
   - CRM → Deal → Stage: "Verhandlung" → "Gewonnen"
   - Gewinnwahrscheinlichkeit: 100%
   - Tatsächlicher Abschlussdatum eintragen

10. **Angebot in Rechnung umwandeln (Teilrechnung 1 - Anzahlung)**
    - Zoho Books → Angebot öffnen → "In Rechnung umwandeln"
    - Nur Anzahlungsposition (30% des Gesamtbetrags)
    - Rechnungstext: "Anzahlung gemäß Angebot [Angebotsnummer]"
    - Versenden

**Phase 5: Projektstart (Projektmanagement)**

11. **Projekt in Zoho Projects erstellen**
    - Zoho Projects → "+ Neues Projekt"
    - Projektname: Wie Deal-Name
    - Kunde verknüpfen (Account aus CRM)
    - Template wählen: "aboutwater Standard-Webprojekt"

12. **Projektteam zuweisen**
    - Projektleiter
    - Designer
    - Entwickler
    - QA Tester

13. **Meilensteine definieren**
    - Kickoff Meeting
    - Design-Freigabe
    - Entwicklung abgeschlossen
    - Testing & QA
    - Go-Live
    - Projektabschluss

14. **CRM mit Projekt verknüpfen**
    - CRM → Deal → Custom Field "Zoho Projekt-ID"
    - Eintragen für Verfolgbarkeit

**Phase 6: Projektverlauf (laufend)**

15. **Zeiterfassung (alle Teammitglieder)**
    - Zoho Projects → Timesheets
    - Täglich Stunden erfassen
    - **aboutwater-Regel:** Mindestens wöchentlich eintragen

16. **Statusupdates**
    - Wöchentliches Projektmeeting
    - Status-Update in Zoho Projects → Activity Stream
    - Bei Problemen: Automatische Benachrichtigung an Projektleiter

**Phase 7: Projektabschluss**

17. **Finale Abnahme**
    - Zoho Projects → Meilenstein "Abnahme" als erledigt markieren
    - Abnahmeprotokoll hochladen

18. **Schlussrechnung erstellen**
    - Zoho Books → Neue Rechnung
    - Positionen:
      - Restbetrag (70% des Projektwertes)
      - ODER: Zeitbasiert (tatsächliche Stunden aus Zoho Projects importieren)
    - Rechnung senden

19. **Projekt archivieren**
    - Zoho Projects → Projekt-Einstellungen → "Archivieren"
    - CRM Deal → Status: "Abgeschlossen"

20. **Kundenzufriedenheit erfassen**
    - E-Mail an Kunde mit Feedback-Formular
    - Ergebnis in CRM → Account → Custom Field "Zufriedenheit" dokumentieren

---

## Monatliche Wartungsverträge

### Wiederkehrende Rechnungen für Bestandskunden

**Setup (einmalig pro Kunde):**

1. **Wartungsvertrag in CRM dokumentieren**
   - CRM → Account → Custom Field "Wartungsvertrag"
   - Details: Umfang, Laufzeit, Kündigungsfrist

2. **Wiederkehrende Rechnung in Zoho Books**
   - Zoho Books → Wiederkehrende Rechnungen
   - Kunde auswählen
   - **Position:**
     - "Monatliche Wartung & Support"
     - Betrag: lt. Vertrag (z.B. 199 EUR)
   - **Intervall:** Monatlich
   - **Startdatum:** Vertragsbeginn
   - **Automatischer Versand:** Aktiviert
   - **Versanddatum:** 1. des Monats

3. **Erinnerung für Vertragsverlängerung**
   - CRM → Account → Task erstellen
   - Fälligkeitsdatum: 2 Monate vor Vertragsende
   - Verantwortlich: Account Manager
   - Notiz: "Vertragsverlängerung besprechen"

**Monatlicher Ablauf (automatisch):**
- 1. des Monats: Zoho Books sendet Rechnung automatisch
- Kunde erhält PDF per E-Mail
- Nach Zahlungseingang: Automatische Buchung (bei Bank-Integration)

---

## Support-Ticket-Workflow

### Von Kundenanfrage bis Lösung

**aboutwater nutzt Zoho Desk für Support**

1. **Ticket-Eingang**
   - Kunde sendet E-Mail an support@aboutwater.de
   - Automatisches Ticket in Zoho Desk

2. **Erstklassifizierung (automatisch)**
   - KI kategorisiert Ticket:
     - Technisch / Allgemein
     - Priorität: Niedrig/Mittel/Hoch/Kritisch
   - Zuweisung an Team:
     - Webentwicklung
     - Design
     - Allgemeiner Support

3. **Antwort innerhalb SLA**
   - **aboutwater SLA:**
     - Kritisch: 2 Stunden
     - Hoch: 4 Stunden
     - Mittel: 8 Stunden
     - Niedrig: 24 Stunden

4. **Ticket-Bearbeitung**
   - Support-Mitarbeiter öffnet Ticket
   - Status: "In Bearbeitung"
   - Lösungsschritte dokumentieren
   - Bei Bedarf: Zoho CRM/Projects konsultieren für Kundenhistorie

5. **Ticket schließen**
   - Lösung dem Kunden mitgeteilt
   - Kunde-Feedback erfragen
   - Status: "Gelöst"
   - Automatische Umfrage (1-5 Sterne)

6. **Monatliches Review**
   - Zoho Desk → Berichte
   - Durchschnittliche Lösungszeit
   - Kundenzufriedenheit
   - Häufigste Problem-Kategorien

---

## Rechnungsstellung-Workflow

### aboutwater-Standards

**Rechnungsnummern-Format:**
- `AW-JJJJ-NNNN`
- Beispiel: AW-2026-0042

**Zahlungsbedingungen (Standard):**
- 30 Tage netto
- Bei Großprojekten: 30% Anzahlung, 70% nach Abschluss
- Bei Wartung: Monatliche Vorauszahlung

**Mahnwesen (automatisiert in Zoho Books):**
- Tag 31: Freundliche Erinnerung (automatisch)
- Tag 45: Erste Mahnung
- Tag 60: Zweite Mahnung
- Tag 75: Übergabe an Inkasso (manuell)

**Konfiguration:**
Settings → Reminders → Payment Reminders aktivieren

---

## Reporting & Analytics

### Monatliche Management-Berichte

**Verantwortlich:** Buchhaltung/Controlling

**Berichte generieren (jeden Monatsanfang):**

1. **Umsatz-Report**
   - Zoho Books → Berichte → Gewinn & Verlust
   - Zeitraum: Vormonat
   - Export als PDF → an Management

2. **Pipeline-Report**
   - Zoho CRM → Berichte → Sales Pipeline
   - Deals nach Stage
   - Forecast für nächsten Monat

3. **Projekt-Übersicht**
   - Zoho Projects → Dashboard
   - Aktive Projekte
   - Meilenstein-Status
   - Ressourcen-Auslastung

4. **Support-Statistik**
   - Zoho Desk → Reports
   - Ticket-Volume
   - Avg. Resolution Time
   - Customer Satisfaction

**Präsentation:**
Monatliches Management-Meeting → Zusammenfassung aller KPIs

---

## Datenschutz & Compliance (DSGVO)

### aboutwater-Richtlinien für Zoho-Nutzung

**Wichtig:** Alle Mitarbeiter müssen folgen:

1. **Zugriffsrechte**
   - Jeder hat nur Zugriff auf notwendige Module
   - Profile werden von IT-Admin vergeben
   - Keine Weitergabe von Login-Daten

2. **Kundendaten**
   - Nur geschäftlich notwendige Daten erfassen
   - Keine sensiblen Daten in Notizfeldern (z.B. Gesundheit, Religion)
   - Löschung auf Kundenwunsch innerhalb 30 Tage

3. **Export & Backup**
   - Monatlicher Export aller Daten
   - Sichere Speicherung (verschlüsselt)
   - Aufbewahrung lt. gesetzlicher Frist (10 Jahre Buchhaltung)

4. **Externe Zugriffe**
   - Kunden-Portale: Nur für autorisierte Kunden
   - API-Keys: Sicher speichern, regelmäßig erneuern

5. **Schulung**
   - Neue Mitarbeiter: DSGVO-Schulung Pflicht
   - Jährliche Auffrischung

---

## Tipps & Tricks für aboutwater-Mitarbeiter

### Produktivitäts-Hacks

**Tastaturkürzel (Zoho CRM):**
- `Strg + N`: Neuer Datensatz (Lead/Kontakt/Deal)
- `Strg + S`: Speichern
- `Strg + E`: Bearbeiten
- `/`: Globale Suche

**E-Mail-Vorlagen nutzen:**
- Settings → Templates → Email Templates
- aboutwater hat Vorlagen für:
  - Angebots-Versand
  - Projekt-Kickoff
  - Rechnung-Follow-up
  - Support-Antworten (häufige Fragen)

**Mobile App nutzen:**
- Kundentermine: Check-in via Zoho CRM App
- Zeiterfassung unterwegs: Zoho Projects App
- Rechnungen freigeben: Zoho Books App (für Manager)

---

## Häufige Fragen (aboutwater-spezifisch)

### Ich habe einen neuen Kunden - was jetzt?

Folge dem **Neukunden-Onboarding** (siehe oben).
Zusammenfassung:
1. Lead in CRM anlegen
2. Qualifizieren
3. Konvertieren zu Kontakt/Account/Deal
4. Angebot erstellen (Zoho Books)
5. Nach Annahme: Projekt anlegen (Zoho Projects)

### Wie erfasse ich Zeiten korrekt?

- **Täglich** in Zoho Projects → Timesheets
- **Format:** Projekt > Task > Stunden
- **Mindestens wöchentlich** eintragen (aboutwater-Regel)
- Bei Vergessen: Nachträglich möglich (max. 1 Woche rückwirkend)

### Kunde hat nicht bezahlt - was tun?

1. Prüfe Zoho Books → Rechnung → Status
2. Tag 31: Automatische Erinnerung (läuft bereits)
3. Tag 45: Persönlicher Anruf
4. Tag 60: Informiere Buchhaltung → Mahnung
5. Tag 75: Geschäftsführung einschalten

### Wie bekomme ich Zugriff auf ein neues Zoho-Modul?

E-Mail an it-support@aboutwater.de
- Welches Modul?
- Warum benötigt?
- Welche Rechte?

Bearbeitungszeit: 1-2 Werktage

---

## Kontakte & Ansprechpartner

**Zoho-Administrator:** Max Mustermann (max.mustermann@aboutwater.de)
**Technischer Support:** IT-Team (it-support@aboutwater.de)
**Buchhaltung (Zoho Books):** Anna Schmidt (buchhaltung@aboutwater.de)
**CRM-Fragen:** Vertriebsleitung (vertrieb@aboutwater.de)

---

## Änderungshistorie

| Datum | Version | Änderung | Autor |
|-------|---------|----------|-------|
| 2026-01 | 1.0 | Erstversion | IT-Team |

---

**Wichtig:**
Dieses Dokument wird regelmäßig aktualisiert. Bei Fragen oder Verbesserungsvorschlägen: Feedback an it-support@aboutwater.de

**Nächste Review:** März 2026
