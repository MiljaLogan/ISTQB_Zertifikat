# Testrealisierung

## Grundlagen der Testvorbereitung

**Die <a href="./Glossar.md#testrealisierung" title="→ Glossar öffnen" class="glossary-term">**Testrealisierung**</a> bildet das entscheidende Bindeglied zwischen der konzeptionellen Testplanung und der praktischen Umsetzung.** In dieser Phase werden sämtliche erforderlichen Vorbereitungen getroffen, um eine reibungslose und effektive <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> zu gewährleisten.

> Die **Testrealisierung** umfasst alle Aktivitäten zur finalen Vorbereitung der <a href="./Glossar.md#testmittel" title="→ Glossar öffnen" class="glossary-term">**Testmittel**</a>, damit die entwickelten <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> ausführungsbereit sind.

**Häufig werden die Arbeitsschritte von <a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">**Testentwurf**</a> und <a href="./Glossar.md#testrealisierung" title="→ Glossar öffnen" class="glossary-term">**Testrealisierung**</a> miteinander verzahnt durchgeführt**, um Synergieeffekte zu nutzen und den Entwicklungsprozess zu optimieren.

## Infrastruktur und Testumgebung

### Aufbau der Testinfrastruktur

**Ein zentraler Schwerpunkt liegt auf der detaillierten Umsetzung der Testinfrastruktur.** Alle benötigten <a href="./Glossar.md#testmittel" title="→ Glossar öffnen" class="glossary-term">**Testmittel**</a> müssen vervollständigt oder bei Bedarf neu erstellt werden.

**Die erforderlichen <a href="./Glossar.md#testrahmen" title="→ Glossar öffnen" class="glossary-term">**Testrahmen**</a> erfordern eine vollständige Programmierung und anschließende Installation in der <a href="./Glossar.md#testumgebung" title="→ Glossar öffnen" class="glossary-term">**Testumgebung**</a>.**

### Qualitätssicherung der Testumgebung

**Da <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> auch durch <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> in der <a href="./Glossar.md#testumgebung" title="→ Glossar öffnen" class="glossary-term">**Testumgebung**</a> entstehen können, ist eine sorgfältige Verifikation des korrekten Aufbaus unerlässlich.**

**Zur Vermeidung von Verzögerungen oder Behinderungen während der <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> müssen sämtliche zusätzlichen Komponenten korrekt implementiert sein:**

* <a href="./Glossar.md#service-virtualisierung" title="→ Glossar öffnen" class="glossary-term">**Service-Virtualisierung**</a>
* <a href="./Glossar.md#simulator" title="→ Glossar öffnen" class="glossary-term">**Simulatoren**</a>
* <a href="./Glossar.md#platzhalter" title="→ Glossar öffnen" class="glossary-term">**Platzhalter**</a>
* <a href="./Glossar.md#treiber" title="→ Glossar öffnen" class="glossary-term">**Treiber**</a>
* Weitere Infrastrukturelemente

### Integration der Testdaten

**Die ordnungsgemäße Überführung sämtlicher <a href="./Glossar.md#testdaten" title="→ Glossar öffnen" class="glossary-term">**Testdaten**</a> in die <a href="./Glossar.md#testumgebung" title="→ Glossar öffnen" class="glossary-term">**Testumgebung**</a> ist zu gewährleisten.** Dies ermöglicht eine nahtlose Verwendung der <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> ohne nachträgliche Modifikationen oder Ergänzungen während der Ausführungsphase.

## Konkretisierung und Strukturierung der Tests

### Verfeinerung der Testfälle

**Neben der Infrastrukturvorbereitung erfordern die <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> eine abschließende Konkretisierung.** Parallel dazu ist die Festlegung des <a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">**Testablaufs**</a> erforderlich, wodurch die <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> in eine logische und sinnvolle Ausführungsreihenfolge gebracht werden.

**Bei der Sequenzierung ist die <a href="./Glossar.md#prioritaet" title="→ Glossar öffnen" class="glossary-term">**Priorität**</a> der einzelnen <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> zu berücksichtigen.**

### Bildung von Testsuiten

**Eine effektive Durchführung erfordert die zweckmäßige Gruppierung der <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> zu <a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">**Testsuiten**</a>.** Diese Strukturierung ermöglicht sowohl eine effiziente Abarbeitung während eines <a href="./Glossar.md#testzyklus" title="→ Glossar öffnen" class="glossary-term">**Testzyklus**</a> als auch eine übersichtliche Organisation der <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a>.

> Eine **<a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">Testsuite</a>** besteht aus mehreren <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> in ihrer Ausführungsreihenfolge, wobei die Sequenz so gewählt wird, dass <a href="./Glossar.md#nachbedingung" title="→ Glossar öffnen" class="glossary-term">**Nachbedingungen**</a> eines <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfalls**</a> als <a href="./Glossar.md#vorbedingung" title="→ Glossar öffnen" class="glossary-term">**Vorbedingungen**</a> des nachfolgenden <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfalls**</a> fungieren können.

**Diese Herangehensweise vereinfacht den <a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">**Testablauf**</a> erheblich**, da nicht für jeden einzelnen <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> separat <a href="./Glossar.md#vorbedingung" title="→ Glossar öffnen" class="glossary-term">**Vor-**</a> beziehungsweise <a href="./Glossar.md#nachbedingung" title="→ Glossar öffnen" class="glossary-term">**Nachbedingungen**</a> explizit definiert werden müssen.

**Zusätzlich sollte jede <a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">**Testsuite**</a> sämtliche Aufräumaktionen nach der Durchführung enthalten**, um eine saubere Ausgangssituation für nachfolgende Tests zu gewährleisten.

## Automatisierung und Effizienzsteigerung

### Überführung in Testskripte

**<a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">**Testabläufe**</a> lassen sich häufig direkt in automatisierte oder manuelle <a href="./Glossar.md#testskript" title="→ Glossar öffnen" class="glossary-term">**Testskripte**</a> transformieren.** Diese Automatisierung führt zu einer erheblichen Reduzierung des zeitlichen Aufwands bei der <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> im Vergleich zu einer ausschließlich manuellen und oft ad-hoc durchgeführten Ausführung.

### Testausführungsplanung

**Die konkrete Ausgestaltung einer effizienten Ausführung der <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a>, <a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">**Testsuiten**</a> und <a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">**Testabläufe**</a> wird im <a href="./Glossar.md#testausfuehrungsplan" title="→ Glossar öffnen" class="glossary-term">**Testausführungsplan**</a> festgelegt.**

## Qualitätssicherung und Verfolgbarkeit

### Aktualisierung der Verfolgbarkeit

**Die <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> der <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> zu den zugrundeliegenden <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> beziehungsweise <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> erfordert gegebenenfalls eine Überprüfung und Aktualisierung.**

**Gleichzeitig müssen auch die <a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">**Testabläufe**</a> und <a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">**Testsuiten**</a> in die <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeitsmatrix**</a> einbezogen werden**, um eine vollständige Transparenz über die Testabdeckung zu gewährleisten.

## Fazit

**Die <a href="./Glossar.md#testrealisierung" title="→ Glossar öffnen" class="glossary-term">**Testrealisierung**</a> stellt eine kritische Phase im <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozess**</a> dar**, in der theoretische Planungen in praktisch ausführbare Teststrukturen überführt werden. Die sorgfältige Vorbereitung der Infrastruktur, die durchdachte Strukturierung der <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> und die Gewährleistung der <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> bilden das Fundament für eine erfolgreiche und effiziente <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a>.