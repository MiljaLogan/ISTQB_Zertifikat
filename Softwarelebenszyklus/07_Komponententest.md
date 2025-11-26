# Komponententest: Elementare Qualitätssicherung auf Codeebene

## Grundlagen der komponentenorientierten Testung

**Im <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententest**</a> werden die auf niedrigster Architekturebene angesiedelten Softwarebausteine einer systematischen Prüfung unterzogen.** Diese kleinsten Softwareeinheiten werden je nach eingesetzter Programmiersprache unterschiedlich bezeichnet - als Module, Units oder im Fall objektorientierter Programmierung als Klassen, wodurch sich auch die alternativen Begriffe Modultest, Unit Test oder Klassentest ergeben.

> **Abstraktionsprinzip:** Unabhängig von der verwendeten Programmiersprache wird allgemein von <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponente**</a> oder Softwarebaustein gesprochen, wodurch der Test als <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententest**</a> bezeichnet wird.

**Diese sprachunabhängige Betrachtungsweise ermöglicht einheitliche Testkonzepte und -strategien über verschiedene Technologie-Stacks hinweg.**

## Testbasis und Informationsquellen

### Spezifikationsbasierte Grundlagen

**Als <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> können komponentenspezifische <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> und das Softwaredesign der <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponente**</a> (Komponentenspezifikation) herangezogen werden.** Diese dokumentationsbasierten Quellen definieren das erwartete Verhalten und die funktionalen Charakteristika.

### Code-basierte Erweiterungen

**Zur Ermittlung von <a href="./Glossar.md#white-box-test" title="→ Glossar öffnen" class="glossary-term">**White-Box-Testfällen**</a> oder zur Gewinnung von Aussagen zur <a href="./Glossar.md#ueberdeckung" title="→ Glossar öffnen" class="glossary-term">**Code-Überdeckung**</a> kann zusätzlich der Sourcecode einer <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponente**</a> analysiert und als <a href="./Glossar.md#testbasis" title="→ Glossar öffnen" class="glossary-term">**Testbasis**</a> verwendet werden.** Die Bewertung der korrekten Reaktion auf <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> erfolgt jedoch weiterhin anhand der Design- und Anforderungsdokumente.

*Beispiel aus "Pixel Leap":* Die Sprungphysik-Komponente wurde sowohl gegen die Gameplay-Spezifikation ("Sprung muss 3 Einheiten hoch sein") als auch durch Code-Analyse der Physik-Algorithmen getestet.*

## Testobjekte und deren Vielfalt

### Klassische Programmbausteine

**Typische <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekte**</a> umfassen Programmmodule, Units und Klassen.** Diese stellen die traditionellen, entwicklernahen Softwareeinheiten dar, die direkt aus der Implementierung hervorgehen.

### Erweiterte Testobjekt-Kategorien

**Moderne Softwareentwicklung erweitert das Spektrum möglicher <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekte**</a> erheblich:**

| Kategorie | Beispiele | Testfokus |
|-----------|-----------|-----------|
| **Skripte** | Shell-Skripte, Batch-Dateien | Ausführungslogik und Fehlerbehandlung |
| **Datenbank-Komponenten** | Stored Procedures, Trigger | SQL-Logik und Performance |
| **Konfigurationsdaten** | JSON/XML-Files, Properties | Strukturelle Validität und Wertebereiche |
| **Migrations-Prozeduren** | Schema-Updates, Datenkonvertierungen | Datenintegrität und Rückwärtskompatibilität |

*Beispiel aus "Pixel Leap":* Neben C#-Klassen wurden auch Unity-ScriptableObjects für Gameplay-Konfiguration, JSON-Dateien für Level-Definitionen und SQL-Skripte für Highscore-Verwaltung getestet.*

## Isolation und Fehlerlokalisation

### Fundamentalprinzip der Isolation

> **Isolation-Prinzip:** Kennzeichnend für den <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententest**</a> ist die Überprüfung einzelner Softwarebausteine isoliert von anderen Systembausteinen.

**Die Isolierung verfolgt primär den Zweck, komponentenexterne Einflüsse beim <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> auszuschließen.** Wird eine <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkung**</a> aufgedeckt, lässt sich deren Ursache eindeutig der getesteten <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponente**</a> zuordnen.

### Komponenteninterne vs. -externe Aspekte

**Die zu testende <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponente**</a> kann selbst aus mehreren Bausteinen zusammengesetzt sein - entscheidend ist die Prüfung komponenteninterner Aspekte ohne Berücksichtigung der Wechselwirkung mit Nachbarkomponenten.** Letzteres ist Gegenstand des <a href="./Glossar.md#komponentenintegrationstest" title="→ Glossar öffnen" class="glossary-term">**Komponentenintegrationstests**</a>.

### Entwicklungsnahe Charakteristika

**Die <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekte**</a> stammen direkt "von der Festplatte" der Programmierer, wodurch sehr entwicklungsnah gearbeitet wird und umfangreiche Programmierkenntnisse erforderlich sind.**

## Praktisches Beispiel: Preisberechnung

### Spezifikation und Implementierung

*Beispiel: Bei der Fahrzeugpreisberechnung ergibt sich der Preis laut Spezifikation wie folgt:*

**Berechnungslogik:**
- Ausgang: Grundpreis (baseprice) abzüglich Händlerrabatt (discount)
- Addition: Sondermodellaufschlag (specialprice) und Zusatzausstattung (extraprice)
- Rabattierung: 10% bei 3+ Zusatzausstattungen, 15% bei 5+ Zusatzausstattungen
- Einschränkung: Händler- und Zubehörrabatt nicht kombinierbar

**Beispiel-Implementierung:**
```python
def calculate_price(baseprice: float, specialprice: float, extraprice: float, extras: int, discount: float) -> float:
    """
    Berechnet den Gesamtpreis eines Fahrzeugs basierend auf verschiedenen Faktoren.
    
    Args:
        baseprice: Grundpreis des Fahrzeugs
        specialprice: Aufpreis für Sondermodell
        extraprice: Gesamtpreis aller Zusatzausstattungen
        extras: Anzahl der gewählten Zusatzausstattungen
        discount: Händlerrabatt in Prozent
    
    Returns:
        Berechneter Gesamtpreis
    """
    if extras >= 3:
        addon_discount = 10
        if extras >= 5:
            addon_discount = 15
    else:
        addon_discount = 0
    
    if discount > addon_discount:
        addon_discount = discount
    
    return baseprice * (100 - discount) / 100.0 + specialprice + extraprice * (100 - addon_discount) / 100.0
```

### Testtreiber-Entwicklung

**Zur Testung dieser Preisberechnung ist ein <a href="./Glossar.md#treiber" title="→ Glossar öffnen" class="glossary-term">**Testtreiber**</a> erforderlich - ein Programm, das Schnittstellenaufrufe absetzt und die Reaktion des <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekts**</a> entgegennimmt.**

**Beispiel-Testtreiber:**
```python
def test_calculate_price() -> bool:
    """
    Testtreiber für die Preisberechnungsfunktion.
    
    Returns:
        True wenn alle Tests bestanden, False bei Fehlern
    """
    test_results = []
    
    # Testfall 01: Standardfall
    price = calculate_price(10000.00, 2000.00, 1000.00, 3, 0)
    test_results.append(abs(price - 12900.00) < 0.01)
    
    # Testfall 02: Hohe Ausstattungszahl
    price = calculate_price(25500.00, 3450.00, 6000.00, 6, 0)
    test_results.append(abs(price - 34050.00) < 0.01)
    
    return all(test_results)
```

### Entwicklertest-Problematik

**Die Notwendigkeit von Programmier-Know-how führt dazu, dass <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententests**</a> häufig von denjenigen Teammitgliedern durchgeführt werden, die auch die <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponente**</a> selbst entwickelt haben.** Dies wird als "Entwicklertest" bezeichnet, obwohl ein <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententest**</a> gemeint ist.

> **Wichtige Unterscheidung:** <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententest**</a> ist nicht <a href="./Glossar.md#debugging" title="→ Glossar öffnen" class="glossary-term">**Debugging**</a>. Debugging bedeutet Fehlerbeseitigung, während <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> der systematische Ansatz zur Aufdeckung von <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> ist.

## Framework-basierte Testautomatisierung

### Vorteile von Test-Frameworks

**Der Einsatz von Komponententest-Frameworks reduziert den Aufwand für die Programmierung von <a href="./Glossar.md#treiber" title="→ Glossar öffnen" class="glossary-term">**Testtreibern**</a> erheblich und führt zu einer Vereinheitlichung der Komponententest-Architektur im Projekt.**

**Etablierte Frameworks umfassen:**
* **JUnit** für Java
* **NUnit** für .NET
* **CppUnit/Google Test** für C++
* **Jest** für JavaScript
* **pytest** für Python

### Framework-Vorteile

**Einheitliche <a href="./Glossar.md#treiber" title="→ Glossar öffnen" class="glossary-term">**Testtreiber**</a> ermöglichen:**
* **Teamweite Kollaboration** - Auch ohne Detailkenntnisse der einzelnen <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponente**</a>
* **Standardisierte Bedienung** - Kommandozeilenschnittstellen und einheitliche APIs
* **Erweiterte Funktionalitäten** - Komfortable Testdatenhandhabung und Protokollierung
* **Übergreifende Auswertung** - Komponentenübergreifende Testanalyse durch einheitliche Datenstrukturen

*Beispiel aus "Pixel Leap":* Die Verwendung des Unity Test Framework ermöglichte es allen Teammitgliedern, Gameplay-Tests zu schreiben, ohne tiefe Kenntnisse der jeweiligen Komponenten-Implementierungen.*

## Testziele im Komponententest

### Funktionalitätstests

**Die wichtigste Aufgabe des <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententests**</a> ist die Sicherstellung, dass das <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> die spezifizierte Funktionalität korrekt und vollständig realisiert.** Funktionalität entspricht dabei dem Ein-/Ausgabeverhalten des <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekts**</a>.

**Zur Prüfung von Korrektheit und Vollständigkeit wird die <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponente**</a> verschiedenen <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> unterzogen, wobei jeder <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> eine bestimmte Ein-/Ausgabekombination (Teilfunktionalität) abdeckt.**

### Robustheitstests

**Jede Softwarekomponente muss im Gesamtsystem mit Nachbarkomponenten zusammenarbeiten, wobei auch fehlerhafte Ansprache möglich ist.** Der <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Test**</a> auf Robustheit stellt sicher, dass die <a href="./Glossar.md#komponente" title="→ Glossar öffnen" class="glossary-term">**Komponente**</a> bei falscher Verwendung nicht das Gesamtsystem zum Absturz bringt.

> **<a href="./Glossar.md#negativtest" title="→ Glossar öffner" class="glossary-term">**Negativtest**</a>-Prinzip:** Als Testeingaben werden Methodenaufrufe, Daten und Sonderfälle verwendet, die laut Spezifikation unzulässig oder nicht vorgesehen sind.

**Negativtest-Beispiele:**
```python
import pytest
from enum import Enum

class ErrorCode(Enum):
    INVALID_PRICE = "INVALID_PRICE"
    INVALID_ARGUMENT = "INVALID_ARGUMENT"

def test_negative_cases():
    """Negative Testfälle für Robustheitsprüfung."""
    
    # Negativer Preis
    with pytest.raises(ValueError, match="INVALID_PRICE"):
        calculate_price(-1000.00, 0.00, 0.00, 0, 0)
    
    # Falscher Datentyp
    with pytest.raises(TypeError, match="INVALID_ARGUMENT"):
        calculate_price("abc", 0.00, 0.00, 0, 0)
    
    # Extreme Werte
    with pytest.raises(ValueError):
        calculate_price(0, 0, 0, -5, 0)  # Negative extras
```

### Charakteristika von Negativtests

**Interessante Aspekte der <a href="./Glossar.md#negativtest" title="→ Glossar öffnen" class="glossary-term">**Negativtests**</a>:**
* **Quantitative Dominanz** - Oft mehr <a href="./Glossar.md#negativtest" title="→ Glossar öffnen" class="glossary-term">**Negativtests**</a> als Positivtests, da falsche Eingaben nahezu unbegrenzt sind
* **Erweiterte Testtreiber** - Auswertung von Ausnahmebehandlung erfordert zusätzliche Funktionalität
* **Implementierungsaufwand** - Oft mehr als 50% des Codes dient der Behandlung von Ausnahmesituationen
* **Qualität vs. Aufwand** - Robustheit hat ihren Preis in Entwicklung und Wartung

*Beispiel aus "Pixel Leap":* Die Input-Handler-Komponente wurde mit extremen Eingabesequenzen getestet (1000 Tastendrücke/Sekunde, simultane widersprüchliche Inputs), um Robustheit bei gestörter Hardware zu gewährleisten.*

## Nicht-funktionale Qualitätsmerkmale

### Effizienz-Tests

**Die <a href="./Glossar.md#performanz" title="→ Glossar öffnen" class="glossary-term">**Effizienz**</a> beschreibt den wirtschaftlichen Umgang mit verfügbaren Rechnerressourcen.** Teilaspekte umfassen Speicherplatzverbrauch und benötigte Rechenzeit komponenteninterner Funktionen.

**Effizienz-Messungen sind besonders relevant:**
* **Eingebettete Systeme** - Limitierte Hardware-Ressourcen
* **Echtzeitsysteme** - Garantierte Zeitschranken erforderlich
* **Performance-kritische Komponenten** - Explizite Anforderungsvorgaben

**Im Unterschied zu anderen <a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">**Testzielen**</a> kann Effizienz anhand geeigneter Teilkriterien (Speicherverbrauch in Kilobyte, Antwortzeit in Millisekunden) exakt gemessen werden.**

### Wartbarkeitstests

**<a href="./Glossar.md#wartbarkeit" title="→ Glossar öffnen" class="glossary-term">**Wartbarkeit**</a> umfasst alle Eigenschaften, die beeinflussen, wie leicht oder schwer Programm-Änderungen und -Weiterentwicklungen fallen.** Entscheidend ist der Aufwand zum Verstehen des vorhandenen Programms und dessen Kontexts.

**Prüfaspekte der Wartbarkeit:**
* **Codestruktur** - Logische Organisation und Modularität
* **Dokumentation** - Kommentierung und Aktualität der Spezifikationen  
* **Verständlichkeit** - Selbsterklärende Variablennamen und Konstanten
* **Konsistenz** - Einheitliche Programmierstandards

**Beispiel schlechter Wartbarkeit:**
```python
# Problematischer Code ohne Kommentare und mit Magic Numbers
def calculate_discount(extras):
    if extras >= 3:
        return 10  # Was bedeutet 10? Prozent? Konstante?
    return 0
```

**Wartbarkeits-Prüfungen erfordern <a href="./Glossar.md#statischer-test" title="→ Glossar öffnen" class="glossary-term">**statische Tests**</a> und <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a>, da sie nicht durch dynamische Testausführung überprüfbar sind.**

## Teststrategien und -ansätze

### White-Box-Test-Dominanz

**Der entwicklungsnahe Charakter des <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententests**</a> mit Sourcecode-Zugang macht ihn zur Domäne des <a href="./Glossar.md#white-box-test" title="→ Glossar öffnen" class="glossary-term">**White-Box-Tests**</a>.**

**<a href="./Glossar.md#white-box-test" title="→ Glossar öffnen" class="glossary-term">**White-Box**</a>-Vorteile:**
* **Strukturbasierte Testfallerstellung** - Nutzung komponenteninterner Programmstrukturen
* **Laufzeit-Beobachtung** - Debugging-Tools zur Variablenüberwachung
* **Zustandsmanipulation** - Gezielte Auslösung von Ausnahmesituationen
* **Vollständigere Abdeckung** - Erkennung nicht-spezifizierter Code-Pfade

**Code-Analyse-Beispiel:**
```python
if discount > addon_discount:
    addon_discount = discount
```
*Diese Code-Stelle ist nicht in der Spezifikation dokumentiert, kann aber durch Code-Analyse erkannt und getestet werden.*

### Black-Box-Alternative

**In der Praxis wird <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententest**</a> häufig auch als <a href="./Glossar.md#black-box-test" title="→ Glossar öffnen" class="glossary-term">**Black-Box-Test**</a> durchgeführt, ohne Nutzung der inneren Struktur für die Testfallauswahl.**

**Gründe für <a href="./Glossar.md#black-box-test" title="→ Glossar öffnen" class="glossary-term">**Black-Box-Tests**</a>:**
* **Skalierbarkeit** - Hunderte/Tausende elementarer Komponenten
* **Praktikabilität** - Code-Einblick nur bei ausgewählten Komponenten machbar
* **Integrations-Realität** - Zusammengesetzte Bausteine als testbare Einheiten
* **Aufwands-Optimierung** - Vertretbarer Analyseaufwand

## Test-First-Entwicklung

### Paradigmenwechsel zum Test-First-Ansatz

**Ein zunehmend verbreiteter Ansatz ist "Test-First" - die Erstellung und Automatisierung von <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> vor der eigentlichen Programmierung.** Diese <a href="./Glossar.md#testgetriebene-entwicklung" title="→ Glossar öffnen" class="glossary-term">**testgetriebene Entwicklung**</a> (TDD) folgt einem iterativen Zyklus.

### TDD-Prozess

**Der Test-First-Zyklus umfasst:**
1. **Test schreiben** - Automatisierte <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfälle**</a> für gewünschte Funktionalität
2. **Test ausführen** - Initialer Fehlschlag (da Code noch nicht existiert)
3. **Code implementieren** - Minimale Implementierung zum Test-Bestehen
4. **Refactoring** - Code-Verbesserung bei beibehaltener Funktionalität
5. **Wiederholung** - Zyklus für nächste Funktionalität

### TDD-Vorteile

**Systematische Testverfahren-Nutzung bei TDD bringt zusätzliche Vorteile:**
* **Vollständige Testabdeckung** - Jede Code-Zeile ist getestet
* **Frühe Fehlerprävention** - Probleme werden vor Implementierung erkannt
* **Robustheit by Design** - <a href="./Glossar.md#negativtest" title="→ Glossar öffnen" class="glossary-term">**Negativtests**</a> werden vor Programmierung berücksichtigt
* **Lebende Dokumentation** - <a href="./Glossar.md#test" title="→ Glossar öffnen" class="glossary-term">**Tests**</a> dokumentieren erwartetes Verhalten

*Beispiel aus "Pixel Leap":* Die Kollisionserkennung wurde vollständig TDD-basiert entwickelt - erst Tests für alle Kollisionsszenarien, dann die Implementierung der Physics-Engine-Integration.*

## Fazit

**Der <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententest**</a> bildet das Fundament systematischer Softwarequalitätssicherung durch die Verifikation elementarer Systembausteine in isolierter Umgebung.** Als entwicklungsnächste <a href="./Glossar.md#teststufe" title="→ Glossar öffnen" class="glossary-term">**Teststufe**</a> ermöglicht er präzise Fehlerlokalisierung und effiziente Qualitätskontrolle bereits auf Code-Ebene.

**Die systematische Prüfung von Funktionalität, Robustheit und nicht-funktionalen Qualitätsmerkmalen durch framework-basierte Automatisierung schafft ein solides Qualitätsfundament für nachgelagerte Teststufen.** Moderne Ansätze wie <a href="./Glossar.md#testgetriebene-entwicklung" title="→ Glossar öffnen" class="glossary-term">**testgetriebene Entwicklung**</a> verstärken diese Effekte durch präventive Qualitätssicherung.

**Erfolgreiche <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententests**</a> erfordern sowohl technische Expertise als auch strategisches Verständnis für Testzielprioritäten und Aufwands-Nutzen-Optimierung.** Die Investition in hochwertige Komponententests zahlt sich durch reduzierte Fehlerkosten in späteren Entwicklungsphasen nachhaltig aus.