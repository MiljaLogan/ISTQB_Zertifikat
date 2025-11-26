### Methodisches Vorgehen bei Reviews

<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> nutzen die menschliche Analyse- und Denkfähigkeit zur systematischen Bewertung komplexer Sachverhalte in Entwicklungsartefakten. Der Erfolg dieser <a href="./Glossar.md#statischer-test" title="→ Glossar öffnen" class="glossary-term">**statischen Testverfahren**</a> hängt maßgeblich von der methodischen Herangehensweise und der angemessenen Auswahl des Reviewverfahrens ab.

### Grundprinzipien der Review-Durchführung

#### Kognitive Analyseprozesse

Die Effektivität von <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> basiert auf intensiven kognitiven Prozessen:

* **Intensives Lesen**: Systematische Durcharbeitung der Dokumente
* **Inhaltliches Nachvollziehen**: Verstehen der fachlichen Zusammenhänge
* **Semantische Analyse**: Bewertung der Bedeutungsebene von Aussagen
* **Logische Verknüpfung**: Prüfung der Konsistenz zwischen verschiedenen Dokumentteilen

> <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> sind oft die einzige Möglichkeit, die Semantik von Dokumenten und Arbeitsergebnissen zu überprüfen, da automatisierte Tools diese Bedeutungsebene nicht erfassen können.

*Beispiel:* Bei der Bewertung von Pixel Leap's Sprungmechanik-Spezifikation müssen Reviewer verstehen, wie sich verschiedene Physikparameter auf das Spielerlebnis auswirken und ob die mathematischen Formeln das gewünschte Spielgefühl erzeugen.

#### Voraussetzungen für erfolgreiche Reviews

**Kritische Erfolgsfaktoren:**

* **Fachliche Kompetenz**: Reviewer müssen das Fachgebiet verstehen
* **Dokumentenverständnis**: Struktur und Inhalt müssen nachvollziehbar sein
* **Zeitliche Ressourcen**: Ausreichend Zeit für gründliche Analyse
* **Methodische Kenntnisse**: Vertrautheit mit <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Techniken

### Terminologische Abgrenzungen

#### Begriffsvielfalt und Verwendung

Der Begriff "<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>" wird in verschiedenen Kontexten verwendet:

| Verwendungskontext | Bedeutung | Abgrenzung |
|-------------------|-----------|------------|
| **Spezifisches Verfahren** | Konkrete <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Methode | Eine von mehreren Techniken |
| **Oberbegriff** | Alle manuellen <a href="./Glossar.md#statischer-test" title="→ Glossar öffnen" class="glossary-term">**statischen Tests**</a> | Sammelbegriff für Verfahren |
| **Prozessbezeichnung** | Gesamter Bewertungsablauf | Methodischer Rahmen |

#### Inspektion als formalisierte Variante

<a href="./Glossar.md#inspektion" title="→ Glossar öffnen" class="glossary-term">**Inspektionen**</a> stellen eine besonders strukturierte Form von <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> dar:

* **Formale Durchführung**: Strikt definierte Prozessschritte
* **<a href="./Glossar.md#metrik" title="→ Glossar öffnen" class="glossary-term">Metriken-Sammlung</a>**: Quantitative Bewertungsdaten
* **Regelbasiertes Vorgehen**: Standardisierte Prüfkriterien
* **Dokumentierte Ergebnisse**: Nachvollziehbare Bewertungsresultate

*Beispiel:* Eine <a href="./Glossar.md#inspektion" title="→ Glossar öffnen" class="glossary-term">**Inspektion**</a> von Pixel Leap's Sicherheitskonzept würde definierte Checklisten verwenden und <a href="./Glossar.md#metrik" title="→ Glossar öffnen" class="glossary-term">**Metriken**</a> wie "Anzahl identifizierter Sicherheitslücken pro Seite" erfassen.

### Spektrum der Review-Formalität

#### Informelle Reviews

<a href="./Glossar.md#informelles-review" title="→ Glossar öffnen" class="glossary-term">**Informelle Reviews**</a> zeichnen sich durch Flexibilität und geringen Overhead aus:

**Charakteristika:**
* **Kein definierter Prozess**: Freie Gestaltung des Ablaufs
* **Flexible Ergebnisdokumentation**: Anpassbare Berichterstattung
* **Spontane Durchführung**: Bedarfsorientierte Initiierung
* **Geringe Ressourcenanforderungen**: Minimaler organisatorischer Aufwand

**Anwendungsgebiete:**
* Frühe Entwicklungsphasen
* Schnelle Qualitätsprüfungen
* Peer-to-Peer-Bewertungen
* Explorative Analysen

#### Formale Reviews

<a href="./Glossar.md#formales-review" title="→ Glossar öffnen" class="glossary-term">**Formale Reviews**</a> bieten strukturierte und nachvollziehbare Bewertungsprozesse:

**Strukturelemente:**
* **Definierte Rollen**: Klare Verantwortlichkeiten der Beteiligten
* **Standardisierte Prozesse**: Einheitliche Durchführungsschritte
* **Dokumentierte Ergebnisse**: Nachvollziehbare Bewertungsresultate
* **<a href="./Glossar.md#qualitaetssicherung" title="→ Glossar öffnen" class="glossary-term">Qualitätssicherung</a>**: Kontrollierte Verfahrensabläufe

### Einflussfaktoren auf die Review-Auswahl

#### Entwicklungsmodell-spezifische Faktoren

Das gewählte <a href="./Glossar.md#softwareentwicklungslebenszyklus" title="→ Glossar öffnen" class="glossary-term">**Softwareentwicklungslebenszyklus-Modell**</a> bestimmt <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Gelegenheiten:

* **<a href="./Glossar.md#sequenzielles-entwicklungsmodell" title="→ Glossar öffnen" class="glossary-term">Sequenzielle Modelle</a>**: Meilenstein-basierte <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a>
* **<a href="./Glossar.md#iteratives-entwicklungsmodell" title="→ Glossar öffnen" class="glossary-term">Iterative Modelle</a>**: Zyklische Bewertungen
* **<a href="./Glossar.md#agile-softwareentwicklung" title="→ Glossar öffnen" class="glossary-term">Agile Ansätze</a>**: Kontinuierliche <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a>

*Beispiel:* In einem agilen Pixel Leap-Projekt würden Sprint-<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> der <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a> alle zwei Wochen stattfinden, während bei einem Wasserfallmodell umfassende Architektur-<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> vor der Implementierungsphase durchgeführt würden.

#### Prozessreife und Dokumentenqualität

Die <a href="./Glossar.md#reife" title="→ Glossar öffnen" class="glossary-term">**Reife**</a> des Entwicklungsprozesses beeinflusst die <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Strategie:

| Reifegrad | Dokumentenqualität | Empfohlenes Vorgehen |
|-----------|-------------------|---------------------|
| **Niedrig** | Unstrukturiert, lückenhaft | <a href="./Glossar.md#informelles-review" title="→ Glossar öffnen" class="glossary-term">**Informelle Reviews**</a>, Coaching |
| **Mittel** | Teilweise standardisiert | Strukturierte <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> |
| **Hoch** | Konsistent, vollständig | <a href="./Glossar.md#formales-review" title="→ Glossar öffnen" class="glossary-term">**Formale Reviews**</a>, <a href="./Glossar.md#inspektion" title="→ Glossar öffnen" class="glossary-term">**Inspektionen**</a> |

#### Komplexitätsbasierte Bewertung

Die Komplexität der zu prüfenden Arbeitsergebnisse bestimmt den erforderlichen Formalisierungsgrad:

**Hochkomplexe Dokumente erfordern:**
* Strukturierte Herangehensweise
* Mehrere Reviewer mit verschiedenen Expertisen
* Systematische Prüfkriterien
* Dokumentierte Bewertungsergebnisse

*Beispiel:* Die Architekturspezifikation für Pixel Leap's Multiplayer-Infrastruktur würde aufgrund ihrer Komplexität eine <a href="./Glossar.md#formales-review" title="→ Glossar öffnen" class="glossary-term">**formale Review**</a> mit Netzwerk-, Sicherheits- und Performance-Experten erfordern.

#### Regulatorische Anforderungen

Gesetzliche und regulatorische Vorgaben können <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Verfahren vorschreiben:

* **<a href="./Glossar.md#audit" title="→ Glossar öffnen" class="glossary-term">Audit</a>-Nachweise**: Dokumentierte Prüfpfade erforderlich
* **Compliance-Standards**: Branchenspezifische Anforderungen
* **Zertifizierungsverfahren**: Externe Bewertungsstandards
* **Rechtliche Dokumentation**: Nachweisbare <a href="./Glossar.md#qualitaetssicherung" title="→ Glossar öffnen" class="glossary-term">**Qualitätssicherung**</a>

### Zielorientierte Review-Auswahl

#### Primäre Review-Ziele

Die Zielsetzung bestimmt maßgeblich die Wahl des <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Verfahrens:

**Fehlerfindung:**
* Systematische <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustand**</a>-Identifikation
* Strukturierte Prüfkriterien
* Dokumentierte Befunde

**Gemeinsames Verständnis:**
* Kollaborative Diskussion
* Konsensbildung
* Wissenstransfer

**Wissensvermittlung:**
* Einarbeitung neuer Teammitglieder
* Kompetenzaufbau
* Mentoring-Aspekte

**Konsensentscheidungen:**
* Diskussionsbasierte Bewertung
* Stakeholder-Alignment
* Entscheidungsfindung

*Beispiel:* Ein <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a> zur Einarbeitung eines neuen Entwicklers in Pixel Leap's Physik-Engine würde als <a href="./Glossar.md#walkthrough" title="→ Glossar öffnen" class="glossary-term">**Walkthrough**</a> durchgeführt, während die Qualitätsprüfung der finalen API-Spezifikation eine strukturierte <a href="./Glossar.md#inspektion" title="→ Glossar öffnen" class="glossary-term">**Inspektion**</a> erfordern würde.

Die methodische Auswahl und Durchführung von <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> ist entscheidend für deren Erfolg und trägt maßgeblich zur <a href="./Glossar.md#qualitaet" title="→ Glossar öffnen" class="glossary-term">**Qualität**</a> der Softwareentwicklung bei.