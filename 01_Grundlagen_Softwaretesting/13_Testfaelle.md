# Testentwurf

## Definition und Zielsetzung

**Beim <a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">**Testentwurf**</a> geht es darum, festzulegen, wie getestet wird.** Im Rahmen des <a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">**Testentwurfs**</a> werden aus den <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> bzw. Zusammenstellungen von <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> abgeleitet.

**Hierzu werden in aller Regel <a href="./Glossar.md#testverfahren" title="→ Glossar öffnen" class="glossary-term">**Testverfahren**</a> genutzt**, die systematische Ansätze zur Erstellung von <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> bereitstellen.

## Abstrakte und konkrete Testfälle

### Unterscheidung der Abstraktionsebenen

**Die Spezifikation der <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> kann dabei auf zwei »Ebenen« erfolgen: abstrakte und konkrete <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a>.**

### Abstrakte Testfälle

**Ein abstrakter <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> enthält keine konkreten Ein- oder Ausgabewerte** für die Eingaben und <a href="./Glossar.md#erwartetes-ergebnis" title="→ Glossar öffnen" class="glossary-term">**erwarteten Ergebnisse**</a>, es werden logische Operatoren zur Beschreibung verwendet.

**Vorteile abstrakter <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a>:**
* Über mehrere <a href="./Glossar.md#testzyklus" title="→ Glossar öffnen" class="glossary-term">**Testzyklen**</a> mit unterschiedlichen konkreten Daten verwendbar
* Dokumentieren adäquat den Umfang des jeweiligen <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfalls**</a>
* Wiederverwendbar und wartungsfreundlich

### Konkrete Testfälle

**Ein konkreter <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> beinhaltet konkrete Werte** für die Eingaben und die vorausgesagten Ergebnisse.

**Da nur konkrete <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> auf dem Rechner zur Ausführung gebracht werden können**, sind die abstrakten <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> zu konkretisieren, d.h., die tatsächlichen Werte für Ein- und Ausgaben müssen festgelegt werden.

### Praktisches Beispiel: Rabattberechnung in "Pixel Leap"

*Stellen wir uns vor, "Pixel Leap" hat ein In-Game-Shop-System mit automatischen Rabatten basierend auf dem Kaufbetrag:*

**Rabattregeln:**
* Kaufpreis < 15,00 € → Rabatt = 0%
* 15,00 € ≤ Kaufpreis ≤ 20,00 € → Rabatt = 5%
* 20,00 € < Kaufpreis < 25,00 € → Rabatt = 7%
* Kaufpreis ≥ 25,00 € → Rabatt = 8,5%

**Abstrakte <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">Testfälle</a>:**

| Abstrakter Testfall | 1 | 2 | 3 | 4 |
|---------------------|---|---|---|---|
| **Eingabewert x (Kaufpreis in €)** | x < 15000 | 15000 ≤ x ≤ 20000 | 20000 < x < 25000 | x ≥ 25000 |
| **Vorausgesagtes Ergebnis (Rabatt in %)** | 0 | 5 | 7 | 8,5 |

**Konkrete <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">Testfälle</a>:**

| Konkreter Testfall | 1 | 2 | 3 | 4 |
|---------------------|---|---|---|---|
| **Eingabewert x (Kaufpreis in €)** | 14500 | 16500 | 24750 | 31800 |
| **Vorausgesagtes Ergebnis (Rabatt in €)** | 0 | 825 | 1732,50 | 2703 |

## Vollständige Testfallspezifikation

### Umfassende Beschreibung erforderlich

**<a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">Testfälle</a> umfassen mehr als nur die <a href="./Glossar.md#testdaten" title="→ Glossar öffnen" class="glossary-term">**Testdaten**</a>.** Für jeden <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> muss Folgendes beschrieben werden:

### Vorbedingungen definieren

**Die Ausgangssituation (<a href="./Glossar.md#vorbedingung" title="→ Glossar öffnen" class="glossary-term">**Vorbedingung**</a>) muss klar beschrieben werden:**
* Welche Randbedingungen für den <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> gelten
* Welche Systemzustände vor der Testausführung einzuhalten sind
* Welche Daten bereits vorhanden sein müssen

### Erwartete Ergebnisse festlegen

**Vor der <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> ist festzulegen, welche Ergebnisse bzw. welches Verhalten erwartet wird:**

* **Ausgaben:** Direkte Systemausgaben
* **Datenänderungen:** Änderungen an globalen (persistenten) Daten
* **Zustandsänderungen:** Modifikationen des Systemzustands
* **Weitere Veränderungen:** Alle sonstigen Reaktionen auf die Testdurchführung

### Anforderungen an Testdaten

**Demzufolge sind Anforderungen an die <a href="./Glossar.md#testdaten" title="→ Glossar öffnen" class="glossary-term">**Testdaten**</a> beim <a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">**Testentwurf**</a> festzulegen.**

## Testorakel

### Bestimmung der erwarteten Ergebnisse

**Um die vorauszusagenden und <a href="./Glossar.md#erwartetes-ergebnis" title="→ Glossar öffnen" class="glossary-term">**erwarteten Ergebnisse**</a> zu bestimmen, sind adäquate Informationsquellen zu verwenden. Dabei gibt es zwei grundlegende Möglichkeiten:**

### Ableitung aus der Testbasis

**Der Sollwert wird aus dem Eingabewert auf Grundlage der <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> (Anforderungsdefinition, Spezifikation usw.) des <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekts**</a> abgeleitet.**

### Inverse Funktionen nutzen

**Gibt es für eine Funktion die entsprechende »Umkehr-« oder inverse Funktion, so kann diese nach dem <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> ausgeführt und die Ausgabe mit der ursprünglichen Eingabe des <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfalls**</a> verglichen werden.**

*Ein Beispiel sind die Verschlüsselung und Entschlüsselung von Daten in "Pixel Leap" für sichere Spielstand-Übertragungen.*

## Weitere Aufgaben beim Testentwurf

### Priorisierung und Verfolgbarkeit

**Neben der Spezifikation von <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> gehören die <a href="./Glossar.md#prioritaet" title="→ Glossar öffnen" class="glossary-term">**Priorisierung**</a> der <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> und die Bereitstellung der Testinfrastruktur zu den Aufgaben beim <a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">**Testentwurf**</a>:**

**Bei der <a href="./Glossar.md#testanalyse" title="→ Glossar öffnen" class="glossary-term">**Testanalyse**</a> wurden bereits die <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> priorisiert.** Diese <a href="./Glossar.md#prioritaet" title="→ Glossar öffnen" class="glossary-term">**Priorisierung**</a> wird für die entworfenen <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> übernommen und kann weiter verfeinert werden.

**So können bei einem Satz von <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a>, der eine <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingung**</a> prüft, für einzelne <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> unterschiedliche <a href="./Glossar.md#prioritaet" title="→ Glossar öffnen" class="glossary-term">**Prioritäten**</a> vergeben werden** (<a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> mit hoher <a href="./Glossar.md#prioritaet" title="→ Glossar öffnen" class="glossary-term">**Priorität**</a> werden zuerst ausgeführt).

**Gleiches gilt für die <a href="./Glossar.md#verfolgbarkeit" title="→ Glossar öffnen" class="glossary-term">**Verfolgbarkeit**</a> der <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a>**, diese kann nun auf die <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> bzw. Sätze von <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> heruntergebrochen werden.

## Testinfrastruktur und Testumgebung

### Bereitstellung der Infrastruktur

**Die Testinfrastruktur ist zu ermitteln und bereitzustellen.** Zur Testinfrastruktur gehören alle organisatorischen Elemente, die für die <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> notwendig sind:

* **<a href="./Glossar.md#testumgebung" title="→ Glossar öffnen" class="glossary-term">Testumgebung</a>** und erforderliche Testwerkzeuge
* Entsprechend ausgestattete Arbeitsplätze
* Hardware- und Softwareressourcen

### Testumgebung definieren

**Eine <a href="./Glossar.md#testumgebung" title="→ Glossar öffnen" class="glossary-term">**Testumgebung**</a> wird benötigt, um das <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> unter Benutzung der spezifizierten <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> auf dem Rechner ausführen zu können.**

**Sie umfasst:**
* Erforderliche Hardware
* Gegebenenfalls benötigte <a href="./Glossar.md#simulator" title="→ Glossar öffnen" class="glossary-term">**Simulatoren**</a>
* Softwarewerkzeuge sowie weitere unterstützende Hilfsmittel

**Damit es bei der Durchführung der <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> nicht zu zeitlichen Verzögerungen kommt**, soll die Testinfrastruktur bereits zu diesem Zeitpunkt so weit wie möglich aufgebaut, integriert und geprüft sein.

## Überdeckungselemente

### Definition der Abdeckungskriterien

**Um Kriterien festzulegen, wann ausreichend getestet ist, werden im Rahmen des <a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">**Testentwurfs**</a> <a href="./Glossar.md#überdeckungselement" title="→ Glossar öffnen" class="glossary-term">**Überdeckungselemente**</a> bestimmt.**

> Ein <a href="./Glossar.md#überdeckungselement" title="→ Glossar öffnen" class="glossary-term">**Überdeckungselement**</a> ist eine Eigenschaft oder eine Kombination von Eigenschaften, die aus einer oder mehreren <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> unter Verwendung eines <a href="./Glossar.md#testverfahren" title="→ Glossar öffnen" class="glossary-term">**Testverfahrens**</a> abgeleitet wird.

### Beispiele für Überdeckungselemente

**Bei verschiedenen <a href="./Glossar.md#testverfahren" title="→ Glossar öffnen" class="glossary-term">**Testverfahren**</a> ergeben sich unterschiedliche <a href="./Glossar.md#überdeckungselement" title="→ Glossar öffnen" class="glossary-term">**Überdeckungselemente**</a>:**

* **<a href="./Glossar.md#äquivalenzklassenbildung" title="→ Glossar öffnen" class="glossary-term">Äquivalenzklassenbildung</a>:** Die <a href="./Glossar.md#äquivalenzklasse" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklassen**</a> sind die <a href="./Glossar.md#überdeckungselement" title="→ Glossar öffnen" class="glossary-term">**Überdeckungselemente**</a>
* **<a href="./Glossar.md#entscheidungstabellentest" title="→ Glossar öffnen" class="glossary-term">Entscheidungstabellentest</a>:** Die Spalten mit ausführbaren Kombinationen von Bedingungen sind die <a href="./Glossar.md#überdeckungselement" title="→ Glossar öffnen" class="glossary-term">**Überdeckungselemente**</a>

## Qualitätssicherung im Testentwurf

### Identifikation von Fehlern

**Wie bei der <a href="./Glossar.md#testanalyse" title="→ Glossar öffnen" class="glossary-term">**Testanalyse**</a> kann auch beim <a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">**Testentwurf**</a> der nützliche Seiteneffekt – die Identifikation von Fehlern in der <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> – eintreten.**

### Verfeinerung der Testbedingungen

**Ebenso können <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a>, die in der <a href="./Glossar.md#testanalyse" title="→ Glossar öffnen" class="glossary-term">**Testanalyse**</a> definiert wurden, im <a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">**Testentwurf**</a> detaillierter spezifiziert werden.**

## Fazit

**Der <a href="./Glossar.md#testentwurf" title="→ Glossar öffnen" class="glossary-term">**Testentwurf**</a> transformiert das "Was" der <a href="./Glossar.md#testanalyse" title="→ Glossar öffnen" class="glossary-term">**Testanalyse**</a> in das "Wie" des <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testens**</a>.** Durch die systematische Ableitung von <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> aus <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a> entstehen ausführbare und nachvollziehbare Testspezifikationen.

**Die Unterscheidung zwischen abstrakten und konkreten <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> ermöglicht sowohl Wiederverwendbarkeit als auch praktische Ausführbarkeit.** Die vollständige Spezifikation aller <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a>-Aspekte gewährleistet reproduzierbare und aussagekräftige <a href="./Glossar.md#testergebnis" title="→ Glossar öffnen" class="glossary-term">**Testergebnisse**</a>.

**Die frühzeitige Bereitstellung der Testinfrastruktur und die Definition klarer <a href="./Glossar.md#überdeckungselement" title="→ Glossar öffnen" class="glossary-term">**Überdeckungselemente**</a> schaffen die Voraussetzungen für eine effiziente <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a>.**