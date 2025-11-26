# Wartungstest - Systematische Qualitätssicherung bei Software-Evolution

Die kontinuierliche Evolution von Softwaresystemen durch <a href="./Glossar.md#wartung" title="→ Glossar öffnen" class="glossary-term">**Wartung**</a> und Pflege erfordert spezialisierte Teststrategien, die sich fundamental von der ursprünglichen Entwicklungsvalidierung unterscheiden. <a href="./Glossar.md#wartungstest" title="→ Glossar öffnen" class="glossary-term">**Wartungstests**</a> adressieren die spezifischen Herausforderungen der Qualitätssicherung bei iterativen Systemänderungen und gewährleisten, dass Modifikationen sowohl ihre beabsichtigten Ziele erreichen als auch keine ungewollten Seiteneffekte verursachen. Diese Testdisziplin bildet das Rückgrat nachhaltiger Softwarequalität über den gesamten Produktlebenszyklus hinweg.

## Grundlagen der Software-Evolution

### Unterscheidung zwischen Wartung und Pflege

**Jedes Softwaresystem benötigt über die Dauer seiner Nutzung kontinuierliche Korrekturen und Ergänzungen, wobei zwischen zwei fundamentalen Kategorien unterschieden wird.** Im Gegensatz zu Hardwareprodukten geht es jedoch nicht um die Erhaltung der Einsatzfähigkeit durch regelmäßige Pflege oder die Reparatur von Abnutzungsschäden, da Software nicht altert oder verschleißt.

#### <a href="./Glossar.md#wartung" title="→ Glossar öffnen" class="glossary-term">**Softwarewartung**</a> im engeren Sinne
**Von <a href="./Glossar.md#wartung" title="→ Glossar öffnen" class="glossary-term">**Softwarewartung**</a> wird gesprochen, wenn <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> beseitigt werden, die bereits im ursprünglichen Produkt enthalten waren.** Diese korrektive <a href="./Glossar.md#wartung" title="→ Glossar öffnen" class="glossary-term">**Wartung**</a> fokussiert auf die Behebung von Implementierungsfehlern und Funktionsdefekten.

#### Softwarepflege als adaptive Anpassung
**Von Softwarepflege wird gesprochen, wenn ein Produkt an geänderte Einsatzbedingungen angepasst wird.** Dies umfasst Anpassungen an neue Betriebssystemversionen, Datenbanksystem-Updates oder veränderte Kommunikationsprotokolle.

*Beispiel aus "Pixel Leap":* <a href="./Glossar.md#wartung" title="→ Glossar öffnen" class="glossary-term">**Wartung**</a> behebt einen Bug in der Sprungphysik, der bei bestimmten Framerate-Bedingungen inkorrekte Kollisionserkennung verursacht. Pflege passt das Spiel an neue Grafiktreiber-APIs an, um Kompatibilität mit aktueller Hardware zu gewährleisten.*

### Auslöser für Systemänderungen

**Verschiedene Faktoren können Änderungen eines Softwareprodukts auslösen, wobei jeder Auslöser spezifische Testanforderungen mit sich bringt:**

#### Korrektive Änderungen
* **Bugfixes** zur Behebung identifizierter <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a>
* **<a href="./Glossar.md#sicherheit-security" title="→ Glossar öffnen" class="glossary-term">**Sicherheits**</a>patches** zur Schließung von Schwachstellen
* **<a href="./Glossar.md#performanz" title="→ Glossar öffnen" class="glossary-term">**Performance**</a>optimierungen** zur Behebung von Leistungsproblemen

#### Evolutionäre Änderungen
* **Funktionserweiterungen** im Zuge der normalen Produktweiterentwicklung
* **<a href="./Glossar.md#benutzererlebnis" title="→ Glossar öffnen" class="glossary-term">**Benutzererlebnis**</a>-Verbesserungen** basierend auf Anwenderfeedback
* **Neue Features** zur Marktdifferenzierung

## Release-Management und Teststrategien

### Herausforderungen der Versionsvalidierung

**In jedem Änderungsfall entsteht eine neue Version oder ein neues Release des Produkts.** Große Teile der neuen Version bleiben gegenüber der Vorversion unverändert, manche Teile werden modifiziert und einige Komponenten werden neu hinzugefügt.

**Dies wirft fundamentale Fragen für die Teststrategie auf:**
* **Vollständige Wiederholung** aller <a href="./Glossar.md#teststufe" title="→ Glossar öffnen" class="glossary-term">**Teststufen**</a> bei jedem Release?
* **Selektive Testung** nur der von Änderungen betroffenen Softwareelemente?
* **<a href="./Glossar.md#risikobasierter-test" title="→ Glossar öffnen" class="glossary-term">**Risikobasierte Priorisierung**</a>** der Testaktivitäten?

## Fehlernachtest bei Softwarewartung

### Grundstrategie der Korrekturvalidierung

**Bei <a href="./Glossar.md#wartung" title="→ Glossar öffnen" class="glossary-term">**Softwarewartung**</a> zur Beseitigung von <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzuständen**</a> bildet der <a href="./Glossar.md#fehlernachtest" title="→ Glossar öffnen" class="glossary-term">**Fehlernachtest**</a> die grundlegende Teststrategie.** An der korrigierten Version müssen alle <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> ausgeführt werden, die in der Vorversion <a href="./Glossar.md#fehlgeschlagen" title="→ Glossar öffnen" class="glossary-term">**fehlgeschlagen**</a> waren und die betreffenden <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> aufgedeckt hatten.

**Diese <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> müssen an der neuen Version das <a href="./Glossar.md#testergebnis" title="→ Glossar öffnen" class="glossary-term">**Testergebnis**</a> "<a href="./Glossar.md#bestanden" title="→ Glossar öffnen" class="glossary-term">**bestanden**</a>" liefern, damit die betreffenden <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> als korrigiert gelten.** Wurden <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> behoben, die bisher nicht durch <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> aufgedeckt wurden, sind entsprechende Tests zu ergänzen und zur Korrekturvalidierung auszuführen.

*Beispiel aus "Pixel Leap":* Ein Sprungphysik-Bug verursachte Phantom-Kollisionen bei hohen Framerates. Der <a href="./Glossar.md#fehlernachtest" title="→ Glossar öffnen" class="glossary-term">**Fehlernachtest**</a> führt systematisch alle Sprung-Szenarien bei verschiedenen Framerate-Bedingungen aus, um zu validieren, dass die Kollisionserkennung nun korrekt funktioniert.*

### Erweiterte Validierung von Umgebungseffekten

**Fehlerkorrektur verändert häufig auch das nicht-fehlerhafte Verhalten von Softwareelementen in der Umgebung der Modifikation.** Dies kann beabsichtigt oder unbeabsichtigt geschehen, erfordert aber in beiden Fällen zusätzliche Testvalidierung.

**Zusätzliche Testanforderungen umfassen:**

#### Validierung beabsichtigter Änderungen
* **Angepasste oder neue <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a>** zur Prüfung der beabsichtigten Wirkung
* **Funktionale Erweiterungstests** für neue oder modifizierte Features
* **<a href="./Glossar.md#benutzererlebnis" title="→ Glossar öffnen" class="glossary-term">**Benutzererlebnis**</a>-Validierung** bei Interface-Änderungen

#### <a href="./Glossar.md#regressionstest" title="→ Glossar öffnen" class="glossary-term">**Regressionstests**</a> für Unverändertheit
* **Wiederholung vorhandener <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a>** zur Validierung unveränderter Funktionalität
* **Systematische Prüfung** der Stabilität nicht-modifizierter Systembereiche
* **End-to-End-Validierung** kritischer Anwendungsszenarien

### Hotfix-Strategien für kritische Probleme

**Bei kritischen <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a>, die sofortige Beseitigung erfordern, ist eine schnelle Notlösung wichtiger als eine vollständige, ausgereifte Lösung.** Hotfixes erfordern angepasste Teststrategien, die Geschwindigkeit und Grundsicherheit ausbalancieren.

**Hotfix-Teststrategien fokussieren auf:**
* **Konzentration auf wichtigste <a href="./Glossar.md#fehlernachtest" title="→ Glossar öffnen" class="glossary-term">**Fehlernachtests**</a>** für Zeitersparnis
* **Kritische Funktionspfad-Validierung** zur Vermeidung neuer Probleme
* **Schnellstmögliche Bereitstellung** beim Kunden
* **Nachgelagerte gründliche Testung** sobald möglich

*Beispiel aus "Pixel Leap":* Ein kritischer Multiplayer-Bug verhindert Spieler-Verbindungen. Der Hotfix wird mit minimalen Tests zur Funktionswiederherstellung schnell deployed, während umfassende <a href="./Glossar.md#regressionstest" title="→ Glossar öffnen" class="glossary-term">**Regressionstests**</a> parallel vorbereitet werden.*

## Strategische Wartungstest-Planung

### Proaktive Testplanung für Wartungsreleases

**Der Test nach <a href="./Glossar.md#wartung" title="→ Glossar öffnen" class="glossary-term">**Softwarewartung**</a> wird erheblich erleichtert und erfolgreicher, wenn Wartungsreleases im Voraus geplant und in Testplänen berücksichtigt werden.** Diese proaktive Herangehensweise reduziert Reaktionszeiten und verbessert die Testqualität.

### Herausforderungen bei Legacy-Systemen

**Bei sehr alten Systemen liegen oft keine oder sehr veraltete Spezifikationen vor, was Wartungsarbeiten und deren Test entsprechend erschwert.** Diese Realität muss bei der Testplanung explizit berücksichtigt werden:

* **Reverse Engineering** bestehender Funktionalität zur Testbasis-Erstellung
* **Explorative Tests** zur Systemverhalten-Dokumentation
* **Schrittweise Testabdeckung-Verbesserung** über mehrere Wartungszyklen
* **Erhöhte Testressourcen** für unzureichend dokumentierte Systembereiche

### Falsche Sparsamkeit vermeiden

**Die Notwendigkeit kontinuierlicher <a href="./Glossar.md#wartung" title="→ Glossar öffnen" class="glossary-term">**Wartung**</a> darf nicht als Argument für grundsätzliche Test-Sparsamkeit missbraucht werden.** Das Motto "Wir bringen sowieso immer wieder neue Versionen raus, also sind übersehene Fehler nicht so schlimm" verkennt die Kosten und <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiken**</a> von Softwarefehlern.

## Auswirkungsanalyse und Systemische Risiken

### Grenzen lokaler Testansätze

**Sowohl <a href="./Glossar.md#fehlernachtest" title="→ Glossar öffnen" class="glossary-term">**Fehlernachtests**</a> als auch Tests nur am Ort oder in der Umgebung der Modifikation sind nicht wirklich ausreichend.** In Softwaresystemen können scheinbar simple lokale Änderungen unerwartete und fatale Auswirkungen auf beliebige andere, auch entfernte Systemteile haben.

### <a href="./Glossar.md#auswirkungsanalyse" title="→ Glossar öffnen" class="glossary-term">**Auswirkungsanalyse**</a> als systematischer Ansatz

**Welche und wie viele <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> nötig sind, um Seiteneffekt-<a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiken**</a> zu minimieren, muss durch spezifische <a href="./Glossar.md#auswirkungsanalyse" title="→ Glossar öffnen" class="glossary-term">**Auswirkungsanalyse**</a> der vorgenommenen Änderungen ermittelt werden.**

**Systematische <a href="./Glossar.md#auswirkungsanalyse" title="→ Glossar öffnen" class="glossary-term">**Auswirkungsanalyse**</a> umfasst:**

#### Abhängigkeitsanalyse
* **Direkte Abhängigkeiten** zwischen modifizierten und anderen <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponenten**</a>
* **Indirekte Kopplungen** über gemeinsame Datenstrukturen oder Services
* **Transitive Abhängigkeiten** in komplexen Aufrufhierarchien

#### Datenfluss-Analyse
* **Gemeinsam genutzte Datenstrukturen** und deren potenzielle Beeinflussung
* **Datenbank-Schema-Änderungen** und deren Auswirkungen auf andere Module
* **API-Kontraktänderungen** und deren Auswirkungen auf Clients

#### Konfiguration und Deployment
* **Umgebungsabhängige Konfigurationen** und deren Änderungsauswirkungen
* **Deployment-Abhängigkeiten** zwischen verschiedenen Systemkomponenten
* **Laufzeit-Umgebungen** und deren potenzielle Beeinflussung

*Beispiel aus "Pixel Leap":* Eine scheinbar lokale Änderung am Punkte-System beeinflusst auch Achievement-Berechnungen, Leaderboard-Rankings und die Tutorial-Progressionslogik. Die <a href="./Glossar.md#auswirkungsanalyse" title="→ Glossar öffnen" class="glossary-term">**Auswirkungsanalyse**</a> identifiziert alle betroffenen Systembereiche für umfassende Testabdeckung.*

## Softwarepflege und adaptive Wartung

### Umgebungsanpassung und Akzeptanztests

**Bei Softwarepflege zur Anpassung an geänderte Einsatzbedingungen sollte erneut ein Test auf Akzeptanz durch die Systembetreiber durchgeführt werden.** Die nicht-funktionalen Eigenschaften des Systems können sich in der neuen Umgebung erheblich vom gewohnten Verhalten unterscheiden.

**Kritische Validierungsaspekte umfassen:**
* **<a href="./Glossar.md#performanz" title="→ Glossar öffnen" class="glossary-term">**Performanz**</a>-Charakteristika** in der neuen Umgebung
* **Ressourcenbedarf und Installationsvoraussetzungen**
* **<a href="./Glossar.md#kompatibilitaet" title="→ Glossar öffnen" class="glossary-term">**Kompatibilität**</a> mit anderen Systemkomponenten**
* **<a href="./Glossar.md#sicherheit-security" title="→ Glossar öffnen" class="glossary-term">**Sicherheits**</a>aspekte** in der veränderten Umgebung

### Datenmigration und -konversion

**Müssen Datenbestände konvertiert oder migriert werden, ist auch dieser Aspekt auf Korrektheit und Vollständigkeit durch geeignete Tests zu prüfen.** Datenmigrationstests bilden einen kritischen Aspekt der Pflege-Validierung.

**Datenmigrations-Teststrategien:**
* **Vollständigkeitsprüfung** aller migrierten Datensätze
* **<a href="./Glossar.md#integritaet" title="→ Glossar öffnen" class="glossary-term">**Integritäts**</a>validierung** der Datenbeziehungen
* **<a href="./Glossar.md#performanz" title="→ Glossar öffnen" class="glossary-term">**Performance**</a>tests** der Migrations-Prozeduren
* **Rollback-Verfahren** für Notfallsituationen

*Beispiel aus "Pixel Leap":* Bei der Anpassung an eine neue Unity-Version müssen Spielstände von der alten zur neuen Serialisierungsstruktur migriert werden. Tests validieren, dass alle Spieler-Daten, Achievements und Einstellungen korrekt übertragen werden.*

## Moderne Wartungstest-Praktiken

### Automatisierung und kontinuierliche Integration

**Moderne <a href="./Glossar.md#wartungstest" title="→ Glossar öffnen" class="glossary-term">**Wartungstest**</a>-Strategien integrieren sich nahtlos in <a href="./Glossar.md#kontinuierliche-integration" title="→ Glossar öffnen" class="glossary-term">**kontinuierliche Integration**</a> und Deployment-Pipelines:**

* **Automatisierte <a href="./Glossar.md#regressionstest" title="→ Glossar öffnen" class="glossary-term">**Regressionstests**</a>** bei jeder Code-Änderung
* **<a href="./Glossar.md#auswirkungsanalyse" title="→ Glossar öffnen" class="glossary-term">**Auswirkungsanalyse**</a>-Tools** zur automatischen Abhängigkeitsidentifikation
* **Intelligente Testauswahl** basierend auf Änderungsumfang
* **Parallel Testing** zur Beschleunigung der Validierung

### DevOps-Integration

**<a href="./Glossar.md#wartungstest" title="→ Glossar öffnen" class="glossary-term">**Wartungstests**</a> werden zunehmend in DevOps-Prozesse integriert, die Entwicklung, Test und Betrieb nahtlos verbinden:**

* **Infrastructure as Code** für reproduzierbare <a href="./Glossar.md#testumgebung" title="→ Glossar öffnen" class="glossary-term">**Testumgebungen**</a>
* **Monitoring-Integration** für proaktive Problemalerkennung
* **Canary Deployments** für schrittweise Rollouts
* **Feature Flags** für kontrollierte Funktionsfreigabe

## Fazit

**<a href="./Glossar.md#wartungstest" title="→ Glossar öffnen" class="glossary-term">**Wartungstests**</a> bilden eine spezialisierte Disziplin der Qualitätssicherung, die sich systematisch von ursprünglichen Entwicklungstests unterscheidet.** Ihre erfolgreiche Anwendung erfordert tiefes Verständnis für Systemabhängigkeiten und potenzielle Änderungsauswirkungen.

**Die Unterscheidung zwischen korrektiver <a href="./Glossar.md#wartung" title="→ Glossar öffnen" class="glossary-term">**Wartung**</a> und adaptiver Pflege bestimmt maßgeblich die erforderlichen Teststrategien.** <a href="./Glossar.md#fehlernachtest" title="→ Glossar öffnen" class="glossary-term">**Fehlernachtests**</a> dominieren bei Korrekturen, während Umgebungsvalidierung bei Anpassungen kritisch wird.

**Die <a href="./Glossar.md#auswirkungsanalyse" title="→ Glossar öffnen" class="glossary-term">**Auswirkungsanalyse**</a> als systematischer Ansatz zur Identifikation potenzieller Seiteneffekte stellt sicher, dass scheinbar lokale Änderungen nicht zu unerwarteten Systemproblemen führen.** Diese Analyse bildet die Grundlage für angemessene Testabdeckung.

**Moderne <a href="./Glossar.md#wartungstest" title="→ Glossar öffnen" class="glossary-term">**Wartungstest**</a>-Praktiken integrieren Automatisierung, <a href="./Glossar.md#kontinuierliche-integration" title="→ Glossar öffnen" class="glossary-term">**kontinuierliche Integration**</a> und DevOps-Prinzipien für effiziente und zuverlässige Qualitätssicherung.** Diese Evolution ermöglicht schnelle, sichere Software-Evolution bei minimalen <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiken**</a>.

**Letztendlich entscheidet die Qualität der <a href="./Glossar.md#wartungstest" title="→ Glossar öffnen" class="glossary-term">**Wartungstests**</a> über die langfristige Stabilität und Anwenderakzeptanz von Softwaresystemen im produktiven Einsatz.**