### Entscheidungstabellentest

Die bisher vorgestellten Verfahren betrachten mehrere Eingabeparameter eines <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekts**</a> unabhängig voneinander. Zur Erstellung der <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> wird jeder Eingabewert einzeln herangezogen. Abhängigkeiten zwischen den verschiedenen Eingabeparametern und deren Auswirkungen auf die Ausgaben gehen nicht explizit bei der Spezifikation der Testfälle ein. Der <a href="./Glossar.md#entscheidungstabellentest" title="→ Glossar öffnen" class="glossary-term">**Entscheidungstabellentest**</a> schließt diese Lücke.

---

#### Ursache-Wirkungs-Graph-Analyse

Ein verwandtes Verfahren, das Abhängigkeiten bei der Ermittlung der Testfälle berücksichtigt, ist die Ursache-Wirkungs-Graph-Analyse. Die logischen Beziehungen zwischen Ursachen und deren Wirkungen in einer <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponente**</a> oder einem System werden in einem sogenannten <a href="./Glossar.md#ursache-wirkungs-diagramm" title="→ Glossar öffnen" class="glossary-term">**Ursache-Wirkungs-Graphen**</a> dargestellt.

##### Grundprinzip

Voraussetzung ist, dass Ursachen und deren Wirkungen aus der Spezifikation ermittelt werden können. Jede Ursache wird als eine Eingabebedingung (Voraussetzung) beschrieben, die aus Eingabewerten oder Kombinationen von Eingabewerten besteht. Die Eingaben werden über logische Operatoren (etwa AND, OR und NOT) verknüpft. Die Eingabebedingung, und damit die Ursache, trifft zu oder nicht – sie kann also wahr oder falsch sein. Die Wirkungen werden analog behandelt und im Graphen vermerkt.

##### Beispiel: Rabattberechnung im Online-Shop

Um einen Rabatt in einem E-Commerce-System zu erhalten, sind folgende Bedingungen zu erfüllen:

* Der Kunde ist registriert
* Der Mindestbestellwert ist erreicht
* Es ist nicht bereits ein anderer Rabattcode aktiv
* Die Aktion ist zeitlich gültig

Als Aktion beziehungsweise Reaktion des Systems sind folgende Möglichkeiten gegeben:

* Rabatt ablehnen
* Hinweis auf fehlende Registrierung anzeigen
* Hinweis auf Mindestbestellwert anzeigen
* Hinweis auf bereits aktiven Rabatt anzeigen
* Rabatt anwenden

##### Vom Graphen zur Entscheidungstabelle

Der Graph ist in eine Entscheidungstabelle umzuformen, aus der dann die Testfälle abzulesen sind. Die einzelnen Schritte vom Graphen zur Tabelle sind:

1. Auswahl einer Wirkung
2. Durchsuchen des Graphen nach Kombinationen von Ursachen, die den Eintritt der Wirkung hervorrufen beziehungsweise nicht hervorrufen
3. Erzeugung jeweils einer Spalte der Entscheidungstabelle für alle gefundenen Ursachenkombinationen und die verursachten Zustände der übrigen Wirkungen
4. Überprüfung, ob Entscheidungstabelleneinträge mehrfach auftreten und gegebenenfalls Entfernen dieser Einträge

---

#### Direkte Erstellung von Entscheidungstabellen

Entscheidungstabellen können auch direkt – und nicht aus Ursache-Wirkungs-Graphen – erstellt werden. Die direkte Erstellung ist in der Praxis der übliche Weg. Um den Sachverhalt zu klären und Kombinationen zu verdeutlichen, können Entscheidungstabellen bereits bei der Spezifikation und nicht erst beim <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> eine wichtige Rolle spielen.

##### Ziel des Verfahrens

Der Test auf Basis von Entscheidungstabellen hat das Ziel, Testfälle zur Prüfung von interessanten Kombinationen von Eingaben zu erstellen. Interessant in dem Sinne, dass mögliche <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> aufgedeckt werden.

> Entscheidungstabellen eignen sich sehr gut zum Erfassen und zum Testen von komplexen Geschäftsregeln – einzuhaltende Bedingungen, die ein System korrekt umsetzen muss.

Verschiedene Kombinationen von Bedingungen führen in aller Regel zu unterschiedlichen Ergebnissen, die mit dem Entscheidungstabellentest systematisch geprüft werden.

##### Varianten

Im einfachsten Fall führt jede Kombination der Bedingungen zu einem Testfall. Aber Bedingungen können sich gegenseitig ausschließen oder beeinflussen, sodass nicht alle möglichen Kombinationen sinnvoll sind.

Alternativ können in Entscheidungstabellen mit erweiterter Eingabe einige oder alle Bedingungen und Aktionen auch mehrere Werte annehmen wie zum Beispiel Zahlenbereiche, <a href="./Glossar.md#aequivalenzklasse" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklassen**</a> oder auch Einzelwerte.

---

#### Struktur der Entscheidungstabelle

In der oberen Hälfte einer Entscheidungstabelle sind die Bedingungen (die Ursachen) aufgeführt, in der unteren die Wirkungen. Die Spalten im rechten Teil der Tabelle definieren die einzelnen Testsituationen – die Kombination von Bedingungen und die bei dieser Kombination erwarteten Aktionen beziehungsweise Ausgaben.

##### Die vier Bereiche

Eine Entscheidungstabelle ist in vier Bereiche unterteilt:

**Oben links**: Hier werden alle Bedingungen (die Ursachen) so aufgeführt, dass sie mit "ja" oder "nein" beantwortet werden können.

**Oben rechts**: In einem ersten Schritt werden hier alle Kombinationen der Bedingungen notiert (bei n Bedingungen sind es 2^n Kombinationen).

**Unten links**: Alle Aktionen (Ausgabe, Berechnung, …) sind hier erfasst.

**Unten rechts**: Hier wird vermerkt, bei welcher Kombination welche Aktion (Wirkung) erfolgen soll.

---

#### Erstellung der Tabelle

##### Schritt 1: Bedingungen ermitteln

Zu ermitteln sind alle Bedingungen, die eine Rolle bei dem Problem spielen. Jede Bedingung ist so zu formulieren, dass sie mit "ja" oder "nein" beantwortet werden kann. Jede Bedingung wird in jeweils eine Zeile (links oben) der Tabelle geschrieben.

##### Schritt 2: Aktionen ermitteln

Zu ermitteln sind alle möglichen Aktionen, die zu berücksichtigen sind. Jede Aktion wird jeweils in eine Zeile (links unten) der Tabelle notiert.

##### Schritt 3: Kombinationen erstellen

Zu erstellen sind alle Kombinationen der Bedingungen – ohne Berücksichtigung von möglichen Abhängigkeiten (oben rechts).

##### Schritt 4: Aktionen zuordnen

Alle Bedingungskombinationen (jede Spalte auf der rechten Seite der Tabelle) sind zu analysieren und es ist zu entscheiden, welche Aktion bei der jeweiligen Kombination zur Ausführung kommen soll. Ein Kreuz ist an die Stelle der Tabelle zu setzen, wo die Bedingungskombination zu einer Aktion führen soll. Es können also mehrere Kreuze bei einer Kombination vorkommen, wenn bei dieser Kombination mehrere Aktionen auszuführen sind.

Jede Bedingung soll in der Tabelle mindestens einmal den Wert "ja" und einmal den Wert "nein" erhalten.

---

#### Minimierung und Konsolidierung

Ist jede Kombination der Bedingungen in der Tabelle enthalten, dann liegt eine vollständige Entscheidungstabelle vor – sie hat so viele Spalten wie Kombinationen.

Die Tabelle kann konsolidiert beziehungsweise minimiert werden, indem:

* Spalten gelöscht werden, die unmögliche Kombinationen von Bedingungen enthalten
* Mögliche, aber nicht durchführbare Kombinationen von Bedingungen (in der Regel mit "N/A" gekennzeichnet) aus der Tabelle gestrichen werden
* Unterschiedliche Bedingungskombinationen, die zu gleichen Aktionen führen, zusammengefasst werden, wenn eine oder mehrere Bedingungen keinen Einfluss auf das Ergebnis haben

N/A steht für "not available" (nicht verfügbar), "not applicable" (nicht anwendbar, unzutreffend) oder "no answer" (keine Antwort).

Jede Spalte der Tabelle entspricht nun einem Testfall, wobei keine Kombinationen beziehungsweise Aktionen doppelt getestet werden. Ebenso kann geprüft werden, ob die Entscheidungstabelle vollständig, redundanzfrei und konsistent ist.

---

#### Beispiel: Versandkostenberechnung im Online-Shop

Eine zeitlich befristete Sonderaktion soll den Umsatz im Online-Shop erhöhen. Für Premium-Kunden ist der Versand immer kostenlos. Für Standardkunden ist der Versand ab einem Bestellwert von 50€ kostenlos. Bei einer Auswahl von Express-Versand durch Standardkunden wird eine Pauschale von 9,99€ berechnet. Für alle anderen Bestellungen gilt die reguläre Versandkostenpauschale von 4,99€.

##### Vollständige Entscheidungstabelle

Der obere Teil der Entscheidungstabelle mit allen Kombinationen sieht wie folgt aus:

| Entscheidungstabelle | TF1 | TF2 | TF3 | TF4 | TF5 | TF6 | TF7 | TF8 |
|----------------------|-----|-----|-----|-----|-----|-----|-----|-----|
| **Bedingungen** | | | | | | | | |
| Premium-Kunde? | ja | ja | ja | ja | nein | nein | nein | nein |
| Bestellwert ≥ 50€? | ja | ja | nein | nein | ja | ja | nein | nein |
| Express-Versand? | ja | nein | ja | nein | ja | nein | ja | nein |

##### Tabelle mit Aktionen und "don't care"

Da sich die Bedingungen teilweise ausschließen oder irrelevant sind, ist die Tabelle entsprechend zu überarbeiten ("–" ist als "don't care" zu interpretieren, da der Wert der Bedingung für das Ergebnis der Aktion irrelevant ist):

| Entscheidungstabelle | TF1 | TF2 | TF3 | TF4 | TF5 | TF6 | TF7 | TF8 |
|----------------------|-----|-----|-----|-----|-----|-----|-----|-----|
| **Bedingungen** | | | | | | | | |
| Premium-Kunde? | ja | ja | ja | ja | nein | nein | nein | nein |
| Bestellwert ≥ 50€? | – | – | – | – | ja | ja | nein | nein |
| Express-Versand? | – | – | – | – | ja | nein | ja | nein |
| **Aktionen** | | | | | | | | |
| Versand kostenlos | X | X | X | X | | X | | |
| Versand 4,99€ | | | | | | | | X |
| Versand 9,99€ | | | | | X | | X | |

##### Konsolidierte Entscheidungstabelle

Die Tabelle kann nun konsolidiert beziehungsweise minimiert werden: Die Testfälle 1–4 sind identisch und können ebenso wie die Testfälle 5 und 7 zusammengelegt werden. Damit ergibt sich folgende Entscheidungstabelle mit insgesamt 4 Testfällen, wobei jeder Testfall zu einer anderen Aktion führt:

| Entscheidungstabelle | TF1 | TF5 | TF6 | TF8 |
|----------------------|-----|-----|-----|-----|
| **Bedingungen** | | | | |
| Premium-Kunde? | ja | nein | nein | nein |
| Bestellwert ≥ 50€? | – | – | ja | nein |
| Express-Versand? | – | ja | nein | nein |
| **Aktionen** | | | | |
| Versand kostenlos | X | | X | |
| Versand 4,99€ | | | | X |
| Versand 9,99€ | | X | | |

---

#### Beispiel: Rabattanwendung im Online-Shop

Ein weiteres Beispiel zeigt die konsolidierte Entscheidungstabelle für die Rabattanwendung:

| Entscheidungstabelle | TF1 | TF2 | TF3 | TF4 | TF5 |
|----------------------|-----|-----|-----|-----|-----|
| **Bedingungen** | | | | | |
| Kunde registriert? | nein | ja | ja | ja | ja |
| Mindestbestellwert erreicht? | – | nein | nein | ja | ja |
| Dritter Versuch? | – | nein | ja | – | – |
| Rabattcode gültig? | – | – | – | nein | ja |
| **Aktionen** | | | | | |
| Hinweis Registrierung | X | | | | |
| Hinweis Mindestbestellwert | | X | | | |
| Rabattcode sperren | | | X | | |
| Hinweis ungültiger Code | | | | X | |
| Rabatt anwenden | | | | | X |

---

#### Komplexität beachten

Wie aus den Beispielen ersichtlich ist, entstehen bei mehr Bedingungen beziehungsweise Abhängigkeiten sehr schnell große umfangreiche Tabellen. Bei n Bedingungen gibt es theoretisch 2^n Kombinationen:

| Anzahl Bedingungen | Anzahl Kombinationen |
|--------------------|----------------------|
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |
| 6 | 64 |
| 10 | 1024 |

Die Minimierung und Konsolidierung der Tabelle ist daher ein wichtiger Schritt, um die Anzahl der Testfälle auf ein handhabbares Maß zu reduzieren.

---

#### Zusammenfassung

| Aspekt | Beschreibung |
|--------|--------------|
| Anwendungsbereich | Komplexe Geschäftsregeln mit Abhängigkeiten |
| Struktur | Bedingungen oben, Aktionen unten, Kombinationen in Spalten |
| Vollständige Tabelle | 2^n Kombinationen bei n Bedingungen |
| Minimierung | Entfernen unmöglicher und redundanter Kombinationen |
| Testfall | Eine Spalte der konsolidierten Tabelle |
| Stärke | Systematische Abdeckung aller relevanten Kombinationen |

Der Entscheidungstabellentest ist ein wirkungsvolles <a href="./Glossar.md#black-box-testverfahren" title="→ Glossar öffnen" class="glossary-term">**Blackbox-Testverfahren**</a> für Systeme mit komplexen Geschäftsregeln und Abhängigkeiten zwischen Eingabeparametern. Die Tabellen können bereits bei der Spezifikation eingesetzt werden, um Vollständigkeit und Konsistenz der <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> zu prüfen.