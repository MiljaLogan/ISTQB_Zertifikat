### Behebung und Berichterstattung als Prozessabschluss

Die abschließende Phase des <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Prozesses gewährleistet die systematische Umsetzung der identifizierten Verbesserungen und dokumentiert die Ergebnisse für zukünftige Prozessoptimierungen.

### Berichterstattung und Dokumentation

#### Protokoll-basierte Dokumentation

Häufig enthält das <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Protokoll bereits alle erforderlichen Informationen:

**Vollständige Protokollinhalte:**
* **Identifizierte <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a>**: Systematische Auflistung aller Befunde
* **Schweregrad-Bewertungen**: Priorisierung der Korrekturen
* **Verantwortlichkeiten**: Zuordnung der Bearbeitungsaufgaben
* **Zeitrahmen**: Terminvorgaben für Korrekturen
* **Akzeptanzentscheidung**: Gesamtbewertung des Dokuments

*Beispiel:* Das Protokoll eines Pixel Leap API-<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> könnte 15 identifizierte Probleme enthalten, davon 2 kritische Fehler (fehlende Authentifizierung), 8 Hauptfehler (unvollständige Parameter) und 5 Nebenfehler (Formatierungsprobleme).

#### Ergänzende Fehlerberichte

Zusätzliche <a href="./Glossar.md#fehlerbericht" title="→ Glossar öffnen" class="glossary-term">**Fehlerberichte**</a> werden erstellt, wenn:

* **Komplexe Probleme**: Detaillierte Erläuterung erforderlich
* **Externe Stakeholder**: Kommunikation außerhalb des <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Teams
* **Tracking-Systeme**: Integration in <a href="./Glossar.md#fehlerverfolgung" title="→ Glossar öffnen" class="glossary-term">**Fehlerverfolgungssysteme**</a>
* **Audit-Anforderungen**: Compliance-Dokumentation

### Korrekturumsetzung und Kommunikation

#### Autorenseitige Problembehandlung

Der Dokumentenautor trägt die Hauptverantwortung für die Korrekturumsetzung:

**Typische Korrekturmaßnahmen:**
* **Inhaltliche Überarbeitung**: Behebung fachlicher <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a>
* **Strukturelle Anpassungen**: Verbesserung der Dokumentenorganisation
* **Ergänzungen**: Hinzufügung fehlender Informationen
* **Klarstellungen**: Beseitigung von Mehrdeutigkeiten

#### Kommunikative Herausforderungen

> Kommunikatives Geschick ist erforderlich, da sich kaum eine Person über die Mitteilung von Fehlern in den eigenen Arbeitsergebnissen freut.

**Konstruktive Kommunikationsstrategien:**
* **Sachliche Fokussierung**: Betonung der Dokumentenverbesserung
* **Positive Rahmung**: Hervorhebung der Qualitätssteigerung
* **Lösungsorientierung**: Konstruktive Verbesserungsvorschläge
* **Wertschätzung**: Anerkennung der geleisteten Arbeit

*Beispiel:* Statt "Ihre Spezifikation enthält 12 Fehler" könnte kommuniziert werden: "Das <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a> hat 12 Verbesserungsmöglichkeiten identifiziert, die die Pixel Leap API-Spezifikation noch robuster machen werden."

### Formale Review-Anforderungen

#### Status-Management und Verfolgung

> <a href="./Glossar.md#formales-review" title="→ Glossar öffnen" class="glossary-term">**Formale Reviews**</a> verlangen mehr strukturierte Nachverfolgung.

**<a href="./Glossar.md#status" title="→ Glossar öffnen" class="glossary-term">Status</a>-Kategorien für <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a>:**

| <a href="./Glossar.md#status" title="→ Glossar öffnen" class="glossary-term">**Status**</a> | Beschreibung | Verantwortlichkeit | Nächster Schritt |
|--------|--------------|-------------------|------------------|
| **Offen** | Problem identifiziert | <a href="./Glossar.md#gutachter" title="→ Glossar öffnen" class="glossary-term">**Gutachter**</a> | Autor bearbeitet |
| **In Bearbeitung** | Korrektur läuft | Autor | Fertigstellung |
| **Behoben** | Korrektur implementiert | Autor | <a href="./Glossar.md#gutachter" title="→ Glossar öffnen" class="glossary-term">**Gutachter**</a> prüft |
| **Verifiziert** | Korrektur bestätigt | <a href="./Glossar.md#gutachter" title="→ Glossar öffnen" class="glossary-term">**Gutachter**</a> | Abschluss |
| **Abgelehnt** | Korrektur unzureichend | <a href="./Glossar.md#gutachter" title="→ Glossar öffnen" class="glossary-term">**Gutachter**</a> | Nachbesserung |

#### Reviewer-Zustimmung und Qualitätskontrolle

**Kontrollierte Status-Übergänge:**
* **<a href="./Glossar.md#gutachter" title="→ Glossar öffnen" class="glossary-term">Gutachter</a>-Freigabe**: Bestätigung der Korrekturqualität
* **Nachverfolgung**: Systematische Überwachung des Fortschritts
* **Eskalation**: Behandlung strittiger Fälle
* **Dokumentation**: Vollständige Aufzeichnung aller Änderungen

*Beispiel:* Bei einem kritischen Sicherheitsfehler in der Pixel Leap Authentifizierung muss der Sicherheitsexperte als <a href="./Glossar.md#gutachter" title="→ Glossar öffnen" class="glossary-term">**Gutachter**</a> die Korrektur explizit freigeben, bevor der <a href="./Glossar.md#status" title="→ Glossar öffnen" class="glossary-term">**Status**</a> auf "Verifiziert" gesetzt werden kann.

#### Endekriterien-Prüfung

Die Erfüllung der <a href="./Glossar.md#endekriterien" title="→ Glossar öffnen" class="glossary-term">**Endekriterien**</a> muss systematisch verifiziert werden:

**Typische <a href="./Glossar.md#endekriterien" title="→ Glossar öffnen" class="glossary-term">**Endekriterien**</a>:**
* **Alle kritischen Fehler behoben**: Keine blockierenden Probleme
* **Hauptfehler adressiert**: Wesentliche Qualitätsmängel beseitigt
* **<a href="./Glossar.md#gutachter" title="→ Glossar öffnen" class="glossary-term">Gutachter</a>-Freigaben**: Bestätigungen aller Verantwortlichen
* **Dokumentation vollständig**: Alle Änderungen dokumentiert

### Prozessverbesserung und Metriken

#### Systematische Auswertung

<a href="./Glossar.md#formales-review" title="→ Glossar öffnen" class="glossary-term">**Formale Reviews**</a> erfordern umfassende Prozessanalyse:

**Auswertungsdimensionen:**
* **Effektivität**: Anzahl und Qualität identifizierter <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a>
* **Effizienz**: Aufwand-Nutzen-Verhältnis des <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a>
* **Prozessqualität**: Einhaltung der definierten Abläufe
* **Teilnehmerzufriedenheit**: Bewertung der <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Erfahrung

#### Kontinuierliche Optimierung

**Verbesserungsmaßnahmen:**
* **<a href="./Glossar.md#checkliste" title="→ Glossar öffnen" class="glossary-term">Checklisten</a>-Aktualisierung**: Anpassung an neue Erkenntnisse
* **Prozess-Refinement**: Optimierung der Abläufe
* **Schulungsbedarfe**: Kompetenzentwicklung der Beteiligten
* **Werkzeug-Verbesserung**: Technische Unterstützung optimieren

*Beispiel:* Nach mehreren Pixel Leap <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> könnte festgestellt werden, dass Performance-Aspekte häufig übersehen werden, was zur Ergänzung entsprechender <a href="./Glossar.md#checkliste" title="→ Glossar öffnen" class="glossary-term">**Checklisten**</a>-Punkte führt.

### Individuelle Review-Verfahren (Exkurs)

#### Ad-hoc-Vorgehen

> Keine Vorgaben sind beim Ad-hoc-<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a> gegeben.

**Charakteristika:**
* **Freie Herangehensweise**: Keine methodischen Vorgaben
* **Sequenzielle Bearbeitung**: Lineares Durchlesen des Dokuments
* **Intuitive Problemerkennung**: Erfahrungsbasierte Bewertung
* **Flexible Dokumentation**: Keine standardisierten Formate

**Vor- und Nachteile:**
* **Vorteile**: Geringer Vorbereitungsaufwand, schnelle Durchführung
* **Nachteile**: Abhängigkeit von individuellen Fähigkeiten, Doppelnennungen

#### Checklisten-basiertes Vorgehen

> <a href="./Glossar.md#checkliste" title="→ Glossar öffnen" class="glossary-term">**Checklisten**</a> unterstützen strukturiertes Lesen und steigern die Effektivität.

**Beispiel-<a href="./Glossar.md#checkliste" title="→ Glossar öffnen" class="glossary-term">**Checkliste**</a> für Anforderungsdokumente:**
- [ ] Liegt das Anforderungsdokument in standardisierter Struktur vor?
- [ ] Existiert ein einleitendes Kapitel zur Dokumentennutzung?
- [ ] Gibt es eine zusammenfassende Projektbeschreibung?
- [ ] Ist ein <a href="./Glossar.md#glossar" title="→ Glossar öffnen" class="glossary-term">**Glossar**</a> für einheitliches Begriffsverständnis vorhanden?

**<a href="./Glossar.md#checkliste" title="→ Glossar öffnen" class="glossary-term">Checklisten</a>-Management:**
* **Regelmäßige Aktualisierung**: Integration neuer Erkenntnisse
* **Spezifische Anpassung**: Dokumenttyp-spezifische Listen
* **Fokussierung**: Beschränkung auf wesentliche Aspekte
* **Ergänzende Suche**: Berücksichtigung von Problemen außerhalb der Liste

#### Szenario-basiertes Vorgehen

> Individuelles "Durchspielen" der späteren Nutzung erhöht die Realitätsnähe.

**<a href="./Glossar.md#use-case" title="→ Glossar öffnen" class="glossary-term">Use-Case</a>-basierte Bewertung:**
* **Anwendungsfall-Simulation**: Nachvollziehen realer Nutzungsszenarien
* **Fehlerklassen-fokussierte Analyse**: Konzentration auf spezifische Problemtypen
* **Strukturierte Richtlinien**: Vorgaben für die Dokumentendurcharbeitung

*Beispiel:* Bei einem Pixel Leap Multiplayer-<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a> könnte ein <a href="./Glossar.md#gutachter" title="→ Glossar öffnen" class="glossary-term">**Gutachter**</a> das Szenario "Spieler tritt Multiplayer-Spiel bei" durchspielen und dabei alle relevanten Spezifikationsabschnitte auf Konsistenz prüfen.

#### Rollenbasiertes und perspektivisches Vorgehen

> Unterschiedliche Rollen und Perspektiven nutzen spezifisches Fachwissen.

**Rollenbasierte Spezialisierung:**
* **Tester-Perspektive**: Fokus auf <a href="./Glossar.md#testbarkeit" title="→ Glossar öffnen" class="glossary-term">**Testbarkeit**</a> und Messbarkeit
* **Designer-Sicht**: Architektonische Auswirkungen und Implementierbarkeit
* **Anwender-Perspektive**: Usability und Funktionalität
* **Administrator-Rolle**: Betrieb und Wartung

**Beispiel rollenbasiertes <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>:**
Ein Anforderungsdokument wird von verschiedenen Rollen bewertet:
- **Designer**: Prüft Auswirkungen auf Systemarchitektur
- **Testerin**: Bewertet Messbarkeit ("zügiges Arbeiten" → konkrete Zeitangaben erforderlich)
- **Endanwender**: Evaluiert Praxistauglichkeit der Funktionen

#### Perspektivisches Vorgehen

> Unterschiedliche Standpunkte berücksichtigen subjektive Stakeholder-Interessen.

**Stakeholder-Perspektiven:**
* **Verkaufssicht**: Kundenanforderungen und Marktrelevanz
* **Entwicklungsperspektive**: Technische Machbarkeit und Aufwand
* **Test-Standpunkt**: Qualitätssicherung und Risikobewertung
* **Management-Sicht**: Ressourcen und Zeitplanung

*Beispiel perspektivisches <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>:*
Bei der Bewertung eines neuen Pixel Leap Features:
- **Verkauf**: Hohe Priorität wegen Kundenwunsch
- **Test**: Niedrige Komplexität, schnelle Umsetzung möglich
- **Entwicklung**: KI-Feature erfordert hohen Lernaufwand

**Empirische Evidenz:**
> Studien sehen das perspektivische <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a> als effektivstes Vorgehen zur Prüfung von Anforderungen und technischen Beschreibungen.

Die systematische Behebung und Berichterstattung schließt den <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Prozess ab und gewährleistet sowohl die Umsetzung der Qualitätsverbesserungen als auch die kontinuierliche Optimierung der <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Verfahren selbst.