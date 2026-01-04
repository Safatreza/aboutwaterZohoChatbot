# Zoho Mail Article

**Source:** https://www.zoho.com/mail/help/adminconsole/email-hosting-setup.html
**Crawled:** 2026-01-04

---

# Hallo! Wie können wir Ihnen helfen?

# E-Mail Hosting in Zoho einrichten

Die Zoho Mail Suite bietet [Unternehmensfunktionen](/mail/enterprise-email.html) für [E-Mail-Hosting](/mail/), die den Anforderungen von Unternehmen aller Arten und Größenordnung gerecht werden. Zoho Mail bietet im Handumdrehen spezifische, domänenbasierte E-Mail-Adressen für alle Mitglieder Ihres Unternehmens. Der gesamte Setup-Prozess ist sehr einfach. Die Schritte zur Migration des E-Mail Hosting an Zoho sowie einige der verfügbaren Funktionen werden hier beschrieben.

[Domäne kaufen](/mail/buy-domain.html) | [Domäne hinzufügen](/mail/help/adminconsole/add-domains.html "Domänen in Zoho hinzufügen") | [Domäne überprüfen](/mail/help/adminconsole/domain-verification.html) | [Benutzer erstellen](/mail/help/adminconsole/adding-users.html) | [MX-Einträge konfigurieren](/mail/help/adminconsole/configure-email-delivery.html) | [E-Mail-Migration](/mail/help/adminconsole/pop-imap-migration.html) | [SPF-Konfiguration](/mail/help/adminconsole/spf-configuration.html) | [DKIM-Konfiguration](/mail/help/adminconsole/dkim-configuration.html)

Sobald Sie das gesamte E-Mail Hosting in Zoho eingerichtet haben, können Sie als Super-Admin auf die Admin-Konsole zugreifen, die zur Verwaltung der E-Mail-Einstellungen des Unternehmens verwendet wird. Es gibt in der Admin-Konsole zahlreiche Möglichkeiten, um Richtlinien für Compliance zu erstellen, Konten zu sichern, Adressbücher zu verwalten, Ressourcen zu buchen usw. Alle Optionen sind menügesteuert, damit Administratoren keine komplexen Befehle oder Codedateien für die Verwaltung der Benutzer und des E-Mail-Service erstellen müssen.

### Die Domäne überprüfen

Sie müssen die [Domäne](/mail/glossary/what-is-domain.html), für die das E-Mail-Hosting eingerichtet werden soll, [hinzufügen](/mail/help/adminconsole/add-domains.html) und überprüfen. Die [Überprüfung](/mail/help/adminconsole/domain-verification.html) ist erforderlich, um sicherzustellen, dass Sie über Administratorrechte für die Domäne verfügen und berechtigt sind, die Domäne mit unseren Services einzurichten und zu verwenden. Wenn Sie Ihre Domäne über Zoho registriert haben, dann können Sie diesen Schritt überspringen.

### Benutzer hinzufügen

Nachdem Ihre Domäne überprüft worden ist, können Sie [Benutzer hinzufügen oder importieren](/mail/help/adminconsole/adding-users.html) und E-Mail-Konten für sie erstellen. Richten Sie [Gruppen](/mail/help/adminconsole/creating-groups.html) für gemeinsame Konten ein, die von mehr als einem Benutzer verwendet werden. Sie können mehrere E-Mail-Adressen für einen einzelnen Benutzer erstellen, indem Sie mehrere [E-Mail-Aliasse](/mail/how-to/create-email-alias.html) für dasselbe Benutzerkonto einrichten.

### MX-Einträge einrichten/Zustellung von E-Mails konfigurieren

Sobald Sie die E-Mail-Konten hinzugefügt haben, müssen Sie die [MX-Einträge](/mail/help/adminconsole/configure-email-delivery.html) für die Domäne ändern. Nachdem Sie die MX-Einträge eingerichtet haben, werden E-Mails an Ihr Zoho Mail-Konto geliefert. Klicken Sie hier, um mehr über die erweiterten Optionen zum [E-Mail Routing](/mail/help/adminconsole/email-routing.html) in Zoho Mail zu erfahren.

### IMAP- oder POP-Migration

Migrieren Sie E-Mail-Konten von Ihrem vorherigen Server mithilfe von [POP- oder IMAP](/mail/help/adminconsole/pop-imap-migration.html)-Protokollen. Sie können sich auch für eine PST-Migration oder Exchange-Migration entscheiden, wenn sich Ihre E-Mails auf Ihrem Exchange Server oder in PST-Dateien befinden.

### SPF-Konfiguration

Wir empfehlen, E-Mails, die von Ihrer Domäne versendet werden, mithilfe von Sender Policy Framework (SPF)-Einträgen zu validieren. [SPF-Einträge](/mail/help/adminconsole/spf-configuration.html) werden auch verwendet, um E-Mail Spoofing (E-Mails, die von Spammern gesendet werden, die die Absender-Adresse in Ihrer Domäne gefälscht haben) zu verhindern, indem festgelegt wird, welche IP-Adressen und Mailserver E-Mails im Auftrag Ihrer Domäne versenden dürfen.

### DKIM (DomainKeys Identified Mail)-Konfiguration

[DKIM](/mail/help/adminconsole/dkim-configuration.html) ist ein gängiges System zur Authentifizierung von E-Mails, das eine eindeutige Signatur in der Kopfzeile umfasst, die durch einen privaten Schlüssel generiert wird, der für die spezifische Domäne konfiguriert wurde. Der öffentliche Schlüssel, der in Ihrem DNS veröffentlicht wird, wird verwendet, um die DKIM-Signatur durch den empfangenden Server zu validieren. Auf Grundlage der Validierungsergebnisse wird die E-Mail als echt oder Spam klassifiziert.

### Zusätzliche Setup-Optionen

**Catch all Setup** : Ein [Catch-all-Konto](/mail/help/adminconsole/catch-all-setup.html) wird eingerichtet, um sicherzustellen, dass E-Mails, die zwar an Ihre Domäne adressiert sind, jedoch an ein Konto, das es nicht gibt oder das falsch geschrieben wurde, nicht verloren gehen. Solche E-Mails werden an das Catch-all-Konto weitergeleitet. Wenn Sie beispielsweise Konten für manager@thatcompany.com und info@thatcompany.com eingerichtet haben, aber ein Absender eine E-Mail an help@thatcompany.com sendet, obwohl Sie diese Adresse nicht eingerichtet haben, wird diese E-Mail an ein Catch-all-Konto weitergeleitet, anstatt dass sie als nicht zustellbar zurückgesendet wird.

**Dual delivery** : Richten Sie die [doppelte Zustellung](/mail/help/adminconsole/configure-dual-delivery.html) für Ihre Domäne ein, indem Sie einen zweiten Mailserver für Ihre Domäne konfigurieren.

**Login page customization** : Sie können eine [persönliche Anmelde-URL erstellen](/mail/help/adminconsole/org-settings.html#alink7), wenn Sie einen CNAME-Alias (der auf business.zoho.com verweist) zu Ihren DNS-Einträgen hinzufügen. Sie können die Seite noch weiter anpassen, indem Sie das Logo Ihres Unternehmens über die Admin-Konsole von Zoho Mail hochladen.

**Miscellaneous** : Sobald Sie die Webmail eingerichtet haben, rufen Sie die Seiten [POP](/mail/help/pop-access.html) und [IMAP](/mail/help/imap-access.html) auf, um die Konfiguration in POP- und IMAP-Clients fortzuführen, wie Outlook, iPhone usw. Zoho Mail bietet auch Services für die [Domänenregistrierung](/mail/help/adminconsole/domains.html) und automatische Erneuerung. Domänen, die über Zoho registriert werden, können nahtlos mit Zoho Mail verwendet werden. Die Überprüfung der Domäne erfolgt automatisch, und MX-Einträge sind vorkonfiguriert.

## Verwandte Seiten

  * [Erste Schritte mit Zoho Mail](/mail/help/login-to-zoho.html)
  * [Domänenregistrierung](/mail/help/adminconsole/domains.html)
  * [POP-Konfiguration](/mail/help/pop-access.html)
  * [IMAP-Konfiguration](/mail/help/imap-access.html)
  * [Erstellen von Gruppen](/mail/help/adminconsole/creating-groups.html)
  * [Assistent für die Migration von Benutzern und E-Mails in Zoho](/mail/help/adminconsole/zoho-mail-migration-wizard.html)



### Sie können noch immer nicht finden, wonach Sie suchen?

Schreiben Sie uns an: [support@zohomail.com](mailto:support@zohomail.com)