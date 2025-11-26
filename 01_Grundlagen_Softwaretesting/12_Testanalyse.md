# Testanalyse

## Definition und Zielsetzung

**Bei der <a href="./Glossar.md#testanalyse" title="→ Glossar öffnen" class="glossary-term">**Testanalyse**</a> geht es darum, zu ermitteln, was genau zu testen ist.** Dazu wird die <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> dahingehend untersucht, ob die zu verwendenden Dokumente ausreichend detailliert sind und testbare Merkmale bzw. Eigenschaften (Features) enthalten, um daraus <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> abzuleiten.

**Wie umfangreich die <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingung**</a> geprüft werden soll, wird durch messbare festzulegende <a href="./Glossar.md#ueberdeckungskriterien" title="→ Glossar öffnen" class="glossary-term">**Überdeckungskriterien**</a> bestimmt.** Ebenso sind die damit verbundenen <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiken**</a> und <a href="./Glossar.md#risikostufe" title="→ Glossar öffnen" class="glossary-term">**Risikostufen**</a> zu definieren und zu priorisieren.

## Untersuchung der Testbasis

### Prüfung von Dokumenten

**Zur detaillierten Untersuchung der <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> und für die in Betracht gezogene <a href="./Glossar.md#teststufe" title="→ Glossar öffnen" class="glossary-term">**Teststufe**</a> können folgende Dokumente bzw. Informationen herangezogen werden:**

### Anforderungsspezifikationen

**<a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">Anforderungsspezifikationen</a>, aus denen das gewünschte <a href="./Glossar.md#funktionaler-test" title="→ Glossar öffnen" class="glossary-term">**funktionale**</a> und <a href="./Glossar.md#nicht-funktionaler-test" title="→ Glossar öffnen" class="glossary-term">**nicht funktionale**</a> <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponenten-**</a> oder Systemverhalten hervorgeht.**

**Zu den Anforderungsspezifikationen gehören:**
* Fachanforderungen
* Funktionale <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a>
* Systemanforderungen
* <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a>
* Epics
* Anwendungsfälle oder ähnliche Arbeitsergebnisse

*Zum Beispiel kann die Spezifikation einer <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderung**</a> zu ungenau in der Festlegung des vorausgesagten Ergebnisses bzw. Systemverhaltens sein, sodass sich <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> nicht so ohne Weiteres ableiten lassen. Eine Nachbesserung ist erforderlich.*

### Entwurfs- und Realisierungsinformationen

**Entwurfs- und Realisierungsinformationen, aus denen die <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponenten-**</a> oder Systemstruktur hervorgeht:**

* System- oder Softwarearchitekturdokumente
* Entwurfsspezifikationen
* Aufrufdiagramme
* Modelldiagramme (z.B. UML- oder Entity-Relationship-Diagramme)
* Schnittstellenspezifikationen oder ähnliche Arbeitsergebnisse

*Zu analysieren ist beispielsweise, wie leicht Schnittstellen anzusprechen sind (Offenheit der Schnittstellen) und wie gut das <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> in kleinere Einheiten zerlegbar ist, um diese Teile separat testen zu können.*

### Testobjekt selbst prüfen

**Die <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponente**</a> oder das System selbst sind zu untersuchen** – darunter:
* Programmtext
* Datenbank-Metadaten und -abfragen
* Weitere Schnittstellen

*Beispielsweise ist der Programmtext zu untersuchen, ob dieser gut strukturiert und damit sowohl leicht verstehbar ist als auch eine geforderte Codeüberdeckung einfach erreicht und nachgewiesen werden kann.*

### Berichte zur Risikoanalyse

**Berichte zur <a href="./Glossar.md#risikoanalyse" title="→ Glossar öffnen" class="glossary-term">**Risikoanalyse**</a>, die <a href="./Glossar.md#funktionaler-test" title="→ Glossar öffnen" class="glossary-term">**funktionale**</a>, <a href="./Glossar.md#nicht-funktionaler-test" title="→ Glossar öffnen" class="glossary-term">**nicht funktionale**</a> und strukturelle Aspekte der <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponente**</a> oder des Systems beinhalten**, sollen ebenfalls untersucht werden.

**Besteht ein hohes <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiko**</a> bei Versagen der Software, ist das <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> sehr gründlich und entsprechend umfangreich durchzuführen.** Bei unkritischer Software kann das <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> weniger formal durchgeführt werden.

## Fehleranalyse in der Testbasis

### Bedeutung der Testbasis-Qualität

**»Grundlage« für den gesamten <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozess**</a> ist die <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a>. Ist die <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> fehlerhaft, können keine »korrekten« <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> und damit keine »korrekten« <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> abgeleitet werden.**

### Mögliche Fehlerarten in Dokumenten

**Die <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> sollte daher zusätzlich im Hinblick auf mögliche Arten von Fehlern analysiert werden:**

* **Mehrdeutigkeiten:** Formulierungen, die unterschiedlich interpretiert werden können
* **Lücken oder Auslassungen:** Unvollständige Funktionsbeschreibungen
* **Inkonsistenzen:** Widersprüchliche Aussagen in den Dokumenten
* **Ungenauigkeiten:** Unpräzise Spezifikationen
* **Widersprüche:** Sich widersprechende Anforderungen
* **Überflüssige Inhalte:** Textpassagen ohne neue Informationen

**Entdeckte Fehler und Unstimmigkeiten in den Dokumenten sind in <a href="./Glossar.md#fehlerbericht" title="→ Glossar öffnen" class="glossary-term">**Fehlerberichten**</a> zu dokumentieren und zu beheben.**

## Testbarkeit

### Definition der Testbarkeit

**In dem Zusammenhang wird auch von <a href="./Glossar.md#testbarkeit" title="→ Glossar öffnen" class="glossary-term">**Testbarkeit**</a> gesprochen. <a href="./Glossar.md#testbarkeit" title="→ Glossar öffnen" class="glossary-term">**Testbarkeit**</a> meint zum einen:**

* Ob die <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> ausreichend präzise formuliert ist, sodass <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> abgeleitet werden können
* Ob die durchzuführenden <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> nachweisen können, dass diese <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> erfüllt sind

**Zum anderen wird damit ausgedrückt:**
* Ob oder wie gut das <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> für die <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> zugänglich ist
* Ob das <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> geeignete Schnittstellen besitzt, über die der gewünschte <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> oder <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> tatsächlich ausgeführt werden kann

### Frühzeitige Fehlererkennung

**Die Identifizierung und Behebung von Fehlern in der <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> ist sehr wichtig**, besonders wenn die Dokumente vorher keinem <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviewprozess**</a> unterzogen wurden.

**Bei Vorgehensweisen wie <a href="./Glossar.md#verhaltensgetriebene-entwicklung" title="→ Glossar öffnen" class="glossary-term">**Behavior Driven Development (BDD)**</a> und <a href="./Glossar.md#abnahmetestgetriebene-entwicklung" title="→ Glossar öffnen" class="glossary-term">**Acceptance Test Driven Development (ATDD)**</a> werden vor der Codierung <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> und <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> aus <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a> und <a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a> erstellt.** Vorteilhaft ist, dass auf diese Weise Fehler frühzeitig erkannt werden können.

## Priorisierung und Verfolgbarkeit

### Priorisierung der Testbedingungen

**Nachdem die <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> identifiziert und definiert sind, ist eine <a href="./Glossar.md#prioritaet" title="→ Glossar öffnen" class="glossary-term">**Priorisierung**</a> der <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> vorzunehmen.**

> Damit soll sichergestellt werden, dass die wichtigen und risikoreichen <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> zuerst und ausreichend getestet werden.

Es kommt leider in Projekten vor, dass aus zeitlichen Restriktionen nicht alle geplanten <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> auch durchgeführt werden.

### Verfolgbarkeit sicherstellen

**Bei der <a href="./Glossar.md#testplanung" title="→ Glossar öffnen" class="glossary-term">**Testplanung**</a> soll sichergestellt werden, dass eine eindeutige bidirektionale <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> zwischen der <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> und den anderen Arbeitsergebnissen der Testaktivitäten vorhanden ist.**

**Die <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> ist hier zu detaillieren:**
* Es muss klar sein, welche <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingung**</a> welche <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> prüft
* Umgekehrt muss erkennbar sein, welche <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> durch welche <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> abgedeckt sind

**Nur so ist später eine fundierte Aussage zu treffen, welche <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> wie intensiv – mit welchen <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a>, abgeleitet aus den <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> – geprüft werden sollen bzw. getestet wurden.**

## Berücksichtigung von Testverfahren

### Systematische Herangehensweise

**Bereits während der <a href="./Glossar.md#testanalyse" title="→ Glossar öffnen" class="glossary-term">**Testanalyse**</a> kann die Beachtung von <a href="./Glossar.md#testverfahren" title="→ Glossar öffnen" class="glossary-term">**Testverfahren**</a> (<a href="./Glossar.md#black-box-testverfahren" title="→ Glossar öffnen" class="glossary-term">**Blackbox-**</a>, <a href="./Glossar.md#white-box-testverfahren" title="→ Glossar öffnen" class="glossary-term">**Whitebox-Verfahren**</a> und <a href="./Glossar.md#erfahrungsbasiertes-testverfahren" title="→ Glossar öffnen" class="glossary-term">**erfahrungsbasiert**</a>) sehr hilfreich sein.**

**Die Verfahren stellen eine gewisse Systematik bereit, die:**
* Die Wahrscheinlichkeit verringert, <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> zu übersehen
* Hilft, präzisere <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> zu definieren

### Beispiel: Äquivalenzklassentest

*So wird beispielsweise beim <a href="./Glossar.md#aequivalenzklassenbildung" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklassentest**</a> sichergestellt, dass der gesamte Eingabebereich für die Erstellung von <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> herangezogen wird. Ein mögliches Übersehen oder Vergessen von negativen Eingaben in der Anforderungsdefinition wird somit verhindert.*

### Erfahrungsbasierte Verfahren

**Werden bei der Durchführung der <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> <a href="./Glossar.md#erfahrungsbasiertes-testverfahren" title="→ Glossar öffnen" class="glossary-term">**erfahrungsbasierte Verfahren**</a> genutzt, können die <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> aus der <a href="./Glossar.md#testanalyse" title="→ Glossar öffnen" class="glossary-term">**Testanalyse**</a> als <a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">**Testziele**</a> in <a href="./Glossar.md#test-charta" title="→ Glossar öffnen" class="glossary-term">**Test-Chartas**</a> einfließen.**

**<a href="./Glossar.md#test-charta" title="→ Glossar öffnen" class="glossary-term">Test-Chartas</a> können verstanden werden als:**
* »Test-Aufträge« mit <a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">**Testzielen**</a> und möglichen Ideen für weitere <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a>
* Skizze oder grobe Landkarte für einen bestimmten <a href="./Glossar.md#explorativer-test" title="→ Glossar öffnen" class="glossary-term">**explorativen Test**</a>

**Wenn die <a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">**Testziele**</a> auf die <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> rückführbar sind, kann auch bei den <a href="./Glossar.md#erfahrungsbasiertes-testverfahren" title="→ Glossar öffnen" class="glossary-term">**erfahrungsbasierten Tests**</a> die erreichte <a href="./Glossar.md#ueberdeckung" title="→ Glossar öffnen" class="glossary-term">**Überdeckung**</a>, z.B. der <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a>, gemessen werden.**

**<a href="./Glossar.md#test-charta" title="→ Glossar öffnen" class="glossary-term">Test-Chartas</a> können auch erst im <a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">**Testentwurf**</a> formuliert oder im Rahmen der Aktivitäten dort weiter verfeinert werden.**

## Fazit

**Die <a href="./Glossar.md#testanalyse" title="→ Glossar öffnen" class="glossary-term">**Testanalyse**</a> ist eine fundamentale Aktivität im <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozess**</a>**, die das "Was" des <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testens**</a> definiert. Sie gewährleistet, dass alle relevanten Aspekte identifiziert und systematisch in <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> überführt werden.

**Die sorgfältige Analyse der <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> und die Sicherstellung ihrer <a href="./Glossar.md#testbarkeit" title="→ Glossar öffnen" class="glossary-term">**Testbarkeit**</a> sind entscheidend für die <a href="./Glossar.md#qualitaet" title="→ Glossar öffnen" class="glossary-term">**Qualität**</a> des gesamten Testvorhabens.** Nur auf Basis einer soliden Analyse können effektive und zielgerichtete <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> entwickelt werden.