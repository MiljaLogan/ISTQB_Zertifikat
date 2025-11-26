# Kollaborative Anforderungsermittlung in agilen Kontexten

## Iterativ-inkrementelle Anforderungsentwicklung

**In Projekten, die iterativen und insbesondere <a href="./Glossar.md#agile-softwareentwicklung" title="→ Glossar öffnen" class="glossary-term">**agilen Vorgehensmodellen**</a> folgen, wird auch die Anforderungsermittlung als iterativ-inkrementeller Prozess gestaltet.** Diese Herangehensweise bedeutet, dass sowohl die Anzahl identifizierter <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> als auch der Detailgrad ihres Verständnisses und ihrer Dokumentation von Iteration zu Iteration zunimmt.

> **Evolutionäres Prinzip:** <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> entwickeln sich kontinuierlich und werden durch systematische Zusammenarbeit aller Beteiligten verfeinert und konkretisiert.

**Diese adaptive Herangehensweise erkennt an, dass Anforderungen in komplexen Projekten selten von Beginn an vollständig verstanden werden können und durch kontinuierliches Lernen und Feedback präzisiert werden müssen.**

## Strategische Zusammenarbeit für Anforderungsqualität

### Fundamentales Kollaborationsprinzip

> **Kollaborationsimperativ:** Enge Zusammenarbeit aller Beteiligten ist essentiell für die korrekte Erfassung und einheitliche Interpretation von Systemanforderungen.

**Damit das zu entwickelnde System die Wünsche und Ziele der Stakeholder optimal erfüllt, ist es notwendig, dass <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> korrekt erfasst werden und alle beteiligten Parteien - Stakeholder, Product Owner und Entwicklungsteam - zu einer gemeinsamen, einheitlichen Interpretation gelangen.**

### Präventive Qualitätssicherung

**In <a href="./Glossar.md#agile-softwareentwicklung" title="→ Glossar öffnen" class="glossary-term">**agilen Vorgehensweisen**</a> wird hoher Wert darauf gelegt, dass Stakeholder, Product Owner und Entwicklungsteam bei Erhebung und Formulierung der <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> kontinuierlich und über alle Iterationen hinweg eng zusammenarbeiten.**

**Diese intensive Kollaboration zielt darauf ab:**
* **Fehlerprävention** - Reduzierung oder Vermeidung von Erhebungs- und Interpretationsfehlern von vornherein
* **Gemeinsame Vision** - Entwicklung einer konsensualen Produktvision, die Fachlichkeit, Entwicklung und <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> gleichermaßen repräsentiert
* **Kontinuierliche Validierung** - Laufende Überprüfung und Anpassung der Anforderungsinterpretation

*Beispiel aus "Pixel Leap":* Wöchentliche "Three Amigos"-Sessions zwischen Product Owner, Entwicklern und Testern führten zu einer 60%igen Reduzierung von Anforderungsänderungen während der Entwicklung.*

## User Stories: Leichtgewichtige Anforderungsnotation

### Konzeptuelle Grundlagen

**<a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> werden in Form von <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a> dokumentiert und verwaltet.** Eine <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> stellt eine leichtgewichtige Notation einer <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderung**</a> dar, wobei diese umgangssprachlich, aber in einem strukturierten, kurzen Textmuster formuliert wird:

> **Standard-Format:** "Als <Rolle> möchte ich, dass <zu erreichendes Ziel>, damit <resultierender Nutzen>"

### Kollaborative Vorteile des Satzschemas

**Die Verwendung eines standardisierten Satzschemas unterstützt die Zusammenarbeit durch:**
* **Formulierungshilfe** - Erleichtert den Beteiligten das "in Worte fassen" von <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a>
* **Verständlichkeit** - Vereinfacht das Lesen und Verstehen bereits erfasster <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a>
* **Konsistenz** - Gewährleistet einheitliche Struktur über alle <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a> hinweg

*Beispiel aus "Pixel Leap":* "Als Spieler möchte ich, dass mein Charakter präzise springt, damit ich herausfordernde Plattform-Sequenzen meistern kann."*

## INVEST-Kriterien für Story-Qualität

### Systematische Qualitätsbewertung

**Zur Beurteilung der Qualität einer <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> können die INVEST-Kriterien herangezogen werden.** Eine hochwertige <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> ist charakterisiert durch:

| Kriterium | Englisch | Beschreibung | Testimplikation |
|-----------|----------|--------------|-----------------|
| **Unabhängig** | Independent | Keine Abhängigkeiten zu anderen Stories | Isolierte <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testdurchführung**</a> möglich |
| **Verhandelbar** | Negotiable | Gestaltungsspielraum in der Umsetzung | Flexible Testansätze erforderlich |
| **Wertvoll** | Valuable | Nutzen für Anwender/Kunden erkennbar | <a href="./Glossar.md#validierung" title="→ Glossar öffnen" class="glossary-term">**Validierungs**</a>tests prioritär |
| **Abschätzbar** | Estimatable | Umsetzungsaufwand bewertbar | Testaufwand planbar |
| **Klein** | Small | Angemessene Größe für Iteration | <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> überschaubar und fokussiert |
| **Testbar** | Testable | Präzise <a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a> definiert | Eindeutige <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> ableitbar |

### Testorientierte Qualitätssicherung

**Teammitglieder mit Testkompetenz sollten insbesondere Feedback zum Kriterium "<a href="./Glossar.md#testbarkeit" title="→ Glossar öffnen" class="glossary-term">**Testbarkeit**</a>" einbringen und Vorschläge entwickeln, wie <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a> oder ihre Abnahmekriterien testbarer formuliert werden können.** Die <a href="./Glossar.md#testbarkeit" title="→ Glossar öffnen" class="glossary-term">**Testbarkeit**</a> einer <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderung**</a> und des implementierenden Codes hat direkten Einfluss auf die Testkosten.

*Beispiel aus "Pixel Leap":* Eine ursprünglich vage Story "Das Spiel soll Spaß machen" wurde durch Tester-Feedback zu "Als Spieler möchte ich innerhalb von 30 Sekunden den Sprungmechanismus verstehen, damit ich ohne Tutorial spielen kann" - eine testbare Formulierung mit messbaren Kriterien.*

## Das 3C-Konzept: Strukturierte Story-Entwicklung

### Systematische Herangehensweise

**Ein bewährtes Vorgehen zur Erstellung von <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a> orientiert sich an den "3 Cs" - einem strukturierten Ansatz, der verschiedene Aspekte der Story-Entwicklung adressiert:**

#### Karte (Card)
**Als Medium für die Notation einer <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> wird eine "Story Card" verwendet.** Diese kann als Eintrag in einem elektronischen Board oder als physische Karteikarte realisiert werden.

**Moderne Implementierungen umfassen:**
* **Digitale Boards** - Jira, Azure DevOps, Trello mit strukturierten Templates
* **Physische Karten** - Traditionelle Karteikarten für Co-Location-Teams
* **Hybride Ansätze** - Kombination digitaler Verwaltung mit physischer Visualisierung

#### Konversation (Conversation)
**Die inhaltliche Klärung und Erarbeitung der <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> erfolgt gemeinsam im Dialog mit den betroffenen Stakeholdern.** Dieser Dialog beginnt in der Releaseplanung und wird kontinuierlich fortgeführt, bis die <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> zur Implementierung bereit ist.

**Typische Konversationsformate:**
* **Story Refinement Sessions** - Regelmäßige Verfeinerungsmeetings
* **Spike-Analysen** - Technische Machbarkeitsstudien
* **Stakeholder-Interviews** - Direkte Nutzerbedarfserhebung

#### Bestätigung (Confirmation)
**Die korrekte Umsetzung jeder <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> muss explizit bestätigt werden.** Dies erfolgt anhand der je Story vereinbarten <a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a> und deren Anwendung im <a href="./Glossar.md#abnahmetest" title="→ Glossar öffnen" class="glossary-term">**Abnahmetest**</a>.

## Akzeptanzkriterien: Testbare Erfolgsbedingungen

### Definition und Funktion

**<a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a> sind die Bedingungen, die die Implementierung einer <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderung**</a> (z.B. als <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> gegeben) erfüllen muss, damit diese von den jeweiligen Stakeholdern akzeptiert wird.**

**Sie können als positive und negative Kriterien formuliert werden:**
* **Positive Kriterien** - "<a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> ist erfüllt, wenn..."
* **Negative Kriterien** - "<a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> ist noch nicht erfüllt, wenn..."

### Funktionale Bedeutung

> **Konzeptuelle Klarstellung:** <a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a> sind nichts anderes als <a href="./Glossar.md#testbedingung" title="→ Glossar öffnen" class="glossary-term">**Testbedingungen**</a>, die im späteren <a href="./Glossar.md#abnahmetest" title="→ Glossar öffnen" class="glossary-term">**Abnahmetest**</a> zur Anwendung kommen.

**<a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a> resultieren aus dem Dialog zwischen Stakeholdern, Product Owner und Entwicklungsteam und tragen zu folgenden Zielen bei:**

| Ziel | Nutzen | Beispiel aus "Pixel Leap" |
|------|--------|---------------------------|
| **Konsensbildung** | Einheitliche Story-Interpretation | "Präzise Sprünge" = max. 50ms Input-Latenz |
| **Umfangsabgrenzung** | Klare Realisierungsgrenzen | Sprungmechanik ohne Wall-Jump-Feature |
| **Planungsgrundlage** | Aufwandsschätzung und -planung | 3 Story Points für Basis-Sprungimplementierung |

### Formulierungsformate

**<a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a> können in verschiedenen Formaten formuliert werden, entscheidend ist ihre Klarheit und Eindeutigkeit:**

#### Szenarioorientierte Formate
* **Gherkin-Schema** - Given/When/Then-Struktur für Behavior-Driven Development
* **Beispielbasierte Beschreibungen** - Konkrete Anwendungsszenarien

#### Regelorientierte Formate
* **Kriterien-Checklisten** - Strukturierte Auflistung von Anforderungen
* **Input-Output-Tabellen** - Tabellarische Zuordnung von Eingaben und erwarteten Ergebnissen

*Beispiel aus "Pixel Leap":*
```
Szenario: Erfolgreicher Sprung
Given: Der Spieler steht auf festem Boden
When: Der Spieler drückt die Sprung-Taste
Then: Der Charakter springt 3 Einheiten hoch
And: Die Sprunganimation wird abgespielt
And: Die Eingabe-Latenz beträgt maximal 50ms
```

## Abnahmetestgetriebene Entwicklung (ATDD)

### Test-First-Philosophie

**<a href="./Glossar.md#abnahmetestgetriebene-entwicklung" title="→ Glossar öffnen" class="glossary-term">**Abnahmetestgetriebene Entwicklung**</a> (ATDD) repräsentiert einen <a href="./Glossar.md#test-first-ansatz" title="→ Glossar öffnen" class="glossary-term">**Test-First-Ansatz**</a>, der sich dadurch auszeichnet, dass <a href="./Glossar.md#abnahmetest" title="→ Glossar öffnen" class="glossary-term">**Abnahmetestfälle**</a> vor der Implementierung der betreffenden <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> in enger Zusammenarbeit zwischen Entwicklungsteam und Stakeholdern erstellt werden.**

### Strukturierter ATDD-Prozess

#### Spezifikations-Workshop
**Als erster Schritt wird häufig ein Spezifikations-Workshop durchgeführt.** Hier wird jede <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> zusammen mit ihren <a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a> von den Teammitgliedern analysiert, diskutiert und ausformuliert.

**Workshop-Ziele:**
* **Qualitätssicherung** - Erkennung und Behebung von Unvollständigkeiten, Mehrdeutigkeiten oder <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzuständen**</a>
* **Konsensbildung** - Gemeinsames Verständnis aller Beteiligten
* **Konkretisierung** - Transformation abstrakter Anforderungen in testbare Kriterien

#### Testfallspezifikation
**Nach der Analyse werden auf Grundlage der <a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a> die <a href="./Glossar.md#abnahmetest" title="→ Glossar öffnen" class="glossary-term">**Abnahmetestfälle**</a> spezifiziert.** Dies erfolgt durch das Team als Ganzes oder durch spezialisierte Teammitglieder.

**Die <a href="./Glossar.md#abnahmetest" title="→ Glossar öffnen" class="glossary-term">**Abnahmetestfälle**</a> fungieren zusätzlich als lebende Beispiele für die Funktionsweise der Software.**

*Beispiel aus "Pixel Leap":* Vor der Implementierung der Sprungmechanik entwickelte das Team 12 Abnahmetestfälle, die verschiedene Sprungszenarien abdeckten - von normalen Sprüngen bis zu Edge Cases wie Sprüngen an Levelgrenzen.*

## Testfallentwicklung und -abdeckung

### Systematische Testverfahren-Integration

**Zum Entwurf von <a href="./Glossar.md#abnahmetest" title="→ Glossar öffnen" class="glossary-term">**Abnahmetestfällen**</a> können sämtliche etablierten <a href="./Glossar.md#testverfahren" title="→ Glossar öffnen" class="glossary-term">**Testverfahren**</a> zum Einsatz kommen.** Die Notation sollte leicht verständlich sein, vorzugsweise in natürlicher Sprache oder unter Nutzung von Schlüsselworten, damit sie auch für Stakeholder zugänglich ist.

### Abdeckungsrichtlinien

> **Abdeckungsprinzip:** Jede <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> sollte durch <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> inhaltlich vollständig abgedeckt werden.

**Dabei sind folgende Prinzipien zu beachten:**

#### Vollständigkeit ohne Überabdeckung
* **Alle Merkmale** der <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> abdecken
* **Nicht über die Story hinausgehen** - keine impliziten, zusätzlichen <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> einführen

#### Redundanzvermeidung
* **Vermeidung doppelter Testung** derselben Story-Merkmale
* **Risikominimierung** widersprüchlicher <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a>
* **Vereinfachte Testpflege** durch klare Zuordnungen

#### Sonderfälle und Edge Cases
* **Komplexe Implementierungsaspekte** adressieren
* **Grenzfälle und Ausnahmesituationen** einbeziehen
* **Schwierig testbare Szenarien** systematisch erfassen

### Diagnosefunktion unklarer Testbarkeit

**Wenn unklar ist, wie eine <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a> getestet werden soll, deutet dies auf grundlegende Probleme hin:**

#### Story-Qualitätsprobleme
* **Unklare Formulierung** der <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Story**</a>
* **Geringer oder fehlender Mehrwert** der Anforderung
* **Oberflächliche Erfassung** der eigentlichen Bedarfe

#### Kompetenzdefizite
* **Fehlendes Test-Know-how** im Team oder bei Stakeholdern
* **Unzureichende fachliche Expertise** für komplexe Domänen
* **Mangelnde Erfahrung** mit testgetriebenen Ansätzen

**Lösungsansätze:**
* **Spezialisierte <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Tester**</a>** sollen beim Testentwurf unterstützen
* **Geeignete Weiterbildungsmaßnahmen** implementieren
* **Story-Refinement** durch erfahrene Team-Coaches

## Negative und nicht-funktionale Testaspekte

### Erweiterte Testperspektiven

> **Testverantwortung:** Aus dem Dialog mit Stakeholdern resultieren typischerweise <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a>, die das Verhalten der Software "im Normalfall" überprüfen.

**Es gehört zu den Aufgaben des Teams und insbesondere der <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Tester**</a>, <a href="./Glossar.md#negativtest" title="→ Glossar öffnen" class="glossary-term">**Negativtests**</a> und <a href="./Glossar.md#nicht-funktionaler-test" title="→ Glossar öffnen" class="glossary-term">**nicht-funktionale Tests**</a> als zusätzliche <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> zu entwerfen, zu ergänzen und durchzuführen.**

### Systematische Kriterienerweiterung

**<a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Tester**</a> sollen die <a href="./Glossar.md#akzeptanzkriterien" title="→ Glossar öffnen" class="glossary-term">**Akzeptanzkriterien**</a> kritisch hinterfragen und wo erforderlich Verbesserungen oder Ergänzungen einbringen:**

| Testtyp | Fokus | Beispiel aus "Pixel Leap" |
|---------|-------|---------------------------|
| **<a href="./Glossar.md#negativtest" title="→ Glossar öffnen" class="glossary-term">**Negativtests**</a>** | Fehlverhalten und Grenzfälle | Sprung-Taste in schneller Folge drücken |
| **<a href="./Glossar.md#performanz" title="→ Glossar öffnen" class="glossary-term">**Performance-Tests**</a>** | Antwortzeiten und Durchsatz | Konstante 60 FPS bei 100 NPCs |
| **<a href="./Glossar.md#gebrauchstauglichkeit" title="→ Glossar öffnen" class="glossary-term">**Usability-Tests**</a>** | Benutzerfreundlichkeit | Lernkurve für neue Spieler |
| **<a href="./Glossar.md#sicherheit-security" title="→ Glossar öffnen" class="glossary-term">**Security-Tests**</a>** | Schutz vor Manipulationen | Cheat-Engine-Resistenz |

*Beispiel aus "Pixel Leap":* Während Stakeholder nur "normale" Sprünge testeten, ergänzten Tester Szenarien wie "Sprung während Sturz", "Mehrfach-Sprung-Input" und "Sprung bei 0% Akku" für umfassende Abdeckung.*

## Fazit

**Die kollaborative Anforderungsermittlung in agilen Kontexten transformiert traditionelle, dokumentenzentrierte Ansätze zu lebendigen, dialogbasierten Prozessen.** Durch die systematische Integration von <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a>, INVEST-Kriterien und <a href="./Glossar.md#abnahmetestgetriebene-entwicklung" title="→ Glossar öffnen" class="glossary-term">**abnahmetestgetriebener Entwicklung**</a> wird eine höhere Anforderungsqualität bei gleichzeitig verbesserter Stakeholder-Einbindung erreicht.

**Das 3C-Konzept schafft einen strukturierten Rahmen für die Evolution von abstrakten Ideen zu testbaren, implementierbaren <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a>.** Die frühzeitige Integration der Testperspektive durch ATDD minimiert Missverständnisse und reduziert kostspielige Nacharbeiten.

**Erfolgreiche agile Teams erkennen, dass hochwertige <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> das Ergebnis kontinuierlicher Zusammenarbeit sind, nicht das Produkt isolierter Analysephasen.** Die Investition in diese kollaborativen Praktiken zahlt sich durch verbesserte Produktqualität, reduzierte Entwicklungsrisiken und erhöhte Stakeholder-Zufriedenheit nachhaltig aus.