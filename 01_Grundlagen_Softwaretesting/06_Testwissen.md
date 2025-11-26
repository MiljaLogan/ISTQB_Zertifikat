# Testwissen frühzeitig und erfolgreich nutzen

## Der Shift-Left-Ansatz im Softwaretest

**Mit dem <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> - genauer mit den Überlegungen und vorbereitenden Arbeiten zum <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> - soll so früh wie möglich begonnen werden.** Dieser Ansatz wird auch als <a href="./Glossar.md#shift-left" title="→ Glossar öffnen" class="glossary-term">**Shift-Left-Ansatz**</a> bezeichnet.

> Frühzeitige Integration von Testwissen in alle Entwicklungsphasen reduziert <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiken**</a> und verbessert die <a href="./Glossar.md#qualitaet" title="→ Glossar öffnen" class="glossary-term">**Softwarequalität**</a> nachhaltig.

## Vorteile der frühen Tester-Beteiligung

### Prüfung der Anforderungen

**Beteiligen sich <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Tester**</a> an der Prüfung der <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> oder an der Verfeinerung von <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a>**, können Unklarheiten und Fehler in den Arbeitsprodukten aufgedeckt und behoben werden.

*Beispiel aus "Pixel Leap": Bei der <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> "Als Spieler möchte ich sammeln können" identifiziert der <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Tester**</a> fehlende Spezifikationen: Welche Objekte? Wie viele? Was passiert beim Sammeln? Die präzisierte <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderung**</a> verhindert spätere Missverständnisse.*

**Die Identifikation und Behebung fehlerhafter <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> reduziert das <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiko**</a>** der Entwicklung falscher oder nicht <a href="./Glossar.md#testbarkeit" title="→ Glossar öffnen" class="glossary-term">**testbarer**</a> Funktionen.

### Zusammenarbeit beim Systemdesign

**Die enge Zusammenarbeit von <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Testern**</a> mit Systemdesignern während des Entwurfs** kann das Verständnis jeder Partei für das Design und dessen <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> erheblich verbessern.

*Beispiel: Beim Design des Kollisionssystems in "Pixel Leap" schlägt der <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Tester**</a> modulare Schnittstellen vor, die isolierte <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> der Sprung-Plattform-Interaktionen ermöglichen. Dies verhindert später aufwendige Architekturänderungen.*

**Dieses erhöhte Verständnis kann das <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiko**</a> grundlegender Konstruktionsfehler reduzieren** und ermöglicht die frühzeitige Identifikation potenzieller <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> zur Prüfung der Schnittstellen.

### Kollaboration während der Codeerstellung

**Arbeiten Entwickler und <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Tester**</a> während der Codeerstellung zusammen**, kann das Verständnis auf beiden Seiten für den Code und dessen <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> verbessert werden.

*Beispiel: Während der Implementierung des Punktesystems diskutieren Entwickler und <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Tester**</a> gemeinsam Edge-Cases wie negative Punkte oder Überlauf-Situationen. Dadurch entstehen sowohl robusterer Code als auch bessere <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a>.*

**Dies reduziert das <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiko**</a> von <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzuständen**</a> im Programmtext** und auch von fehlerhaften <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> zur Prüfung des Programmtextes (falsch negatives Ergebnis).

### Verifikation und Validierung vor Freigabe

**Wenn <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Tester**</a> die Software vor deren Freigabe <a href="./Glossar.md#verifizierung" title="→ Glossar öffnen" class="glossary-term">**verifizieren**</a> und <a href="./Glossar.md#validierung" title="→ Glossar öffnen" class="glossary-term">**validieren**</a>**, können weitere <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> erkannt und behoben werden, die ansonsten unentdeckt geblieben wären.

*Beispiel: Vor Release von "Pixel Leap" entdeckt der <a href="./Glossar.md#systemtest" title="→ Glossar öffnen" class="glossary-term">**Systemtest**</a>, dass bestimmte Sprungkombinationen bei schwächeren Geräten zu <a href="./Glossar.md#performanz" title="→ Glossar öffnen" class="glossary-term">**Performance**</a>-Problemen führen - ein Problem, das in der isolierten Entwicklungsumgebung nicht aufgefallen war.*

**Dies erhöht die Wahrscheinlichkeit, dass die Software den Bedürfnissen der Interessenvertreter gerecht wird** und die <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> erfüllt.

## Zusätzlicher Nutzen

**Zusätzlich zu diesen Beispielen trägt das Erreichen der definierten <a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">**Testziele**</a> zum allgemeinen Erfolg der <a href="./Glossar.md#softwareentwicklungslebenszyklus" title="→ Glossar öffnen" class="glossary-term">**Softwareentwicklung**</a> bzw. der <a href="./Glossar.md#wartung" title="→ Glossar öffnen" class="glossary-term">**Wartung**</a> bei.**

### Praktische Auswirkungen

**Durch frühzeitige Testbeteiligung entstehen messbare Vorteile:**
* Reduzierte Nacharbeit durch klarere <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a>
* Weniger Architektur-Refactoring durch <a href="./Glossar.md#testbarkeit" title="→ Glossar öffnen" class="glossary-term">**testfreundliches**</a> Design  
* Geringere Bugrate durch kollaborative Entwicklung
* Höhere Kundenzufriedenheit durch bessere <a href="./Glossar.md#validierung" title="→ Glossar öffnen" class="glossary-term">**Validierung**</a>

## Fazit

**Der <a href="./Glossar.md#shift-left" title="→ Glossar öffnen" class="glossary-term">**Shift-Left-Ansatz**</a> macht aus <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Testern**</a> Partner im gesamten Entwicklungsprozess** statt nur Prüfer am Ende der Kette. Die frühe Integration von Testwissen in alle Phasen - von <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> über Design bis zur Implementierung - führt zu qualitativ besserer Software und effizienteren Entwicklungsprozessen.

**Für "Pixel Leap" bedeutet dies:** Testexpertise fließt von der ersten Konzeptidee bis zum finalen Release kontinuierlich ein und stellt sicher, dass das Spiel nicht nur technisch funktioniert, sondern auch die Spielererwartungen erfüllt.
