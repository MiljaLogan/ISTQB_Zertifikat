# Verfolgbarkeit

## Grundlagen der Verfolgbarkeit im Testprozess

**Die <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> (Traceability) bildet das verbindende Element zwischen <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a>, Testarbeitsergebnissen und <a href="./Glossar.md#testmittel" title="→ Glossar öffnen" class="glossary-term">**Testmitteln**</a>.** Sie ermöglicht die Nachvollziehbarkeit von Beziehungen zwischen <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a>, <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiken**</a> und <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> und stellt somit einen kritischen Erfolgsfaktor für die Qualitätssicherung dar.

> Die **<a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">Verfolgbarkeit</a>** schafft transparente Verbindungen zwischen allen Elementen des <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozesses**</a> und ermöglicht eine fundierte <a href="./Glossar.md#testueberwachung" title="→ Glossar öffnen" class="glossary-term">**Testüberwachung**</a> sowie <a href="./Glossar.md#teststeuerung" title="→ Glossar öffnen" class="glossary-term">**Teststeuerung**</a>.

*Beispiel aus "Pixel Leap":* Die Verfolgbarkeitsmatrix verknüpfte die Anforderung "Sprungmechanik muss präzise funktionieren" mit den Testbedingungen "Sprungphysik" und "Kollisionserkennung", den entsprechenden Testfällen TC_001 bis TC_005 sowie den Risiken "Gameplay-Breaking-Bugs" und "Spielerfrustration".

## Bedeutung für Testüberwachung und -steuerung

### Fundamentale Rolle im Testprozess

**Die <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> ist entscheidend für die Implementierung einer effektiven <a href="./Glossar.md#testueberwachung" title="→ Glossar öffnen" class="glossary-term">**Testüberwachung**</a> und <a href="./Glossar.md#teststeuerung" title="→ Glossar öffnen" class="glossary-term">**Teststeuerung**</a>, die sich über den gesamten <a href="./Glossar.md#testprozess" title="→ Glossar öffnen" class="glossary-term">**Testprozess**</a> erstrecken.**

**Beziehungen zwischen jedem Element der <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> und den verschiedenen Ergebnissen der Testaktivitäten müssen etabliert und gepflegt werden.**

### Überdeckungsanalyse

**Der Grad der erreichten <a href="./Glossar.md#ueberdeckung" title="→ Glossar öffnen" class="glossary-term">**Überdeckung**</a> lässt sich mithilfe der <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> bestimmen.** Beispielsweise kann ermittelt werden, ob alle <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> mit mindestens einem <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> geprüft wurden.

**Diese Erkenntnisse dienen als Grundlage für weitere <a href="./Glossar.md#teststeuerung" title="→ Glossar öffnen" class="glossary-term">**Teststeuerungsmaßnahmen**</a> und ermöglichen fundierte Entscheidungen über den Testfortschritt.**

## Erweiterte Vorteile der Verfolgbarkeit

### Auswirkungsanalyse von Änderungen

**Die <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> ermöglicht eine präzise <a href="./Glossar.md#auswirkungsanalyse" title="→ Glossar öffnen" class="glossary-term">**Auswirkungsanalyse**</a> von Änderungen.** Es kann systematisch analysiert werden, welche Modifikationen der <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> sich auf welche <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a>, <a href="./Glossar.md#testablauf" title="→ Glossar öffnen" class="glossary-term">**Testabläufe**</a>, <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> und <a href="./Glossar.md#testelement" title="→ Glossar öffnen" class="glossary-term">**Testelemente**</a> auswirken.

*Beispiel aus "Pixel Leap":* Als die Spielphysik-Engine von Unity auf Unreal umgestellt wurde, zeigte die Verfolgbarkeitsmatrix sofort, dass 23 von 156 Testfällen angepasst werden mussten, da sie direkt mit der Engine-spezifischen Sprungmechanik verknüpft waren.

### Risikobewertung und Restrisiko-Analyse

**Bei vorhandener <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> der <a href="./Glossar.md#testergebnis" title="→ Glossar öffnen" class="glossary-term">**Testergebnisse**</a> zu den identifizierten <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiken**</a> kann der Umfang des Restrisikos des <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekts**</a> fundierter beurteilt werden.**

**Diese Verknüpfung ermöglicht es, gezielt Bereiche mit hohem Restrisiko zu identifizieren und entsprechende Maßnahmen einzuleiten.**

### Abstraktion für Stakeholder-Kommunikation

**Durch die <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> können <a href="./Glossar.md#testergebnis" title="→ Glossar öffnen" class="glossary-term">**Testergebnisse**</a> auf eine abstraktere Ebene "gehoben" werden, wodurch das <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> auch für Nicht-Tester nachvollziehbar wird.**

> **Wichtige Erkenntnis:** Die bloße Betrachtung durchgeführter <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> gibt keine Auskunft darüber, wie intensiv und wie "breit" getestet wurde.

**Erst mit den Informationen aus der <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> lassen sich für jede interessierte Personengruppe verständliche Aussagen treffen.** Auch kann die Erfüllung von IT-Governance-Kriterien auf einem abstrakten Niveau nachgewiesen werden.

## Verbesserung der Testberichterstattung

### Testfortschritts- und Abschlussberichte

**<a href="./Glossar.md#testfortschrittsbericht" title="→ Glossar öffnen" class="glossary-term">**Testfortschrittsberichte**</a> und <a href="./Glossar.md#testabschlussbericht" title="→ Glossar öffnen" class="glossary-term">**Testabschlussberichte**</a> werden durch die <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> erheblich verständlicher und aussagekräftiger.**

**Der Status der Elemente der <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> ist in die Berichte aufzunehmen.** Zu jeder einzelnen <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderung**</a> kann eine der folgenden Aussagen getroffen werden:

| Status | Beschreibung |
|--------|--------------|
| **<a href="./Glossar.md#bestanden" title="→ Glossar öffnen" class="glossary-term">Tests bestanden</a>** | Alle zugehörigen <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> wurden erfolgreich durchgeführt |
| **<a href="./Glossar.md#fehlgeschlagen" title="→ Glossar öffnen" class="glossary-term">Tests fehlgeschlagen</a>** | <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> sind aufgetreten |
| **Tests ausstehend** | Geplante <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> stehen noch aus |

### Stakeholder-gerechte Aufbereitung

**Technische Aspekte des <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testens**</a> können mithilfe der <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> so aufbereitet werden, dass sie für verschiedene Stakeholder verständlich sind.**

**Die Beurteilung der Produktqualität, der Prozessfähigkeit und des Projektfortschritts anhand von Unternehmenszielen wird somit ermöglicht.**

*Beispiel aus "Pixel Leap":* Für das Management wurde aus der technischen Verfolgbarkeitsmatrix ein Dashboard erstellt, das zeigte: "87% der kritischen Gameplay-Features sind vollständig getestet und freigegeben", anstatt der technischen Details über 247 einzelne Testfälle.

## Praktische Umsetzung und Werkzeugunterstützung

### Organisatorische Managementsysteme

**Um die Vorteile der <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> vollständig zu nutzen, entwickeln einige Unternehmen eigene Managementsysteme.** Diese Systeme organisieren die Arbeitsergebnisse so, dass die benötigten Informationen zur <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> automatisch bereitgestellt werden.

### Kommerzielle Testmanagement-Werkzeuge

**Verschiedene am Markt erhältliche <a href="./Glossar.md#testmanagement" title="→ Glossar öffnen" class="glossary-term">**Testmanagement**</a>-Werkzeuge implementieren <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeits**</a>funktionen und automatisieren viele der manuellen Schritte.**

### Moderne Implementierungsansätze

**Zeitgemäße Umsetzungen der <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> umfassen:**

* **Integrierte ALM-Plattformen** - Application Lifecycle Management mit durchgängiger Verfolgbarkeit
* **Automatisierte Matrix-Generierung** - Dynamische Erstellung von Verfolgbarkeitsmatrizen aus Metadaten
* **Real-time Dashboards** - Live-Aktualisierung der Verfolgbarkeitsinformationen
* **API-basierte Synchronisation** - Automatischer Abgleich zwischen verschiedenen Werkzeugen

*Beispiel aus "Pixel Leap":* Das Entwicklungsteam verwendete Jira für Requirement-Management, verknüpft mit TestRail für Testfälle und Jenkins für Testautomatisierung. Eine API-Integration stellte sicher, dass jede Code-Änderung automatisch mit den betroffenen Tests und Anforderungen verknüpft wurde.

## Erfolgsfaktoren für effektive Verfolgbarkeit

### Granularitätsebenen

**Die <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> sollte auf angemessenen Granularitätsebenen implementiert werden:**

| Ebene | Von | Zu | Zweck |
|-------|-----|-----|-------|
| **Strategisch** | Geschäftsziele | <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> | Business-Alignment |
| **Taktisch** | <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> | <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> | Abdeckungsnachweis |
| **Operativ** | <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> | <a href="./Glossar.md#testergebnis" title="→ Glossar öffnen" class="glossary-term">**Testergebnisse**</a> | Ausführungsnachweis |

### Bidirektionale Verfolgbarkeit

**Eine bidirektionale <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> ermöglicht sowohl Forward- als auch Backward-Tracing:**

* **Forward-Tracing:** Von <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> zu <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> und Ergebnissen
* **Backward-Tracing:** Von <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> zurück zu ursprünglichen <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a>

## Herausforderungen und Lösungsansätze

### Wartungsaufwand

**Die Pflege der <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> erfordert kontinuierliche Aufmerksamkeit und kann ressourcenintensiv sein.**

**Lösungsansätze:**
* Automatisierung der Matrix-Updates
* Integration in bestehende Workflows
* Verwendung von Metadaten und Tags

### Komplexitätsmanagement

**Bei großen Projekten kann die Verfolgbarkeitsmatrix schnell unübersichtlich werden.**

**Bewältigungsstrategien:**
* Hierarchische Darstellungen
* Filterbare Views für verschiedene Stakeholder
* Fokussierung auf kritische Pfade

## Fazit

**Die <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> ist kein Selbstzweck, sondern ein strategisches Instrument zur Qualitätssicherung und Risikominimierung.** Sie schafft Transparenz, ermöglicht fundierte Entscheidungen und verbessert die Kommunikation zwischen allen Projektbeteiligten.

**Eine gut implementierte <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> transformiert das <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> von einer isolierten Aktivität zu einem integrierten Bestandteil des gesamten Entwicklungsprozesses** und trägt maßgeblich zum Projekterfolg bei.

**Investitionen in robuste Verfolgbarkeitssysteme zahlen sich durch verbesserte <a href="./Glossar.md#qualitaet" title="→ Glossar öffnen" class="glossary-term">**Qualität**</a>, reduzierte <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiken**</a> und erhöhte Stakeholder-Zufriedenheit langfristig aus.**