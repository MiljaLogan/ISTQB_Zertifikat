# Der Testprozess

## Einordnung in die Softwareentwicklung

**<a href="./Glossar.md#softwareentwicklungslebenszyklus" title="→ Glossar öffnen" class="glossary-term">Softwareentwicklungslebenszyklus-Modelle</a> – kurz Entwicklungsmodelle – dienen dazu, die anfallenden Arbeiten bei der Neu- oder Weiterentwicklung von Softwaresystemen zu strukturieren, zu planen und zu steuern.** Als Anleitung, um in einem Softwareprojekt <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> strukturiert durchzuführen, reicht eine Darstellung der Aufgaben, wie sie in den Entwicklungsmodellen zu finden ist, meist nicht aus.

**Zusätzlich zur Einordnung des <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testens**</a> in die gesamte Entwicklung wird ein verfeinerter Ablaufplan für die Testarbeiten selbst benötigt.** Das heißt, der »Inhalt« der Entwicklungsaufgabe »<a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a>« muss in kleinere Arbeitsabschnitte gegliedert werden.

## Aufbau eines Testprozesses

### Bewährte Testaktivitäten

**Es gibt eine Reihe von gebräuchlichen und in der Praxis bewährten Testaktivitäten.** Ein geeigneter <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozess**</a> besteht aus solchen Testaktivitäten. Je nach vorgegebener oder vorgefundener Projektsituation ist ein geeigneter, spezifischer Prozess für das <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> der Software daraus zusammenzustellen.

**Welche Testaktivitäten in diesem <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozess**</a> enthalten sind, wie sie umgesetzt und wann sie durchgeführt werden, hängt von vielen Faktoren ab** und soll individuell in der <a href="./Glossar.md#teststrategie" title="→ Glossar öffnen" class="glossary-term">**Teststrategie**</a> eines Unternehmens oder eines Projekts festgelegt werden.

> Werden einzelne Testaktivitäten weggelassen, ist die Wahrscheinlichkeit höher, dass das <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> die zu erreichenden Ziele verfehlt.

### Hauptaktivitäten im Testprozess

**Ein <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozess**</a> wird in der Regel folgende Aktivitäten umfassen:**

1. **<a href="./Glossar.md#testplanung" title="→ Glossar öffnen" class="glossary-term">Testplanung</a>**
2. **<a href="./Glossar.md#testueberwachung" title="→ Glossar öffnen" class="glossary-term">Testüberwachung</a> und <a href="./Glossar.md#teststeuerung" title="→ Glossar öffnen" class="glossary-term">-steuerung</a>**
3. **<a href="./Glossar.md#testanalyse" title="→ Glossar öffnen" class="glossary-term">Testanalyse</a>**
4. **<a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">Testentwurf</a>**
5. **<a href="./Glossar.md#testrealisierung" title="→ Glossar öffnen" class="glossary-term">Testrealisierung</a>**
6. **<a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">Testdurchführung</a>**
7. **<a href="./Glossar.md#testabschluss" title="→ Glossar öffnen" class="glossary-term">Testabschluss</a>**

**Jede dieser Aktivitäten besteht ihrerseits wieder aus mehreren Einzelaufgaben**, die entsprechende Arbeitsergebnisse liefern und je nach Projekt variieren können.

## Praktische Umsetzung des Testprozesses

### Überlappung und Parallelität

**Obgleich die Aufgaben des <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozesses**</a> in sequenzieller Reihenfolge angegeben sind und die einzelnen Aufgaben teilweise logisch aufeinander aufbauen, können und dürfen sie sich in der praktischen Anwendung überschneiden** und teilweise auch gleichzeitig durchgeführt werden.

**Selbst bei einer angestrebten schrittweisen logischen Abfolge der Testaktivitäten wird es bei einer vorgegebenen sequenziellen Entwicklung sowohl Überlappung, Kombination, Parallelität oder Wegfall von einzelnen Teilen der Aktivitäten geben.**

### Anpassung an den Projektkontext

**Eine Anpassung der Aktivitäten ist in Abhängigkeit des System- und Projektkontexts somit unabhängig vom eingesetzten Entwicklungsmodell meist erforderlich.**

## Iterativer Testprozess

### Agile Entwicklungsansätze

**Oft wird Software in kleinen Iterationen erstellt, so gibt es beim <a href="./Glossar.md#agile-softwareentwicklung" title="→ Glossar öffnen" class="glossary-term">**agilen Vorgehen**</a> »Build & Test«-Iterationen, die kontinuierlich durchgeführt werden.** Testaktivitäten finden innerhalb dieses Entwicklungsansatzes somit ebenfalls iterativ und kontinuierlich statt.

### Kontinuierliches Testen

**In <a href="./Glossar.md#agile-softwareentwicklung" title="→ Glossar öffnen" class="glossary-term">**agilen Umgebungen**</a> werden die <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozess**</a>-Aktivitäten in kurzen Zyklen wiederholt:**

* Jede Iteration enthält alle Testaktivitäten
* <a href="./Glossar.md#kontinuierlicher-test" title="→ Glossar öffnen" class="glossary-term">**Kontinuierliches Testen**</a> ermöglicht frühe Fehlererkennung
* Schnelle Rückkopplung zwischen Entwicklung und <a href="./Glossar.md#qualitaetssicherung" title="→ Glossar öffnen" class="glossary-term">**Qualitätssicherung**</a>

## Testmanagement und Verantwortlichkeiten

### Rolle des Testmanagements

**Ein Großteil der Aktivitäten ist vom <a href="./Glossar.md#testmanagement" title="→ Glossar öffnen" class="glossary-term">**Testmanagement**</a> durchzuführen oder zu verantworten.** Dies umfasst:

* **Strategische Planung:** Entwicklung der <a href="./Glossar.md#teststrategie" title="→ Glossar öffnen" class="glossary-term">**Teststrategie**</a>
* **Operative Steuerung:** <a href="./Glossar.md#testueberwachung" title="→ Glossar öffnen" class="glossary-term">**Testüberwachung**</a> und -kontrolle
* **Ressourcenmanagement:** Personal- und Budgetplanung
* **Berichtswesen:** <a href="./Glossar.md#testberichterstattung" title="→ Glossar öffnen" class="glossary-term">**Testberichterstattung**</a> an Stakeholder

### Inhaltliche Planung durch Testkonzept

**Das <a href="./Glossar.md#testkonzept" title="→ Glossar öffnen" class="glossary-term">**Testkonzept**</a> bildet die inhaltliche Grundlage für die <a href="./Glossar.md#testplanung" title="→ Glossar öffnen" class="glossary-term">**Testplanung**</a>** und definiert:

* **<a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">Testziele</a>** und Erfolgskriterien
* **<a href="./Glossar.md#testansatz" title="→ Glossar öffnen" class="glossary-term">Testansatz</a>** und <a href="./Glossar.md#testverfahren" title="→ Glossar öffnen" class="glossary-term">**Testverfahren**</a>
* **<a href="./Glossar.md#teststufe" title="→ Glossar öffnen" class="glossary-term">Teststufen</a>** und <a href="./Glossar.md#testumgebung" title="→ Glossar öffnen" class="glossary-term">**Testumgebungen**</a>
* **<a href="./Glossar.md#eingangskriterien" title="→ Glossar öffnen" class="glossary-term">Eingangskriterien</a>** und <a href="./Glossar.md#endekriterien" title="→ Glossar öffnen" class="glossary-term">**Endekriterien**</a>

## Fazit

**Ein strukturierter <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozess**</a> ist essentiell für erfolgreiches <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a>.** Die sieben Hauptaktivitäten bieten einen bewährten Rahmen, der je nach Projektkontext angepasst werden kann.

**Die Flexibilität des <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozesses**</a> ermöglicht sowohl sequenzielle als auch <a href="./Glossar.md#agile-softwareentwicklung" title="→ Glossar öffnen" class="glossary-term">**agile Entwicklungsansätze**</a>**, während die klare Struktur sicherstellt, dass alle wichtigen Aspekte des <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testens**</a> berücksichtigt werden.

**Erfolgreiches <a href="./Glossar.md#testmanagement" title="→ Glossar öffnen" class="glossary-term">**Testmanagement**</a> koordiniert diese Aktivitäten** und stellt sicher, dass der <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozess**</a> optimal an die jeweiligen Projektanforderungen angepasst ist.