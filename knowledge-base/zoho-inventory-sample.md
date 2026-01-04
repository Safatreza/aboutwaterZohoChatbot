# Zoho Inventory Documentation
## Lagerverwaltung & Bestandsführung

**Quelle:** Zoho Inventory Help
**Letzte Aktualisierung:** Januar 2026

---

## Was ist Zoho Inventory?

Zoho Inventory ist eine cloudbasierte Lagerverwaltungssoftware für die Bestandsführung, Auftragsverwaltung und Versandabwicklung.

**Hauptfunktionen:**
- Bestandsverwaltung
- Auftragsabwicklung
- Versandmanagement
- Multi-Warehouse Support
- Seriennummern-Tracking
- Barcode-Scanning
- Integration mit E-Commerce

---

## Artikel anlegen

### Neuen Artikel erstellen

**Schritt-für-Schritt:**

1. **Zoho Inventory öffnen**
   - https://inventory.zoho.eu
   - Anmelden

2. **Zum Artikel-Modul**
   - Klicke "Artikel" in der Navigation
   - Oder: "+ Neuer Artikel"

3. **Artikeltyp wählen**
   - **Ware:** Physisches Produkt (Standard)
   - **Dienstleistung:** Nicht-physisch
   - **Paket:** Kombination mehrerer Artikel

4. **Grunddaten eingeben**
   - **Name:** Produktbezeichnung
   - **SKU:** Artikelnummer (eindeutig)
   - **Einheit:** Stück, Meter, Liter, etc.

5. **Preise definieren**
   - **Verkaufspreis:** Regulärer Preis
   - **Einkaufspreis:** Einstandspreis (für Kalkulation)
   - **MwSt:** 19% oder 7%

6. **Bestandsinformationen**
   - **Anfangsbestand:** Aktuelle Menge
   - **Lagerort:** Welches Warehouse
   - **Mindestbestand:** Warnung bei Unterschreitung
   - **Nachbestellmenge:** Empfohlene Bestellmenge

7. **Zusätzliche Optionen**
   - **Bild:** Produktfoto hochladen
   - **Beschreibung:** Details für Kunden
   - **Kategorie:** Produktgruppe
   - **Lieferant:** Bevorzugter Lieferant

8. **Speichern**
   - "Speichern" klicken
   - Artikel ist nun im System

---

## Bestand verwalten

### Bestandsbewegungen erfassen

**Wareneingang buchen:**

1. Gehe zu "Bestandsanpassungen"
2. "+ Neue Anpassung"
3. **Typ:** Hinzufügen
4. **Grund:** Wareneingang, Retoure, Korrektur
5. **Datum:** Buchungsdatum
6. **Artikel auswählen:** Aus Liste
7. **Menge:** Anzahl hinzufügen
8. **Lagerort:** Ziel-Warehouse
9. Speichern

**Warenausgang buchen:**

Gleicher Prozess, aber:
- **Typ:** Reduzieren
- **Grund:** Verkauf, Schwund, Beschädigung

**Lagerbestand prüfen:**
- "Berichte" → "Bestandswert"
- Zeigt aktuellen Bestand aller Artikel
- Filter nach Lagerort möglich

---

## Bestellungen erstellen

### Kundenauftrag (Sales Order)

**Wenn Kunde bestellt:**

1. "Bestellungen" → "+ Neue Bestellung"
2. **Kunde:** Auswählen (aus Zoho CRM/Books)
3. **Bestellnummer:** Auto-generiert
4. **Bestelldatum:** Heute oder wählen

5. **Artikel hinzufügen:**
   - Klicke "+ Artikel hinzufügen"
   - Wähle aus Katalog
   - **Menge:** Anzahl
   - **Preis:** Verkaufspreis (vorausgefüllt)
   - Weitere Artikel hinzufügen

6. **Versanddetails:**
   - Lieferadresse (aus Kundendaten)
   - Versandart
   - Erwartetes Lieferdatum

7. **Speichern & Bestätigen**
   - "Speichern" für Entwurf
   - "Bestätigen" für aktive Bestellung

**Bestand wird automatisch reserviert!**

---

## Lieferungen erstellen

### Aus Bestellung versenden

**Wenn Ware versendet wird:**

1. Öffne Bestellung
2. Klicke "Lieferung erstellen"
3. **Lieferschein-Nummer:** Auto-generiert
4. **Verpackung:** Anzahl Pakete
5. **Versandanbieter:** DHL, UPS, etc.
6. **Tracking-Nummer:** Sendungsnummer eingeben

7. **Artikel prüfen:**
   - Liste zeigt bestellte Artikel
   - Menge anpassen falls Teillieferung

8. **Versand bestätigen**
   - "Versand markieren"
   - **Bestand wird automatisch reduziert**
   - Kunde erhält optional Tracking-Link

---

## Seriennummern verwalten

### Für einzeln verfolgbare Artikel

**Seriennummern-Tracking aktivieren:**

1. Öffne Artikel
2. Einstellungen → "Seriennummern verwalten" ✓
3. Speichern

**Bei Wareneingang:**
- System fragt nach Seriennummern
- Gib jede Seriennummer ein (z.B. SN001, SN002)
- Werden im System hinterlegt

**Bei Verkauf:**
- Wähle spezifische Seriennummer aus
- Historie bleibt erhalten (wer hat wann gekauft)

**Vorteil:**
- Rückverfolgbarkeit
- Garantie-Management
- Fehlersuche bei Defekten

---

## Bestellungen beim Lieferanten

### Purchase Order erstellen

**Wenn Nachschub benötigt wird:**

1. "Einkauf" → "+ Neue Bestellung"
2. **Lieferant:** Auswählen oder neu anlegen
3. **Bestelldatum:** Heute
4. **Lieferdatum:** Erwartete Lieferung

5. **Artikel hinzufügen:**
   - Wähle Artikel
   - **Menge:** Bestellmenge
   - **Preis:** Einkaufspreis (vom Lieferanten)

6. **Senden an Lieferant:**
   - "Speichern und senden"
   - E-Mail geht an Lieferant
   - PDF-Anhang

**Bei Wareneingang:**
- Purchase Order öffnen
- "Empfang erfassen"
- Menge bestätigen
- **Bestand wird automatisch erhöht**

---

## Mehrlager-Verwaltung

### Mehrere Lagerorte nutzen

**Lagerort anlegen:**

1. "Einstellungen" → "Lagerorte"
2. "+ Neuer Lagerort"
3. **Name:** z.B. "Hauptlager München"
4. **Adresse:** Vollständige Adresse
5. **Typ:** Warehouse, Filiale, Konsignationslager
6. Speichern

**Zwischen Lagern transferieren:**

1. "Transfers" → "+ Neuer Transfer"
2. **Von:** Quell-Lagerort
3. **Nach:** Ziel-Lagerort
4. **Artikel:** Auswählen
5. **Menge:** Transfer-Menge
6. **Grund:** Umverteilung, Retoure, etc.
7. Bestätigen

**Bestand pro Lagerort:**
- Berichte → Bestand nach Lagerort
- Zeigt Verteilung aller Artikel

---

## Barcode-Integration

### Artikel per Barcode scannen

**Setup:**

1. Einstellungen → "Barcode aktivieren"
2. Barcode-Format wählen (EAN-13, UPC, etc.)
3. Für jeden Artikel: Barcode hinterlegen

**Nutzung:**

- **Wareneingang:** Barcode scannen statt manuell wählen
- **Kommissionierung:** Scan zum Picken
- **Inventur:** Schnelle Bestandsaufnahme

**Hardware:**
- USB Barcode-Scanner
- Oder: Zoho Inventory Mobile App mit Kamera

---

## Integration mit Zoho Books

### Synchronisation Bestand ↔ Rechnung

**Automatischer Ablauf:**

1. **In Inventory:** Kundenauftrag erstellen
2. **Sync:** Auftrag erscheint in Zoho Books
3. **In Books:** Rechnung aus Auftrag erstellen
4. **Sync zurück:** Rechnungsstatus in Inventory

**Bestandsrelevanz:**
- Rechnung in Books = Bestand in Inventory reduziert
- Gutschrift in Books = Bestand in Inventory erhöht

**Konfiguration:**
- Settings → Integrations → Zoho → Books
- Aktivieren
- Mapping konfigurieren

---

## Versandintegrationen

### DHL, UPS, DPD anbinden

**Beispiel: DHL Integration**

1. Settings → Integrations → Shipping → DHL
2. API-Zugangsdaten eingeben (von DHL)
3. Standard-Paketgrößen konfigurieren

**Bei Lieferung:**
- "Versandetikett drucken"
- System erstellt automatisch DHL-Label
- Tracking-Nummer wird übernommen
- Kunde erhält Tracking-Link

**Unterstützte Anbieter:**
- DHL
- UPS
- FedEx
- DPD
- Hermes

---

## Berichte & Analysen

### Wichtige Berichte

**Bestandswert:**
- Berichte → Bestandswert
- Zeigt Gesamtwert des Lagers
- Nach Artikel, Kategorie, Lagerort

**Bewegungshistorie:**
- Berichte → Bestandsbewegungen
- Alle Ein- und Ausgänge
- Zeitraum wählbar

**Niedrigbestand-Warnung:**
- Berichte → Artikel unter Mindestbestand
- Zeigt kritische Artikel
- → Nachbestellung auslösen

**Bestseller:**
- Berichte → Meistverkaufte Artikel
- Zeitraum: Monat, Quartal, Jahr
- Für Einkaufsplanung

---

## E-Commerce Integration

### Shopify, WooCommerce, Amazon

**Beispiel: Shopify-Integration**

1. Settings → Integrations → E-Commerce → Shopify
2. Shopify Store verbinden (OAuth)
3. Sync-Einstellungen:
   - ✓ Bestand synchronisieren
   - ✓ Bestellungen importieren
   - ✓ Preise aktualisieren

**Automatischer Ablauf:**
- Kunde bestellt in Shopify
- Bestellung importiert nach Inventory
- Bestand wird reduziert
- Bestand synct zurück zu Shopify
- Lieferung erfassen → Tracking zu Shopify

---

## Mobile App

### Zoho Inventory unterwegs

**Funktionen:**
- Bestand prüfen
- Bestellungen erfassen
- Barcode scannen (Kamera)
- Lieferungen markieren
- Bestandsanpassungen

**Installation:**
- iOS: App Store
- Android: Google Play
- Suche: "Zoho Inventory"

**Offline-Modus:**
- Daten werden gecacht
- Änderungen offline möglich
- Auto-Sync bei Internetverbindung

---

## Häufige Fragen

### Wie mache ich eine Inventur?

1. "Bestandsanpassung" → "Inventur"
2. Wähle Lagerort
3. Zähle physisch alle Artikel
4. Gib Ist-Bestand ein
5. System vergleicht mit Soll-Bestand
6. Differenzen werden angezeigt
7. Bestätige → Bestand wird korrigiert

### Wie erstelle ich Bundles/Sets?

1. Neuer Artikel → Typ: "Paket"
2. Füge mehrere Einzelartikel hinzu
3. Verkaufspreis für das gesamte Set
4. Bei Verkauf: Einzelartikel-Bestand wird reduziert

### Wie tracke ich Chargen?

Ähnlich wie Seriennummern:
- Artikel-Einstellungen → "Chargen verwalten"
- Bei Wareneingang: Chargennummer eingeben (z.B. LOT2026-001)
- Für Lebensmittel, Pharma (MHD-Tracking)

---

## aboutwater-spezifisch

### Lagerhaltung bei aboutwater

**Lagerorte:**
1. Hauptlager: München
2. Außenlager: Berlin (für Nordkunden)

**Standard-Prozess:**
- Wareneingang: Hauptlager München
- Transfer nach Berlin: Wöchentlich (nach Bedarf)
- Versand: Vom nächstgelegenen Lager

**Mindestbestände:**
- A-Artikel (Bestseller): 100 Stück
- B-Artikel: 50 Stück
- C-Artikel: 20 Stück

---

## Tipps & Best Practices

### Bestandsoptimierung

- Wöchentliche Niedrigbestand-Prüfung
- ABC-Analyse nutzen
- Saisonale Schwankungen berücksichtigen
- Lieferantenperformance tracken

### Fehlerve rmeidung

- Doppelte SKUs vermeiden
- Seriennummern für teure Artikel
- Regelmäßige Inventuren (quartalsweise)
- Mehraugenprinzip bei Anpassungen

---

**Hinweis:** Sample-Dokumentation. Für vollständige Infos siehe https://www.zoho.com/inventory/help/
