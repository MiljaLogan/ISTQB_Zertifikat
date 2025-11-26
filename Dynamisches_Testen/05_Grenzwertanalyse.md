### Grenzwertanalyse

Die <a href="./Glossar.md#grenzwertanalyse" title="→ Glossar öffnen" class="glossary-term">**Grenzwertanalyse**</a> liefert eine sehr sinnvolle Ergänzung zu den <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a>, die durch die <a href="./Glossar.md#aequivalenzklassenbildung" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklassenbildung**</a> ermittelt werden. <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> in Programmen treten häufig an den Grenzbereichen der <a href="./Glossar.md#aequivalenzklasse" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklassen**</a> auf, da hier Fallunterscheidungen in den Programmen erforderlich sind, die fehlerträchtig sein können. Ein Test mit <a href="./Glossar.md#grenzwert" title="→ Glossar öffnen" class="glossary-term">**Grenzwerten**</a> deckt daher oft <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> auf.

---

#### Grundprinzip

Der Minimum- und der Maximumwert einer Äquivalenzklasse sind die beiden Ränder beziehungsweise Grenzwerte dieser Klasse. Alle Werte, die zwischen dem Minimum- und dem Maximumwert der Äquivalenzklasse liegen, gehören zu dieser Äquivalenzklasse.

##### Anwendungsvoraussetzungen

Das Verfahren lässt sich nur anwenden, wenn folgende Bedingungen erfüllt sind:

* Die Menge der Daten, die in eine Äquivalenzklasse fallen, ist geordnet – das heißt, sie besteht aus numerischen Daten oder es kann eine zumindest partielle Ordnung über den Daten definiert werden
* Es lassen sich tatsächliche Grenzwerte identifizieren – es muss also ein Minimum- und ein Maximumwert bestimmbar sein

##### Vorgehensweise

Bei der Grenzwertanalyse werden die beiden Grenzwerte der Äquivalenzklassen einer Überprüfung unterzogen. An jedem Rand wird der exakte Grenzwert (Minimum- oder Maximumwert der Äquivalenzklasse) und ein beziehungsweise zwei direkt benachbarte Werte zur Erstellung von Testfällen herangezogen.

Für Gleitkommazahlen ist eine entsprechende Toleranz der Rechengenauigkeit zu wählen. Dabei ist das kleinste mögliche Inkrement zu verwenden, um die Grenzen einem genauen Test zu unterziehen.

Für jeden Grenzwert ergeben sich somit zwei beziehungsweise drei Testfälle. Bei benachbarten Äquivalenzklassen ist der nächstgrößere Wert des Maximumwerts einer Äquivalenzklasse der Minimumwert der benachbarten Äquivalenzklasse.

---

#### 2-Wert-Grenzwertanalyse

Bei der 2-Wert-Grenzwertanalyse sind für jeden Grenzwert (Minimum- beziehungsweise Maximumwert der Äquivalenzklasse) zwei <a href="./Glossar.md#ueberdeckungselement" title="→ Glossar öffnen" class="glossary-term">**Überdeckungselemente**</a> zu berücksichtigen:

* Der Grenzwert selbst innerhalb der Äquivalenzklasse
* Der engste Nachbar, der zur angrenzenden Äquivalenzklasse gehört

*Beispiel: Im E-Commerce-System wird der Kundenrabatt auf maximal 50% begrenzt. Aus der Spezifikation ergeben sich die Äquivalenzklassen gÄK: [0, …, 50] und uÄK: ]50, …, MAX_FLOAT]. Als Testdaten zur Überprüfung der Grenzwerte dieser beiden benachbarten Äquivalenzklassen werden die Werte 50 und 50.01 gewählt. Der Wert 50 liegt in der gültigen Äquivalenzklasse und ist dort der größtmögliche Wert (Maximumwert). Der Wert 50.01 liegt in der ungültigen Äquivalenzklasse und ist dort der kleinstmögliche Wert (Minimumwert). Die Werte 49.99 und 50.02 bringen scheinbar keinen weiteren Erkenntnisgewinn, da sie sich weiter innerhalb der jeweiligen Äquivalenzklassen befinden.*

---

#### 3-Wert-Grenzwertanalyse

Bei der 3-Wert-Grenzwertanalyse sind für jeden Grenzwert drei Überdeckungselemente vorgesehen:

* Der Grenzwert selbst
* Seine beiden benachbarten Werte

Zwei dieser drei Überdeckungselemente fallen dabei in eine Äquivalenzklasse. Die 3-Wert-Grenzwertanalyse ist daher strenger – ein zusätzlicher Wert und somit ein zusätzlicher Testfall – als die 2-Wert-Grenzwertanalyse.

---

#### Wann welche Grenzwertanalyse einsetzen?

Die Entscheidung zwischen 2-Wert- und 3-Wert-Grenzwertanalyse hängt davon ab, welche Arten von fehlerhaften Implementierungen aufgedeckt werden sollen.

##### Analyse anhand der Implementierung

*Beispiel: Es wird davon ausgegangen, dass es im Programmcode an entsprechender Stelle eine Abfrage der Form `if (discount > 50)` gibt. Durch welche <a href="./Glossar.md#testdaten" title="→ Glossar öffnen" class="glossary-term">**Testdaten**</a> kann nun eine fehlerhafte Implementierung dieser Bedingung aufgedeckt werden?*

Mit den Testdaten 49.99, 50 und 50.01 werden die Wahrheitswerte false, false und true durch die Abfrage ermittelt, und die entsprechenden Programmpfade kommen zur Ausführung.

| Implementierte Abfrage | 49.99 | 50 | 50.01 | Anmerkung |
|------------------------|-------|-----|-------|-----------|
| `discount > 50` (korrekt) | false | false | true | Erwartete Auswertung |
| `discount >= 50` | false | true | true | 50 ist fehleraufdeckend |
| `discount != 50` | true | false | true | 49.99 ist fehleraufdeckend |
| `discount < 50` | true | false | false | 49.99 und 50.01 sind fehleraufdeckend |
| `discount <= 50` | true | true | false | Alle drei Werte sind fehleraufdeckend |
| `discount == 50` | false | true | false | 49.99 und 50 sind fehleraufdeckend |

##### Empfehlungen

Das Testdatum 50.01 scheint auf den ersten Blick keinen zusätzlichen Nutzen zu bringen, da der Wert 50 bereits den Wert false liefert und damit den Wechsel zur benachbarten Äquivalenzklasse anzeigt. Eine fehlerhafte Realisierung der Abfrage mit `if (discount >= 50)` führt zu den Wahrheitswerten false, true und true. Auch hier kann auf den Test mit 50.01 eigentlich verzichtet werden, da der Wert 50 zu einem falschen Ergebnis (true statt false) führt und den Fehlerzustand aufdeckt.

Erst bei einer grob fehlerhaften Umsetzung der Abfrage mit `if (discount != 50)` und den Wahrheitswerten true, false und true wird deutlich, dass nur dieser Test mit dem Wert 49.99 die fehlerhafte Realisierung aufdeckt.

> Es ist zu entscheiden, wann der Test mit zwei Testwerten als ausreichend angesehen wird und wann es Sinn macht, die 3-Wert-Grenzwertanalyse einzusetzen. Die falsche Abfrage im Programmtext kann bei der Durchführung eines Codereviews erkannt werden, da nicht wie gefordert eine Bereichsgrenze, sondern auf Ungleichheit des Wertes abgefragt wird. Allerdings kann dieser Fehlerzustand bei einem Codereview auch leicht übersehen werden. Nur mit einem Grenzwerttest mit drei Werten werden solche fehlerhaften Implementierungen erkannt.

---

#### Praktische Hinweise zur Grenzwertanalyse

##### 2-Wert-Grenzwertanalyse bei benachbarten Klassen

Für die 2-Wert-Grenzwertanalyse bei zwei benachbarten Äquivalenzklassen ist der Grenzwert innerhalb einer Klasse und der benachbarte außerhalb dieser Klasse zu wählen. Der benachbarte Wert ist zugleich der Grenzwert der Nachbarklasse.

Damit ist es gleichgültig, von welcher der beiden Äquivalenzklassen aus die beiden Werte zur Prüfung der Grenze ermittelt werden. Es sind die gleichen Werte, die zur Erstellung von zwei Testfällen heranzuziehen sind.

##### 3-Wert-Grenzwertanalyse bei benachbarten Klassen

Für die 3-Wert-Grenzwertanalyse bei zwei benachbarten Äquivalenzklassen ist ein weiterer Wert erforderlich. Für jeden Grenzwert sind auch seine beiden direkten Nachbarn auszuwählen.

Da die beiden Grenzwerte (Minimum- beziehungsweise Maximum der jeweiligen Äquivalenzklasse A beziehungsweise B) identisch sind, die jeweiligen inneren Nachbarn aber nicht, ergeben sich nach dem Verfahren insgesamt vier Testfälle zur Prüfung des Übergangs zwischen den beiden benachbarten Äquivalenzklassen.

##### Vereinfachung in der Praxis

In aller Regel wird der Übergang von einer Äquivalenzklasse in eine benachbarte einheitlich mit einer Abfrage – also aus Sicht einer Äquivalenzklasse – umgesetzt. In der Praxis ist es daher meist nicht erforderlich, eine Grenze zwischen zwei benachbarten Äquivalenzklassen mit der 3-Wert-Grenzwertanalyse aus Sicht beider Klassen mit insgesamt vier Testfällen zu prüfen.

Es muss aber entschieden werden, aus welcher Äquivalenzklasse der Grenzwert genommen wird, um seine Nachbarn zu ermitteln.

---

#### Beispiel: Ganzzahlige Eingabe

Für das Beispiel mit zwei Äquivalenzklassen mit gültigen Werten und einer mit ungültigen Werten für den Test eines ganzzahligen Eingabewertes (etwa die Bestellmenge `quantity` im E-Commerce-System mit gÄK1: [1, …, 99]) ergeben sich nach der 2-Wert- beziehungsweise 3-Wert-Grenzwertanalyse folgende Testeingabewerte:

| Äquivalenzklasse | 2-Wert-Grenzwertanalyse | 3-Wert-Grenzwertanalyse |
|------------------|-------------------------|-------------------------|
| uÄK1: [MIN_INT, …, 0] | MIN_INT-1, MIN_INT | MIN_INT-1, MIN_INT, MIN_INT+1 |
| | 0, 1 | 0, 1, 2 |
| gÄK1: [1, …, 99] | 0, 1 | 0, 1, 2 |
| | 99, 100 | 98, 99, 100 |
| uÄK2: [100, …, MAX_INT] | 99, 100 | 98, 99, 100 |
| | MAX_INT, MAX_INT+1 | MAX_INT-1, MAX_INT, MAX_INT+1 |

Bei Berücksichtigung von zwei Werten je Grenzwert ergeben sich sechs Testdaten, die zur Erstellung von Testfällen heranzuziehen sind. Bei der 3-Wert-Grenzwertanalyse sind es zehn Werte.

##### Überlappende Grenzwerte

Ein Testfall mit dem Eingabewert 0 prüft den größten Wert der ungültigen Äquivalenzklasse uÄK1. Dieser Testfall prüft aber auch den direkten Nachbarn außerhalb der unteren Grenze (1) der gültigen Äquivalenzklasse gÄK1. Entsprechendes gilt für den Wert 1.

##### Technische Grenzen beachten

Zu beachten ist, dass Werte oberhalb der oberen Grenze beziehungsweise unterhalb der unteren Grenze der Rand-Äquivalenzklassen aus technischen Gründen manchmal nicht als konkrete Eingabewerte genutzt werden können (im Beispiel sind dies MIN_INT-1 und MAX_INT+1).

##### Vollständigkeit der Testfälle

In der Tabelle sind nur die Testwerte für die Eingabevariable angegeben. Damit die Testfälle komplett sind, gehört zu jedem der einzelnen Werte das jeweils <a href="./Glossar.md#erwartetes-ergebnis" title="→ Glossar öffnen" class="glossary-term">**erwartete Verhalten**</a> des <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekts**</a> beziehungsweise die jeweils erwarteten Ausgaben sowie gegebenenfalls die jeweiligen <a href="./Glossar.md#vorbedingung" title="→ Glossar öffnen" class="glossary-term">**Vor-**</a> und <a href="./Glossar.md#nachbedingung" title="→ Glossar öffnen" class="glossary-term">**Nachbedingungen**</a>.

---

#### Abwägung des Testaufwands

Auch bei der Grenzwertanalyse ist zu entscheiden, ob der Testaufwand gerechtfertigt ist und jeder Grenzwert mit seinen benachbarten Werten (mit ein oder zwei weiteren Werten) jeweils für einen extra Testfall berücksichtigt werden soll.

Es können auch die Testfälle mit den Repräsentanten der Äquivalenzklassen weggelassen werden, die sich nicht aus der Grenzwertanalyse ergeben. Es wird dann davon ausgegangen, dass die Testfälle mit den Werten aus der Mitte einer Äquivalenzklasse keine zusätzlichen Erkenntnisse liefern, da Testfälle mit dem maximalen und dem minimalen Wert innerhalb der Äquivalenzklasse in jeweils einem Testfall überprüft werden.

---

#### Grenzen des Verfahrens

##### Keine Grenzwerte bei Mengen

Für Eingabewerte, die aus einer ungeordneten Menge auszuwählen sind, lassen sich keine Grenzwerte angeben.

*Beispiel: Ein Benutzer kann verschiedene Zahlungsarten wählen: Kreditkarte, PayPal, Rechnung oder Lastschrift. Die Möglichkeiten für den Eingabewert sind im mathematischen Sinne aus einer Menge zu wählen, die aus vier Elementen besteht. Grenzwerte lassen sich hier nicht identifizieren. Eine mögliche Ordnung über alphabetische Sortierung ist nicht sinnvoll, da die Reihenfolge keine Relevanz für die Verarbeitung hat.*

##### Anwendung auf Ausgabewerte

Beide Grenzwertanalysen können selbstverständlich auch für solche Äquivalenzklassen angewendet werden, die für Ausgabewerte gebildet wurden.

---

#### Zusammenfassung

| Aspekt | 2-Wert-Grenzwertanalyse | 3-Wert-Grenzwertanalyse |
|--------|-------------------------|-------------------------|
| Überdeckungselemente pro Grenzwert | 2 | 3 |
| Testfälle pro Grenze zwischen Klassen | 2 | 4 |
| Aufwand | Geringer | Höher |
| Fehlererkennungsrate | Gut | Sehr gut |
| Empfohlen bei | Standardfällen | Kritischen Systemen |

Die Grenzwertanalyse ist ein wirkungsvolles <a href="./Glossar.md#black-box-testverfahren" title="→ Glossar öffnen" class="glossary-term">**Blackbox-Testverfahren**</a>, das in Kombination mit der Äquivalenzklassenbildung eine hohe Fehlererkennungsrate ermöglicht. Die Entscheidung zwischen 2-Wert- und 3-Wert-Analyse sollte basierend auf der Kritikalität des <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekts**</a> und den verfügbaren Testressourcen getroffen werden.