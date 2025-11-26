### Äquivalenzklassenbildung

Stellen Sie sich vor, eine Funktion akzeptiert Zahlen von 1 bis 1000. Müssen wirklich alle tausend Werte getestet werden? Die <a href="./Glossar.md#aequivalenzklassenbildung" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklassenbildung**</a> beantwortet diese Frage mit Nein. Das <a href="./Glossar.md#black-box-testverfahren" title="→ Glossar öffnen" class="glossary-term">**Blackbox-Testverfahren**</a> basiert auf einer einfachen Erkenntnis: Viele Eingabewerte führen zum identischen Verhalten des Programms. Warum also jeden einzeln prüfen?

---

#### Die Kernidee

Eingabewerte lassen sich gruppieren. Innerhalb einer Gruppe – der <a href="./Glossar.md#aequivalenzklasse" title="→ Glossar öffnen" class="glossary-term">**Äquivalenzklasse**</a> oder Partition – reagiert das <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> auf jeden Wert gleich. Folglich reicht ein einziger Stellvertreter aus dieser Gruppe. Die Prüfung dieses Repräsentanten gilt für die gesamte Klasse.

*Beispiel: Die Sprungstärke in Pixel Leap liegt zwischen 0 und 100 Prozent. Ob 23%, 47% oder 81% – die Physik-Engine verarbeitet alle gleich. Ein Test mit 50% deckt die gesamte Klasse ab.*

---

#### Zwei Kategorien von Klassen

Neben erlaubten Eingaben existieren auch unerlaubte. Beide verdienen Beachtung.

##### Gültige Klassen

Hier landen alle Werte, für die das System ein definiertes Verhalten zeigt. Die Spezifikation beschreibt, was bei diesen Eingaben passieren soll.

##### Ungültige Klassen

Diese enthalten Werte, die das System ablehnen oder ignorieren soll. Auch solche ohne definierte Verarbeitung gehören hierher.

*Beispiel: Sprungstärke -20% oder 150% sind ungültig. Trotzdem muss getestet werden, ob das Spiel solche Eingaben korrekt abfängt.*

Die Zuordnung ist nicht immer eindeutig. Entscheidend ist die Spezifikation: Was soll verarbeitet werden? Was soll zurückgewiesen werden?

---

#### Vom Wertebereich zum Testfall

Der Weg zu den <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfällen**</a> folgt einem klaren Schema.

##### Erster Schritt: Grenzen abstecken

Jede Eingabevariable hat einen Definitionsbereich. Beim <a href="./Glossar.md#komponententest" title="→ Glossar öffnen" class="glossary-term">**Komponententest**</a> sind das Methodenparameter, beim <a href="./Glossar.md#systemtest" title="→ Glossar öffnen" class="glossary-term">**Systemtest**</a> vielleicht Formularfelder. Dieser Bereich bildet zunächst eine einzige gültige Klasse. Alles außerhalb ist ungültig.

##### Zweiter Schritt: Feiner unterteilen

Nicht alle gültigen Werte werden gleich behandelt. Wo die Spezifikation unterschiedliches Verhalten vorsieht, entstehen Unterklassen. Die Aufteilung endet, wenn jede <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderung**</a> ihrer eigenen Klasse entspricht.

##### Dritter Schritt: Stellvertreter benennen

Aus jeder Klasse wird ein konkreter Wert ausgewählt. Er vertritt alle anderen Klassenmitglieder im Test.

##### Vierter Schritt: Testfall komplettieren

Zum Eingabewert gehören noch die <a href="./Glossar.md#vorbedingung" title="→ Glossar öffnen" class="glossary-term">**Vorbedingungen**</a> und das <a href="./Glossar.md#erwartetes-ergebnis" title="→ Glossar öffnen" class="glossary-term">**erwartete Ergebnis**</a>. Erst dann ist der Testfall vollständig.

---

#### Nicht nur Eingaben zählen

Das Prinzip funktioniert auch umgekehrt: Ausgabewerte lassen sich ebenfalls partitionieren. Allerdings steigt der Aufwand, denn zu jedem Ausgabe-Repräsentanten müssen die erzeugenden Eingaben gefunden werden.

##### Weitere Anwendungsfelder

Äquivalenzklassen beschränken sich nicht auf Schnittstellen. Sie eignen sich für:

* Interne Variablen und Zustände
* Konfigurationseinstellungen
* Zeitpunkte – etwa vor versus nach einem Ereignis
* Schnittstellenparameter bei <a href="./Glossar.md#integrationstest" title="→ Glossar öffnen" class="glossary-term">**Integrationstests**</a>

*Beispiel: Das Einsammeln eines Bonus-Items in Pixel Leap vor oder nach Ablauf des Timers – zwei Klassen, zwei unterschiedliche Verhaltensweisen.*

---

#### Regeln für saubere Partitionierung

Eine korrekte Aufteilung erfüllt bestimmte Kriterien.

##### Keine Überlappung

Jeder denkbare Wert gehört in genau eine Klasse. Überschneidungen sind verboten – sonst wäre unklar, welcher Repräsentant zuständig ist.

##### Keine leeren Klassen

Eine Partition ohne Elemente ergibt keinen Sinn und darf nicht existieren.

##### Verschiedene Strukturen möglich

Klassen können zusammenhängend sein (wie ein Zahlenintervall) oder aus Einzelwerten bestehen. Sie können geordnet oder ungeordnet sein, endlich oder theoretisch unendlich.

> Sorgfalt zahlt sich aus: Die Qualität der Klassenbildung bestimmt direkt, welche Testfälle entstehen und wie wahrscheinlich sie <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> aufdecken. Die Ableitung aus Spezifikationen ist selten trivial.

---

#### Kritische Stellen: Die Klassengrenzen

Besonders vielversprechend sind Tests an den Rändern. Dort lauern häufig Probleme – denn umgangssprachliche Formulierungen sind selten mathematisch präzise.

*Beispiel: "Unter 50 Punkten gibt es keinen Bonus." Gehört 50 dazu oder nicht? Ist x ≤ 50 gemeint oder x < 50? Ein gezielter Test mit exakt 50 Punkten klärt das.*

Die <a href="./Glossar.md#grenzwertanalyse" title="→ Glossar öffnen" class="glossary-term">**Grenzwertanalyse**</a> widmet sich genau diesen kritischen Werten.

---

#### Zahlen als Eingaben: Ein Durchgang

Anhand eines ganzzahligen Parameters lässt sich das Vorgehen gut nachvollziehen.

*Beispiel: Der Parameter `bonusMultiplier` in Pixel Leap. Zunächst existiert eine einzige gültige Klasse – alle darstellbaren Ganzzahlen von MIN_INT bis MAX_INT. Ungültig ist alles andere, zusammengefasst als NaN (Not a Number).*

| Parameter | Klasse |
|-----------|--------|
| bonusMultiplier | gÄK1: [MIN_INT, …, MAX_INT] |
| | uÄK1: NaN |

MIN_INT und MAX_INT bezeichnen die hardwareabhängigen Extremwerte. Im Rechner sind Zahlen begrenzt – anders als in der Mathematik. Überschreitungen dieser Grenzen verursachen oft Probleme, weil entsprechende Prüfungen fehlen.

##### Was gilt als ungültig?

Zur NaN-Klasse zählen nicht-numerische Eingaben, aber auch Gleitkommazahlen, wenn Ganzzahlen erwartet werden. Reagiert das System auf alle ungültigen Werte identisch – etwa mit einer Fehlermeldung –, genügt eine gemeinsame Klasse.

Allerdings: Ein erfahrener <a href="./Glossar.md#tester" title="→ Glossar öffnen" class="glossary-term">**Tester**</a> wird trotzdem eine Dezimalzahl probieren. Vielleicht rundet das Programm stillschweigend? Solche Tests entstammen dem <a href="./Glossar.md#erfahrungsbasiertes-testverfahren" title="→ Glossar öffnen" class="glossary-term">**erfahrungsbasierten Testen**</a>.

##### Weitere Unterteilung sinnvoll

Negative und positive Zahlen verhalten sich oft unterschiedlich. Die Null ist ein notorischer Problemfall. Also verfeinern:

| Parameter | Klasse | Repräsentant |
|-----------|--------|--------------|
| bonusMultiplier | gÄK1: [MIN_INT, …, -1] | -123 |
| | gÄK2: [0, …, MAX_INT] | 654 |
| | uÄK1: NaN | "f" |

Die Wahl der Repräsentanten ist hier beliebig – -123 und 654 haben keinen besonderen Grund. Hinzu kommen die <a href="./Glossar.md#grenzwert" title="→ Glossar öffnen" class="glossary-term">**Grenzwerte**</a>: MIN_INT, -1, 0, MAX_INT. Für NaN existieren keine echten Grenzen.

Insgesamt entstehen sieben Testwerte:

{"f", MIN_INT, -123, -1, 0, 654, MAX_INT}

Zu jedem gehört das erwartete Verhalten – nur so lässt sich nach dem Test beurteilen, ob ein Fehler vorliegt.

---

#### Komplexere Datentypen

Mit Zahlen gelingt die Klassenbildung leicht. Doch das Prinzip trägt weiter. Auch Aufzählungen, Strukturen oder Objektmengen lassen sich partitionieren.

*Beispiel: Pixel Leap bietet vier Charaktertypen – Speedster, Jumper, Tank, Balanced. Die Physik-Engine berechnet für jeden andere Sprungparameter. Hier braucht jeder Typ seinen eigenen Testfall.*

*Anders bei der Darstellung von Sammelobjekten: Ob Speedster oder Tank einsammelt, ist vermutlich egal. Ein Repräsentant genügt – aber dann gilt die Aussage nur für diesen. Über die anderen Typen ist nichts bekannt.*

---

#### Fazit

Die Äquivalenzklassenbildung reduziert die Testfallmenge drastisch, ohne die Aussagekraft zu opfern. Ihr Erfolg steht und fällt mit der Qualität der Partitionierung. In Kombination mit der Grenzwertanalyse steigt die Wahrscheinlichkeit, kritische <a href="./Glossar.md#fehlerzustand" title="→ Glossar öffnen" class="glossary-term">**Fehlerzustände**</a> zu entdecken.