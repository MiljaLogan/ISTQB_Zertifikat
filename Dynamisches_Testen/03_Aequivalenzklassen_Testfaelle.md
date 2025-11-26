### Testfälle aus Äquivalenzklassen kombinieren

Die Klassen sind gebildet, die Repräsentanten gewählt – doch wie entstehen daraus vollständige <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a>? Bei Funktionen mit mehreren Parametern müssen die Stellvertreter sinnvoll zusammengestellt werden. Die <a href="./Glossar.md#aequivalenzklassenbildung" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklassenmethode**</a> liefert dafür klare Regeln.

---

#### Grundproblem: Mehrere Parameter

Ein <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> hat selten nur einen Eingang. Typischerweise existieren mehrere Parameter, jeder mit mindestens zwei Klassen – einer gültigen und einer ungültigen. Pro Parameter also mindestens zwei Repräsentanten.

Für einen Testfall braucht jeder Parameter einen konkreten Wert. Welche Repräsentanten gehören zusammen? Nach welchen Kriterien kombinieren?

---

#### Die Kombinationsregeln

##### Gültige Werte: Alles mit allem

Sämtliche Repräsentanten gültiger Klassen werden untereinander kombiniert. Jede mögliche Zusammenstellung ergibt einen eigenen Testfall. Das Testobjekt soll schließlich alle spezifizierten Verhaltensweisen zeigen.

##### Ungültige Werte: Einzeln prüfen

Anders bei ungültigen Repräsentanten. Sie werden niemals untereinander kombiniert, sondern immer nur mit gültigen Werten der anderen Parameter. Jede ungültige Klasse erhält ihren eigenen Negativ-Testfall.

Warum diese Trennung? Ein ungültiger Wert löst eine Fehlerbehandlung aus – unabhängig von den anderen Parametern. Treffen mehrere ungültige Werte aufeinander, maskieren sie sich gegenseitig. Nur eine Ausnahme wird ausgelöst, die anderen bleiben verborgen. Außerdem wäre bei einer <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkung**</a> unklar, welcher Parameter sie verursacht hat. Unnötiger Analyseaufwand wäre die Folge.

---

#### Das Mengenproblem

Die Anzahl gültiger Testfälle ergibt sich multiplikativ: Zahl der gültigen Klassen von Parameter 1 mal Zahl der gültigen Klassen von Parameter 2 und so weiter. Bei wenigen Parametern explodiert das schnell auf Hunderte von Kombinationen.

##### Strategien zur Reduktion

Nicht immer ist die volle Kombinatorik machbar. Dann helfen diese Ansätze:

**Nach Nutzungshäufigkeit priorisieren**: Welche Kombinationen kommen in der Praxis oft vor? Diese zuerst testen.

**<a href="./Glossar.md#grenzwert" title="→ Glossar öffnen" class="glossary-term">**Grenzwerte**</a> bevorzugen**: Testfälle mit Randwerten haben höhere Trefferquoten für Fehler.

**Paarweise statt vollständig**: Jeder Repräsentant trifft jeden anderen mindestens einmal – aber nicht in jeder Kombination.

**Each-Choice-Minimum**: Jeder Repräsentant kommt in mindestens einem Testfall vor. Das absolute Minimum.

---

#### Praxisbeispiel: Bestellpreisberechnung

Eine Methode im Online-Shop berechnet den Gesamtpreis einer Bestellung. Sie kennt fünf Parameter:

```python
def calculate_order_total(
    item_price: float,      # Einzelpreis
    quantity: int,          # Menge
    shipping_cost: float,   # Versand
    discount_code: int,     # Rabattcode-Typ
    customer_discount: float # Kundenrabatt
) -> float:
```

##### Schritt 1: Rohe Klasseneinteilung

Allein aus der Schnittstelle entstehen pro Parameter eine gültige und eine ungültige Klasse:

| Parameter | Gültige Klasse | Ungültige Klasse |
|-----------|----------------|------------------|
| item_price | Alle Gleitkommazahlen | NaN |
| quantity | Alle Ganzzahlen | NaN |
| shipping_cost | Alle Gleitkommazahlen | NaN |
| discount_code | Alle Ganzzahlen | NaN |
| customer_discount | Alle Gleitkommazahlen | NaN |

##### Schritt 2: Verfeinerung durch Spezifikation

Die funktionale Beschreibung liefert Details:

* Preise sind nicht negativ
* Mengen liegen zwischen 1 und 99
* Rabattcodes kennen vier Stufen: 0 (kein Rabatt), 1 (5%), 2 (10%), 3 (15%)
* Kundenrabatt maximal 50%

Daraus entstehen differenziertere Klassen. Die Analyse offenbart auch Lücken – etwa fehlende Obergrenzen für Preise. Solche Unklarheiten erfordern Rücksprache.

| Parameter | Klasse | Repräsentant |
|-----------|--------|--------------|
| item_price | gÄK: [0, …, MAX_DOUBLE] | 29.99 |
| | uÄK1: negative Werte | -1.00 |
| | uÄK2: NaN | "abc" |
| quantity | gÄK: [1, …, 99] | 3 |
| | uÄK1: ≤ 0 | 0 |
| | uÄK2: ≥ 100 | 150 |
| | uÄK3: NaN | "abc" |
| shipping_cost | gÄK: [0, …, MAX_DOUBLE] | 4.99 |
| | uÄK1: negative Werte | -1.00 |
| | uÄK2: NaN | "abc" |
| discount_code | gÄK1: 0 | 0 |
| | gÄK2: 1 | 1 |
| | gÄK3: 2 | 2 |
| | gÄK4: 3 | 3 |
| | uÄK1: negative Werte | -1 |
| | uÄK2: ≥ 4 | 99 |
| | uÄK3: NaN | "abc" |
| customer_discount | gÄK: [0, …, 50] | 10.00 |
| | uÄK1: negative Werte | -1.00 |
| | uÄK2: > 50 | 75.00 |
| | uÄK3: NaN | "abc" |

Bilanz: 20 Klassen insgesamt – 7 gültige, 13 ungültige.

##### Schritt 3: Repräsentanten wählen

Theoretisch taugt jeder Wert einer Klasse. Praktisch lohnt sich Sorgfalt: Plausible Werte wählen, die im Echtbetrieb vorkommen. Für ungültige Klassen genügen einfache, eindeutige Vertreter.

Die Klassenbildung gelingt selten perfekt. Zeitmangel oder fehlende Details führen zu Kompromissen. Manche Klassen überlappen vielleicht doch. Deshalb: Repräsentanten mit Bedacht wählen – innerhalb einer Klasse könnten einzelne Werte doch anders verarbeitet werden.

##### Schritt 4: Testfälle bauen

Jetzt wird kombiniert. Gültige Klassen: 1 × 1 × 1 × 4 × 1 = 4 Testfälle. Ungültige Klassen: 2 + 3 + 2 + 3 + 3 = 13 separate Testfälle. Zusammen 17 Stück.

| Nr | item_price | quantity | shipping | code | cust_disc | Ergebnis |
|----|------------|----------|----------|------|-----------|----------|
| 1 | 29.99 | 3 | 4.99 | 0 | 10.00 | 85.96 |
| 2 | 29.99 | 3 | 4.99 | 1 | 10.00 | 81.46 |
| 3 | 29.99 | 3 | 4.99 | 2 | 10.00 | 76.96 |
| 4 | 29.99 | 3 | 4.99 | 3 | 10.00 | 72.46 |
| 5 | -1.00 | 3 | 4.99 | 0 | 10.00 | FEHLER |
| 6 | "abc" | 3 | 4.99 | 0 | 10.00 | FEHLER |
| 7 | 29.99 | 0 | 4.99 | 0 | 10.00 | FEHLER |
| 8 | 29.99 | 150 | 4.99 | 0 | 10.00 | FEHLER |
| 9 | 29.99 | "abc" | 4.99 | 0 | 10.00 | FEHLER |
| 10 | 29.99 | 3 | -1.00 | 0 | 10.00 | FEHLER |
| 11 | 29.99 | 3 | "abc" | 0 | 10.00 | FEHLER |
| 12 | 29.99 | 3 | 4.99 | -1 | 10.00 | FEHLER |
| 13 | 29.99 | 3 | 4.99 | 99 | 10.00 | FEHLER |
| 14 | 29.99 | 3 | "abc" | 0 | 10.00 | FEHLER |
| 15 | 29.99 | 3 | 4.99 | 0 | -1.00 | FEHLER |
| 16 | 29.99 | 3 | 4.99 | 0 | 75.00 | FEHLER |
| 17 | 29.99 | 3 | 4.99 | 0 | "abc" | FEHLER |

##### Beobachtungen

Bei den Negativ-Tests bleiben die gültigen Parameter konstant. Nur der eine ungültige Wert variiert. So ist klar, wer die Reaktion auslöst.

Vier der fünf Parameter haben nur eine gültige Klasse – daher die geringe Zahl an Positiv-Tests. Eine weitere Reduktion ist hier unnötig.

##### Sollergebnisse bestimmen

Für Negativ-Tests ist das einfach: der erwartete Fehlercode. Für Positiv-Tests muss gerechnet werden – etwa per Tabellenkalkulation:

* Test 1: (29.99 × 3) × 0.90 + 4.99 = 85.96
* Test 2: (29.99 × 3) × 0.95 × 0.90 + 4.99 = 81.46
* Test 3: (29.99 × 3) × 0.90 × 0.90 + 4.99 = 76.96
* Test 4: (29.99 × 3) × 0.85 × 0.90 + 4.99 = 72.46

---

#### Hinweis zur Teststufe

Manche ungültigen Werte – etwa eine Menge von Null – werden in der Praxis oft schon früher abgefangen. Die Benutzeroberfläche oder eine Validierungsschicht lässt sie gar nicht durch.

Die Negativ-Testfälle bleiben trotzdem sinnvoll, wenn die Methode selbst das Testobjekt ist. Beim <a href="./Glossar.md#systemtest" title="→ Glossar öffnen" class="glossary-term">**Systemtest**</a> können sie entfallen – vorausgesetzt, die vorgelagerte Prüfung wurde bereits getestet.

Welche Testfälle auf welcher <a href="./Glossar.md#teststufe" title="→ Glossar öffnen" class="glossary-term">**Teststufe**</a> laufen, entscheidet die <a href="./Glossar.md#testplanung" title="→ Glossar öffnen" class="glossary-term">**Testplanung**</a>.

---

#### Zusammenfassung

| Regel | Umsetzung |
|-------|-----------|
| Gültige kombinieren | Alle Permutationen bilden |
| Ungültige isolieren | Jede für sich mit sonst gültigen Werten |
| Explosion vermeiden | Priorisierung, Paarweise, Each-Choice |
| Konstanz wahren | Bei Negativ-Tests nur einen Parameter variieren |
| Soll festlegen | Vor dem Test das Ergebnis berechnen |

Die systematische Kombination von Repräsentanten führt zu einer überschaubaren, aber aussagekräftigen Testfallmenge. Der Schlüssel liegt in der sauberen Trennung von gültigen und ungültigen Werten sowie in der bewussten Entscheidung über den Kombinationsgrad.