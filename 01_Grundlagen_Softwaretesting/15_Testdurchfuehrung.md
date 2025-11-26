# Testdurchführung

## Grundlagen der Testausführung

**Die <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> stellt die operative Umsetzung der zuvor entwickelten Testkonzepte dar.** Entsprechend dem <a href="./Glossar.md#testausfuehrungsplan" title="→ Glossar öffnen" class="glossary-term">**Testausführungsplan**</a> werden die <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> in verschiedenen Formen zur Ausführung gebracht.

**Die Ausführung kann in unterschiedlichen Modalitäten erfolgen:**
* Manuelle Durchführung
* Automatisierte Abarbeitung
* Kontinuierliche <a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">**Testabläufe**</a>
* <a href="./Glossar.md#testsitzung" title="→ Glossar öffnen" class="glossary-term">**Testsitzungen**</a> in Paararbeit

## Vorbereitung und Vollständigkeitsprüfung

### Systemverifikation vor Testbeginn

**Zu Beginn der <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> empfiehlt sich eine gründliche Überprüfung der Vollständigkeit aller zu testenden Komponenten sowie der eingesetzten <a href="./Glossar.md#testmittel" title="→ Glossar öffnen" class="glossary-term">**Testmittel**</a>.**

**Das <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> wird in der bereitgestellten <a href="./Glossar.md#testumgebung" title="→ Glossar öffnen" class="glossary-term">**Testumgebung**</a> installiert und auf grundlegende Start- sowie Ablauffähigkeit geprüft.** Erst bei problemloser Grundfunktionalität kann mit der eigentlichen Testausführung begonnen werden.

### Smoke-Test als Startverfahren

> **Empfehlung:** Die <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> sollte stets mit der Überprüfung der Hauptfunktionalitäten des <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekts**</a> mittels <a href="./Glossar.md#smoke-test" title="→ Glossar öffnen" class="glossary-term">**Smoke-Test**</a> beginnen.

**Zeigen sich bereits in dieser Phase <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> oder Abweichungen von den <a href="./Glossar.md#erwartetes-ergebnis" title="→ Glossar öffnen" class="glossary-term">**erwarteten Ergebnissen**</a>, ist eine tiefergehende Testausführung wenig zielführend.** Die fehlerhaften Grundfunktionen müssen zunächst korrigiert werden, bevor detailliertere Prüfungen sinnvoll sind.

## Protokollierung und Dokumentation

### Vollständige Testprotokollierung

> **Grundsatz:** <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> ohne <a href="./Glossar.md#testprotokoll" title="→ Glossar öffnen" class="glossary-term">**Protokollierung**</a> sind wertlos.

**Die Ausführung der <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> und <a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">**Testsuiten**</a> – ob manuell oder durch Werkzeugeinsatz entsprechend dem <a href="./Glossar.md#testausfuehrungsplan" title="→ Glossar öffnen" class="glossary-term">**Testausführungsplan**</a> – erfordert eine exakte und vollständige Dokumentation.** Es ist zu vermerken, welche <a href="./Glossar.md#testlauf" title="→ Glossar öffnen" class="glossary-term">**Testläufe**</a> mit welchen Ergebnissen durchgeführt wurden:

* <a href="./Glossar.md#bestanden" title="→ Glossar öffnen" class="glossary-term">**Bestanden**</a>
* <a href="./Glossar.md#fehlgeschlagen" title="→ Glossar öffnen" class="glossary-term">**Fehlgeschlagen**</a>
* Blockiert

### Zweck der Protokollierung

**Die <a href="./Glossar.md#testprotokoll" title="→ Glossar öffnen" class="glossary-term">**Testprotokolle**</a> erfüllen mehrere wesentliche Funktionen:**

**Nachvollziehbarkeit:** Die <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> muss auch für nicht direkt beteiligte Personen – beispielsweise Kunden – transparent und verständlich sein.

**Strategienachweis:** Es ist zu belegen, dass die geplante <a href="./Glossar.md#teststrategie" title="→ Glossar öffnen" class="glossary-term">**Teststrategie**</a> tatsächlich umgesetzt wurde.

**Detaillierte Dokumentation:** Aus dem <a href="./Glossar.md#testprotokoll" title="→ Glossar öffnen" class="glossary-term">**Testprotokoll**</a> muss hervorgehen, welche Komponenten wann, von wem, mit welcher Intensität und mit welchem Ergebnis geprüft wurden.

**Vollständigkeitsnachweis:** Ausgelassene geplante <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> oder <a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">**Testabläufe**</a> sind entsprechend zu vermerken.

## Konfigurationsmanagement und Reproduzierbarkeit

### Verwaltung der Testressourcen

> **Wichtigkeit:** Nachvollziehbarkeit und Reproduzierbarkeit sind kritische Erfolgsfaktoren.

**Bei jeder <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> ist neben dem <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> oder einzelnen <a href="./Glossar.md#testelement" title="→ Glossar öffnen" class="glossary-term">**Testelementen**</a> eine Vielzahl von Informationen und Dokumenten beteiligt:**

* <a href="./Glossar.md#testrahmen" title="→ Glossar öffnen" class="glossary-term">**Testrahmen**</a>
* Eingabedateien
* <a href="./Glossar.md#testprotokoll" title="→ Glossar öffnen" class="glossary-term">**Testprotokolle**</a>
* Weitere unterstützende Materialien

**Die zu einem <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> oder <a href="./Glossar.md#testlauf" title="→ Glossar öffnen" class="glossary-term">**Testlauf**</a> gehörenden Informationen und Daten müssen so verwaltet werden, dass eine spätere Wiederholung der <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> mit identischen Daten und Randbedingungen problemlos möglich ist.**

**Die entsprechenden IDs und Versionen der verwendeten <a href="./Glossar.md#testmittel" title="→ Glossar öffnen" class="glossary-term">**Testmittel**</a> sind zu dokumentieren und dem Konfigurationsmanagement zuzuführen.**

## Fehlerbehandlung und -management

### Identifikation von Fehlerwirkungen

> **Prüfungserfordernis:** Tritt bei der Testausführung eine Differenz zwischen tatsächlichem und vorausgesagtem Ergebnis auf, ist bei der Auswertung der <a href="./Glossar.md#testprotokoll" title="→ Glossar öffnen" class="glossary-term">**Testprotokolle**</a> zu entscheiden, ob tatsächlich eine <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkung**</a> vorliegt.

**Bei der Erkennung einer <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkung**</a> sind folgende Schritte durchzuführen:**

* Entsprechende Dokumentation der <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkung**</a>
* Erste grobe Prüfung möglicher Ursachen
* Gegebenenfalls Spezifikation und Ausführung ergänzender <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a>
* Erstellung eines <a href="./Glossar.md#fehlerbericht" title="→ Glossar öffnen" class="glossary-term">**Fehlerberichts**</a> über die aufgedeckten <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a>

### Fehlerkorrektur und Nachtest

**Nach der Korrektur des <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustands**</a> ist zu prüfen, ob die <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkung**</a> beseitigt wurde und bei der Korrektur keine weiteren <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> entstanden sind.** Gegebenenfalls sind neue <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> zu spezifizieren, die den modifizierten oder neuen Programmcode überprüfen.

### Qualitätssicherung bei der Fehlermeldung

> **Sorgfaltspflicht:** Es ist gewissenhaft zu prüfen, ob der <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustand**</a> tatsächlich im <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> liegt.

**Nichts schadet der Glaubwürdigkeit eines <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Testers**</a> mehr als eine gemeldete vermeintliche <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkung**</a>, deren Ursache jedoch in einem fehlerhaften <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> liegt.** Befürchtungen oder Selbstzensur sollten jedoch nicht dazu führen, dass potenzielle <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> vorsichtshalber nicht gemeldet werden – dies könnte ebenso fatal sein.

### Praktikabilität der Fehlerkorrektur

**Idealerweise sollten <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> einzeln korrigiert und erneut getestet werden, um unbeabsichtigte gegenseitige Beeinflussungen der Änderungen zu vermeiden.** In der Praxis erweist sich dies jedoch als nicht durchführbar.

**Bei unabhängigen <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Testern**</a> (nicht den Entwicklern selbst) ist eine separate Korrektur einzelner <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> nicht praktikabel.** Der Aufwand, jede <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkung**</a> einzeln dem Entwickler zu melden und erst nach erfolgter Korrektur weiterzutesten, ist nicht gerechtfertigt.

**Deshalb werden üblicherweise mehrere <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> korrigiert und anschließend mit einem neuen Softwareversionsstand zur erneuten Testung vorgelegt.**

## Messungen und Überdeckungsanalyse

### Erfassung von Metriken

**Neben der reinen Protokollierung der Differenzen zwischen <a href="./Glossar.md#erwartetes-ergebnis" title="→ Glossar öffnen" class="glossary-term">**erwarteten**</a> und tatsächlichen Ergebnissen sind Messungen zur Ermittlung der <a href="./Glossar.md#ueberdeckung" title="→ Glossar öffnen" class="glossary-term">**Überdeckungsgrade**</a> der <a href="./Glossar.md#ueberdeckungselement" title="→ Glossar öffnen" class="glossary-term">**Überdeckungselemente**</a> durchzuführen.**

**Bei Bedarf ist auch eine Protokollierung des Zeitverbrauchs vorzunehmen.** Hierzu sind entsprechende Werkzeuge einzusetzen.

## Verfolgbarkeit und Ergebnisbewertung

### Aktualisierung der Verfolgbarkeitsmatrix

> **Kontinuierliche Aufgabe:** Bei allen bisherigen Aktivitäten des <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozesses**</a> spielt die bidirektionale <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> eine wichtige Rolle.

**Die <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> ist zu prüfen und zu aktualisieren, damit zwischen <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a>, <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a>, <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a>, <a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">**Testabläufen**</a> und <a href="./Glossar.md#testergebnis" title="→ Glossar öffnen" class="glossary-term">**Testergebnissen**</a> die jeweiligen Beziehungen aktuell bleiben.**

### Vollständigkeitsbewertung

**Nach Abschluss der <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> kann mithilfe der <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> ermittelt werden, ob zu jedem Element der entsprechenden <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> ein zugehöriger <a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">**Testablauf**</a> ausgeführt wurde.**

**So kann beispielsweise festgestellt werden:**
* Welche <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> alle geplanten und durchgeführten <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> bestanden haben
* Welche <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> aufgrund fehlgeschlagener <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> nicht erfolgreich verifiziert werden konnten
* Ob <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> bei der Testausführung aufgetreten sind
* Welche <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> noch nicht geprüft wurden, da geplante <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> noch ausstehen

### Erfolgsbewertung und Abschluss

> **Zielerreichung:** Solche Informationen ermöglichen eine definitive Aussage, ob die vereinbarten <a href="./Glossar.md#ueberdeckungskriterien" title="→ Glossar öffnen" class="glossary-term">**Überdeckungskriterien**</a> erreicht wurden und damit der <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> als erfolgreich beendet angesehen werden kann.

**Durch die <a href="./Glossar.md#ueberdeckungskriterien" title="→ Glossar öffnen" class="glossary-term">**Überdeckungskriterien**</a> und die <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> können die Ergebnisse der <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> so dokumentiert werden, dass sie für die Stakeholder verständlich und direkt nachvollziehbar sind.**

## Fazit

**Die <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> stellt den operativen Höhepunkt des <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozesses**</a> dar**, in dem alle vorangegangenen Planungen und Vorbereitungen in konkrete Testergebnisse münden. Die systematische Protokollierung, gewissenhafte Fehlerbehandlung und kontinuierliche Verfolgbarkeit gewährleisten nicht nur die <a href="./Glossar.md#qualitaet" title="→ Glossar öffnen" class="glossary-term">**Qualität**</a> der Testausführung, sondern schaffen auch die notwendige Transparenz für alle Stakeholder.

**Die Balance zwischen gründlicher Dokumentation und praktikablen Arbeitsabläufen ist dabei entscheidend für den Erfolg der gesamten Testaktivitäten.**