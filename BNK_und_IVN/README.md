# BNK Lernzettel

## Inhalt

* [Python](#python)
  * [Generelle Syntax](#generelle-syntax)
  * [Collections](#collections)
  * [Klassen und Vererbung](#klassen-und-vererbung)
  * [Enumerators](#enumerators)
  * [Decorator](#decorators)
  * [Metaklassen](#metaklassen)
* [Künstliche Intelligenz](#künstliche-intelligenz)
  * [Allgemeine Informationen](#allgemeine-informationen)
  * [Agenten](#agenten)
  * [Endliche Automaten](#endliche-automaten)
  * [Behaviour Trees](#behaviour-trees)
  * [Neuronale Netze](#neuronale-netze)
* [XML](#xml)
  * [Generelles](#generelles)
  * [SVG](#svg)
  * [SMIL](#smil)
  * [Schema (XSD)](#xsd)
  * [Schematron](#schematron)
  * [Transformation (XSLT)](#xslt)
  * [DOM](#dom)
  * [Document Type Definition (DTD)](#dtd)
  * [XPath, XLink, XQuery](#xpath-xlink-xquery)
  * [Ajax](#ajax)
* [Verschiedenes](#verschiedenes)
  * [Vim](#vim)

## Python

Python ist eine interpretierte Programmiersprache, die als Skriptsprache genutzt wird und dynamisch typisiert ist

### Generelle Syntax

#### Variablen

```python
    myInt = 1            # int
    myFloat = 1.0          # float
    myString = "string"     # string
    myInt = myFloat = myString = True # dynamische Typisierung

    # same as 2^3
    myNumber = 2 ** 3
```

#### Funktionen

```python
    def function(parameter):
        pass

    # parameter as List
    def params(*args):
        pass

    # parameter as Dictionary
    def named_params(**kwargs):
        pass
```

#### Abfragen und Schleifen

```python
    if True is True: # ==
        pass

    if True is not False: # !=
        pass

    if True is True and False is False: # &&
        pass

    if True is True or False is False: # ||
        pass

    for x in range(begin, exclusive_end, step):
        pass

    for x in array:
        pass

    while True:
        pass
```

#### String Formatierung

```python
    name = "Kevin"
    age = 22
    print("%s is %d years old" % (name, age))

    # => gibt 5 aus weil 5 Zeichen
    print(len(name))

    # => gibt 3 aus weil "v" an dritter Stelle
    print(name.index("v"))

    # => gibt 1 aus weil nur einmal "K" im string vorkommt
    print(name.count("K"))

    # => gibt "evi" aus, er geht von Anfangsindex bis zum Endindex [start:end], negativ numbers gehen vom ende des strings aus, z.B. -3 -> dritte stelle von rechts
    print(name[2:4])

    # => gibt "en" aus, er geht von index 2 bis 5, überspringt aber immer 2 indexe [start:end:step]
    print(name[2:5:2])

    # => gibt "niveK" aus, er geht einfach von Start bis Ende rückwärts durch, wenn die Variablen leer gelassen werden, nimmt er den Anfang und Ende vom gesamten String
    print(name[::-1])

    # => gibt jeweils "KEVIN" und "kevin" aus
    print(name.upper())
    print(name.lower())

    # => gibt true und false aus
    print(name.startswith("K"))
    print(name.endswith("asdfasdfasdf"))

    # => macht aus den String mehrere Strings und packt sie in eine Liste, er splittet jeweils an der Leerstelle " "
    names = "Kevin Daniel Phillip Tom"
    allnames = names.split(" ")
```

### Collections

```python
    list  = [] # mutable
    tuple = () # immutable
    dict  = {} # mutable, mgl. keys: int, string, objekt/instanz, tuple

    x = list[begin, exclusive_end, step]

    # LISTS
    # Initialisierungsmethoden einer Liste
    listA = [1, 2, 3]

    # Der Liste hinzufügen
    listA.append(myInt)

    # Listen zusammenfügen,
    listA = [1, 2, 3]
    listB = [5, 6, 7]
    listC = listA + listB
    print(listC)
    # => [1, 2, 3, 5, 6, 7]

    print([1, 2, 3] * 3)
    # => [1, 2, 3, 1, 2, 3, 1, 2, 3]

    # DICTIONARIES
    # Initialiserungsmethoden eines Dictionarys
    # jeweils Key / Value
    myDict = {}
    myDict[1] = "Hallo"
    myDict[2] = "Ich"
    myDict[3] = "Bims"

    myDict = {
        1 : "Hey"
        2 : "na"
        3 : "du"
        4 : "Giraffe"
    }

    # Aus dem Dictionary löschen
    del myDict[1]
    # oder
    myDict.pop(1)

    # Durch Dictionary iterieren
    for number, text in myDict.items():
        print("%d gehört zu %s" % (number, text))
```

### Klassen und Vererbung

```python
    class Parent:
        def __init__(self, x): # constructor, self = aktuelle Instanz
            self.x = x # globale Variable
            y = 10     # lokale Variable

        def __add__(self, other): # +-operator
            return self.x + other.x

        def _private(self): # private methode (Unterstrich)
            pass

        def my_function(self):
            print("Hi")

        def add_method(self, a, b):
            return a + b

    class Child(Parent): # Child erbt von Parent
        self.y = super.x # super = instanz der Elternklasse
        pass

    # Klassenobjekt erzeugen
    myClass = Parent(5)
    myClass.my_function()
    myInt = myClass.x
    print(myClass.add_method(2, 3))
```

### Enumerators

```python
    import random

    def lottery():
        # returns 6 numbers between 1 and 40
        for i in range(6):
            yield random.randint(1, 40)

        # returns a 7th number between 1 and 15
        yield random.randint(1,15)
```

Diamantproblem: Wenn eine Klasse von zwei Klassen erbt, die beide die gleiche Funktion/Feld implementieren ist unklar von welcher Klasse die Funktion geerbt wird

### Decorators

### Metaklassen

```python
    MyExampleClass = type('ExampleClass', (), {'myInt' : 0, 'myString' : 'hallo'}) # returns a class object
    print(MyExampleClass)
    print(MyExampleClass()) # create an instance with the class
```

## Künstliche Intelligenz

### Allgemeine Informationen

#### Verfahren

* symbolisch &rarr; Das Wissen ist im KI-System explizit abgebildet. Dies kann durch Symbole, wie *Freund* oder *Feind* geschehen.
* subsymbolisch &rarr; Das Wissen ist nicht in Symbolen gespeichert und liegt somit nur in impliziter Form vor, dies ist zum Beispiel der Fall bei neuronalen Netzwerken

#### Typen

* starke KI &rarr; Nachempfinden des menschlichen Denkverhaltens
* schwache KI &rarr; KI-Technologien anwenden, um Probleme der echten Welt zu lösen
* Illusion of Intelligence &rarr; Intelligenz ist nur subjektiv (häufig der Ansatz für Game-AI)

#### Turing-Test

Testet, ob eine Maschine menschliches Denkverhalten nachahmen kann. Wenn ein Tester die Maschine nicht von einem Menschen unterscheiden kann, hat die Maschine bestanden. Das Chinese-Room-Argument allerdings zeigt, dass der Turing-Test allein nicht genügt um einer Maschine ein Bewusstsein zuzusprechen.

### Agenten

* Agenten sind autonome Einheiten, die ihre Umgebung wahrnehmen und mit ihr interagiern
* Typen:
  * rationaler Agent &rarr; handelt so, dass das Ziel möglichst *gut* erreicht wird
  * idealer rationaler Agent &rarr; optimiert seine Performance anhand von Beobachtungen und Wissen.
* Eigenschaften:
  * Proaktiv &rarr; Löst Aktionen aufgrund eigener Initiative aus
  * Reaktiv &rarr; Reagiert auf Veränderungen der Umwelt
  * Autonom &rarr; Arbeitet weitgehend unabhängig vom Nutzer
* optionale Eigenschaften:
  * Anpassungsfähig &rarr; Lernt aus Erfahrungen
  * Sozial &rarr; Kommuniziert mit anderen Agenten
  * Mobil &rarr; Kann den Ort wechseln
* PAGE-Modell (4 Bausteine eines Agenten)
  * **P**erception
  * **A**ctions
  * **G**oals
  * **E**nvironment

#### subkognitive / reaktive Agenten

* einfacher reaktiver Agent &rarr; Eine Wahrnehmung führt zu einer Aktion
* beobachtender reaktiver Agent &rarr; Gedächtnis, bestehend aus Erinnerungen, trägt zur Entscheidung bei

#### kognitive Agenten

* zielorientierter Agent &rarr; Speichert Wunschzustände und entscheidet basierend auf Erreichbarkeit
* nutzenorientierter Agent &rarr; Gewichtet Weltzustände nach einem Nützlichkeitsfaktor

#### Umgebung von Agenten

Die Umgebung in der sich Softwareagenten aufhalten, kann mit den folgen Kriterien beschrieben werden

* Zugänglich &rarr; alle etschidungsrelevanten Teile der Umgebung sind beobachtbat
* Determiniertheit &rarr; Aktionen haben eindeutige Folgen auf die Umgebung
* Episodisch &rarr; Erfahrung kann in einzelne Episoden (z.B.: Wahrnehmung, Handlung etc.) eingeteilt werden
* Statisch &rarr; Umgebung bleibt während der Entschidung unverändert
* Auflösung &rarr; Ist die Umgebung diskret (fest Größe) oder kontinuirlich

#### Multiagentensystem

* mehrere gleichartige oder unterschiedlich spezialisierte Einheiten in der gleichen Umgebung &rarr; Ameisenhaufen, Bienenkolonie
* zwei Ansätze
  * Bottom-Top &rarr; Spezifische Regeln werden auf Individuenebene deklariert und damit unabhängige Agenten definiert
  * Top-Bottom &rarr; Interaktionsregeln und damit der Verband wird definiert

#### Heuristiken

Heuristiken sind Methoden bzw. Faustregeln, die genutzt werden können um den Prozess der Entscheidungsfindung von Agenten zu beschreiben

* "most constrained" &rarr; Die Aktion mit den meisten Eischränkungen soll zuerst ausgeführt werden
* "das schwierigste zuert" &rarr; Die Aktion, die die meiste Arbeit benötigt, wird bevorzugt
* "das erfolgsversprechendste zuerst" &rarr; Die Aktion, die den meisten Nutzen hat, soll zuerst ausgeführt werden.

&rarr; Der Spieler soll denken, dass die KI "schlau ist", ohne dies tatsächlich zu sein

### Endliche Automaten

Endliche Automaten sind abstrakte Maschinen, die eine feste Anzahl an Zuständen haben und zwischen diesen wechseln (Input &rarr; ZustandA &rarr; ZustandB &rarr; Output) z.B.: Unity Animator.

* Deterministisch &rarr; Verhalten ist eindeutig und konstant nachvollziehbar und vorbestimmt &rarr; leicht zu beherrschen
* Nicht Deterministisch &rarr; Verhalten ist nicht eindeutig bestimmt und Zufall spielt eine Rolle bei den Übergänge &rarr; realistischer

### Behaviour Trees

### Neuronale Netze

Neuronale Netze sind Netzwerke von autonom agierenden Recheneinheiten (Neuronen), die sich in ihrem Aufbau an neuronalen System der Biologie orientieren. Das erste Neuronale Netzwerk war das sog. Perzeptron, welches 1962 von Frank Rosenblatt erfunden wurde.

Problembeschreibung &rarr; **Netz** &rarr; Problemlösung

Neuronale Netze passen sich in einer Lernphase an die Problemphase an. Dieses Lernen geschieht über die Veränderung des Netzes.

#### Allgemeines

#### Neuronen

##### Aufbau

##### Biologie als Vorbild

#### Lernvorgänge

##### Lernparadigmen

* supervised Learning (überwachtes Lernen) &rarr; Beim supervised Learning liefert das Netz einen Ist-Output, woraufhin dieser mit dem Soll-Output verglichen wird. Weicht der Ist-Output vom Soll-Output ab, wird der Fehler gesucht und minimiert.

* unsupervised Learning (unüberwachtes Lernen) &rarr; Beim unsupervised Learning passt sich das Netz quasi live an den Input an und benötigt kein Eingreifen in seine Struktur. Dies geschieht z.B. indem häufig genutzte Verbindungen gestärkt werden. Problem hierbei ist, dass die Richtigkeit des Netzes in einem lokalen Minimum landen kann und somit nicht sein volles Potenzial genutzt wird.

TODO: Grafik

## XML

XML steht für Extensible Markup Language und ist eine Sprache zur Darstellung von Daten in hierarchischen Strukturen. XML kann sowohl von Menschen, als auch von Maschinen gut verstanden werden. XML erlaubt es mehrere verschiedene Dialekte im gleichen Dokument zu habel, sofern jeder mit einem eindeutigen Prefix ausgewiesen wird.

### Generelles

```xml
    <!-- Jede XML-Datei sollte diesen Header haben -->
    <?xml version="1.0" encoding="utf-8"?>
    <!-- Daten, die die Datei hält -->
    <Node attribute="value">
        Text
    </Node>
```

### SVG

SVG steht für Scalable Vector Graphics und ist ein XML-Dialekt, der zur Definition von 2D Vektorgrafiken genutzt wird.

### SMIL

SMIL steht für Synchronized Multimedia Integration Language und ist ein XML-Dialekt, mit dem man zeitsynchron Multimediainhalte (Bilder, Videos, Ton etc.) animieren kann.

### XSD

XSD steht für XML Schema Definition und wird dazu genutzt, den Aufbau einer XML-Datei, sowie die Datentypen der ihrer Attribute zu validieren.

```xml
    <!-- Namespace -->
    <schema xmlns="http://www.w3.org/2001/XMLSchema">
```

#### Einfache Typen

Einfache Typen sind atomare Datentypen. Dies bedeutet hier, dass sie keine Elemente unter sich haben können (Leaf Nodes)

```xml
    <simpleType name="monatInt"></simpleType>
```

#### Komplexe Typen

Komplexe Typen sind Datentypen, die Child-Nodes haben können.

```xml
    <complexType name="pc-Typ">
    <sequence>
        <element name="name"       type="string"/>
        <element name="hersteller" type="string"/>
        <element name="prozessor"  type="string"/>
        <element name="kommentar"  type="string"  minOccurs="0" maxOccurs="unbounded"/>
    </sequence>
    </complexType>
```

#### Elemente

Elemente sind die eigentlichen XML-Nodes, die der Nutzer in der XML-Datei verwenden kann, sie können von einem vordefinierten Typen sein, müssen sonst aber einem Typen zugewiesen werden

```xml
    <element type="pc-Typ" name="PC"/>
```

#### Attribute

Typen können Attribute haben.

```xml
<attribute name="id" type="integer"/>
```

#### Erweiterungen und Einschränkungen

Komplexe und einfache Typen können im Nachhinein erweitert werden.

```xml
    <extension base="pc-Typ">
        <attribute name="id" type="int"/>
        <element name="ram" type="integer"/>
    </extension>
```

Bestehende Typen können außerdem weiter eingeschränkt werden. Hierzu müssen alle Elemente und Attribute der Vorlage kopiert, können aber verändert werden.

#### Typischer Aufbau einer XSD-Datei

```xml
    <schema xmlns="http://www.w3.org/2001/XMLSchema">
        <!-- Typen -->
        <complexType name="pc-Typ">
            <sequence>
                <element name="name"       type="string"/>
                <element name="hersteller" type="string"/>
                <element name="prozessor"  type="string"/>
                <element name="kommentar"  type="string"  minOccurs="0" maxOccurs="unbounded"/>
            </sequence>
        </complexType>

        <!-- Erweiterungen und Einschränkungen -->
        <extension base="pc-Typ">
            <attribute name="id" type="int"/>
            <element name="ram" type="integer"/>
        </extension>

        <!-- Elemente -->
        <element type="pc-Typ" name="PC"/>
    </schema>
```

### Schematron

Schematron ist eine Möglichkeit Unit Tests für XML-Dateien zu schreiben. Sie validieren somit den Inhalt der Tags und nicht den Aufbau der XML-Datei

```xml
    <schema xmlns="http://purl.oclc.org/dsdl/schematron">
```

#### Patterns und Rules

Patterns sind eine Möglichkeit seine Unit-Tests zu gruppieren, während man mit Rules den Kontext seiner Tests festlegt

```xml
    <pattern id="name">
        <rule context="XPath zum gewünschten Kontext">
        </rule>
    </pattern>
```

#### Tests

```xml
    <assert test="x=y">Nachricht, wenn der Test fehlschlägt</assert>

    <report test="x=y">Nachricht, wenn der Test erfolgreich ist</report>
```

#### Variablen

```xml
    <let name="name" value="val"/>

    <!-- Aufruf mit $name -->
```

### XSLT

XSLT steht für eXtensible Stylesheet Language Transformations und ist ein XML-Dialekt, der es erlaubt jede belibige XML-Datei wie XHTML zu behandeln.

```xml
    <stylesheet version="1.0" xmlns="http://www.w3.org/1999/XSL/Transform">
        <template match="context">
            <!-- html -->
        </template>
    </stylesheet>
```

#### Werte abrufen

```xml
    <value-of select="XPath Ausdruck zum Wert" />
```

#### Schleifen

```xml
    <!-- Geht über alle Kindelemente der ausgewählten Node -->
    <for-each select="XPath Ausdruck zur Branch-Node" />
        <value-of select="XPath Ausdruck zum Wert" />
    </for-each>
```

#### Sortierung

```xml
    <for-each select="XPath Ausdruck zur Branch-Node" />
        <sort select="XPath Ausdruck zum Wert" order="ascending|descending">
        <value-of select="XPath Ausdruck zum Wert" />
    </for-each>
```

### DOM

### DTD

### XPath XLink XQuery

#### XPath

XPath ist eine Abfragesprache, die dazu dient Element in einem XML-Dokument zu addressieren und auszuwerten.

```xml
    <Root>
        <Element attr="attribute">
            Text
        </Element>
    </Root>

    <!-- Root -->
    <element xpath="/">

    <!-- Text in einem Tag -->
    <element xpath="/Root/Element">

    <!-- Attribute -->
    <element xpath="/Root/Element[@attr]">
```

#### XLink

#### XQuery

### Ajax

## Verschiedenes

### Vim

*Vim* ist ein mit Plugins erweiterbarer Texteditor, der in den 80ern entwickelt wurde. *Vim* ist auf allen Unix-Systemen (Linux, MacOS) vorinstalliert und läuft sowohl als eigenständiges Programm als auch in der Kommandozeile.
