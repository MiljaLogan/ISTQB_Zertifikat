### Prüfbare Arbeitsergebnisse in der Softwareentwicklung

Die moderne Softwareentwicklung erzeugt eine Vielzahl von Arbeitsergebnissen, die alle zur Gesamtqualität des entstehenden Systems beitragen. <a href="./Glossar.md#statischer-test" title="→ Glossar öffnen" class="glossary-term">**Statische Tests**</a> ermöglichen die systematische Bewertung dieser Artefakte, bevor sie als Grundlage für nachfolgende Entwicklungsaktivitäten dienen.

### Spezifikationen und Anforderungsdokumente

#### Klassische Spezifikationsarten

<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> können auf alle Arten von Spezifikationen angewendet werden, um <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> zu identifizieren, bevor diese in die Implementierung einfließen:

* **Geschäftsanforderungen**: Strategische Ziele und Geschäftsprozesse
* **<a href="./Glossar.md#funktionaler-test" title="→ Glossar öffnen" class="glossary-term">Funktionale Anforderungen</a>**: Systemverhalten und Features
* **<a href="./Glossar.md#nicht-funktionaler-test" title="→ Glossar öffnen" class="glossary-term">Nicht-funktionale Anforderungen</a>**: Performance, Usability, Skalierbarkeit
* **<a href="./Glossar.md#sicherheit-security" title="→ Glossar öffnen" class="glossary-term">Sicherheitsanforderungen</a>**: Datenschutz, Zugriffskontrolle, Compliance

*Beispiel:* Bei Pixel Leap könnte ein <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a> der Performance-Anforderungen aufdecken, dass die Spezifikation "flüssiges Gameplay" zu unspezifisch ist und konkrete Framerate-Ziele (60 FPS) definiert werden müssen.

#### Häufige Probleme in Spezifikationen

<a href="./Glossar.md#statische-analyse" title="→ Glossar öffnen" class="glossary-term">**Statische Analysen**</a> identifizieren typische Qualitätsmängel in Anforderungsdokumenten:

| Problemtyp | Beschreibung | Auswirkung |
|------------|--------------|------------|
| **Inkonsistenzen** | Widersprüchliche Aussagen | Implementierungsunsicherheit |
| **Mehrdeutigkeiten** | Interpretationsspielräume | Unterschiedliche Umsetzungen |
| **Widersprüche** | Sich ausschließende Anforderungen | Unlösbare Konflikte |
| **Lücken** | Fehlende Informationen | Unvollständige Implementierung |
| **Ungenauigkeiten** | Vage Formulierungen | Qualitätsprobleme |
| **Redundanzen** | Doppelte Inhalte | Wartungsaufwand |

### Agile Entwicklungsartefakte

#### User Stories und Backlog-Elemente

In <a href="./Glossar.md#agile-softwareentwicklung" title="→ Glossar öffnen" class="glossary-term">**agilen Entwicklungsumgebungen**</a> fokussieren sich <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> auf spezifische Artefakte:

* **Epics**: Übergeordnete Funktionalitätsbereiche
* **<a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">User Stories</a>**: Konkrete Benutzeranforderungen
* **Product-Backlog-Elemente**: Priorisierte Entwicklungsaufgaben
* **<a href="./Glossar.md#test-charta" title="→ Glossar öffnen" class="glossary-term">Test-Chartas</a>**: Explorative Testrichtlinien

#### Kollaborative Reviewprozesse

<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> unterstützen agile Kollaborationspraktiken:

* **Example Mapping**: Gemeinsame Konkretisierung von Anforderungen
* **Story Writing**: Kollaborative Erstellung von <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a>
* **Backlog Refinement**: Kontinuierliche Verbesserung der Anforderungen

*Beispiel:* Ein <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a> einer Pixel Leap <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> "Als Spieler möchte ich präzise springen können" würde prüfen, ob messbare <a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a> wie "Input-Latenz unter 50ms" definiert sind.

#### Definition of Ready

<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> stellen sicher, dass <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a> definierten Qualitätskriterien entsprechen:

* **Vollständigkeit**: Alle notwendigen Informationen vorhanden
* **Verständlichkeit**: Klare, eindeutige Formulierung
* **Testbarkeit**: Messbare <a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a>
* **Schätzbarkeit**: Aufwand bewertbar

### Architektur- und Entwurfsdokumente

#### Strukturelle Designartefakte

Während der Entwurfsphase entstehen verschiedene Modelle und Spezifikationen, die durch <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> bewertet werden können:

* **Architekturspezifikationen**: Systemstruktur und Komponentenbeziehungen
* **Klassendiagramme**: Objektorientierte Designmodelle
* **Schnittstellendefinitionen**: API-Spezifikationen
* **Datenmodelle**: Datenbankstrukturen und -beziehungen

*Beispiel:* Ein Architektur-<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a> für Pixel Leap könnte die Trennung zwischen Sprungmechanik-Komponente und Rendering-System bewerten und potenzielle Performance-Engpässe identifizieren.

#### Web-Entwicklungsartefakte

Auch webspezifische Entwicklungsartefakte sind <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-geeignet:

* **HTML-Strukturen**: Semantische Korrektheit
* **CSS-Stylesheets**: Konsistenz und Wartbarkeit
* **JavaScript-Code**: Funktionalität und Performance

### Testbezogene Arbeitsergebnisse

#### Testdokumentation

Alle beim <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> entstehenden <a href="./Glossar.md#testmittel" title="→ Glossar öffnen" class="glossary-term">**Testmittel**</a> profitieren von systematischen <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a>:

* **<a href="./Glossar.md#testkonzept" title="→ Glossar öffnen" class="glossary-term">Testkonzepte</a>**: Strategische Testplanung
* **<a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">Testfälle</a>**: Spezifische Prüfszenarien
* **<a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">Testabläufe</a>**: Ausführungssequenzen
* **<a href="./Glossar.md#testskript" title="→ Glossar öffnen" class="glossary-term">Testskripte</a>**: Automatisierte Testprozeduren

#### Akzeptanzkriterien

<a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a> und <a href="./Glossar.md#abnahmetest" title="→ Glossar öffnen" class="glossary-term">**Abnahmetest**</a>-Spezifikationen erfordern besondere Aufmerksamkeit, da sie die finale Qualitätsbewertung definieren.

*Beispiel:* <a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a> für Pixel Leap's Kollisionssystem könnten spezifizieren: "Kollisionserkennung funktioniert bei 100+ gleichzeitigen NPCs ohne Framerate-Einbruch unter 55 FPS."

### Projektmanagement-Dokumente

#### Planungs- und Steuerungsdokumente

<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> erstrecken sich auch auf projektbezogene Arbeitsergebnisse:

* **Verträge**: Rechtliche und technische Vereinbarungen
* **Projektpläne**: Zeitliche und ressourcenbezogene Planung
* **Budget- und Zeitpläne**: Wirtschaftliche Projektsteuerung
* **Benutzeranleitungen**: Dokumentation für Endanwender

### Grenzen der statischen Analyse

#### Nicht analysierbare Artefakte

Bestimmte Arbeitsergebnisse eignen sich nicht für <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a>:

* **Schwer interpretierbare Dokumente**: Unstrukturierte oder unverständliche Inhalte
* **Rechtlich geschützte Artefakte**: Drittanbieter-Code ohne Analyserechte
* **Binäre Ausführungsdateien**: Ohne Quellcode-Zugang

> Menschliche Analyse- und Denkfähigkeit ist Voraussetzung für effektive <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a>. Dokumente müssen interpretierbar und verständlich sein.

### Prozessverbesserung durch Reviews

#### Kontinuierliche Optimierung

<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Ergebnisse ermöglichen die systematische Verbesserung des Entwicklungsprozesses:

* **Fehleranalyse**: Identifikation wiederkehrender Problemmuster
* **Prozessoptimierung**: Anpassung problematischer Arbeitsschritte
* **Schulungsbedarfe**: Gezielte Weiterbildung der Teammitglieder
* **<a href="./Glossar.md#qualitaetssicherung" title="→ Glossar öffnen" class="glossary-term">Qualitätssicherung</a>**: Präventive Maßnahmen zur Fehlervermeidung

*Beispiel:* Häufige Inkonsistenzen in Pixel Leap's Physik-Spezifikationen könnten auf unzureichende Abstimmung zwischen Game-Design und Entwicklung hinweisen, was durch verbesserte Kollaborationsprozesse adressiert werden könnte.

Die Vielfalt prüfbarer Arbeitsergebnisse zeigt das umfassende Potenzial <a href="./Glossar.md#statischer-test" title="→ Glossar öffnen" class="glossary-term">**statischer Tests**</a> für die <a href="./Glossar.md#qualitaetssicherung" title="→ Glossar öffnen" class="glossary-term">**Qualitätssicherung**</a> in der Softwareentwicklung.