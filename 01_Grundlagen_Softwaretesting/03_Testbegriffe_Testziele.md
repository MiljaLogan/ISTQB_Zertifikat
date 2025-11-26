# Testbegriff und Testziele

## Testen versus Debugging - Eine wichtige Abgrenzung

### Klare Aufgabentrennung

**<a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> und <a href="./Glossar.md#debugging" title="→ Glossar öffnen" class="glossary-term">**Debugging**</a> werden häufig verwechselt, obwohl es sich um völlig unterschiedliche Aktivitäten handelt:**

- **<a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">Testen</a>** zielt darauf ab, <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> gezielt aufzudecken
- **<a href="./Glossar.md#debugging" title="→ Glossar öffnen" class="glossary-term">Debugging</a>** lokalisiert und behebt die zugrundeliegenden <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> im Code

> Während <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> Probleme sichtbar macht, löst <a href="./Glossar.md#debugging" title="→ Glossar öffnen" class="glossary-term">**Debugging**</a> diese im Quellcode.

**Das <a href="./Glossar.md#debugging" title="→ Glossar öffnen" class="glossary-term">**Debugging**</a> obliegt dem jeweiligen Entwicklungsteam**, das für die betroffene Codekomponente verantwortlich ist. Erst wenn eine <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkung**</a> durch <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> identifiziert wurde, kann die Fehlersuche und -behebung beginnen.

### Fehlernachtests - Kontrolle der Korrekturen

**Nach der Fehlerbehebung müssen <a href="./Glossar.md#fehlernachtest" title="→ Glossar öffnen" class="glossary-term">**Fehlernachtests**</a> durchgeführt werden**, um zu <a href="./Glossar.md#verifizierung" title="→ Glossar öffnen" class="glossary-term">**verifizieren**</a>, dass die Korrekturmaßnahmen erfolgreich waren. Diese <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> führen häufig dieselben Personen durch, die auch die ursprünglichen Fehler entdeckt haben.

Bei automatisierten <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> ist der <a href="./Glossar.md#fehlernachtest" title="→ Glossar öffnen" class="glossary-term">**Fehlernachtest**</a> besonders einfach: Der zuvor <a href="./Glossar.md#fehlgeschlagen" title="→ Glossar öffnen" class="glossary-term">**fehlgeschlagene**</a> <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> sollte nun erfolgreich durchlaufen.

### Seiteneffekte und Regressionen

**Fehlerbehebungen können unbeabsichtigt neue Probleme verursachen.** Solche Seiteneffekte manifestieren sich oft bei völlig anderen Eingabekonstellationen und erfordern zusätzliche <a href="./Glossar.md#regressionstest" title="→ Glossar öffnen" class="glossary-term">**Regressionstests**</a>, die über den ursprünglich fehlgeschlagenen <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> hinausgehen.

## Vielfältige Testziele

### Qualitätsbewertung und Vertrauen schaffen

**<a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">Testen</a> verfolgt mehrere strategische <a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">**Testziele**</a>:**

* **Qualitative Bewertung** von Arbeitsergebnissen wie Spezifikationen, <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a> und Programmcode
* **Vollständigkeitsnachweis** der <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungsumsetzung**</a>
* **Vertrauensbildung** bei Stakeholdern durch fundierte <a href="./Glossar.md#qualitaet" title="→ Glossar öffnen" class="glossary-term">**Qualitätsinformationen**</a>

### Risikominimierung und Compliance

* **<a href="./Glossar.md#risiko" title="→ Glossar öffnen" class="glossary-term">Risikoreduktion</a>** durch Aufdeckung und Behebung von <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a>
* **<a href="./Glossar.md#konformitaet" title="→ Glossar öffnen" class="glossary-term">Compliance</a>-Nachweis** für vertragliche, rechtliche oder regulatorische <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a>
* **<a href="./Glossar.md#integrationstest" title="→ Glossar öffnen" class="glossary-term">Integrationsentscheidungen</a>** durch Bewertung der Systemteil-<a href="./Glossar.md#qualitaet" title="→ Glossar öffnen" class="glossary-term">**Qualität**</a>

### Technische Zielsetzungen

**<a href="./Glossar.md#ueberdeckung" title="→ Glossar öffnen" class="glossary-term">Überdeckungsmessung</a>:** <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> liefern Informationen darüber, ob geforderte <a href="./Glossar.md#ueberdeckungskriterien" title="→ Glossar öffnen" class="glossary-term">**Überdeckungsziele**</a> erreicht wurden oder zusätzliche <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> benötigt werden.

**Freigabeentscheidungen:** Systematische Bereitstellung von Informationen für fundierte Entscheidungen über Systemfreigaben.

## Kontextabhängige Zielsetzungen

### Variationen nach Entwicklungsmodell und Teststufe

**Die spezifischen <a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">**Testziele**</a> variieren erheblich je nach:**

- **Entwicklungsmodell** (<a href="./Glossar.md#agile-softwareentwicklung" title="→ Glossar öffnen" class="glossary-term">**agil**</a> versus traditionell)
- **<a href="./Glossar.md#teststufe" title="→ Glossar öffnen" class="glossary-term">Teststufe</a>** (<a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponenten-**</a>, <a href="./Glossar.md#systemtest" title="→ Glossar öffnen" class="glossary-term">**System-**</a>, <a href="./Glossar.md#abnahmetest" title="→ Glossar öffnen" class="glossary-term">**Abnahmetest**</a>)
- **Projektkontext** und Stakeholder-Erwartungen

### Beispiele spezifischer Zielsetzungen

**<a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">Komponententests</a>** konzentrieren sich primär auf:
- Maximale <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungsaufdeckung**</a>
- Hohe <a href="./Glossar.md#ueberdeckung" title="→ Glossar öffnen" class="glossary-term">**Codeüberdeckung**</a>
- Frühzeitige <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustandsidentifikation**</a>

**<a href="./Glossar.md#abnahmetest" title="→ Glossar öffnen" class="glossary-term">Abnahmetests</a>** fokussieren auf:
- Nachweis der <a href="./Glossar.md#gebrauchstauglichkeit" title="→ Glossar öffnen" class="glossary-term">**Gebrauchstauglichkeit**</a>
- Erfüllung <a href="./Glossar.md#funktionaler-test" title="→ Glossar öffnen" class="glossary-term">**funktionaler**</a> und <a href="./Glossar.md#nicht-funktionaler-test" title="→ Glossar öffnen" class="glossary-term">**nicht-funktionaler Anforderungen**</a>  
- <a href="./Glossar.md#risikobewertung" title="→ Glossar öffnen" class="glossary-term">**Risikobewertung**</a> für Freigabeentscheidungen

## Systematik der Testbezeichnungen

### Kategorien der Testbenennung

**Die Vielfalt der Testbegriffe lässt sich systematisch ordnen:**

| Kategorie | Beschreibung | Beispiele |
|-----------|--------------|-----------|
| **<a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">Testziel</a>** | Benennung nach Testzweck | Lasttest, Sicherheitstest |
| **<a href="./Glossar.md#testverfahren" title="→ Glossar öffnen" class="glossary-term">Testmethode</a>** | Benennung nach Verfahren | <a href="./Glossar.md#zustandsuebergangstest" title="→ Glossar öffnen" class="glossary-term">**Zustandsbasierter Test**</a> |
| **<a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">Testobjekt</a>** | Benennung nach Prüfgegenstand | GUI-Test, Datenbanktest |
| **<a href="./Glossar.md#teststufe" title="→ Glossar öffnen" class="glossary-term">Teststufe</a>** | Benennung nach Entwicklungsphase | <a href="./Glossar.md#systemtest" title="→ Glossar öffnen" class="glossary-term">**Systemtest**</a>, <a href="./Glossar.md#integrationstest" title="→ Glossar öffnen" class="glossary-term">**Integrationstest**</a> |
| **<a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">Testperson</a>** | Benennung nach Durchführenden | Entwicklertest, Anwendertest |
| **Testumfang** | Benennung nach Abdeckungsgrad | Partieller <a href="./Glossar.md#regressionstest" title="→ Glossar öffnen" class="glossary-term">**Regressionstest**</a> |

### Perspektivenwechsel statt neue Testarten

**Viele scheinbar unterschiedliche <a href="./Glossar.md#testart" title="→ Glossar öffnen" class="glossary-term">**Testarten**</a> sind lediglich verschiedene Betrachtungsweisen derselben Testaktivitäten.** Die Benennung erfolgt je nach Fokus der jeweiligen Diskussion oder Dokumentation.

## Testbasis als Fundament

**Die <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> bildet das Referenzsystem für alle Testaktivitäten.** Sie umfasst sämtliche Informationen, die zur Bestimmung korrekten Systemverhaltens herangezogen werden:

- <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungsspezifikationen**</a>
- <a href="./Glossar.md#user-story" title="→ Glossar öffnen" class="glossary-term">**User Stories**</a>  
- Systemdokumentation
- Standards und Richtlinien

> Ohne klare <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> ist keine objektive Fehlerbewertung möglich.

## Fazit

**Erfolgreiches <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> erfordert klare <a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">**Zieldefinition**</a> und systematisches Vorgehen.** Die Unterscheidung zwischen <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> und <a href="./Glossar.md#debugging" title="→ Glossar öffnen" class="glossary-term">**Debugging**</a>, das Verständnis für kontextabhängige Zielsetzungen und die strukturierte Betrachtung verschiedener Testaspekte bilden das Fundament professioneller <a href="./Glossar.md#qualitaetssicherung" title="→ Glossar öffnen" class="glossary-term">**Qualitätssicherung**</a>.

**Die Vielfalt der Testbegriffe sollte nicht verwirren, sondern als Werkzeugkasten für präzise Kommunikation über Testaktivitäten verstanden werden.**