### Testfälle aus der Grenzwertanalyse

Die <a href="./Glossar.md#grenzwertanalyse" title="→ Glossar öffnen" class="glossary-term">**Grenzwertanalyse**</a> liefert systematisch Testwerte, die zu vollständigen <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> kombiniert werden müssen. In Analogie zur Testfallermittlung bei der <a href="./Glossar.md#aequivalenzklassenbildung" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklassenbildung**</a> können die Werte aus einer gültigen <a href="./Glossar.md#aequivalenzklasse" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklasse**</a> miteinander zu Testfällen kombiniert werden. Die Werte aus einer ungültigen Äquivalenzklasse sind wieder separat zu überprüfen und können nicht mit anderen ungültigen Werten kombiniert werden.

Die Werte aus dem mittleren Bereich einer Äquivalenzklasse müssen nicht für einen extra Testfall verwendet werden, wenn die beiden <a href="./Glossar.md#grenzwert" title="→ Glossar öffnen" class="glossary-term">**Grenzwerte**</a> innerhalb der Äquivalenzklasse bereits für Testfälle vorgesehen sind.

---

#### Beispiel: 3-Wert-Grenzwertanalyse für E-Commerce-Preisberechnung

Wird die 3-Wert-Grenzwertanalyse auf die gültigen Äquivalenzklassen zur Prüfung der Methode `calculate_order_total()` angewendet, ergeben sich die folgenden grenzwertbasierten <a href="./Glossar.md#testdaten" title="→ Glossar öffnen" class="glossary-term">**Testdaten**</a> je Parameter:

| Parameter | Nachbarwert | [Grenzwert | Nachbarwert | … | Nachbarwert | Grenzwert] | Nachbarwert |
|-----------|-------------|------------|-------------|---|-------------|------------|-------------|
| item_price | 0-ε | [0 | 0+ε | … | MAX_FLOAT-ε | MAX_FLOAT] | MAX_FLOAT+ε |
| quantity | 0 | [1 | 2 | … | 98 | 99] | 100 |
| shipping_cost | 0-ε | [0 | 0+ε | … | MAX_FLOAT-ε | MAX_FLOAT] | MAX_FLOAT+ε |
| discount_code | -1 | [0 | 1 | 2 | 3] | 4 |
| customer_discount | 0-ε | [0 | 0+ε | … | 50-ε | 50] | 50+ε |

Die zu berücksichtigende Genauigkeit ε hängt von der Aufgabenstellung und der Zahlendarstellung des Rechners ab.

##### Ermittlung der Testdaten

Bei alleiniger Berücksichtigung der Werte, die innerhalb der Äquivalenzklassen liegen (in der Tabelle die Werte in eckigen Klammern), ergeben sich 4 + 4 + 4 + 4 + 4 = 20 grenzwertbasierte Repräsentanten. Von diesen sind einige bereits durch vorherige Testfälle geprüft.

Somit sind folgende Werte für weitere Testfälle zu berücksichtigen:

* **item_price**: 0.00, 0.01, MAX_FLOAT-0.01, MAX_FLOAT
* **quantity**: 1, 2, 98, 99
* **shipping_cost**: 0.00, 0.01, MAX_FLOAT-0.01, MAX_FLOAT
* **discount_code**: 0, 1, 2, 3
* **customer_discount**: 0.00, 0.01, 49.99, 50.00

Da alle Werte aus gültigen Äquivalenzklassen stammen, können sie miteinander zu Testfällen kombiniert werden.

---

#### Beispiel-Testfälle

| Testfall | item_price | quantity | shipping_cost | discount_code | customer_discount | Erwartetes Ergebnis |
|----------|------------|----------|---------------|---------------|-------------------|---------------------|
| 18 | 0.00 | 1 | 0.00 | 0 | 0.00 | 0.00 |
| 19 | 0.01 | 2 | 0.01 | 1 | 0.01 | 0.03 |
| 20 | MAX_FLOAT-0.01 | 98 | MAX_FLOAT-0.01 | 2 | 49.99 | >MAX_FLOAT |
| 21 | MAX_FLOAT-0.01 | 3 | 4.99 | 0 | 10.00 | >MAX_FLOAT |
| 22 | 29.99 | 99 | 4.99 | 0 | 10.00 | 2723.19 |
| 23 | 29.99 | 3 | MAX_FLOAT-0.01 | 0 | 10.00 | >MAX_FLOAT |

##### Erläuterungen zu den Testfällen

**Testfall 18** prüft alle gültigen unteren Grenzen der Äquivalenzklassen der Parameter. Der Testfall scheint keinen Bezug zur Realität zu haben – ein Artikel mit Preis 0 wird selten vorkommen. Das liegt allerdings an der ungenauen Spezifikation der Methode, bei der keine Unter- und Obergrenzen für die Parameterwerte angegeben sind.

**Testfall 19** nutzt die Nachbarwerte der unteren Grenzen sowie für die Menge einen Wert größer als eins. Somit wird mit diesem Testfall die Rechengenauigkeit geprüft.

**Testfall 20** kombiniert die nächsten Werte aus der obigen Auflistung. Das <a href="./Glossar.md#erwartetes-ergebnis" title="→ Glossar öffnen" class="glossary-term">**erwartete Ergebnis**</a> ist eher spekulativ. Ein Blick in die Spezifikation der Methode ergibt, dass die Preise multipliziert und addiert werden. Es ist daher sinnvoll, die jeweiligen Maximalwerte einzeln zu prüfen, was in den Testfällen 21 bis 23 erfolgt.

Weitere sinnvolle Testfälle ergeben sich, wenn die Werte der anderen Parameter auf 0.00 gesetzt werden, um zu prüfen, ob die Maximalwerte ohne zusätzliche Berechnung (kein Überlauf?) korrekt bearbeitet werden.

---

#### Auswirkungen präziser Spezifikationen

Am Beispiel wird sehr deutlich, welche Auswirkungen eine ungenaue Spezifikation auf den Test hat. Wird vor der Erstellung der Testfälle Rücksprache mit dem Kunden genommen und konnten dadurch die Wertebereiche der Parameter genauer angegeben werden, führt das zu einer Verringerung des Testaufwands.

##### Beispiel mit präzisierter Spezifikation

Der Kunde hat folgende Informationen gegeben:

* Der Artikelpreis liegt zwischen 0.50 und 9999.99
* Die Bestellmenge liegt zwischen 1 und 50 Stück
* Die Versandkosten liegen zwischen 0.00 und 49.99
* Der Kundenrabatt kann maximal 30% betragen

Nach entsprechender Erstellung der Äquivalenzklassen ergeben sich für den 3-Wert-Grenzwerttest bei der Berücksichtigung nur der Werte innerhalb der Äquivalenzklassen folgende gültige Werte der Parameter:

* **item_price**: 0.50, 0.51, 9999.98, 9999.99
* **quantity**: 1, 2, 49, 50
* **shipping_cost**: 0.00, 0.01, 49.98, 49.99
* **discount_code**: 0, 1, 2, 3
* **customer_discount**: 0.00, 0.01, 29.99, 30.00

Alle diese Werte sind frei zu Testfällen kombinierbar.

##### Ungültige Grenzwerte

Für die Werte, die außerhalb der Äquivalenzklassen liegen, ist jeweils ein Testfall zu erstellen. Folgende Werte sind dabei zu berücksichtigen:

* **item_price**: 0.49, 10000.00
* **quantity**: 0, 51
* **shipping_cost**: -0.01, 50.00
* **discount_code**: -1, 4
* **customer_discount**: -0.01, 30.01

> Es wird sehr deutlich, dass nach der genaueren Spezifikation weniger Testfälle zu erstellen sind und auch die jeweiligen Sollergebnisse klar vorherzusagen sind. Frühzeitig – schon bei der Spezifikation – an das <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> zu denken lohnt sich!

##### Ergänzende Testfälle

Eine Ergänzung der Testfälle mit den Grenzwerten des Rechners (MAX_FLOAT, MIN_FLOAT usw.) ist anzuraten. Mögliche <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> bei Berechnungen in Zusammenhang mit den Hardwarebeschränkungen können so aufgedeckt werden.

---

#### Praktische Tipps zur Testfallerstellung nach der 2-Wert-Grenzwertanalyse

Bei den folgenden Tipps wird davon ausgegangen, dass ein Test mit zwei Werten ausreicht, da <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Codereviews**</a> vorab durchgeführt und die möglichen falschen Bereichsabfragen dabei aufgedeckt wurden.

##### Eingabewertebereiche

Bei einem Eingabewertebereich sind die Grenzwerte und die benachbarten Werte außerhalb des Bereichs heranzuziehen.

*Beispiel: Bereich [-1.0; +1.0], Testdaten: -1.0 und +1.0 sowie -1.001 und +1.001. Die zu wählende Genauigkeit hängt von der Beschreibung der spezifizierten Aufgabe ab.*

##### Anzahl von Datensätzen

Ist für eine Datei die Anzahl der enthaltenen Datensätze zwischen 1 und 100 vorgegeben, so ergeben sich nach der Grenzwertanalyse folgende Überlegungen:

* Datei enthält keinen Datensatz
* Datei enthält einen Datensatz
* Datei enthält 100 Datensätze
* Datei enthält 101 Datensätze

##### Ausgabebereiche

Dienen Ausgabebereiche als Grundlage, kann beispielsweise wie folgt vorgegangen werden: Die Ausgabe des <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekts**</a> ist ein ganzzahliger Wert zwischen 500 und 1000. Zu erzielende Ergebnisse: 500 und 1000 sowie 499 und 1001.

Es kann allerdings einen gewissen Aufwand erfordern, die entsprechenden Eingabetestdaten zu ermitteln, um genau die geforderten Ausgaben zu erhalten. Es kann auch unmöglich sein, einen falschen Ausgabewert zu erhalten – Überlegungen hierzu können aber helfen, weitere <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> aufzudecken.

##### Anzahl bei Ausgabewerten

Ist bei den Ausgabewerten die erlaubte Anzahl entscheidend, ist in Analogie zur Anzahl bei den Eingabewerten zu verfahren: Ausgabe von 1 bis 4 Daten, zu erzeugende Ausgaben: 1 und 4 sowie 0 und 5 Daten.

##### Geordnete Mengen

Bei geordneten Mengen sind das erste und das letzte Element für den Test von besonderem Interesse.

---

#### Weitere Überlegungen zu Testdaten

##### Komplexe Datenstrukturen

Sind als Ein- oder Ausgaben komplexe Datenstrukturen gegeben, so können beispielsweise eine leere Liste, ein leerer Warenkorb oder die Nullmatrix als Grenzwerte angesehen und für den Test berücksichtigt werden.

##### Numerische Berechnungen

Bei numerischen Berechnungen sind als Grenzen sowohl eng beieinander liegende Werte als auch weit entfernte Werte für die Testfallermittlung heranzuziehen.

##### Ungültige Äquivalenzklassen

Für ungültige Äquivalenzklassen ist eine Grenzwertanalyse nur dort sinnvoll, wo abhängig von einer Äquivalenzklassengrenze eine unterschiedliche Ausnahmebehandlung des Testobjekts erwartet wird.

##### Extremfälle und Ressourcengrenzen

Zusätzlich sind Testfälle mit sehr großen Datenstrukturen, Listen und Tabellen durchzuführen, um beispielsweise Puffer-, Datei- oder Speichergrenzen zu überschreiten und somit das Verhalten des Testobjekts in diesen Extremfällen zu prüfen.

Bei Listen und Tabellen sind besonders interessant:

* Leere Listen
* Volle Listen
* Das erste Element
* Das letzte Element

An diesen Stellen sind wegen falscher Programmierung oft Fehlerwirkungen nachweisbar – das sogenannte **Off-by-one-Problem**.

*Beispiel: Ein Warenkorb im E-Commerce-System kann maximal 100 Artikel enthalten. Testfälle sollten einen leeren Warenkorb, einen Warenkorb mit einem Artikel, einen mit 99 Artikeln, einen mit 100 Artikeln und den Versuch, einen 101. Artikel hinzuzufügen, umfassen. Besonders das Hinzufügen und Entfernen des ersten und letzten Artikels sollte getestet werden.*

---

#### Zusammenfassung

| Aspekt | Empfehlung |
|--------|------------|
| Kombination gültiger Werte | Frei kombinierbar zu Testfällen |
| Kombination ungültiger Werte | Separat testen, nicht kombinieren |
| Mittlere Werte | Können entfallen, wenn Grenzwerte getestet werden |
| Spezifikationsqualität | Präzise Spezifikation reduziert Testaufwand erheblich |
| Hardwaregrenzen | Immer zusätzlich testen (MAX_FLOAT, MIN_INT etc.) |
| Komplexe Strukturen | Leere und volle Strukturen als Grenzfälle betrachten |

Die systematische Erstellung von Testfällen aus der Grenzwertanalyse erfordert sorgfältige Planung und Abstimmung mit der Spezifikation. Der Aufwand für präzise <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> zahlt sich durch reduzierte Testfallmengen und klarere Sollergebnisse aus.