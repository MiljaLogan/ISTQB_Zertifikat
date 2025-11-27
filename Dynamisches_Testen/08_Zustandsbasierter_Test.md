### Zustandsbasierter Test

Bei einer ganzen Reihe von Systemen hat neben den Eingabewerten auch der bisherige Ablauf des Systems Einfluss auf die Berechnung der Ausgaben beziehungsweise auf das Systemverhalten. Das heißt, die Historie ist zu berücksichtigen, die das System durchlaufen hat. Zur Veranschaulichung der Historie werden Zustandsmodelle verwendet, die Grundlage für den <a href="./Glossar.md#zustandsuebergangstest" title="→ Glossar öffnen" class="glossary-term">**zustandsbasierten Test**</a> sind.

---

#### Grundkonzepte

##### Zustände und Übergänge

Das System oder <a href="./Glossar.md#testobjekt" title="→ Glossar öffnen" class="glossary-term">**Testobjekt**</a> kann beginnend von einem Startzustand unterschiedliche Zustände annehmen. Zustandsänderungen oder -übergänge werden durch Ereignisse ausgelöst – beispielsweise Funktionsaufrufe oder Eingaben – und es wird davon ausgegangen, dass die Übergänge direkt erfolgen.

##### Wächterbedingungen (Guard Conditions)

Führt ein Ereignis zu zwei oder mehreren Übergängen aus dem gleichen Zustand, so muss unterscheidbar sein, welcher Übergang zu wählen ist. Hierzu werden sogenannte **Wächterbedingungen** (Guard Conditions) an jedem von einem Zustand ausgehenden Übergang angegeben, wodurch festgelegt wird, welcher Übergang und damit welcher Folgezustand bei dem Ereignis eintritt.

##### Syntax für Übergänge

Bei den Zustandsänderungen können Aktionen durchzuführen sein. Die vollständige Syntax für einen Übergang lautet:

> **Ereignis [Wächterbedingung] / Aktion**

Neben dem Startzustand gibt es als weiteren speziellen Zustand den Endzustand. Modelliert wird das Verhalten in Zustandsautomaten (Zustandsübergangsdiagrammen) und/oder Zustandsübergangstabellen.

---

#### Eigenschaften von Zustandsautomaten

Ein Zustandsautomat ändert seinen Zustand in Abhängigkeit von seinem aktuellen Zustand und der nächsten Eingabe. Die Eingabe kann auch ein Ereignis sein. Es gibt nur endlich viele Zustände. Der Automat kann in jedem Zustand oder bei jedem Übergang von einem Zustand zum nächsten eine Aktion tätigen (etwa eine Ausgabe).

Für das <a href="./Glossar.md#testen" title="→ Glossar öffnen" class="glossary-term">**Testen**</a> werden folgende Vereinfachungen angenommen:

* **Aktionen sind mit Übergängen verbunden**, nicht mit Zuständen
* **Der Automat ist deterministisch**: Nach einer gegebenen Folge von Eingaben (Ereignissen) und einem gegebenen Startzustand befindet sich der Automat in einem eindeutig definierten Folgezustand
* **Der Automat ist vollständig**: In jedem Zustand gibt es einen Übergang für jede mögliche Eingabe

Die Vollständigkeit kann erreicht werden, wenn der Automat so erweitert wird, dass für bisher nicht berücksichtigte Eingaben ein Übergang entweder ohne eine Aktion auf denselben Zustand führt oder zu einem Fehlerzustand führt.

---

#### Beispiel: Online-Shop mit Bestellprozess

Der zustandsbasierte Test soll an einem Beispiel erörtert werden.

In einem E-Commerce-System durchläuft eine Bestellung verschiedene Zustände. Ein Kunde kann seinen Warenkorb bearbeiten, zur Kasse gehen, bezahlen und die Bestellung abschließen. Bestimmte Aktionen sind nur in bestimmten Zuständen erlaubt.

##### Zustandsmodell

Der Sachverhalt wird in einem Zustandsautomaten modelliert. Es gibt vier Zustände (Warenkorb, Checkout, Zahlung, Bestätigt) und Übergänge zwischen den jeweiligen Zuständen. Es gibt einen Start- und einen Endzustand.

Unter der <a href="./Glossar.md#vorbedingung" title="→ Glossar öffnen" class="glossary-term">**Vorbedingung**</a>, dass mindestens ein Artikel im Warenkorb liegt, wird vom Startzustand automatisch in den Zustand "Warenkorb" gewechselt. Von diesem Zustand gibt es mehrere Folgezustände:

* Wird "Zur Kasse" gewählt, befindet sich das System im Zustand "Checkout"
* Wird im Checkout die Zahlung eingeleitet, wechselt das System in den Zustand "Zahlung"
* Nach erfolgreicher Zahlung wechselt das System in den Zustand "Bestätigt"
* Aus "Checkout" oder "Zahlung" kann zurück zum "Warenkorb" gewechselt werden

##### Zustandsübergangstabelle

| Aktueller Zustand | Ereignis | Folgezustand |
|-------------------|----------|--------------|
| Warenkorb | zur_kasse | Checkout |
| Warenkorb | artikel_entfernen | Warenkorb |
| Warenkorb | warenkorb_leeren | Endzustand |
| Checkout | zahlung_starten | Zahlung |
| Checkout | zurück | Warenkorb |
| Checkout | adresse_ändern | Checkout |
| Zahlung | zahlung_erfolgreich | Bestätigt |
| Zahlung | zahlung_fehlgeschlagen | Checkout |
| Zahlung | abbrechen | Warenkorb |
| Bestätigt | neue_bestellung | Warenkorb |
| Bestätigt | session_beenden | Endzustand |

Da in der Tabelle sämtliche Übergänge zwischen allen Zuständen enthalten sein können, gibt es Übergänge, die im Automaten nicht dargestellt sind und nach der Spezifikation auch nicht auftreten dürfen. Diese nicht spezifizierten – oder auch unzulässigen – Übergänge sind für den Test aber durchaus von Bedeutung, um <a href="./Glossar.md#fehlerwirkung" title="→ Glossar öffnen" class="glossary-term">**Fehlerwirkungen**</a> aufzuzeigen.

---

#### Testfälle beim zustandsbasierten Test

##### Ein konkreter Testfall

Ein möglicher <a href="./Glossar.md#testfall" title="→ Glossar öffnen" class="glossary-term">**Testfall**</a> mit Vor- und <a href="./Glossar.md#nachbedingung" title="→ Glossar öffnen" class="glossary-term">**Nachbedingung**</a> ist folgender:

* **Vorbedingung**: System ist im Zustand "Warenkorb" mit mindestens einem Artikel
* **Ereignis**: zur_kasse
* **Sollreaktion**: Zustandsübergang zum Zustand "Checkout"
* **Nachbedingung**: Zustand ist "Checkout"

##### Anwendungsbereiche

Das Testobjekt kann beim zustandsbasierten Test ein komplettes System mit unterschiedlichen Systemzuständen, aber auch eine Klasse mit verschiedenen Zuständen in einem objektorientierten System sein. Immer wenn die Historie zu unterschiedlichem Verhalten führt, ist ein zustandsbasierter Test durchzuführen.

---

#### Testkriterien und Abstufungen

Beim zustandsbasierten Test können unterschiedliche Abstufungen der Testintensität festgelegt werden.

##### Minimale Forderung: Alle Zustände erreichen

Eine minimale Forderung ist das Erreichen aller möglichen Zustände. In dem gegebenen Beispiel sind dies die vier Zustände Warenkorb, Checkout, Zahlung und Bestätigt. Zum Erreichen aller vier Zustände reicht folgender Testfall aus:

**Testfall 1** (Notation: [Zustand], Ereignis):

[Warenkorb], zur_kasse → [Checkout], zahlung_starten → [Zahlung], zahlung_erfolgreich → [Bestätigt]

##### Alle Ereignisse testen

Es sind allerdings nicht alle Ereignisse im Test zum Tragen gekommen. Eine weitere Forderung für den Test besteht darin, alle Ereignisse mindestens einmal zu testen. Testfall 1 ist dann um die Ereignisse artikel_entfernen, zurück, adresse_ändern, zahlung_fehlgeschlagen, abbrechen und session_beenden zu ergänzen.

##### Anzustrebendes Testkriterium

Ein anzustrebendes Testkriterium beim zustandsbasierten Test ist, dass bei jedem Zustand alle für diesen Zustand spezifizierten Ereignisse mindestens einmal zur Ausführung kommen. Die Übereinstimmung zwischen dem im Zustandsmodell spezifizierten gewünschten Verhalten und dem tatsächlichen Verhalten des Testobjekts kann dann festgestellt werden.

##### Unzulässige Übergänge testen

Bei kritischen Systemen sollen auch die nicht im Automaten spezifizierten Übergänge – aber in der Zustandsübergangstabelle enthaltenen – getestet werden. Beispielsweise wäre zu testen, ob im Zustand "Bestätigt" das Ereignis zahlung_starten ausgeführt werden kann und zu einer nicht spezifizierten Zustandsänderung führt.

---

#### Umgang mit Zyklen im Automaten

Die einfache Sicht, nur die Zustände und/oder die Übergänge separat zu testen, wird dem Testen von Zustandsautomaten nicht wirklich gerecht. Der Automat beschreibt Zyklen von nahezu beliebiger Tiefe. Im Beispiel ist ein ständiger Wechsel zwischen den Zuständen "Warenkorb" und "Checkout" möglich und entspricht ja auch der täglichen Nutzung.

Aber wie tief soll getestet werden? Wie können Zyklen behandelt beziehungsweise aufgebrochen werden?

##### Testfallerzeugung mit Übergangsbaum

Die Testfallerzeugung mit dem Übergangsbaum konzentriert sich auf den separaten Test von Abfolgen von Zustandsübergängen, die immer mit dem Startzustand beginnen.

Aus dem Zustandsautomaten wird ein sogenannter Übergangsbaum erstellt. Ziel dabei ist die Aufstellung von Ereignis- oder Eingabefolgen und die Eliminierung von Mehrfachzyklen. Wenn ein in der bisher erzeugten Folge bereits vorliegender Zustand wieder erreicht wird (einfacher Zyklus), wird die weitere Expandierung des Baums abgebrochen.

**Vorgehensweise:**

1. Als Wurzel des Baums wird der Startzustand verwendet
2. Jeder mögliche Zustandsübergang im Automaten zu einem Folgezustand wird im Übergangsbaum zu einem neuen Knoten, der den Folgezustand repräsentiert. Die Kante zwischen den beiden Knoten ist mit dem Ereignis verbunden, das den Übergang auslöst
3. Dieser Schritt wird so lange wiederholt, bis ein bereits im Automaten besuchter Zustand erreicht wird (dadurch werden mehrfache Zyklen vermieden) oder ein Zustand keine abgehenden Übergänge besitzt (Endzustand)

Der so erzeugte Baum repräsentiert alle möglichen Pfade im Automaten vom Startzustand bis zu einem Endzustand beziehungsweise bis zu einem Zustand, der bereits Bestandteil des bis dahin aufgesammelten Pfads ist. Jeder Pfad von der Wurzel des Baums zu einem Blatt repräsentiert einen Testfall, eine Folge von Eingaben beziehungsweise Ereignissen.

##### Erweiterter Übergangsbaum

Ein erweiterter Übergangsbaum wird dadurch erzeugt, dass an jedem Zustand alle möglichen Ereignisse eintreten sollen, auch solche auf die der Automat in diesem Zustand nicht reagieren soll. Diese unzulässigen Übergänge – wenn sie überhaupt im Test ausführbar sind – müssen bei der <a href="./Glossar.md#testdurchfuehrung" title="→ Glossar öffnen" class="glossary-term">**Testausführung**</a> zu einer Zurückweisung oder Ignorierung des Ereignisses oder zu einer Fehlerbehandlung führen.

---

#### N-Switch-Überdeckung

Dass jeder Übergang, und damit auch jeder Zustand, mindestens einmal durchlaufen wird, ist ein eher einfaches Kriterium zur Beendigung des zustandsbasierten Tests. Je nach <a href="./Glossar.md#anforderung" title="→ Glossar öffnen" class="glossary-term">**Anforderungen**</a> an die <a href="./Glossar.md#qualitaet" title="→ Glossar öffnen" class="glossary-term">**Qualität**</a> der Software wird dieses minimale Kriterium nicht immer ausreichen.

Ein umfassenderer Test betrachtet Zustandsübergänge und Folgen unterschiedlicher Länge von Übergängen. Wenn einzelne Übergänge (oder Folgen von Übergängen) von Ausgangszustand Za zum Zielzustand Zz getestet werden sollen, muss zuerst eine Folge von Ereignissen ausgeführt werden, die zum Ausgangszustand Za der zu testenden Übergangsfolge führt. Danach sind die Ereignisse beziehungsweise Eingaben auszuführen, die die eigentlich zu testende Folge zur Ausführung bringen.

##### Abstufungen der N-Switch-Überdeckung

Die Längen der zu testenden Übergangsfolgen können je nach Testintensität variieren. Das Verfahren wird als <a href="./Glossar.md#n-switch-ueberdeckung" title="→ Glossar öffnen" class="glossary-term">**N-Switch-Überdeckung**</a> bezeichnet. N ist dabei die Anzahl der Zustände zwischen dem Anfangs- und dem Zielzustand der zu testenden Folge von Zuständen:

| Überdeckung | Beschreibung |
|-------------|--------------|
| 0-Switch | Ein Übergang von einem Zustand direkt zum Folgezustand |
| 1-Switch | Zwei Übergänge (ein Zustand zwischen Anfangs- und Zielzustand) |
| 2-Switch | Drei Übergänge (zwei Zustände zwischen Anfangs- und Zielzustand) |

Dabei ist zu beachten, dass die Zustände in den Folgen auch dieselben sein können, wenn nämlich eine Eingabe den Zustand nicht ändert. Mit dem Verfahren kann der Test von Zyklen im Automaten strukturiert durchgeführt und die Anzahl der Zyklen nach oben beschränkt werden.

---

#### Anwendung beim GUI-Test

Zustandsbasiertes Testen eignet sich auch gut als Technik beim <a href="./Glossar.md#systemtest" title="→ Glossar öffnen" class="glossary-term">**Systemtest**</a>, wenn Tests der grafischen Bedienoberfläche des Testobjekts durchzuführen sind.

Die Bedienoberfläche besteht in der Regel aus einer Menge von Masken oder Dialogboxen, zwischen denen durch Eingabeaktionen (Menüauswahl, OK-Button usw.) hin und her gewechselt werden kann. Werden Masken beziehungsweise Dialogboxen als Zustände aufgefasst und Eingabeaktionen als Zustandsübergänge, so können die Navigationsmöglichkeiten durch die Bedienoberfläche mit einem Zustandsautomaten modelliert werden.

*Beispiel: Beim Test der Benutzeroberfläche eines Online-Shops wurde so vorgegangen: Der Test beginnt in der Hauptseite (Zustand 1). Über die Aktion "Mein Konto" erfolgt der Wechsel in den Dialog "Kontoverwaltung" (Zustand 2). Die Aktion "Abbrechen" beendet diesen Dialog und es erfolgt der Rücksprung in Zustand 1. Innerhalb eines Zustands können dann zustandslokale Tests erfolgen, die die eigentliche Funktionalität der angesteuerten Seite prüfen. Auf analoge Weise kann die Navigation durch beliebig komplexe Dialogketten dargestellt werden. Das Zustandsmodell der Bedienoberfläche hilft sicherzustellen, dass alle Dialoge im Test beachtet und geprüft werden.*

---

#### Zusammenfassung

| Aspekt | Beschreibung |
|--------|--------------|
| Anwendungsbereich | Systeme mit historieabhängigem Verhalten |
| Modellierung | Zustandsautomaten und Zustandsübergangstabellen |
| Minimales Kriterium | Alle Zustände mindestens einmal erreichen |
| Empfohlenes Kriterium | Alle Übergänge mindestens einmal durchlaufen |
| Erweitertes Kriterium | Auch unzulässige Übergänge testen |
| Zyklenbehandlung | Übergangsbaum oder N-Switch-Überdeckung |
| GUI-Test | Masken als Zustände, Aktionen als Übergänge |

Der zustandsbasierte Test ist ein wirkungsvolles <a href="./Glossar.md#black-box-testverfahren" title="→ Glossar öffnen" class="glossary-term">**Blackbox-Testverfahren**</a> für Systeme, deren Verhalten von der Vorgeschichte abhängt. Die Wahl des geeigneten Testkriteriums – von einfacher Zustandsüberdeckung bis zur N-Switch-Überdeckung – hängt von den Qualitätsanforderungen und dem verfügbaren Testbudget ab.