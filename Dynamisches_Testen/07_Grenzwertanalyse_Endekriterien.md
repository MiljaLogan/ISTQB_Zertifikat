### Endekriterien und Bewertung der Grenzwertanalyse

Die systematische Anwendung der <a href="./Glossar.md#grenzwertanalyse" title="→ Glossar öffnen" class="glossary-term">**Grenzwertanalyse**</a> erfordert ebenso wie die <a href="./Glossar.md#aequivalenzklassenbildung" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklassenbildung**</a> messbare Kriterien, um festzustellen, wann der Test als ausreichend angesehen werden kann. Die <a href="./Glossar.md#ueberdeckung" title="→ Glossar öffnen" class="glossary-term">**Überdeckung**</a> der <a href="./Glossar.md#grenzwert" title="→ Glossar öffnen" class="glossary-term">**Grenzwerte**</a> liefert ein solches Kriterium und ermöglicht eine objektive Bewertung der Testintensität.

---

#### Berechnung der Grenzwertüberdeckung

In Analogie zum <a href="./Glossar.md#endekriterien" title="→ Glossar öffnen" class="glossary-term">**Endekriterium**</a> bei der Äquivalenzklassenbildung lässt sich auch eine anzustrebende Überdeckung der Grenzwerte vorab festlegen und nach der Durchführung der Tests berechnen. Die Berechnung ist sowohl für die 2-Wert- als auch die 3-Wert-Grenzwertanalyse anzuwenden:

> **GW-Überdeckung = (Anzahl getestete GW / Gesamtzahl GW) × 100%**

##### Besonderheiten bei der Zählung

Bei der Berechnung ist zu beachten, dass nicht nur der direkte Grenzwert, sondern auch die jeweiligen benachbarten Werte ober- und unterhalb der Grenzwerte zu berücksichtigen sind. Der Begriff "GW" in der Formel umfasst also die Grenzwerte und deren direkte Nachbarn – ein oder zwei je nach gewähltem Verfahren.

Es werden allerdings nur unterschiedliche Werte zur Berechnung herangezogen. Zusammenfallende Werte benachbarter <a href="./Glossar.md#aequivalenzklasse" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklassen**</a> werden als ein Wert gezählt, da ja auch nur ein <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> mit dem entsprechenden Eingabewert durchgeführt wird.

*Beispiel: Bei der Grenze zwischen zwei Äquivalenzklassen für den Kundenrabatt (gÄK: [0, …, 50] und uÄK: ]50, …, MAX_DOUBLE]) ist der Wert 50 sowohl der Maximumwert der gültigen als auch der Nachbarwert der ungültigen Klasse. Er wird nur einmal gezählt.*

---

#### Bewertung des Verfahrens

##### Kombination mit der Äquivalenzklassenbildung

Die Grenzwertanalyse ist in Verbindung mit der Äquivalenzklassenbildung durchzuführen, da an den Grenzen der Äquivalenzklassen häufiger <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> nachzuweisen sind als innerhalb der Klassen.

Äquivalenzklassenbildung und die gewählte Grenzwertanalyse (2- oder 3-Wert) lassen sich sehr sinnvoll kombinieren, geben aber dennoch genügend Freiheitsgrade in der Wahl der konkreten <a href="./Glossar.md#testdaten" title="→ Glossar öffnen" class="glossary-term">**Testdaten**</a>.

##### Anforderungen an den Tester

> Die Grenzwertanalyse erfordert – sofern es nicht um einfache rein numerische Datenbereiche geht – eine hohe Kreativität, um die entsprechenden Testdaten an den Grenzen festzulegen. Dieser Aspekt wird oft nicht genügend beachtet, da das Verfahren sehr einfach erscheint, obwohl die Bestimmung der relevanten Grenzen nicht trivial ist.

*Beispiel: Bei einem E-Commerce-System ist die Bestimmung der Grenzwerte für einen Artikelpreis einfach (0.00, MAX_DOUBLE). Die Bestimmung der Grenzwerte für komplexere Bedingungen wie "Mindestbestellwert für kostenlosen Versand abhängig von Kundengruppe und Lieferregion" erfordert hingegen sorgfältige Analyse der Spezifikation und kreatives Denken.*

---

#### Zusammenfassung

| Aspekt | Beschreibung |
|--------|--------------|
| <a href="./Glossar.md#ueberdeckungselement" title="→ Glossar öffnen" class="glossary-term">**Überdeckungselement**</a> | Grenzwert mit seinen Nachbarwerten |
| <a href="./Glossar.md#ueberdeckungskriterien" title="→ Glossar öffnen" class="glossary-term">**Überdeckungskriterium**</a> | Prozentsatz der getesteten Grenzwerte |
| Zählung | Zusammenfallende Werte nur einmal zählen |
| Stärke | Hohe Fehlererkennungsrate an kritischen Stellen |
| Herausforderung | Kreativität bei nicht-trivialen Grenzen erforderlich |
| Empfehlung | Immer in Kombination mit Äquivalenzklassenbildung anwenden |

Die Grenzwertanalyse ist ein wirkungsvolles <a href="./Glossar.md#black-box-testverfahren" title="→ Glossar öffnen" class="glossary-term">**Blackbox-Testverfahren**</a>, das seine volle Stärke in der Kombination mit der Äquivalenzklassenbildung entfaltet. Die scheinbare Einfachheit des Verfahrens sollte nicht darüber hinwegtäuschen, dass die Identifikation relevanter Grenzen fundiertes Fachwissen und analytisches Denken erfordert.