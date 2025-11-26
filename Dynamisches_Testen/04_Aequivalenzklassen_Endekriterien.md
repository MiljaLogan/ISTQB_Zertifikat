### Wann ist genug getestet? Endekriterien für die Äquivalenzklassenbildung

Irgendwann muss Schluss sein. Doch wann? Die <a href="./Glossar.md#aequivalenzklassenbildung" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklassenbildung**</a> liefert ein messbares Kriterium: die <a href="./Glossar.md#ueberdeckung" title="→ Glossar öffnen" class="glossary-term">**Überdeckung**</a>. Sie zeigt, welcher Anteil der Klassen bereits geprüft wurde – und was noch fehlt.

---

#### Die Überdeckungsformel

Jede <a href="./Glossar.md#aequivalenzklasse" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklasse**</a> – ob gültig oder ungültig – ist ein <a href="./Glossar.md#ueberdeckungselement" title="→ Glossar öffnen" class="glossary-term">**Überdeckungselement**</a>. Ein einziger <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> mit einem passenden Repräsentanten genügt, um eine Klasse als abgedeckt zu werten.

Die Rechnung ist simpel:

> **ÄK-Überdeckung = (geprüfte Klassen / alle Klassen) × 100%**

*Beispiel: 20 Klassen existieren, 16 wurden getestet. Das ergibt 80% Überdeckung.*

##### Konkretes Szenario

Im E-Commerce-Beispiel entstanden 20 Äquivalenzklassen. Alle 17 Testfälle zusammen decken sie vollständig ab – 100%. Fallen aus Zeitgründen die letzten drei Negativ-Tests weg, bleiben drei ungültige Klassen des Parameters `customer_discount` ungeprüft. Die Überdeckung sinkt auf 17/20 = 85%.

---

#### Überdeckung als Steuerungsinstrument

Der Prozentwert dient zwei Zwecken.

##### Vor dem Test: Ziel definieren

Die <a href="./Glossar.md#testplanung" title="→ Glossar öffnen" class="glossary-term">**Testplanung**</a> legt fest, welche Überdeckung erreicht werden soll. 80%? 95%? 100%? Je kritischer die Software, desto höher die Anforderung.

##### Nach dem Test: Ergebnis prüfen

Wurden die geplanten Testfälle ausgeführt? Hat die tatsächliche Überdeckung das Ziel erreicht? Das <a href="./Glossar.md#endekriterien" title="→ Glossar öffnen" class="glossary-term">**Endekriterium**</a> ist messbar und nachweisbar.

*Beispiel: Geplant waren 80% Überdeckung. Mit 16 von 20 Klassen ist das Ziel erreicht – der Test nach Äquivalenzklassenbildung kann enden.*

---

#### Die Tücke: Qualität der Klassenbildung

Eine hohe Prozentzahl klingt gut. Doch sie täuscht, wenn die Klassenbildung fehlerhaft war.

Wurden Klassen übersehen? Dann bezieht sich die 100% auf eine zu kleine Gesamtmenge. Das Ergebnis sieht besser aus, als es ist. Die tatsächliche Testintensität bleibt unter dem Anschein.

> Der Überdeckungsgrad ist nur so aussagekräftig wie die Klassenbildung sorgfältig war. Wer Klassen vergisst, betrügt sich selbst.

---

#### Stärken des Verfahrens

Die Systematik zahlt sich aus. Mehrere Vorteile entstehen:

**Vollständigkeit**: Spezifizierte Bedingungen und Einschränkungen werden nicht übersehen. Die methodische Analyse deckt sie auf.

**Effizienz**: Überflüssige Testfälle entfallen. Werte aus derselben Klasse lösen identisches Verhalten aus – einer genügt.

**Breite Anwendbarkeit**: Das Verfahren funktioniert nicht nur für Methodenparameter. Es eignet sich auch für:

* Interne Variablen und Zustände
* Konfigurationswerte
* Zeitabhängige Bedingungen
* Schnittstellenparameter bei <a href="./Glossar.md#integrationstest" title="→ Glossar öffnen" class="glossary-term">**Integrationstests**</a>

Damit passt die Methode zum <a href="./Glossar.md#systemtest" title="→ Glossar öffnen" class="glossary-term">**Systemtest**</a>, <a href="./Glossar.md#integrationstest" title="→ Glossar öffnen" class="glossary-term">**Integrationstest**</a> und <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententest**</a> gleichermaßen.

---

#### Grenzen des Verfahrens

Eine Schwäche bleibt: Parameter werden isoliert betrachtet. Wechselwirkungen zwischen ihnen – etwa "wenn A groß, dann muss B klein sein" – erfasst die Methode nicht automatisch.

Solche Abhängigkeiten erfordern zusätzliche Unterteilungen und entsprechende Kombinationen. Der Aufwand steigt erheblich. Hier helfen andere Verfahren wie der <a href="./Glossar.md#entscheidungstabellentest" title="→ Glossar öffnen" class="glossary-term">**Entscheidungstabellentest**</a>.

---

#### Ideale Ergänzung: Grenzwertanalyse

Allein eingesetzt ist die Äquivalenzklassenbildung bereits nützlich. Ihre volle Stärke entfaltet sie in Kombination mit der <a href="./Glossar.md#grenzwertanalyse" title="→ Glossar öffnen" class="glossary-term">**Grenzwertanalyse**</a>. Denn <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> lauern besonders an den Klassengrenzen. Wer beide Methoden kombiniert, findet mehr Fehler als mit jeder einzeln.

---

#### Auf einen Blick

| Aspekt | Beschreibung |
|--------|--------------|
| Überdeckungselement | Einzelne Äquivalenzklasse |
| Abdeckungskriterium | Ein Repräsentant pro Klasse |
| Formel | geprüfte / alle × 100% |
| Stärke | Systematik, Effizienz, breite Einsetzbarkeit |
| Schwäche | Keine Berücksichtigung von Parameterabhängigkeiten |
| Empfehlung | Mit Grenzwertanalyse kombinieren |

Die Äquivalenzklassenbildung macht Testfortschritt messbar. Sie zeigt, was erledigt ist und was noch aussteht. Doch das Maß ist nur so gut wie die zugrunde liegende Analyse – Sorgfalt bei der Klassenbildung bleibt unersetzlich.