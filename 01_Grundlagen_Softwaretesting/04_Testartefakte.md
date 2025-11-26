# Testartefakte und ihre Zusammenhänge

## Grundlagen der Testdokumentation

### Die Testbasis als Fundament

**Die <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> bildet das Herzstück aller Testaktivitäten.** Sie umfasst sämtliche Dokumente und Informationen, die zur Beurteilung herangezogen werden, ob ein Testverhalten fehlerhaft ist oder den Erwartungen entspricht.

> Die <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> definiert das Sollverhalten des <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekts**</a> und ermöglicht objektive Bewertungen von <a href="./Glossar.md#testergebnis" title="→ Glossar öffnen" class="glossary-term">**Testergebnissen**</a>.

**Typische Bestandteile der <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a>:**
* <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungsdokumente**</a> und Spezifikationen
* <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a> und <a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a>
* Systemdokumentation
* Gesunder Menschenverstand und Fachwissen

## Von der Testbasis zum Testfall

### Testbedingungen als Zwischenschritt

**Da die gesamte <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> nicht durch einen einzigen <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> überprüfbar ist, müssen fokussierte Aspekte definiert werden.** Diese <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen (Test Conditions)**</a> repräsentieren spezifische Prüfpunkte, die für das Erreichen der <a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">**Testziele**</a> relevant sind.

**Beispiele für <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a>:**
* Preisberechnungsfunktionen
* Kombinationen von Produktkonfigurationen  
* Benutzeroberflächen-Eigenschaften ("Look and Feel")
* Systemantwortzeitverhalten

### Testelemente definieren

**Parallel zur Ableitung von <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> werden <a href="./Glossar.md#testelement" title="→ Glossar öffnen" class="glossary-term">**Testelemente**</a> identifiziert** - die konkreten Teile des Systems, die durch spezifische <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> geprüft werden sollen.

*Beispiel: Zur <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingung**</a> "Preisberechnung" gehört das <a href="./Glossar.md#testelement" title="→ Glossar öffnen" class="glossary-term">**Testelement**</a> `calculate_price()` - eine Methode, die mit entsprechenden <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> validiert wird.*

## Testfall und Testlauf

### Vom statischen Plan zur dynamischen Ausführung

**Ein <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> beschreibt die Prüfung einer oder mehrerer <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a>.** Wenn dieser <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> auf dem Rechner ausgeführt wird - das <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> also mit konkreten <a href="./Glossar.md#testdaten" title="→ Glossar öffnen" class="glossary-term">**Testdaten**</a> versehen und gestartet wird - entsteht ein <a href="./Glossar.md#testlauf" title="→ Glossar öffnen" class="glossary-term">**Testlauf**</a>.

**Der <a href="./Glossar.md#testlauf" title="→ Glossar öffnen" class="glossary-term">**Testlauf**</a> umfasst:**
* Herstellung der erforderlichen <a href="./Glossar.md#vorbedingung" title="→ Glossar öffnen" class="glossary-term">**Vorbedingungen**</a>
* Bereitstellung der <a href="./Glossar.md#testdaten" title="→ Glossar öffnen" class="glossary-term">**Testdaten**</a>
* Ausführung des <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a>
* Prüfung der Ergebnisse gegen <a href="./Glossar.md#erwartetes-ergebnis" title="→ Glossar öffnen" class="glossary-term">**erwartete Sollwerte**</a>

> Die Bewertung erfolgt durch Vergleich zwischen <a href="./Glossar.md#istergebnis" title="→ Glossar öffnen" class="glossary-term">**Istergebnis**</a> und Sollergebnis basierend auf der <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a>.

## Organisation und Strukturierung

### Testsuiten und Testausführungspläne

**Einzelne <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> isoliert auszuführen ist ineffizient.** Stattdessen werden sie in <a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">**Testsuiten**</a> gruppiert, die gemeinsam in einem <a href="./Glossar.md#testzyklus" title="→ Glossar öffnen" class="glossary-term">**Testzyklus**</a> durchlaufen werden.

**Der <a href="./Glossar.md#testausfuehrungsplan" title="→ Glossar öffnen" class="glossary-term">**Testausführungsplan**</a>** legt die zeitliche Sequenz fest, in der verschiedene <a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">**Testsuiten**</a> abgearbeitet werden, und koordiniert die gesamte Testaktivität.

### Automatisierung durch Testskripte

**<a href="./Glossar.md#testskript" title="→ Glossar öffnen" class="glossary-term">**Testskripte**</a> automatisieren die Ausführung von <a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">**Testsuiten**</a>** und enthalten:
* Reihenfolge der <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a>
* Aktionen zur Vorbedingungsherstellung  
* Aufräumaktivitäten nach <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a>

Bei manuellen <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> werden diese Informationen als <a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">**Testablauf (Test Procedure)**</a> dokumentiert.

## Dokumentation und Berichtswesen

### Protokollierung und Berichterstattung

**Alle <a href="./Glossar.md#testlauf" title="→ Glossar öffnen" class="glossary-term">**Testläufe**</a> müssen systematisch protokolliert werden.** Die Einzelergebnisse fließen in zusammenfassende <a href="./Glossar.md#testbericht" title="→ Glossar öffnen" class="glossary-term">**Testberichte**</a> ein, die Stakeholdern einen Überblick über <a href="./Glossar.md#testfortschritt" title="→ Glossar öffnen" class="glossary-term">**Testfortschritt**</a> und -qualität geben.

### Strategische Planung

**Das <a href="./Glossar.md#testkonzept" title="→ Glossar öffnen" class="glossary-term">**Testkonzept**</a>** steht am Anfang aller Testüberlegungen und definiert:
* Auswahl der <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekte**</a> und <a href="./Glossar.md#testverfahren" title="→ Glossar öffnen" class="glossary-term">**Testverfahren**</a>
* Festlegung der <a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">**Testziele**</a>  
* Koordination der Testaktivitäten
* <a href="./Glossar.md#testberichterstattung" title="→ Glossar öffnen" class="glossary-term">**Berichterstattungsverfahren**</a>

**Der <a href="./Glossar.md#testplan" title="→ Glossar öffnen" class="glossary-term">**Testzeitplan**</a>** konkretisiert die zeitliche Dimension und koordiniert alle Testaktivitäten untereinander.

## Übersicht der Testartefakte

| Artefakt | Beschreibung | Zweck | Erstellungsphase |
|----------|--------------|-------|------------------|
| **<a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">Testbasis</a>** | Gesamtheit aller Referenzdokumente und Informationen | Definiert Sollverhalten und Bewertungsgrundlage | Projektbeginn |
| **<a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">Testbedingung</a>** | Spezifischer, testbarer Aspekt der <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">Testbasis</a> | Fokussierung auf prüfbare Eigenschaften | <a href="./Glossar.md#testanalyse" title="→ Glossar öffnen" class="glossary-term">Testanalyse</a> |
| **<a href="./Glossar.md#testelement" title="→ Glossar öffnen" class="glossary-term">Testelement</a>** | Konkreter Systemteil, der getestet wird | Identifikation der Prüfobjekte | <a href="./Glossar.md#testanalyse" title="→ Glossar öffnen" class="glossary-term">Testanalyse</a> |
| **<a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">Testfall</a>** | Spezifikation einer Prüfung | Beschreibt WAS getestet wird | <a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">Testdesign</a> |
| **<a href="./Glossar.md#testlauf" title="→ Glossar öffnen" class="glossary-term">Testlauf</a>** | Ausführung eines <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">Testfalls</a> auf dem System | Erzeugt tatsächliche <a href="./Glossar.md#testergebnis" title="→ Glossar öffnen" class="glossary-term">Testergebnisse</a> | <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">Testdurchführung</a> |
| **<a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">Testsuite</a>** | Zusammenfassung mehrerer <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">Testfälle</a> | Organisiert <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">Testfälle</a> in logische Gruppen | <a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">Testdesign</a> |
| **<a href="./Glossar.md#testausfuehrungsplan" title="→ Glossar öffnen" class="glossary-term">Testausführungsplan</a>** | Zeitliche Ablaufplanung der <a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">Testsuiten</a> | Koordiniert Testreihenfolge und -zyklen | <a href="./Glossar.md#testplanung" title="→ Glossar öffnen" class="glossary-term">Testplanung</a> |
| **<a href="./Glossar.md#testskript" title="→ Glossar öffnen" class="glossary-term">Testskript</a>** | Automatisierte Ausführungslogik | Ermöglicht wiederholbare, automatisierte <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">Tests</a> | <a href="./Glossar.md#testrealisierung" title="→ Glossar öffnen" class="glossary-term">Testimplementierung</a> |
| **<a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">Testablauf (Test Procedure)</a>** | Manuelle Ausführungsanweisung | Anleitung für manuelle <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">Testdurchführung</a> | <a href="./Glossar.md#testrealisierung" title="→ Glossar öffnen" class="glossary-term">Testimplementierung</a> |
| **<a href="./Glossar.md#testprotokoll" title="→ Glossar öffnen" class="glossary-term">Testprotokoll</a>** | Dokumentation der <a href="./Glossar.md#testlauf" title="→ Glossar öffnen" class="glossary-term">Testlaufergebnisse</a> | Erfasst alle Testresultate und Beobachtungen | <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">Testdurchführung</a> |
| **<a href="./Glossar.md#testbericht" title="→ Glossar öffnen" class="glossary-term">Testbericht</a>** | Zusammenfassung der <a href="./Glossar.md#testergebnis" title="→ Glossar öffnen" class="glossary-term">Testergebnisse</a> | Informiert Stakeholder über Testqualität und -fortschritt | Testauswertung |
| **<a href="./Glossar.md#testkonzept" title="→ Glossar öffnen" class="glossary-term">Testkonzept</a>** | Strategisches Planungsdokument | Definiert <a href="./Glossar.md#testansatz" title="→ Glossar öffnen" class="glossary-term">Testansatz</a>, -ziele und -organisation | <a href="./Glossar.md#testplanung" title="→ Glossar öffnen" class="glossary-term">Testplanung</a> |
| **<a href="./Glossar.md#testplan" title="→ Glossar öffnen" class="glossary-term">Testzeitplan</a>** | Zeitliche Koordination aller Testaktivitäten | Plant Ressourcen und Termine | <a href="./Glossar.md#testplanung" title="→ Glossar öffnen" class="glossary-term">Testplanung</a> |

## Zusammenhänge verstehen

### Prozessorientierte Betrachtung

**Die verschiedenen Artefakte entstehen in unterschiedlichen Phasen des <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozesses**</a>:**

1. **<a href="./Glossar.md#testplanung" title="→ Glossar öffnen" class="glossary-term">Testplanung</a>:** <a href="./Glossar.md#testkonzept" title="→ Glossar öffnen" class="glossary-term">Testkonzept</a> und <a href="./Glossar.md#testplan" title="→ Glossar öffnen" class="glossary-term">Testzeitplan</a>
2. **<a href="./Glossar.md#testanalyse" title="→ Glossar öffnen" class="glossary-term">Testanalyse</a>:** <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">Testbedingungen</a> und <a href="./Glossar.md#testelement" title="→ Glossar öffnen" class="glossary-term">Testelemente</a>  
3. **<a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">Testdesign</a>:** <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">Testfälle</a> und <a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">Testsuiten</a>
4. **<a href="./Glossar.md#testrealisierung" title="→ Glossar öffnen" class="glossary-term">Testimplementierung</a>:** <a href="./Glossar.md#testskript" title="→ Glossar öffnen" class="glossary-term">Testskripte</a> und <a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">Testabläufe</a>
5. **<a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">Testdurchführung</a>:** <a href="./Glossar.md#testlauf" title="→ Glossar öffnen" class="glossary-term">Testläufe</a> und <a href="./Glossar.md#testprotokoll" title="→ Glossar öffnen" class="glossary-term">Protokolle</a>
6. **Bewertung:** <a href="./Glossar.md#testbericht" title="→ Glossar öffnen" class="glossary-term">Testberichte</a>

### Praktische Umsetzung

**Die <a href="./Glossar.md#qualitaet" title="→ Glossar öffnen" class="glossary-term">**Qualität**</a> der <a href="./Glossar.md#testmittel" title="→ Glossar öffnen" class="glossary-term">**Testartefakte**</a> bestimmt maßgeblich den Erfolg der gesamten Testaktivität.** Unvollständige oder ungenaue <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> führt zu unzuverlässigen <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a>, während schlecht strukturierte <a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">**Testsuiten**</a> die <a href="./Glossar.md#effizienz" title="→ Glossar öffnen" class="glossary-term">**Effizienz**</a> der <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> beeinträchtigen.

> Systematische Dokumentation und klare Strukturierung der <a href="./Glossar.md#testmittel" title="→ Glossar öffnen" class="glossary-term">**Testartefakte**</a> sind Voraussetzung für reproduzierbare und aussagekräftige <a href="./Glossar.md#testergebnis" title="→ Glossar öffnen" class="glossary-term">**Testergebnisse**</a>.

## Fazit

**Professionelles <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> erfordert eine durchdachte Struktur von Artefakten**, die aufeinander aufbauen und sich gegenseitig ergänzen. Von der grundlegenden <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> über spezifische <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> bis hin zu ausführbaren <a href="./Glossar.md#testskript" title="→ Glossar öffnen" class="glossary-term">**Testskripten**</a> bildet jedes Element einen wichtigen Baustein im Gesamtsystem der <a href="./Glossar.md#qualitaetssicherung" title="→ Glossar öffnen" class="glossary-term">**Qualitätssicherung**</a>.

**Die systematische Verwaltung dieser Artefakte ermöglicht nicht nur effiziente <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a>**, sondern auch <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Nachvollziehbarkeit**</a>, Wiederverwendbarkeit und kontinuierliche Verbesserung der <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozesse**</a>.