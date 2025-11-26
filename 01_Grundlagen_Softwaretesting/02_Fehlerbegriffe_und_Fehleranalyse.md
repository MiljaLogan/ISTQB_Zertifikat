# Fehlerbegriffe und Fehleranalyse im Softwaretest

## Was macht einen Fehler zum Fehler?

### Die Testbasis als Bewertungsgrundlage

**Ein Verhalten kann nur dann als fehlerhaft bewertet werden, wenn zuvor definiert wurde, was als korrekt gilt.** Diese Referenz bildet die sogenannte <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> - eine Sammlung von <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a>, Spezifikationen und weiteren Informationen, die als Maßstab für die Bewertung dient.

> Ein Fehler ist die Nichterfüllung einer festgelegten <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderung**</a> - die Abweichung zwischen dem tatsächlichen und dem erwarteten Systemverhalten.

**Software altert nicht wie physische Produkte.** Jeder Softwarefehler existiert bereits seit dem Zeitpunkt seiner Entstehung im Code und wird erst bei der Ausführung sichtbar.

## Die Fehlerkette verstehen

### Von der Ursache zur sichtbaren Auswirkung

**<a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">Fehlerwirkung (Failure)</a>:** Das nach außen sichtbare, fehlerhafte Verhalten des Systems. Dies kann ein falscher Ausgabewert, ein Systemabsturz oder eine nicht funktionierende Funktion sein.

**<a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">Fehlerzustand (Fault/Defekt/Bug)</a>:** Die eigentliche Ursache im Code - beispielsweise eine falsch programmierte Anweisung oder ein vergessener Programmteil.

**<a href="./Glossar.md#fehlhandlung" title="→ Glossar öffnen" class="glossary-term">Fehlhandlung (Error)</a>:** Die menschliche Handlung, die zum <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustand**</a> führte, wie fehlerhafte Programmierung oder Missverständnisse bei der Anforderungsanalyse.

### Komplexe Wechselwirkungen

**Fehlermaskierung** kann auftreten, wenn sich mehrere <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> gegenseitig kompensieren. Eine <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkung**</a> wird erst sichtbar, nachdem maskierende Fehler korrigiert wurden. Dies erklärt, warum Fehlerbehebungen manchmal neue Probleme verursachen.

**Ein <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustand**</a> muss nicht zwangsläufig zu einer <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkung**</a> führen.** Die Auswirkung kann ausbleiben, sporadisch oder systematisch auftreten und sich weit entfernt von der ursprünglichen Fehlerquelle manifestieren.

## Häufige Ursachen für Fehlhandlungen

### Menschliche Faktoren
* **Zeitdruck** - in Softwareprojekten allgegenwärtig
* **Komplexität** der Aufgaben, Architekturen und Technologien
* **Unaufmerksamkeit** durch Ablenkung, Konzentrationsmangel oder Müdigkeit

### Kommunikation und Verständnis
* **Missverständnisse** bei der Interpretation von <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a>
* **Unklare Schnittstellen** zwischen Systemkomponenten
* **Unterschiedliche Auslegungen** von Spezifikationen zwischen Projektbeteiligten

### Technische Herausforderungen
* **Neue Technologien**, die noch nicht vollständig verstanden werden
* **Unerfahrenheit** oder unzureichende Ausbildung
* **Komplexe Systeminteraktionen** bei großen Anwendungen

## Testergebnisse richtig interpretieren

### Falsch-positive und falsch-negative Ergebnisse

**Nicht jedes unerwartete <a href="./Glossar.md#testergebnis" title="→ Glossar öffnen" class="glossary-term">**Testergebnis**</a> deutet auf einen echten Softwarefehler hin:**

| Ergebnistyp | Beschreibung | Konsequenz |
|-------------|--------------|------------|
| **Falsch-positiv** | <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> zeigt Fehler an, obwohl das System korrekt funktioniert | Unnötige Fehlersuche |
| **Falsch-negativ** | <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> übersieht vorhandenen Fehler | Fehler bleibt unentdeckt |
| **Richtig-positiv** | <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> deckt tatsächlichen Fehler auf | Erfolgreiche Fehlerfindung |
| **Richtig-negativ** | <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> bestätigt korrektes Verhalten | <a href="./Glossar.md#verifizierung" title="→ Glossar öffnen" class="glossary-term">**Verifikation**</a> der Funktionalität |

### Praktisches Beispiel: Unklare Anforderungen

*Ein Finanzierungssystem soll Kreditzinssätze basierend auf Bonitätsprüfungen reduzieren. Die <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderung**</a> verschwieg jedoch, dass diese Reduktion bei Sonderaktionen nicht gilt. Kunden erhielten dadurch initially zu niedrige Zinssätze angeboten, was zu Beschwerden bei der späteren Abrechnung führte.*

Dieses Beispiel zeigt, wie **unvollständige Spezifikationen** zu <a href="./Glossar.md#fehlhandlung" title="→ Glossar öffnen" class="glossary-term">**Fehlhandlungen**</a> in der Entwicklung und letztendlich zu Problemen im Produktivbetrieb führen.

## Lernen aus Fehlern

### Prozessverbesserung durch Fehleranalyse

**Die systematische Analyse von Fehlern und deren Ursachen ermöglicht nachhaltigen Lerneffekt.** Durch die Untersuchung der Fehlerkette - von der <a href="./Glossar.md#fehlhandlung" title="→ Glossar öffnen" class="glossary-term">**Fehlhandlung**</a> über den <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustand**</a> bis zur <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkung**</a> - können Prozessverbesserungen implementiert werden, die ähnliche Probleme in Zukunft verhindern.

### Abgrenzung: Testen versus Debugging

**<a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">Testen</a> identifiziert <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a>, <a href="./Glossar.md#debugging" title="→ Glossar öffnen" class="glossary-term">**Debugging**</a> lokalisiert und behebt <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a>.** Während <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> primär das Aufdecken von Problemen zum Ziel hat, fokussiert sich <a href="./Glossar.md#debugging" title="→ Glossar öffnen" class="glossary-term">**Debugging**</a> auf die Ursachenanalyse und Problemlösung im Code.

## Fazit

**Das Verständnis der Fehlerkette ist fundamental für effektives <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a>.** Die klare Unterscheidung zwischen <a href="./Glossar.md#fehlhandlung" title="→ Glossar öffnen" class="glossary-term">**Fehlhandlung**</a>, <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustand**</a> und <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkung**</a> ermöglicht es, sowohl die unmittelbaren Symptome als auch die zugrundeliegenden Ursachen systematisch anzugehen.

**Erfolgreiche <a href="./Glossar.md#qualitaetssicherung" title="→ Glossar öffnen" class="glossary-term">**Qualitätssicherung**</a> erfordert mehr als das reine Aufspüren von Fehlern** - sie umfasst die kontinuierliche Verbesserung von Prozessen und die Schaffung von Rahmenbedingungen, die <a href="./Glossar.md#fehlhandlung" title="→ Glossar öffnen" class="glossary-term">**Fehlhandlungen**</a> minimieren.