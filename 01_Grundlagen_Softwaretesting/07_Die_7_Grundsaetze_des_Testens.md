# Die sieben Grundsätze des Testens

## Fundamentale Prinzipien der Qualitätssicherung

**Die folgenden sieben Grundsätze haben sich über Jahrzehnte der Testpraxis herauskristallisiert** und gelten als universelle Leitlinien für professionelles <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a>. Sie bilden das konzeptionelle Fundament für alle <a href="./Glossar.md#testaktivitaeten" title="→ Glossar öffnen" class="glossary-term">**Testaktivitäten**</a>.

## Grundsatz 1: Testen zeigt die Anwesenheit von Fehlerzuständen

**<a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">Testen</a> kann das Vorhandensein von <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> und damit von <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzuständen**</a> nachweisen.** Je nach Testaufwand und Intensität verringert sich die Wahrscheinlichkeit, dass noch unentdeckte <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> im <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> vorhanden sind.

> <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">Testen</a> kann jedoch nicht beweisen, dass keine <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> im <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> vorhanden sind.

**Praktisches Beispiel aus "Pixel Leap":**
*Wenn alle durchgeführten <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> der Sprungmechanik erfolgreich verlaufen, bedeutet dies nicht, dass das System fehlerfrei ist. Es könnte noch ungetestete Kombinationen geben (z.B. Sprung während eines Power-ups bei gleichzeitigem Plattformwechsel), die Fehler aufdecken würden.*

**Selbst wenn keine <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> im <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> aufgezeigt wurden, ist dies kein Nachweis für Fehlerfreiheit oder Korrektheit.**

## Grundsatz 2: Vollständiges Testen ist nicht möglich

**Ein vollständiger <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> aller möglichen Eingabewerte und deren Kombinationen unter Berücksichtigung aller Vor- und Randbedingungen ist nicht durchführbar** - außer bei sehr trivialen <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekten**</a>.

**Beispiel der kombinatorischen Explosion:**
*In "Pixel Leap" mit 10 Level-Typen, 8 Charaktervarianten, 15 Power-ups und 20 Gegnertypen ergeben sich bereits 24.000 Basis-Kombinationen. Hinzu kommen verschiedene Plattform-Konfigurationen, Timing-Varianten und Spielerzustände - die Gesamtzahl wird schnell astronomisch.*

**<a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">Tests</a> sind immer nur Stichproben**, und der Testaufwand ist deshalb unter Verwendung von <a href="./Glossar.md#testverfahren" title="→ Glossar öffnen" class="glossary-term">**Testverfahren**</a> nach <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiko**</a> und <a href="./Glossar.md#prioritaet" title="→ Glossar öffnen" class="glossary-term">**Prioritäten**</a> zu steuern.

## Grundsatz 3: Frühes Testen spart Zeit und Geld

**Testaktivitäten - sowohl <a href="./Glossar.md#statischer-test" title="→ Glossar öffnen" class="glossary-term">**statische**</a> als auch <a href="./Glossar.md#dynamischer-test" title="→ Glossar öffnen" class="glossary-term">**dynamische**</a> - sollen im System- oder <a href="./Glossar.md#softwareentwicklungslebenszyklus" title="→ Glossar öffnen" class="glossary-term">**Softwareentwicklungslebenszyklus**</a> so früh wie möglich beginnen** und definierte <a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">**Testziele**</a> verfolgen. Dieser Ansatz wird auch als <a href="./Glossar.md#shift-left" title="→ Glossar öffnen" class="glossary-term">**"Shift Left"**</a> bezeichnet.

**Kostenvorteil des frühen <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testens**</a>:**
*Ein Fehler in der Spielmechanik-Spezifikation von "Pixel Leap", der in der <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungsphase**</a> für 1 Stunde Aufwand behoben werden kann, würde in der Implementierungsphase 10 Stunden und nach dem Release möglicherweise ein komplettes Update mit Hunderten von Arbeitsstunden erfordern.*

**Durch frühzeitiges Prüfen werden <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> frühzeitig erkannt** und kostenintensive späte Änderungen reduziert oder vermieden.

## Grundsatz 4: Häufung von Fehlerzuständen

**<a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">Fehlerzustände</a> sind in der Regel nicht gleichmäßig über das gesamte System verteilt.** Vielmehr finden sich die meisten <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> in nur wenigen Teilen (<a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponenten**</a>) eines Systems.

**Praktisches Beispiel:**
*In "Pixel Leap" zeigt sich, dass 80% aller Bugs im Kollisionssystem auftreten, während die Menü-Navigation nahezu fehlerfrei ist. Diese Beobachtung führt dazu, dass zusätzliche Testressourcen auf das Kollisionssystem konzentriert werden.*

**Die geschätzte oder beobachtete Anhäufung von <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzuständen**</a>** kann zur <a href="./Glossar.md#risikoanalyse" title="→ Glossar öffnen" class="glossary-term">**Risikoanalyse**</a> genutzt werden, um den Testaufwand gezielt auf fehlerträchtige Bereiche zu konzentrieren.

## Grundsatz 5: Testfälle "nutzen sich ab"

**Werden <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">Tests</a> an unveränderten Systemversionen nur wiederholt, decken sie keine neuen <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> mehr auf.** Damit die <a href="./Glossar.md#effektivitaet" title="→ Glossar öffnen" class="glossary-term">**Effektivität**</a> der <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> nicht absinkt, sind vorhandene <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> regelmäßig zu prüfen und durch neue oder modifizierte <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> zu ergänzen.

**Beispiel aus der Spieleentwicklung:**
*Die ursprünglichen <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> für "Pixel Leap" prüften Standard-Sprungsequenzen. Nach mehreren Updates finden diese <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> keine neuen Bugs mehr. Erst neue <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> für komplexe Sprung-Kombinationen oder Edge-Cases decken weitere Probleme auf.*

**Trotzdem kann die Wiederholung unveränderten <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> sinnvoll sein**, insbesondere bei automatisierten <a href="./Glossar.md#regressionstest" title="→ Glossar öffnen" class="glossary-term">**Regressionstests**</a>.

## Grundsatz 6: Testen ist kontextabhängig

**Je nach Einsatzgebiet und Umfeld des zu prüfenden Systems ist das <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> anzupassen.** Keine zwei Systeme sind auf exakt gleiche Art und Weise zu testen.

**Kontextuelle Unterschiede:**

| Systemtyp | Testfokus | Besonderheiten |
|-----------|-----------|----------------|
| **Mobile Games** | <a href="./Glossar.md#performanz" title="→ Glossar öffnen" class="glossary-term">**Performance**</a>, Akkulaufzeit, Touch-Interface | Verschiedene Gerätegrößen, OS-Versionen |
| **Online-Multiplayer** | Netzwerk-Synchronisation, Latenz | Server-Last, Verbindungsabbrüche |
| **Embedded Games** | Real-time Constraints, Hardware-Integration | Begrenzte Ressourcen, deterministische Abläufe |

**Intensität des <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testens**</a>, Definition der <a href="./Glossar.md#endekriterien" title="→ Glossar öffnen" class="glossary-term">**Endekriterien**</a> und <a href="./Glossar.md#testverfahren" title="→ Glossar öffnen" class="glossary-term">**Testverfahren**</a>** sind bei jedem System entsprechend seines Einsatzumfelds festzulegen.

## Grundsatz 7: Trugschluss - Keine Fehler bedeutet ein brauchbares System

**Trotz gründlicher <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">Tests</a> aller spezifizierten <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> und Beheben aller gefundenen <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> kann ein System entwickelt worden sein**, das schwer zu nutzen ist oder die Bedürfnisse der Nutzer nicht erfüllt.

**Beispiel aus "Pixel Leap":**
*Alle technischen <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> sind erfolgreich - Sprungmechanik funktioniert präzise, Kollisionen werden korrekt erkannt, <a href="./Glossar.md#performanz" title="→ Glossar öffnen" class="glossary-term">**Performance**</a> ist optimal. Dennoch beschweren sich Spieler, dass das Spiel zu schwierig und frustrierend ist, weil die Sprungdistanzen unintuitiv sind.*

> Ein technisch fehlerfreies System kann trotzdem unbrauchbar oder von schlechter <a href="./Glossar.md#qualitaet" title="→ Glossar öffnen" class="glossary-term">**Qualität**</a> sein.

**Präventive Maßnahmen:**
* Frühzeitige Einbeziehung der späteren Nutzer in den Entwicklungsprozess
* Nutzung von Prototyping und User-Testing
* <a href="./Glossar.md#validierung" title="→ Glossar öffnen" class="glossary-term">**Validierung**</a> der User Experience zusätzlich zur technischen <a href="./Glossar.md#verifizierung" title="→ Glossar öffnen" class="glossary-term">**Verifikation**</a>

## Fazit

**Diese sieben Grundsätze bilden das konzeptionelle Rückgrat professionellen <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testens**</a>.** Sie helfen dabei, realistische Erwartungen zu setzen, Ressourcen effizient einzusetzen und sowohl technische als auch benutzerzentrierte <a href="./Glossar.md#qualitaet" title="→ Glossar öffnen" class="glossary-term">**Qualität**</a> sicherzustellen.

**Für "Pixel Leap" bedeuten sie:** Ein systematischer, <a href="./Glossar.md#risikobasierter-test" title="→ Glossar öffnen" class="glossary-term">**risikobasierter**</a> Ansatz, der technische Korrektheit und Spielerfahrung gleichermaßen berücksichtigt, frühzeitig beginnt und kontinuierlich an neue Erkenntnisse angepasst wird.
