### Dynamischer Test

Software lässt sich auf zwei grundlegend verschiedene Arten prüfen: Entweder man analysiert den Code, ohne ihn auszuführen, oder man bringt das Programm tatsächlich zum Laufen und beobachtet sein Verhalten. Letzteres bezeichnet man als <a href="./Glossar.md#dynamischer-test" title="→ Glossar öffnen" class="glossary-term">**dynamischen Test**</a>. Diese Prüfmethode steht im Zentrum vieler Qualitätssicherungsmaßnahmen, denn erst die tatsächliche Ausführung offenbart, wie sich ein <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> unter realen Bedingungen verhält.

Wer <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> systematisch herleiten möchte, kann auf unterschiedliche Methoden zurückgreifen. Diese gliedern sich in drei Hauptkategorien: <a href="./Glossar.md#black-box-testverfahren" title="→ Glossar öffnen" class="glossary-term">**Blackbox-Verfahren**</a>, <a href="./Glossar.md#white-box-testverfahren" title="→ Glossar öffnen" class="glossary-term">**Whitebox-Verfahren**</a> und <a href="./Glossar.md#erfahrungsbasiertes-testverfahren" title="→ Glossar öffnen" class="glossary-term">**erfahrungsbasierte Verfahren**</a>.

---

#### Wozu dienen Testverfahren?

Während der <a href="./Glossar.md#testanalyse" title="→ Glossar öffnen" class="glossary-term">**Testanalyse**</a> und des <a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">**Testentwurfs**</a> greifen <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Tester**</a> auf etablierte <a href="./Glossar.md#testverfahren" title="→ Glossar öffnen" class="glossary-term">**Testverfahren**</a> zurück. Diese Methoden leisten dreierlei: Sie helfen dabei, <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> zu analysieren, passende <a href="./Glossar.md#ueberdeckungselement" title="→ Glossar öffnen" class="glossary-term">**Überdeckungselemente**</a> auszuwählen und geeignete <a href="./Glossar.md#testdaten" title="→ Glossar öffnen" class="glossary-term">**Testdaten**</a> zu identifizieren.

Ein wesentlicher Vorteil dieser Methoden liegt in ihrer Fähigkeit, die Testfallmenge sinnvoll einzugrenzen. Statt wahllos Eingaben auszuprobieren, entsteht eine überschaubare Anzahl gezielter Prüfungen. Ob diese Menge ausreicht, lässt sich anhand der <a href="./Glossar.md#ueberdeckung" title="→ Glossar öffnen" class="glossary-term">**Überdeckung**</a> beurteilen – also dem Anteil der geprüften Elemente an der Gesamtmenge.

---

#### Voraussetzungen für die Testausführung

##### Programme müssen lauffähig sein

Damit ein dynamischer Test stattfinden kann, braucht es ein ausführbares Programm. Bei frühen <a href="./Glossar.md#teststufe" title="→ Glossar öffnen" class="glossary-term">**Teststufen**</a> wie dem <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententest**</a> oder <a href="./Glossar.md#integrationstest" title="→ Glossar öffnen" class="glossary-term">**Integrationstest**</a> existiert oft noch kein vollständiges System. Das Testobjekt muss dann in einen <a href="./Glossar.md#testrahmen" title="→ Glossar öffnen" class="glossary-term">**Testrahmen**</a> eingebettet werden.

*Beispiel: Die Sprungphysik-Komponente von Pixel Leap soll geprüft werden, obwohl das Gesamtspiel noch nicht spielbar ist. Ein Testrahmen kapselt die Komponente und ermöglicht isolierte Prüfungen der Berechnungen.*

##### Simulation fehlender Programmteile

Häufig ruft das Testobjekt andere Module auf, die noch nicht fertiggestellt sind. <a href="./Glossar.md#platzhalter" title="→ Glossar öffnen" class="glossary-term">**Platzhalter**</a> – auch Stubs oder Mock-Objekte genannt – übernehmen dann deren Rolle. Sie liefern vordefinierte Antworten und simulieren so das erwartete Verhalten.

*Beispiel: Pixel Leap benötigt für die Highscore-Anzeige Daten vom Online-Backend. Da dieses noch in Entwicklung ist, liefert ein Platzhalter feste Punktestände. So lässt sich die Anzeigelogik unabhängig testen.*

Umgekehrt muss auch der Aufrufer des Testobjekts simuliert werden. Ein <a href="./Glossar.md#treiber" title="→ Glossar öffnen" class="glossary-term">**Treiber**</a> übernimmt diese Aufgabe und versorgt das Testobjekt mit Eingaben. Gemeinsam bilden Treiber und Platzhalter den Testrahmen.

Solche Rahmen entstehen entweder durch manuelle Entwicklung, durch Anpassung generischer Vorlagen oder mithilfe von Generatoren. Erst wenn alles zusammengesetzt ist, kann die eigentliche Prüfung beginnen.

---

#### Warum systematisches Vorgehen entscheidend ist

Das <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> verfolgt zwei Ziele: Einerseits soll nachgewiesen werden, dass die Software ihre <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> erfüllt. Andererseits sollen <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> aufgedeckt werden. Beides soll mit vertretbarem Aufwand gelingen.

Wer ohne Methode testet – quasi nach Gefühl –, riskiert Lücken. Wichtige Szenarien bleiben ungeprüft, während andere mehrfach durchlaufen werden. Systematik schafft hier Abhilfe.

##### Drei Schritte zum Test

Die Durchführung gliedert sich in drei Phasen:

* Zunächst werden Rahmenbedingungen geklärt und Ziele definiert
* Dann erfolgt die Spezifikation einzelner Testfälle
* Schließlich wird die <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testausführung**</a> geplant – typischerweise als Abfolge mehrerer Testfälle

Wie formal dieses Vorgehen ausfällt, hängt von verschiedenen Faktoren ab: Handelt es sich um sicherheitskritische Software? Wie ausgereift sind die Entwicklungsprozesse? Welche Zeitvorgaben existieren? Wie erfahren ist das Team?

---

#### Ziele und Voraussetzungen klären

Ausgangspunkt ist die <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a>. Sie liefert die Grundlage für alle weiteren Überlegungen. Was genau soll geprüft werden? Welche <a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">**Testziele**</a> werden verfolgt?

*Beispiel: Für Pixel Leap lautet eine Testbedingung: "Bei Tastendruck muss die Spielfigur innerhalb von 50 Millisekunden eine Aufwärtsbewegung starten."*

Besondere Aufmerksamkeit verdienen Szenarien mit hohem <a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">**Risiko**</a>. Außerdem müssen Voraussetzungen geklärt werden – etwa welche Datenbestände benötigt werden.

##### Der Wert der Verfolgbarkeit

<a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> bezeichnet die explizite Verknüpfung zwischen Anforderungen und den zugehörigen Testfällen. Diese Verbindung ermöglicht eine <a href="./Glossar.md#auswirkungsanalyse" title="→ Glossar öffnen" class="glossary-term">**Auswirkungsanalyse**</a>: Ändert sich eine Anforderung, lässt sich sofort erkennen, welche Testfälle betroffen sind.

Darüber hinaus erlaubt die Verfolgbarkeit eine Messung der Abdeckung. Ein <a href="./Glossar.md#ueberdeckungskriterien" title="→ Glossar öffnen" class="glossary-term">**Überdeckungskriterium**</a> – etwa "jede Anforderung mindestens einmal prüfen" – definiert, wann der Test beendet werden kann.

In der Praxis wächst die Testfallzahl schnell auf Hunderte oder Tausende an. Ohne dokumentierte Verfolgbarkeit wäre es unmöglich, bei Änderungen die relevanten Testfälle zu identifizieren.

---

#### Was gehört zur Testfallspezifikation?

Ein vollständiger Testfall umfasst mehr als nur Eingabewerte. Er definiert auch die <a href="./Glossar.md#vorbedingung" title="→ Glossar öffnen" class="glossary-term">**Vorbedingungen**</a>, das <a href="./Glossar.md#erwartetes-ergebnis" title="→ Glossar öffnen" class="glossary-term">**erwartete Ergebnis**</a> und die <a href="./Glossar.md#nachbedingung" title="→ Glossar öffnen" class="glossary-term">**Nachbedingungen**</a>.

> Entscheidend ist: Das Soll-Ergebnis muss feststehen, bevor der Test läuft. Andernfalls besteht die Gefahr, fehlerhafte Ausgaben fälschlich als korrekt zu akzeptieren.

*Beispiel: Ein Sprungtest für Pixel Leap spezifiziert als Vorbedingung, dass die Figur auf festem Boden steht. Die Eingabe ist der Tastendruck. Erwartet wird eine Aufwärtsbewegung mit definierter Höhe. Als Nachbedingung gilt die Landung auf einer Plattform.*

---

#### Organisation der Testausführung

Einzelne Testfälle nacheinander auszuführen ist ineffizient. Stattdessen fasst man sie zu <a href="./Glossar.md#testsuite" title="→ Glossar öffnen" class="glossary-term">**Testsuiten**</a> zusammen – auch Testsequenzen oder Testszenarien genannt.

Der <a href="./Glossar.md#testausfuehrungsplan" title="→ Glossar öffnen" class="glossary-term">**Testausführungsplan**</a> dokumentiert diese Zusammenstellung. Er gruppiert Testfälle nach Themen oder Zielen, vermerkt <a href="./Glossar.md#prioritaet" title="→ Glossar öffnen" class="glossary-term">**Prioritäten**</a> und Abhängigkeiten und kennzeichnet <a href="./Glossar.md#regressionstest" title="→ Glossar öffnen" class="glossary-term">**Regressionstests**</a>. Auch die zeitliche Planung – wer testet wann was – gehört dazu.

##### Automatisierung durch Testskripte

Für die automatisierte Ausführung dienen <a href="./Glossar.md#testskript" title="→ Glossar öffnen" class="glossary-term">**Testskripte**</a>. Sie enthalten Anweisungen in einer Programmiersprache oder vergleichbaren Notation. Neben der reinen Ausführung können Skripte auch Vorbedingungen herstellen und das <a href="./Glossar.md#istergebnis" title="→ Glossar öffnen" class="glossary-term">**Istergebnis**</a> mit dem Soll vergleichen.

*Beispiel: Für Pixel Leap könnten Testskripte mit NUnit (C#/Unity) verschiedene Sprungszenarien automatisch durchspielen und die Ergebnisse protokollieren.*

---

#### Die drei Kategorien der Testverfahren

Zur methodischen Testfallermittlung existieren zahlreiche Verfahren. Sie lassen sich drei Kategorien zuordnen – wobei manche Verfahren Elemente mehrerer Kategorien vereinen und dann als Greybox-Verfahren gelten.

##### Blackbox-Verfahren

Diese Methoden betrachten das Testobjekt von außen. Der interne Aufbau spielt keine Rolle – man interessiert sich nur für Ein- und Ausgaben. Daher heißen sie auch spezifikationsbasierte Verfahren.

Der Beobachtungspunkt (Point of Observation) und der Steuerungspunkt (Point of Control) liegen beide außerhalb des Testobjekts. Die Testfälle bleiben gültig, solange sich das geforderte Verhalten nicht ändert – unabhängig von Implementierungsdetails.

Als Grundlage dienen Spezifikationen, Anforderungsbeschreibungen, Anwendungsfälle oder <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a>. Auch formale Modelle eignen sich zur systematischen Ableitung.

*Beispiel: Eine User Story für Pixel Leap lautet: "Als Spieler möchte ich durch Tastendruck springen, um Hindernisse zu überwinden." Daraus lassen sich verschiedene Testfälle ableiten – einfacher Sprung, Sprung von einer Kante, Sprung während der Bewegung.*

Ein zusätzlicher Nutzen: Die systematische Analyse deckt oft Lücken zwischen Anforderungen und Implementierung auf. Als Minimalkriterium gilt: Jede Anforderung sollte mindestens ein Testfall prüfen.

##### Whitebox-Verfahren

Im Gegensatz dazu blicken <a href="./Glossar.md#white-box-testverfahren" title="→ Glossar öffnen" class="glossary-term">**Whitebox-Verfahren**</a> ins Innere. Sie orientieren sich an der Programmstruktur und werden daher auch strukturbasierte Verfahren genannt.

Hier kann der Beobachtungspunkt innerhalb des Testobjekts liegen. In Ausnahmefällen – wenn bestimmte Situationen von außen nicht provozierbar sind – greift man auch steuernd ein.

Die Testbasis umfasst neben den Anforderungen auch Informationen über Architektur, Feinentwurf oder Quellcode. Daher können diese Tests erst nach der Implementierung entstehen. Typisches Ziel ist ein bestimmter Überdeckungsgrad.

*Beispiel: Für die Kollisionserkennung in Pixel Leap soll eine <a href="./Glossar.md#anweisungsueberdeckung" title="→ Glossar öffnen" class="glossary-term">**Anweisungsüberdeckung**</a> von 80% erreicht werden. Nicht ausgeführte Codepfade werden identifiziert und gezielt durch zusätzliche Testfälle angesteuert.*

Diese Verfahren eignen sich primär für untere Teststufen. Ein <a href="./Glossar.md#systemtest" title="→ Glossar öffnen" class="glossary-term">**Systemtest**</a> am Quellcode orientiert ist selten sinnvoll.

##### Erfahrungsbasierte Verfahren

Die dritte Kategorie nutzt das Wissen von Beteiligten – Testern, Entwicklern, Anwendern. Grundlage sind Erfahrungen mit ähnlichen Systemen, Kenntnisse über typische Fehlerquellen und Intuition.

*Beispiel: Ein erfahrener Tester weiß, dass Plattformspiele oft Probleme bei gleichzeitiger Eingabe von Sprung und Richtungswechsel zeigen. Er erstellt entsprechende Testfälle, obwohl die Spezifikation diese Kombination nicht erwähnt.*

Ein Nachteil: Meist lässt sich kein Überdeckungsgrad messen. Daher fehlt ein objektives Abbruchkriterium. Deshalb kombiniert man diese Verfahren typischerweise mit Blackbox- oder Whitebox-Methoden. Ihr Wert liegt darin, <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> zu finden, die andere Verfahren übersehen.

---

#### Wo welches Verfahren passt

| Kategorie | Blickrichtung | Beobachtungspunkt | Steuerungspunkt | Geeignete Teststufen |
|-----------|---------------|-------------------|-----------------|----------------------|
| Blackbox | Ein-/Ausgaben | Außen | Außen | Alle |
| Whitebox | Struktur | Innen | Kann innen liegen | Komponenten-, Integrationstest |
| Erfahrungsbasiert | Wissen | Variabel | Variabel | Alle |

Blackbox-Verfahren decken alle Teststufen ab und sind Pflicht bei Test-First-Ansätzen wie der <a href="./Glossar.md#testgetriebene-entwicklung" title="→ Glossar öffnen" class="glossary-term">**testgetriebenen Entwicklung**</a>. Whitebox-Verfahren entfalten ihre Stärke bei Komponenten- und Integrationstests. Erfahrungsbasierte Verfahren ergänzen beide als wertvolle Zusatzperspektive.

Die Wahl hängt von mehreren Faktoren ab: verfügbare Testbasis, aktuelle Teststufe, definierte Testziele sowie Erfahrung des Teams. In der Praxis liefert oft die Kombination verschiedener Methoden die besten Ergebnisse.