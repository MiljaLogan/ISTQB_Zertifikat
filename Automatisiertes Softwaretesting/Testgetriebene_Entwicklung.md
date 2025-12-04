und # Testgetriebene Entwicklung und moderne Entwicklungspraktiken

## Einleitung

Die moderne Softwareentwicklung hat sich in den letzten Jahrzehnten grundlegend gewandelt. Während früher Tests typischerweise erst nach der Implementierung durchgeführt wurden, setzen heute viele Entwicklungsteams auf Ansätze, bei denen das Testen bereits vor dem Schreiben des Produktionscodes beginnt. Diese Umkehrung der traditionellen Reihenfolge – Tests vor Code – bildet das Fundament für eine Reihe innovativer Praktiken, die nicht nur die Softwarequalität verbessern, sondern auch den gesamten Entwicklungsprozess effizienter gestalten. In Kombination mit Automatisierung und kontinuierlichen Prozessen entstehen so leistungsfähige Entwicklungsumgebungen, die schnelle Feedbackzyklen ermöglichen und die Zusammenarbeit zwischen verschiedenen Teams fördern.

---

### Test-First: Das Grundprinzip der testgetriebenen Entwicklung

#### Umkehrung der traditionellen Testreihenfolge

Das zentrale Merkmal testgetriebener Ansätze besteht darin, dass <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> bereits vor der eigentlichen Programmierung entworfen und automatisiert werden. Diese grundlegende Umkehrung der üblichen Arbeitsweise bedeutet, dass zum Zeitpunkt der Implementierung oder Änderung von Produktcode die entsprechenden automatisierten Tests bereits vollständig vorliegen.

> **Kernprinzip:** Tests werden geschrieben, bevor der zu testende Code existiert.

#### Unmittelbares Feedback durch sofortige Testausführung

Sobald auch nur kleinste Änderungen am Code vorgenommen werden, können die vorbereiteten Tests sofort ausgeführt werden. Eine Codeänderung gilt erst dann als abgeschlossen, wenn sämtliche zugehörigen Tests erfolgreich durchlaufen wurden. Treten <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> auf, muss der Code unmittelbar korrigiert werden. Diese Vorgehensweise verkörpert das Konzept des frühestmöglichen Testens – oft als <a href="./Glossar.md#shift-left" title="→ Glossar öffnen" class="glossary-term">**Shift-Left**</a> bezeichnet – in besonders konsequenter Form.

*Beispiel:* Bei der Entwicklung des Videospiels Pixel Leap würde ein Entwickler zunächst automatisierte Tests für die Sprungmechanik schreiben, die definieren, wie hoch und weit die Spielfigur springen soll. Erst danach wird der eigentliche Code für die Sprungfunktion implementiert und muss diese Tests bestehen.

#### Tests als ausführbare Spezifikation

Die im Voraus erstellten Testfälle definieren präzise das erwartete Verhalten des zu entwickelnden Codes. Damit übernehmen sie faktisch die Rolle einer Spezifikation – allerdings in einer Form, die direkt vom Computer ausgeführt und überprüft werden kann. Bei konsequenter Anwendung dieses Prinzips können automatisierte Tests herkömmliche Spezifikationsdokumente in Textform teilweise oder vollständig ersetzen.

#### Steuerungsfunktion der Tests

Durch diese beiden Aspekte – unmittelbares Feedback und Spezifikationscharakter – nehmen die vorab definierten Tests eine steuernde Rolle ein: Sie lenken den Ablauf der Programmierarbeiten und geben vor, welche Funktionalität als nächstes implementiert werden muss. Diese steuernde Wirkung erstreckt sich letztlich auf den gesamten Entwicklungsprozess, was die Bezeichnung „testgetrieben" rechtfertigt.

---

### Varianten testgetriebener Ansätze

Je nachdem, auf welcher <a href="./Glossar.md#teststufe" title="→ Glossar öffnen" class="glossary-term">**Teststufe**</a> diese Praktiken eingesetzt werden und welche Werkzeuge zur Automatisierung verwendet werden, haben sich verschiedene Ausprägungen testgetriebener Entwicklung etabliert:

#### Testgetriebene Entwicklung (Test-Driven Development, TDD)

<a href="./Glossar.md#testgetriebene-entwicklung" title="→ Glossar öffnen" class="glossary-term">**Testgetriebene Entwicklung**</a> bezeichnet die ursprüngliche Variante, bei der der Test-First-Ansatz auf der Ebene des <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententests**</a> angewendet wird. Für die Automatisierung kommen spezielle <a href="./Glossar.md#unittest-framework" title="→ Glossar öffnen" class="glossary-term">**Unit-Test-Frameworks**</a> zum Einsatz.

**Hauptmerkmale:**
* Fokus auf einzelne <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponenten**</a> und deren isolierte Funktionalität
* Einsatz von Unit-Test-Frameworks zur Testautomatisierung
* Kann detaillierte Spezifikationsdokumente und umfangreiche Entwurfsdokumente überflüssig machen

*Beispiel:* Für eine Funktion, die in Pixel Leap die Kollisionserkennung zwischen der Spielfigur und Hindernissen berechnet, würde zunächst ein Unit-Test geschrieben, der verschiedene Kollisionsszenarien definiert. Erst dann wird die Kollisionslogik selbst programmiert.

#### Abnahmetestgetriebene Entwicklung (Acceptance Test-Driven Development, ATDD)

<a href="./Glossar.md#abnahmetestgetriebene-entwicklung" title="→ Glossar öffnen" class="glossary-term">**Abnahmetestgetriebene Entwicklung**</a> überträgt das Test-First-Konzept auf die Ebene der Anforderungserhebung und des <a href="./Glossar.md#abnahmetest" title="→ Glossar öffnen" class="glossary-term">**Abnahmetests**</a>.

**Hauptmerkmale:**
* Zu jeder <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderung**</a> werden <a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Abnahmekriterien**</a> als Testfälle formuliert
* Abnahmetestfälle existieren bereits vor der Implementierung der jeweiligen Funktionalität
* Fördert frühzeitige gemeinsame Interpretation der Anforderungen zwischen <a href="./Glossar.md#testmanager" title="→ Glossar öffnen" class="glossary-term">**Stakeholdern**</a> und Entwicklungsteam
* Akzeptanztests können manuell oder automatisiert durchgeführt werden

*Beispiel:* Für die Anforderung „Der Spieler soll durch Drücken der Leertaste springen können" werden in Pixel Leap zunächst präzise Abnahmetestfälle definiert: „Wenn die Leertaste gedrückt wird, springt die Figur 3 Einheiten hoch" und „Ein zweites Drücken während des Sprungs hat keine Wirkung". Diese Tests werden erstellt, bevor die Sprungfunktion implementiert wird.

#### Verhaltensgetriebene Entwicklung (Behavior-Driven Development, BDD)

<a href="./Glossar.md#verhaltensgetriebene-entwicklung" title="→ Glossar öffnen" class="glossary-term">**Verhaltensgetriebene Entwicklung**</a> stellt den Gedanken der ausführbaren Spezifikation in den Vordergrund und verwendet dafür eine an natürlicher Sprache orientierte Notation.

**Hauptmerkmale:**
* Anforderungen an das Sollverhalten werden als Beispiele oder Szenarien beschrieben
* Verwendung eines standardisierten Satzschemas (typischerweise: Gegeben … Wenn … Dann … bzw. englisch: Given … When … Then …)
* Ziel ist Verständlichkeit auch für Stakeholder mit geringem IT-Fachwissen
* BDD-Werkzeuge können diese Texte einlesen und in automatisiert ausführbare Tests umwandeln

*Beispiel:* In Pixel Leap könnte eine BDD-Spezifikation lauten:
```gherkin
Gegeben die Spielfigur steht auf festem Boden
Wenn der Spieler die Leertaste drückt
Dann springt die Figur 3 Einheiten nach oben
```

Diese menschenlesbare Beschreibung wird durch BDD-Tools in ausführbaren Testcode übersetzt.

---

### Kontinuierliche Integration und automatisierte Auslieferung

#### Continuous Integration: Häufige Integration von Codeänderungen

<a href="./Glossar.md#kontinuierliche-integration" title="→ Glossar öffnen" class="glossary-term">**Kontinuierliche Integration**</a> (CI) stellt eine konsequente Weiterentwicklung inkrementeller Integrationsstrategien dar. Das zentrale Prinzip besteht darin, dass Teammitglieder ihre Codeänderungen sehr häufig integrieren – üblicherweise mindestens einmal pro Tag, oft auch mehrfach täglich.

**Ablauf der Integration:**
* Jeder geänderte oder neue Codebaustein wird nach seiner Fertigstellung einzeln in die zentrale Integrationsumgebung übertragen
* Die Integration erfolgt in einen bereits vorhandenen, integrierten Versionsstand (Build)
* Neue Bausteine werden nicht mit anderen, ebenfalls neuen und noch nicht integrierten Bausteinen kombiniert
* Das Ergebnis jeder Integration ist ein neuer Build

> **Wichtig:** Häufige Integration verhindert große, schwer zu behebende Integrationsprobleme, da Konflikte frühzeitig erkannt werden.

#### Continuous Delivery: Automatisierung des Integrationsprozesses

Theoretisch könnte <a href="./Glossar.md#kontinuierliche-integration" title="→ Glossar öffnen" class="glossary-term">**Kontinuierliche Integration**</a> manuell durchgeführt werden. In der Praxis ist jedoch eine umfassende Automatisierung unerlässlich, um häufige Integrationen praktikabel zu machen. <a href="./Glossar.md#kontinuierliche-auslieferung" title="→ Glossar öffnen" class="glossary-term">**Continuous Delivery**</a> (CD) bezeichnet die Gesamtheit der Techniken, Prozesse und Werkzeuge, die das automatisierte Einspielen geänderter Software in die teaminterne Integrations- und <a href="./Glossar.md#testumgebung" title="→ Glossar öffnen" class="glossary-term">**Testumgebung**</a> (Staging-Area) ermöglichen.

**Vorteile der Automatisierung:**
* Praktikabilität häufiger Integrationen
* Reproduzierbare, standardisierte Abläufe
* Minimierung manueller Fehlerquellen

Da beide Praktiken – CI und CD – eng miteinander verzahnt sind und sich nicht eindeutig voneinander abgrenzen lassen, werden sie häufig gemeinsam als „CI/CD-Prozess" bezeichnet.

#### Unterstützung frühzeitigen Testens durch CI/CD

Ein CI/CD-Prozess leistet einen wesentlichen Beitrag zum Ziel des frühzeitigen Testens. Unmittelbar nach jeder Codeänderung – also zum frühestmöglichen Zeitpunkt – werden automatisch alle in den Prozess eingebundenen Tests ausgelöst. Dies umfasst sowohl statische als auch <a href="./Glossar.md#dynamischer-test" title="→ Glossar öffnen" class="glossary-term">**dynamische**</a> Codeanalysen.

**Feedback-Mechanismus:**
* Dank der Automatisierung entfallen Überlegungen, ob Zeit oder Ressourcen für Tests ausreichen
* Sämtliche Testergebnisse liegen unmittelbar als Feedback vor
* Voraussetzung: Der Testumfang und die benötigte Ausführungszeit bleiben in praktikablen Grenzen

*Beispiel:* Bei Pixel Leap wird nach jeder Änderung am Spielcode automatisch eine Testsuite ausgeführt, die Gameplay-Mechaniken, Kollisionserkennung, Score-Berechnung und Menünavigation überprüft. Das Team erhält innerhalb von Minuten Feedback über die Qualität der Änderung.

#### Continuous Deployment: Automatische Auslieferung in Produktion

Läuft ein CI/CD-Prozess zuverlässig und automatisiert, kann er zu <a href="./Glossar.md#kontinuierliche-bereitstellung" title="→ Glossar öffnen" class="glossary-term">**Continuous Deployment**</a> erweitert werden. Bei diesem erweiterten Ansatz wird ein getesteter Build – vorausgesetzt alle Testfälle wurden erfolgreich durchlaufen – anschließend automatisch auch in die Produktionsumgebung übertragen und dort installiert.

**Anwendungsbereiche:**
* Besonders verbreitet bei webbasierten E-Commerce-Anwendungen
* Viele Unternehmen praktizieren dies mittlerweile routinemäßig
* Erfordert hohes Vertrauen in die automatisierten Tests und den gesamten Prozess

---

### DevOps: Integration von Entwicklung und Betrieb

#### Verbindung von Development und Operations

Um Schnelligkeit und Produktivität der Softwareentwicklung weiter zu steigern, streben zahlreiche Unternehmen an, ihre Entwicklungsprozesse (Development, „Dev") mit den Betriebsprozessen (Operations, „Ops") zu einem integrierten, gemeinsamen Ablauf zu verbinden. Diese integrierte Prozesskette wird als DevOps-Auslieferungskette oder DevOps-Pipeline bezeichnet.

#### Mehr als nur technische Integration

Die Realisierung von DevOps erfordert mehr als den Aufbau einer gemeinsamen Werkzeugkette mit zusammenwirkenden Tools aus Entwicklung, <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> und Betrieb. Damit die beteiligten Teams, Abteilungen und Unternehmenseinheiten tatsächlich enger kooperieren, sind auch kulturelle Veränderungen im Unternehmen notwendig.

**Erforderliche Veränderungen:**
* Abbau von Silos zwischen Entwicklung und Betrieb
* Gemeinsame Verantwortung für Qualität und Stabilität
* Veränderte Kommunikationsstrukturen
* Neue Rollenverteilungen

#### DevOps als Shift-Left und Shift-Right

DevOps unterstützt das Ziel frühzeitigen Testens, indem es auf einem vorhandenen CI/CD-Prozess aufbaut. Die Akzeptanz dieses Prozesses wird über die Entwicklungsteams hinaus verbreitert und die Motivation zu dessen kontinuierlicher Optimierung steigt.

**Shift-Right: Feedback aus dem Produktivbetrieb**

Der Betriebsteil im DevOps-Prozess liefert zusätzlich wertvolle Informationen über das tatsächliche Verhalten der Software im Produktivbetrieb:

* Daten zur tatsächlichen Nutzung bereitgestellter Funktionen
* Informationen über Auslastung und <a href="./Glossar.md#performanz" title="→ Glossar öffnen" class="glossary-term">**Performanz**</a> der Anwendungen
* Ausfallzeiten und Daten zur <a href="./Glossar.md#zuverlaessigkeit" title="→ Glossar öffnen" class="glossary-term">**Zuverlässigkeit**</a>

Solche Betriebsdaten sind ohne DevOps für Entwicklungsteams oft gar nicht, nur umständlich oder sehr verspätet verfügbar. Sie verschaffen zusätzliches Feedback über die entwickelte Software und ergänzen die durch Testen gewonnenen Informationen. Maßnahmen zur automatisierten Messung, Erfassung (Monitoring) und Weiterleitung solcher Daten werden unter dem Begriff „Shift-Right"-Strategie zusammengefasst.

*Beispiel:* Bei Pixel Leap könnte das DevOps-Monitoring zeigen, dass 80% der Spieler bereits in Level 3 scheitern. Diese Information aus dem Produktivbetrieb führt dazu, dass das Entwicklungsteam den Schwierigkeitsgrad anpasst oder zusätzliche Tutorials implementiert.

#### Herausforderungen und Risiken bei DevOps-Einführung

Die Einführung von DevOps bringt spezifische Herausforderungen mit sich:

**Organisatorische Herausforderungen:**
* Definition und Etablierung der DevOps-Auslieferungskette bei allen Beteiligten
* Beschaffung, Einführung und Wartung von CI/CD-Werkzeugen

**Technische Herausforderungen:**
* Aufbau und Ausbau der <a href="./Glossar.md#testautomatisierung" title="→ Glossar öffnen" class="glossary-term">**Testautomatisierung**</a> erfordern zusätzliche Ressourcen
* Laufende Pflege automatisierter Tests kann aufwendig und komplex sein
* Nicht alle manuellen Tests, insbesondere solche aus Benutzerperspektive, lassen sich durch automatisierte Tests ersetzen

---

### Retrospektiven als Instrument der kontinuierlichen Verbesserung

#### Vielfalt der Verbesserungsmaßnahmen

Die Bandbreite möglicher Maßnahmen zur Prozessverbesserung ist groß. Jede Maßnahme erfordert Investitionen – sei es in Form von Zeit, Personal oder Budget. Daher muss sorgfältig geklärt werden, welche der potenziell verfügbaren Maßnahmen in der jeweiligen Situation für das Projekt, das Team oder das Unternehmen den besten Nutzen bringt und in welchem Zeitrahmen dieser Nutzen realisiert werden kann.

#### Konzept der Retrospektive

<a href="./Glossar.md#retrospektive" title="→ Glossar öffnen" class="glossary-term">**Retrospektiven**</a> sind ein wichtiges Instrument, das zur Identifikation sinnvoller Verbesserungsmaßnahmen beiträgt. Eine Retrospektive ist eine Teamsitzung, in der ein Team – beispielsweise ein Managementteam, Projektteam oder Entwicklungsteam – reflektiert, ob und wie es seine zurückliegenden Aufgaben und Ziele erreicht hat und wo Möglichkeiten zur Verbesserung der Arbeitsweise gesehen werden.

> **Fokus:** Retrospektiven konzentrieren sich primär auf Prozessverbesserungen, nicht auf Produktverbesserungen.

#### Typische Fragestellungen in Retrospektiven

Die Teilnehmer einer Retrospektive diskutieren typischerweise folgende Aspekte:

* Was funktioniert gut und sollte beibehalten werden?
* Was verläuft nicht erfolgreich und kann durch welche Maßnahmen verbessert werden?
* Wie und wann können identifizierte Verbesserungsmaßnahmen umgesetzt werden?

#### Testbezogene Themen in Retrospektiven

Retrospektiven behandeln häufig Themen mit direktem Bezug zum Testen:

**Qualität der Testbasis:**
* Maßnahmen zur Verbesserung der <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a>
* Qualität der Anforderungsdokumente und anderer Grundlagendokumente

**Effektivität und Effizienz des Testens:**
* Steigerung durch zusätzliche Automatisierung
* Optimierung vorhandener Testprozesse
* Verbesserung der <a href="./Glossar.md#ueberdeckung" title="→ Glossar öffnen" class="glossary-term">**Testüberdeckung**</a>

**Testmittel:**
* Einsatz und Qualität der <a href="./Glossar.md#testmittel" title="→ Glossar öffnen" class="glossary-term">**Testmittel**</a>
* Optimierung des <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozesses**</a>
* Bewertung eingesetzter Tools
* Verbesserung der Infrastruktur

**Kompetenzentwicklung:**
* Weiterbildung und Lernen
* Ausweitung von Zertifizierungen
* Aufbau von Spezialwissen

**Team und Zusammenarbeit:**
* Teamkultur und Kommunikationsstil
* Teamzusammenhalt
* Zusammenarbeit zwischen Personen in unterschiedlichen Rollen
* Verbesserung der Schnittstellen zwischen Entwicklung, Test und Betrieb

*Beispiel:* Das Pixel Leap-Team stellt in einer Retrospektive fest, dass die manuellen Tests für die Benutzeroberfläche sehr zeitaufwendig sind. Als Verbesserungsmaßnahme wird beschlossen, für die häufigsten UI-Tests ein automatisiertes Framework einzuführen und zwei Teammitglieder entsprechend zu schulen.

#### Organisation und Durchführung von Retrospektiven

**Zeitpunkt:**
Der Zeitpunkt für Retrospektiven richtet sich üblicherweise nach Vorgaben oder Empfehlungen des verwendeten Softwareentwicklungslebenszyklusmodells oder des Qualitätsmanagementsystems:

* <a href="./Glossar.md#agile-softwareentwicklung" title="→ Glossar öffnen" class="glossary-term">**Agile Methoden**</a> wie Scrum sehen zum Abschluss jeder Iteration eine Sprint-Retrospektive vor
* Retrospektiven können am Ende eines Projekts durchgeführt werden
* Retrospektiven sind nach dem Erreichen wichtiger Projektmeilensteinen sinnvoll
* Bei Bedarf können Retrospektiven jederzeit einberufen werden

**Dokumentation und Nachverfolgung:**
Die Ergebnisse jeder Retrospektive müssen in einem Protokoll oder Bericht festgehalten werden. Die Umsetzung der beschlossenen Maßnahmen muss konsequent verfolgt und überprüft werden. Nur durch diese systematische Nachverfolgung können Retrospektiven einen nachhaltigen Beitrag zur kontinuierlichen Verbesserung leisten.

---

## Zusammenfassung

Testgetriebene Entwicklungsansätze und moderne Automatisierungspraktiken haben die Softwareentwicklung grundlegend verändert. Das Test-First-Prinzip – Tests vor Code – ermöglicht frühzeitiges Feedback und stellt sicher, dass Software von Anfang an testbar entwickelt wird. Die verschiedenen Ausprägungen (TDD, ATDD, BDD) adressieren unterschiedliche Ebenen und Zielgruppen, vom technischen Komponententest bis zur geschäftlichen Akzeptanzprüfung.

Kontinuierliche Integration und automatisierte Auslieferungsprozesse (CI/CD) bauen auf dieser Grundlage auf und ermöglichen es, Änderungen schnell und sicher in Produktion zu bringen. DevOps erweitert diese Perspektive, indem es Entwicklung und Betrieb verzahnt und wertvolles Feedback aus dem Produktivbetrieb zurück in den Entwicklungsprozess führt.

Retrospektiven schließlich sorgen dafür, dass Teams ihre Arbeitsweise kontinuierlich reflektieren und verbessern können. Alle diese Praktiken zusammen bilden ein leistungsfähiges Ökosystem für moderne, qualitätsorientierte Softwareentwicklung.
