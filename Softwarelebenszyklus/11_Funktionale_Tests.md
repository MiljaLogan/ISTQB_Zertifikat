# Funktionale Tests - Verhaltensvalidierung von Softwaresystemen

Die systematische Validierung des von außen sichtbaren Ein-/Ausgabeverhaltens von Softwaresystemen bildet den Kern <a href="./Glossar.md#funktionaler-test" title="→ Glossar öffnen" class="glossary-term">**funktionaler Tests**</a>. Diese essenzielle <a href="./Glossar.md#testart" title="→ Glossar öffnen" class="glossary-term">**Testart**</a> subsumiert alle Testverfahren und -methoden, die das beobachtbare Systemverhalten gegen spezifizierte Erwartungen prüfen. <a href="./Glossar.md#funktionaler-test" title="→ Glossar öffnen" class="glossary-term">**Funktionale Tests**</a> verwenden ausschließlich <a href="./Glossar.md#black-box-testverfahren" title="→ Glossar öffnen" class="glossary-term">**Black-Box-Testverfahren**</a> zur <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a>-Erstellung und nutzen funktionale <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> als <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> für die Definition des erwarteten Sollverhaltens.

## Funktionale Anforderungen als Testgrundlage

### Definition und Charakteristika funktionaler Anforderungen

**Funktionale <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> spezifizieren das Verhalten, das das System oder Systemteile erbringen müssen.** Sie beschreiben das "Was" - die konkreten Leistungen, die ein System oder Teilsystem erbringen soll. Ihre vollständige Umsetzung bildet die Grundvoraussetzung dafür, dass das System überhaupt einsetzbar wird.

**Ob und wie umfassend ein System seine funktionalen <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> erfüllt, wird als <a href="./Glossar.md#funktionale-angemessenheit" title="→ Glossar öffnen" class="glossary-term">**funktionale Angemessenheit**</a> bezeichnet.** Dieses <a href="./Glossar.md#qualitaetsmerkmal" title="→ Glossar öffnen" class="glossary-term">**Qualitätsmerkmal**</a> umfasst drei wesentliche Aspekte: <a href="./Glossar.md#funktionale-vollstaendigkeit" title="→ Glossar öffnen" class="glossary-term">**funktionale Vollständigkeit**</a>, <a href="./Glossar.md#funktionale-korrektheit" title="→ Glossar öffnen" class="glossary-term">**funktionale Korrektheit**</a> und funktionelle Zweckmäßigkeit.

### Beispielhafte funktionale Anforderungen

*Beispiel aus "Pixel Leap":* Funktionale Anforderungen für das Charakter-Bewegungssystem könnten folgendermaßen spezifiziert werden:

**F 100:** Der Spieler kann seinen Charakter mittels Tastatureingaben horizontal bewegen (Links-/Rechtspfeiltasten)

**F 101:** Bei Betätigung der Sprungtaste führt der Charakter einen physikalisch realistischen Sprung mit konfigurierbarer Höhe und Weite aus

**F 102:** Die Sprungphysik berücksichtigt die aktuelle Bewegungsgeschwindigkeit für die horizontale Sprungweite

**F 103:** Nur bei Bodenkontakt sind weitere Sprünge möglich; Doppelsprünge werden nur bei entsprechender Power-Up-Aktivierung ermöglicht

**Diese funktionalen <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> definieren klar abgrenzbare, testbare Systemverhalten ohne interne Implementierungsdetails zu spezifizieren.**

## Ableitung funktionaler Testfälle

### Systematische Testfall-Entwicklung

**<a href="./Glossar.md#funktionaler-test" title="→ Glossar öffnen" class="glossary-term">**Funktionale Tests**</a> werden ermittelt, indem zu jeder funktionalen <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderung**</a> mindestens ein <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> abgeleitet wird.** Die Entwicklung erfolgt systematisch durch Analyse der Anforderungsspezifikation und Identifikation prüfbarer Verhaltensaspekte.

*Beispiel aus "Pixel Leap":* Für die Anforderung F 102 (Sprungphysik berücksichtigt Bewegungsgeschwindigkeit) könnten folgende <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> entwickelt werden:

**T 102.1:** Charakter springt aus dem Stand - Sprungweite entspricht Basis-Distanz gemäß Spezifikation

**T 102.2:** Charakter springt während schneller Vorwärtsbewegung - Sprungweite erhöht sich proportional zur Laufgeschwindigkeit

**T 102.3:** Charakter springt während Rückwärtsbewegung - Sprungweite reduziert sich entsprechend der negativen Geschwindigkeit

**T 102.4:** Charakter springt bei maximaler Bewegungsgeschwindigkeit - Sprungweite erreicht spezifizierten Maximalwert

### Mehrfach-Testfälle für komplexe Anforderungen

**Typischerweise wird mehr als nur ein <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> benötigt, um eine funktionale <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderung**</a> umfassend zu testen.** Funktionale Anforderungen enthalten häufig eine Reihe von Varianten und Sonderfällen, die durch eine systematische Abfolge von <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> abgedeckt werden müssen.

**Durch Einsatz zusätzlicher <a href="./Glossar.md#black-box-testverfahren" title="→ Glossar öffnen" class="glossary-term">**Black-Box-Testverfahren**</a> wie <a href="./Glossar.md#aequivalenzklassenbildung" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklassenbildung**</a> können diese Beispiel-<a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> systematisch verfeinert und ergänzt werden.** Diese methodische Herangehensweise gewährleistet umfassende Abdeckung aller relevanten Eingabe- und Verhaltensvarianten.

### Erfolgs- und Abschlusskriterien

**Entscheidend ist das definierte Abschlusskriterium: Sind die definierten <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> oder eine in der Testspezifikation festgelegte Mindestanzahl davon fehlerfrei durchgelaufen, wird die entsprechende Funktionalität als korrekt implementiert betrachtet.** Dieses binäre Erfolgskriterium bildet die Grundlage für Projektfortschritt und Qualitätsbewertung.

## Teststufen-spezifische Anwendung

### Universelle Einsetzbarkeit funktionaler Tests

**<a href="./Glossar.md#funktionaler-test" title="→ Glossar öffnen" class="glossary-term">**Funktionales Testen**</a> kommt in jeder <a href="./Glossar.md#teststufe" title="→ Glossar öffnen" class="glossary-term">**Teststufe**</a> zum Einsatz, wobei sich jeweils die verwendete <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> unterscheidet.** Die grundlegenden Prinzipien der Verhaltensvalidierung bleiben dabei konsistent, während sich der Detaillierungsgrad und die Perspektive ändern.

### Niedrige Teststufen (Komponenten- und Integrationstest)

**Im <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententest**</a> und <a href="./Glossar.md#integrationstest" title="→ Glossar öffnen" class="glossary-term">**Integrationstest**</a> dient die technische Spezifikation der <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponenten**</a> als <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a>.** Schnittstellenspezifikationen (APIs) und teilweise auch White-Box-Informationen ergänzen die funktionale Validierung auf dieser technischen Ebene.

### Höhere Teststufen (System-, Systemintegrations- und Abnahmetest)

**Im <a href="./Glossar.md#systemtest" title="→ Glossar öffnen" class="glossary-term">**Systemtest**</a>, <a href="./Glossar.md#systemintegrationstest" title="→ Glossar öffnen" class="glossary-term">**Systemintegrationstest**</a> und <a href="./Glossar.md#abnahmetest" title="→ Glossar öffnen" class="glossary-term">**Abnahmetest**</a> dienen funktionale System<a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**anforderungen**</a> als <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a>.** Diese anwenderorientierten Anforderungen beschreiben das erwartete Systemverhalten aus Geschäftsperspektive und Endnutzersicht.

*Beispiel aus "Pixel Leap":* Während auf <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponenten**</a>ebene die mathematische Korrektheit der Physics-Engine getestet wird, validiert der <a href="./Glossar.md#systemtest" title="→ Glossar öffnen" class="glossary-term">**Systemtest**</a> das Spielerlebnis: "Fühlen sich die Sprünge responsiv und natürlich an?"*

## Anwendungsfall- und geschäftsprozessbasiertes Testen

### Erweiterte Testmethodik für Geschäftssysteme

**Wenn ein Softwaresystem den Zweck hat, bestimmte Geschäftsprozesse des Kunden zu automatisieren oder zu unterstützen, bildet anwendungsfall- oder geschäftsprozessbasiertes Testen eine besonders geeignete, verwandte Testmethode.** Diese Herangehensweise erweitert die anforderungsbasierte Sichtweise um realistische Nutzungsszenarien.

### Geschäftsprozess-orientierte Testszenarien

*Beispiel aus "Pixel Leap":* Der grundlegende Spieler-Geschäftsprozess könnte folgendermaßen strukturiert sein:

**Spieleinstieg:** Der Spieler startet das Spiel und wählt einen Schwierigkeitsgrad

**Charaktersteuerung:** Der Spieler navigiert durch das erste Level und lernt die Grundsteuerung

**Herausforderungsbewältigung:** Der Spieler überwindet erste Hindernisse und sammelt Erfahrungen

**Progression:** Der Spieler schaltet neue Levels frei und entwickelt seine Fähigkeiten weiter

**Längerfristige Bindung:** Der Spieler kehrt regelmäßig zurück und erkundet fortgeschrittene Inhalte

### Geschäftsprozessanalyse als Testgrundlage

**Eine Geschäftsprozessanalyse zeigt, welche Geschäftsprozesse relevant sind, wie häufig und in welchem Kontext sie auftreten, welche Personen, Firmen oder externe Systeme daran beteiligt sind.** Auf Grundlage dieser Analyse werden als <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> Testszenarien entwickelt, die typische Geschäftsvorfälle realitätsnah nachbilden.

**Die Priorität der Testszenarien richtet sich nach Häufigkeit und Relevanz sowie nach dem <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiko**</a> der entsprechenden Geschäftsprozesse.** Diese <a href="./Glossar.md#risikobasierter-test" title="→ Glossar öffnen" class="glossary-term">**risikobasierte Priorisierung**</a> gewährleistet effiziente Ressourcenallokation bei der Testplanung.

### Unterschied zwischen anforderungs- und prozessbasiertem Testen

**Während beim anforderungsbasierten <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> einzelne Systemfunktionen im Fokus stehen, betrachtet geschäftsprozessbasiertes <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> zusammenhängende Abläufe.** Statt isolierter Funktionsprüfung werden hintereinandergeschaltete Tests durchgeführt, die realistische Anwendungssequenzen abbilden.

**Prozessbasierte Testsequenzen:**
* **End-to-End-Workflows** von Anfang bis Abschluss eines Geschäftsvorgangs
* **Multi-System-Interaktionen** über Systemgrenzen hinweg
* **Realistische Datenvolumen** und -komplexität
* **Zeitliche Abhängigkeiten** und Sequenzierungsanforderungen

*Beispiel aus "Pixel Leap":* Statt nur die Speicherfunktion zu testen (anforderungsbasiert), wird der komplette Spielfortschritt von Charaktererstellung über mehrere Levels bis zur automatischen Cloud-Synchronisation getestet (prozessbasiert).*

## Grenzen funktionaler Tests

### Notwendigkeit nicht-funktionaler Validierung

**Für Anwender ist oft nicht nur entscheidend, ob bestimmte Funktionen verfügbar sind, sondern wie gut sie damit arbeiten können.** Die Akzeptanz hängt maßgeblich davon ab, ob die Software leicht zu bedienen ist, ob sie schnell genug reagiert und übersichtliche Ausgaben liefert.

**Neben funktionalen Kriterien müssen deshalb auch die nicht-funktionalen Eigenschaften systematisch geprüft und validiert werden.** <a href="./Glossar.md#funktionaler-test" title="→ Glossar öffnen" class="glossary-term">**Funktionale Tests**</a> allein reichen nicht aus, um die Gesamtqualität und Anwenderakzeptanz eines Systems zu gewährleisten.

### Ergänzende Testarten

**Kritische nicht-funktionale Aspekte umfassen:**
* **<a href="./Glossar.md#gebrauchstauglichkeit" title="→ Glossar öffnen" class="glossary-term">**Gebrauchstauglichkeit**</a> und <a href="./Glossar.md#benutzererlebnis" title="→ Glossar öffnen" class="glossary-term">**Benutzererlebnis**</a>** - Wie intuitiv und angenehm ist die Systemnutzung?
* **<a href="./Glossar.md#performanz" title="→ Glossar öffnen" class="glossary-term">**Performance**</a> und Antwortzeiten** - Reagiert das System schnell genug?
* **<a href="./Glossar.md#skalierbarkeit" title="→ Glossar öffnen" class="glossary-term">**Skalierbarkeit**</a> und <a href="./Glossar.md#zuverlaessigkeit" title="→ Glossar öffnen" class="glossary-term">**Zuverlässigkeit**</a>** - Funktioniert das System auch unter Last?
* **<a href="./Glossar.md#sicherheit-security" title="→ Glossar öffnen" class="glossary-term">**Sicherheit**</a> und Datenschutz** - Sind sensible Daten angemessen geschützt?

*Beispiel aus "Pixel Leap":* Das Spiel könnte alle funktionalen Anforderungen erfüllen, aber trotzdem scheitern, wenn die Ladezeiten zwischen Levels zu lang sind oder die Steuerung nicht präzise genug reagiert.*

## Best Practices für funktionale Tests

### Systematische Testfall-Entwicklung

**Erfolgreiche funktionale Tests erfordern methodische Herangehensweise bei der <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a>-Entwicklung:**

#### Vollständige Anforderungsabdeckung
* **Systematische Durchsicht** aller funktionalen <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a>
* **Rückverfolgbarkeit** zwischen <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> und <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a>
* **Lückenidentifikation** bei unvollständig getesteten Funktionen

#### Realitätsnahe Testdaten
* **Repräsentative Eingabedaten** entsprechend produktivem Einsatz
* **Grenzwerte und Extremfälle** für Robustheitsprüfung
* **Ungültige Eingaben** für Fehlerbehandlungs-Validierung

#### Kombinatorische Testabdeckung
* **<a href="./Glossar.md#aequivalenzklassenbildung" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklassenbildung**</a>** für systematische Eingaberaumaufteilung
* **<a href="./Glossar.md#grenzwertanalyse" title="→ Glossar öffnen" class="glossary-term">**Grenzwertanalyse**</a>** für kritische Übergangsbereiche
* **Kombinationstests** für Interaktionen zwischen Funktionen

### Kontinuierliche Validierung

**Moderne Entwicklungsansätze integrieren funktionale Tests in kontinuierliche Validierungsprozesse:**
* **Automatisierte Testausführung** bei jeder Code-Änderung
* **Regressions-Validierung** zum Schutz bestehender Funktionalität
* **Frühzeitige Fehleridentifikation** durch <a href="./Glossar.md#shift-left" title="→ Glossar öffnen" class="glossary-term">**Shift-Left**</a>-Ansätze

## Fazit

**<a href="./Glossar.md#funktionaler-test" title="→ Glossar öffnen" class="glossary-term">**Funktionale Tests**</a> bilden das Rückgrat der Softwarevalidierung, indem sie systematisch prüfen, ob implementierte Systeme die spezifizierten Verhaltensanforderungen erfüllen.** Ihre methodische Durchführung auf allen <a href="./Glossar.md#teststufe" title="→ Glossar öffnen" class="glossary-term">**Teststufen**</a> gewährleistet, dass entwickelte Software nicht nur technisch funktioniert, sondern auch die beabsichtigten Geschäftsziele unterstützt.

**Die Erweiterung anforderungsbasierter Tests um geschäftsprozess-orientierte Szenarien erhöht die Realitätsnähe der Validierung erheblich.** Durch diese holistische Betrachtung werden nicht nur isolierte Funktionen, sondern auch deren Zusammenspiel in realistischen Anwendungskontexten geprüft.

**Gleichzeitig verdeutlichen die Grenzen funktionaler Tests die Notwendigkeit komplementärer Testarten.** Nur die systematische Kombination funktionaler und nicht-funktionaler <a href="./Glossar.md#testart" title="→ Glossar öffnen" class="glossary-term">**Testarten**</a> schafft ein vollständiges Qualitätsbild, das sowohl technische Korrektheit als auch Anwenderakzeptanz gewährleistet.

**Die kontinuierliche Weiterentwicklung von Testmethoden und -werkzeugen ermöglicht es, funktionale Tests immer effizienter und effektiver zu gestalten, ohne dabei an Gründlichkeit oder Aussagekraft zu verlieren.**