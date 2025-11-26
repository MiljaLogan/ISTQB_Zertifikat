### Der strukturierte Reviewprozess

Die systematische Durchführung von <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> erfordert einen strukturierten Prozessrahmen, der sowohl Flexibilität als auch methodische Konsistenz gewährleistet. Moderne Standards wie die ISO/IEC 20246 definieren generische Prozessmodelle, die an verschiedene Projektanforderungen angepasst werden können.

### Grundlagen des standardisierten Reviewprozesses

#### Flexibler Strukturrahmen

Der standardisierte <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviewprozess**</a> bietet einen anpassbaren Rahmen für verschiedene Anwendungsszenarien:

* **Strukturierte Basis**: Definierte Aktivitäten und Übergänge
* **Situative Anpassung**: Skalierung von <a href="./Glossar.md#informelles-review" title="→ Glossar öffnen" class="glossary-term">**informell**</a> bis <a href="./Glossar.md#formales-review" title="→ Glossar öffnen" class="glossary-term">**formal**</a>
* **Modulare Durchführung**: Wiederholbare Prozesszyklen
* **Qualitätssicherung**: Konsistente Bewertungsstandards

> Bei <a href="./Glossar.md#formales-review" title="→ Glossar öffnen" class="glossary-term">**formalen Reviews**</a> sind mehrere der definierten Aufgaben für die verschiedenen Aktivitäten zwingend erforderlich, während <a href="./Glossar.md#informelles-review" title="→ Glossar öffnen" class="glossary-term">**informelle Reviews**</a> eine Teilmenge der Aktivitäten nutzen können.

#### Skalierbarkeit für umfangreiche Arbeitsergebnisse

Große oder komplexe Dokumente erfordern eine modulare Herangehensweise:

* **Iterative Durchführung**: Mehrfache Prozesszyklen für Teilbereiche
* **Segmentierte Bewertung**: Aufteilen in bewertbare Einheiten
* **Konsolidierte Ergebnisse**: Zusammenführung der Teilbewertungen
* **Gesamtbewertung**: Holistische Qualitätseinschätzung

*Beispiel:* Die umfassende Architekturspezifikation von Pixel Leap könnte in separate <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> für Rendering-System, Physik-Engine, Audio-Framework und Netzwerk-Infrastruktur aufgeteilt werden.

### Die fünf Kernaktivitäten des Reviewprozesses

#### Schematische Darstellung des Prozessablaufs

```
┌─────────────────────────────────────────────────────────┐
│                    Reviewprozess                        │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────┐    │
│  │                   Planung                       │    │
│  └─────────────────────────────────────────────────┘    │
│                           ↓                             │
│  ┌─────────────────────────────────────────────────┐    │
│  │                Reviewbeginn                     │    │
│  └─────────────────────────────────────────────────┘    │
│                           ↓                             │
│  ┌─────────────────────────────────────────────────┐    │
│  │            Individuelles Review                 │    │
│  └─────────────────────────────────────────────────┘    │
│                           ↓                             │
│  ┌─────────────────────────────────────────────────┐    │
│  │         Kommunikation und Analyse               │    │
│  └─────────────────────────────────────────────────┘    │
│                           ↓                             │
│  ┌─────────────────────────────────────────────────┐    │
│  │       Behebung und Berichterstattung            │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

### Detaillierte Aktivitätsbeschreibung

#### 1. Planung

Die <a href="./Glossar.md#testplanung" title="→ Glossar öffnen" class="glossary-term">**Planungsphase**</a> legt das Fundament für ein erfolgreiches <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>:

**Zentrale Planungsaufgaben:**
* **Zielsetzung definieren**: Klare <a href="./Glossar.md#testziel" title="→ Glossar öffnen" class="glossary-term">**Reviewziele**</a> festlegen
* **Scope abgrenzen**: Umfang und Grenzen des <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a>
* **Ressourcenplanung**: Personal, Zeit und Werkzeuge
* **Kriterien festlegen**: <a href="./Glossar.md#eingangskriterien" title="→ Glossar öffnen" class="glossary-term">**Eingangskriterien**</a> und <a href="./Glossar.md#endekriterien" title="→ Glossar öffnen" class="glossary-term">**Endekriterien**</a>

*Beispiel:* Für ein <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a> der Pixel Leap Multiplayer-Spezifikation würde geplant: Ziel ist die Identifikation von Sicherheitslücken, Scope umfasst Authentifizierung und Datensynchronisation, benötigt werden Netzwerk- und Sicherheitsexperten für 4 Stunden.

#### 2. Reviewbeginn

Die Initiierungsphase bereitet alle Beteiligten auf das <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a> vor:

**Wesentliche Startaktivitäten:**
* **Dokumentenverteilung**: Bereitstellung der zu prüfenden Artefakte
* **Rollenverteilung**: Zuweisung von <a href="./Glossar.md#moderator" title="→ Glossar öffnen" class="glossary-term">**Moderator**</a>, <a href="./Glossar.md#gutachter" title="→ Glossar öffnen" class="glossary-term">**Gutachtern**</a>, <a href="./Glossar.md#protokollant" title="→ Glossar öffnen" class="glossary-term">**Protokollant**</a>
* **Terminkoordination**: Abstimmung der Verfügbarkeiten
* **Werkzeugbereitstellung**: Technische Infrastruktur

#### 3. Individuelles Review

Die eigenständige Bewertungsphase bildet das Herzstück des Prozesses:

**Kernaktivitäten der individuellen Analyse:**
* **Dokumentenstudium**: Intensive Auseinandersetzung mit den Inhalten
* **<a href="./Glossar.md#anomalie" title="→ Glossar öffnen" class="glossary-term">Anomalie</a>-Identifikation**: Systematische Suche nach Problemen
* **Bewertungsdokumentation**: Strukturierte Erfassung der Befunde
* **Vorbereitung der Diskussion**: Aufbereitung für die Kommunikationsphase

*Beispiel:* Jeder <a href="./Glossar.md#gutachter" title="→ Glossar öffnen" class="glossary-term">**Gutachter**</a> analysiert eigenständig die Pixel Leap Audio-API-Spezifikation und dokumentiert identifizierte Inkonsistenzen, fehlende Parameter oder unklare Schnittstellenbeschreibungen.

#### 4. Kommunikation und Analyse

Die kollaborative Bewertungsphase konsolidiert die individuellen Erkenntnisse:

**Zentrale Kommunikationsaktivitäten:**
* **Befundpräsentation**: Vorstellung der identifizierten Probleme
* **Diskussion und Bewertung**: Gemeinsame Analyse der <a href="./Glossar.md#anomalie" title="→ Glossar öffnen" class="glossary-term">**Anomalien**</a>
* **Konsensbildung**: Einigung über Relevanz und <a href="./Glossar.md#prioritaet" title="→ Glossar öffnen" class="glossary-term">**Priorität**</a>
* **Lösungsansätze**: Entwicklung von Verbesserungsvorschlägen

**Strukturierte Diskussionsführung:**
* **<a href="./Glossar.md#moderator" title="→ Glossar öffnen" class="glossary-term">Moderator</a>** leitet die Sitzung
* **<a href="./Glossar.md#protokollant" title="→ Glossar öffnen" class="glossary-term">Protokollant</a>** dokumentiert Ergebnisse
* **<a href="./Glossar.md#gutachter" title="→ Glossar öffnen" class="glossary-term">Gutachter</a>** präsentieren Befunde
* **Autor** erläutert Hintergründe

#### 5. Behebung und Berichterstattung

Die Abschlussphase stellt die Umsetzung und Dokumentation sicher:

**Wesentliche Abschlussaktivitäten:**
* **<a href="./Glossar.md#fehlerbericht" title="→ Glossar öffnen" class="glossary-term">Fehlerbericht</a>-Erstellung**: Dokumentation der identifizierten Probleme
* **Korrekturmaßnahmen**: Umsetzung der vereinbarten Verbesserungen
* **<a href="./Glossar.md#fehlernachtest" title="→ Glossar öffnen" class="glossary-term">Nachprüfung</a>**: Verifikation der Korrekturen
* **Abschlussbericht**: Zusammenfassung der <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Ergebnisse

### Prozessadaptation und Flexibilität

#### Anpassung an Projektanforderungen

Der generische Prozess kann situativ angepasst werden:

| <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Typ | Planungsintensität | Individuelle Phase | Kommunikation | Dokumentation |
|------------|-------------------|-------------------|---------------|---------------|
| **<a href="./Glossar.md#informelles-review" title="→ Glossar öffnen" class="glossary-term">Informell</a>** | Minimal | Flexibel | Ad-hoc | Grundlegend |
| **Strukturiert** | Moderat | Systematisch | Geplant | Detailliert |
| **<a href="./Glossar.md#formales-review" title="→ Glossar öffnen" class="glossary-term">Formal</a>** | Umfassend | Standardisiert | Moderiert | Vollständig |

#### Kontinuierliche Prozessverbesserung

<a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Review**</a>-Prozesse sollten kontinuierlich optimiert werden:

* **<a href="./Glossar.md#metrik" title="→ Glossar öffnen" class="glossary-term">Metriken</a>-Sammlung**: Effektivitäts- und Effizienzmessung
* **<a href="./Glossar.md#retrospektive" title="→ Glossar öffnen" class="glossary-term">Retrospektiven</a>**: Regelmäßige Prozessbewertung
* **Anpassungen**: Iterative Verbesserungen
* **Schulungen**: Kompetenzentwicklung der Beteiligten

*Beispiel:* Nach mehreren Pixel Leap <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviews**</a> könnte das Team feststellen, dass die individuelle Phase zu kurz bemessen war, und die Planungsrichtlinien entsprechend anpassen.

Der strukturierte <a href="./Glossar.md#review" title="→ Glossar öffnen" class="glossary-term">**Reviewprozess**</a> gewährleistet systematische <a href="./Glossar.md#qualitaetssicherung" title="→ Glossar öffnen" class="glossary-term">**Qualitätssicherung**</a> bei gleichzeitiger Flexibilität für verschiedene Projektanforderungen und bildet damit ein wesentliches Element moderner Softwareentwicklung.