# BNK Lernzettel

## Inhalt

* [Python](#python)
  * [Generelle Syntax](#generelle-syntax)
  * [Collections](#collections)
  * [Klassen und Vererbung](#klassen-und-vererbung)
  * [Generators](#generators)
  * [Doctests](#doctests)
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

Python ist eine interpretierte Programmiersprache, die als Skriptsprache genutzt wird und dynamisch typisiert ist.

### Generelle Syntax

#### Variablen

```python
    my_int = 1               # int
    my_float = 1.0           # float
    my_string = "string"     # string
    my_int = my_float = my_string = True # dynamische Typisierung

    # Potenzen
    my_number = 2 ** 3 # equivalent zu 2 * 2 * 2
```

#### Funktionen

```python
    def function(parameter):
        pass

    # parameter als Liste
    def params(*args):
        pass

    # parameter als Dictionary
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

    # old-school / C methode
    print("%s is %d years old" % (name, age))
    # neuere string format methode
    print("{} is {} years old".format(name, age))
    # string interpolation
    print(f"{name} is {age} years old")

    # gibt 5 aus weil 5 Zeichen
    print(len(name))

    # gibt 3 aus weil "v" an dritter Stelle
    print(name.index("v"))

    # gibt 1 aus weil nur einmal "K" im string vorkommt
    print(name.count("K"))

    # gibt "evi" aus, er geht von Anfangsindex bis zum Endindex [start:end], negativ numbers gehen vom ende des strings aus, z.B. -3 -> dritte stelle von rechts
    print(name[2:4])

    # gibt "en" aus, er geht von index 2 bis 5, überspringt aber immer 2 indexe [start:end:step]
    print(name[2:5:2])

    # gibt "niveK" aus, er geht einfach von Start bis Ende rückwärts durch, wenn die Variablen leer gelassen werden, nimmt er den Anfang und Ende vom gesamten String
    print(name[::-1])

    # gibt jeweils "KEVIN" und "kevin" aus
    print(name.upper())
    print(name.lower())

    # gibt true und false aus
    print(name.startswith("K"))
    print(name.endswith("asdfasdfasdf"))

    # macht aus den String mehrere Strings und packt sie in eine Liste, er splittet jeweils am Leerzeichen " "
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

    my_int = 4
    # Der Liste hinzufügen
    list_a.append(my_int)

    # Listen zusammenfügen,
    list_a = [1, 2, 3]
    list_b = [5, 6, 7]
    list_c = list_a + list_b
    print(list_c)
    print([1, 2, 3] * 3)

    '''
    >>> [1, 2, 3, 5, 6, 7]
    >>> [1, 2, 3, 1, 2, 3, 1, 2, 3]
    '''

    # DICTIONARIES
    # Initialiserungsmethoden eines Dictionarys
    # jeweils Key / Value
    my_dict = {}
    my_dict[1] = "Hallo, "
    my_dict[2] = "ich"
    my_dict[3] = "bins"

    my_dict = {
        1: "Hey, "
        2: "na"
        3: "du"
        4: "Giraffe"
    }

    # Aus dem Dictionary löschen
    del my_dict[1] # löscht den Wert permanent
    # oder
    my_dict.pop(1) # entfernt den Wert und gibt ihn zurück

    # Durch Dictionary iterieren
    for key, val in my_dict.items():
        print("%d gehört zu %s" % (key, val))
```

### Klassen und Vererbung

```python
    class Parent:
        def __init__(self, x): # constructor, self = aktuelle Instanz (equivalent zu this)
            self.x = x # klassenweite Variable
            y = 10     # lokale Variable

        def __add__(self, other): # +-operator
            return self.x + other.x

        def _private_method(self): # private methode (Unterstrich)
            pass

        def my_method(self):
            print("Hi")

        def add_method(self, a, b):
            return a + b

    class Child(Parent): # Child erbt von Parent
        self.y = super.x # super = instanz der Elternklasse
        pass

    # Klassenobjekt erzeugen
    my_class = Child(5)
    my_class.my_method()
    my_int = my_class.x
    print(my_class.add_method(2, 3))
```

Diamantproblem &rarr; Wenn eine Klasse von zwei Klassen erbt, die beide die gleiche Funktion/Feld implementieren, ist unklar von welcher Klasse die Funktion geerbt wird

### Generators

Generatoren ermöglichen die inkrementelle Ausführung von Funktionen und besonders Schleifen.

```python
    import random

    def lottery():
        # gibt nacheinander zufällige Zahlen von 1 bis 49 zuück
        for i in range(6):
            yield random.randint(1, 50)

        # gibt eine siebte Zahl zwischen 1 und 15 zurück
        yield random.randint(1,15)

    print("for-schleife (1-49)")
    print(lottery.next())
    print(lottery.next())
    print(lottery.next())
    print(lottery.next())
    print(lottery.next())
    print(lottery.next())
    print("extra aufruf (1-15)")
    print(lottery.next())

    '''
    >>> for-schleife (1-49)
    >>> 1
    >>> 48
    >>> 22
    >>> 19
    >>> 31
    >>> 12
    >>> extra aufruf (1-15)
    >>> 15
    '''
```

Generators können außerdem genutzt werden um in kürzerer Schreibweise Listen zu erstellen/befüllen

```python
    my_list = [x * 2 for x in range(8)]

    print(my_list)

    '''
    >>> [0, 2, 4, 6, 8, 10, 12, 14]
    '''

    # mit Bedingung
    my_list = [x * 2 for x in range(8) if x % 2 is 0]

    print(my_list)

    '''
    >>> [0, 4, 8, 12]
    '''
```

### Doctests

### Decorators

Decorators erlauben es eine Funktion zu erweitern, ohne sie verändern zu müssen. Sie können als Funktionen oder als Klassen deklariert werden.

```python
    # Als Funktion
    def decorator_function(original_function):
        # Code hier wird einmal ausgeführt
        print("Executed on Declaration")
        def wrapper_function():
            # Code hier wird bei jedem Funktionsaufruf ausgeführt
            print("Executed on Call")
            return original_function()
        return wrapper_function

    @decorator_function # declaration
    def display(msg):
        print(msg)
    
    # equivalent zu @decorator_function:
    # display = decorator_function(display) # declaration

    display("Foo") # call
    display("Bar") # call

    '''
    Output:
    >>> Executed on Declaration
    >>> Executed on Call
    >>> Foo
    >>> Executed on Call
    >>> Bar
    '''

    # Als Klasse
    class DecoratorClass():
        def __init__(self, original_function):
            # Code hier wird einmal ausgeführt
            print("Executed on Declaration")
            self.original_function = original_function

        def __call__(self, param):
            # Code hier wird bei jedem Funktionsaufruf ausgeführt
            print("Executed on Call")
            return self.original_function(param)

    @DecoratorClass # declaration
    def display(msg):
        print(msg)

    display("foo")
    display("bar")

    '''
    Output:
    >>> Executed on Declaration
    >>> Executed on Call
    >>> Foo
    >>> Executed on Call
    >>> Bar
    '''
```

Decorators funktionieren, indem sie ein delegate (genannt clusure) zu einer Hilfsfunktion (wrapper) zurückgeben. Der Wrapper ruft die eigentliche Funktion auf und gibt ihre Werte zurück.

### Metaklassen

In python hat jedes Objekt eine Klasse zu der sie gehört und damit einen Typen. Klassen sind auch Objekte und haben somit auch einen Typen, genannt Metaklasse. Im Normalfall haben Klassen die Metaklasse 'type', man kann ihnen allerdings eine selbst definierte Metaklasse zuweisen.

```python
    # Normalfall
    class Class:
    my_int = 10

    instance = Class()

    print(type(instance)) # instance ist vom Typ Class
    print(type(Class)) # Class ist vom Typ Type

    # Eigen Metaklasse
    class A(type):
        def __new__(self, class_name, super_classes, members):
            return type.__new__(self, class_name, super_classes, members)

    class B(metaclass=A):
        my_string = 'Foo'

    b = B()
    print(type(b)) # b ist vom Typ B
    print(type(B)) # B ist vom Typ A und nicht von Type

```

Klassen können erstellt werden, indem man ein Objekt der Metaklasse instanziiert (im Normalfall mit der type-Funktion).

```python
    # Normalfall
    MyExampleClass = type('ExampleClass', (), {'myInt' : 0, 'myString' : 'hallo'})
    print(MyExampleClass) # ein Objekt vom Typ type
    print(MyExampleClass()) # ein Objekt vom Typ MyExampleClass

    # Mit eigener Metaklasse
    C = A('C', (), {'my_float' : 0.0})
    print(C) # ein Objekt vom Typ A
    print(C()) # ein Objekt vom Typ C
```

## Künstliche Intelligenz

### Allgemeine Informationen

#### Verfahren

* symbolisch &rarr; Das Wissen ist im KI-System explizit abgebildet. Dies kann durch Symbole, wie *Freund* oder *Feind* geschehen.
* subsymbolisch &rarr; Das Wissen ist nicht in Symbolen gespeichert und liegt somit nur in impliziter Form vor, dies ist zum Beispiel der Fall bei neuronalen Netzwerken.

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

* Zugänglich &rarr; Alle etschidungsrelevanten Teile der Umgebung sind beobachtbar
* Determiniertheit &rarr; Aktionen haben eindeutige Folgen auf die Umgebung
* Episodisch &rarr; Erfahrung kann in einzelne Episoden (z.B.: Wahrnehmung, Handlung) eingeteilt werden
* Statisch &rarr; Umgebung bleibt während der Entschidung unverändert
* Auflösung &rarr; Ist die Umgebung diskret (fest Größe) oder kontinuirlich

#### Multiagentensystem

* mehrere gleichartige oder unterschiedlich spezialisierte Einheiten in der gleichen Umgebung &rarr; Ameisenhaufen, Bienenkolonie
* zwei Ansätze
  * Bottom-Top &rarr; Spezifische Regeln werden auf Individuenebene deklariert und damit unabhängige Agenten definiert
  * Top-Bottom &rarr; Interaktionsregeln und damit der Verband wird definiert

#### Heuristiken

Heuristiken sind Methoden bzw. Faustregeln, die genutzt werden können um den Prozess der Entscheidungsfindung von Agenten zu beschreiben

* "most constrained" &rarr; Die Aktion mit den meisten Einschränkungen soll zuerst ausgeführt werden
* "das schwierigste zuert" &rarr; Die Aktion, die die meiste Arbeit benötigt, wird bevorzugt
* "das erfolgsversprechendste zuerst" &rarr; Die Aktion, die den meisten Nutzen hat, soll zuerst ausgeführt werden.

&rarr; Der Spieler soll denken, dass die KI "schlau ist", ohne dies tatsächlich zu sein

### Endliche Automaten

Endliche Automaten sind abstrakte Maschinen, die eine feste Anzahl an Zuständen haben und zwischen diesen wechseln (Input &rarr; ZustandA &rarr; ZustandB &rarr; Output) z.B.: Unity Animator.

* Deterministisch &rarr; Verhalten ist eindeutig, konstant nachvollziehbar und vorbestimmt &rarr; leicht zu beherrschen
* Nicht Deterministisch &rarr; Verhalten ist nicht eindeutig bestimmt und Zufall spielt eine Rolle bei den Übergängen &rarr; realistischer

### Behaviour Trees

Behaviour Trees sind Baumstrukturen, die Aktionsmuster beschreiben. Sie bestehen aus Nodes, die hintereinander geschaltet werden und zu bestimmten Konditionen eine Aktion ausführen. Nodes auf der gleichen Ebene werden nacheinander abgearbeitet und sobald eine Kondition erfüllt ist wird die Aktion ausgeführt eine Ebene tiefer gegangen.

![Aufbau von Behaviour Trees](https://github.com/rausc-daniel/INH17GAbschlussklausuren/blob/master/BNK_und_IVN/img/behaviour_trees.png)

### Neuronale Netze

Neuronale Netze sind Netzwerke von autonom agierenden Recheneinheiten (Neuronen), die sich in ihrem Aufbau an neuronalen System der Biologie orientieren. Das erste Neuronale Netzwerk war das sog. Perzeptron, welches 1962 von Frank Rosenblatt erfunden wurde.

Problembeschreibung &rarr; **Netz** &rarr; Problemlösung

Neuronale Netze passen sich in einer Lernphase an die Problemstellung an. Dieses Lernen geschieht über die Veränderung des Netzes.

#### Neuronen

##### Aufbau

Ein Neuron besteht aus mehreren gewichteten Inputs (w0..w1), einem Threshold (T) und einem Output (o).

* Inputs &rarr; Die Inputs kommen von den Neuronen in der vorherigen Schicht und werden einzeln gewichtet.
* Threshold &rarr; Ist die Summe der Inputs größer als der Threshold, feuert das Neuron. Der Threshold kann ein Schwellenwert sein, oder durch eine Aktivierungsfunktion bestimmt werden.
* Output &rarr; Der Output ist ein binärer Wert (feuert / feuert nicht) oder das Ergebnis der Aktivierungsfunktion. Er wird an alle Neuronen in der nächsten Schicht weitergeleitet

![Aufbau eines Neurons](https://github.com/rausc-daniel/INH17GAbschlussklausuren/blob/master/BNK_und_IVN/img/neuron.png)

##### Biologie als Vorbild

Der Aufbau von neuronales Netzen orientiert sich an der Struktur von Nervensystemen in Tieren.

![Biologie als Vorbild](https://github.com/rausc-daniel/INH17GAbschlussklausuren/blob/master/BNK_und_IVN/img/biology.png)

##### Programmbeispiel

```python
    class Neuron():

    weights = []

    def __init__(self, threshold, inputs, weights = None):
        self.threshold = threshold
        self.neurons = inputs
        if weights is None:
            for i in len(self.neurons):
                self.weights[i] = randrange(-1, 1)
        else:
            self.weights = weights

    def evaluate(self):
        res = 0
        for i in range(len(self.neurons)):
            res = res + (self.weights[i] * self.neurons[i].fire())
        return res

    def fire(self):
        if self.evaluate() > self.threshold:
            return 1
        return 0
```

#### Topologie

Die Topologie eines Netzes beschreibt seinen Aufbau. Bestandteile hiervon sind die Anzahl der Schichten, wie viele Neuronen jede Schicht enthält und welche Neuronen mit welchen Anderen verbunden sind. Außerdem beschreibt sie wie viele Input- und Output-Neuronen das Netz hat.

#### Lernvorgänge

Neuronale Netze können auf diverse Arten lernen. Die zwei wichtigsten sind die Veränderung der Netztopologie (z.B. durch genetische Algorithmen) und die Anpassung von Gewichtungen der einzelnen Verbindungen.

##### Lernparadigmen

* supervised Learning (überwachtes Lernen) &rarr; Beim supervised Learning liefert das Netz einen Ist-Output, woraufhin dieser mit dem Soll-Output verglichen wird. Weicht der Ist-Output vom Soll-Output ab, wird der Fehler gesucht und minimiert.

* unsupervised Learning (unüberwachtes Lernen) &rarr; Beim unsupervised Learning passt sich das Netz quasi live an den Input an und benötigt kein Eingreifen in seine Struktur. Dies geschieht z.B. indem häufig genutzte Verbindungen gestärkt werden. Problem hierbei ist, dass die Richtigkeit des Netzes in einem lokalen Minimum landen kann und somit nicht sein volles Potenzial genutzt wird.

![Lokale Minima](https://github.com/rausc-daniel/INH17GAbschlussklausuren/blob/master/BNK_und_IVN/img/local_minima.png)

##### Delta-Regel

Die Delta Regel ist eine der wichtigsten Lernmethoden des supervised learning. Sie ist für Feed-Forward-Netze gedacht, also Netze, die ihren Output nicht weiterverarbeiten. Sie funktioniert indem der Ist-Output von jedem Neuron mit seinem Soll-Ouput verglichen wird und bei Abweichungen angepasst wird. Die Anpassung geschieht mithilfe eines Lernfaktors an den Gewichten der einzelnen Verbindungen.

![Delta Regel](https://github.com/rausc-daniel/INH17GAbschlussklausuren/blob/master/BNK_und_IVN/img/delta.png)

Der beliebtiste Algorithmus zur Anwendung der Delta-Regel ist die *Backpropagation*. Hier wird das Netz solange rückwärts iteriert bis die Quelle des Fehlers gefunden wurde und währenddessen für jede Verbindung die Delta-Regel angewandt.

##### Hebb'sche-Regel

Die Hebb'sche Regel ist eine Lernregel für zirkulare Netze, die ihren Output weiterverarbeiten und ist somit für unsupervised learning gedacht. Sie belohnt Verbindungen, bei denen beide Neuronen feuern indem das Gewicht dieser Verbindung erhöht wird. Alle anderen Kombinationen bleiben unberührt.

![Hebb'sche Regel](https://github.com/rausc-daniel/INH17GAbschlussklausuren/blob/master/BNK_und_IVN/img/hebb.png)

#### Nicht linear Separierbare Probleme und zusätliche Schichten

In neuronalen Netzwerken generiert jede Schicht eine Gerade (bei 3 Parametern Hyperebene genannt), die zwei Gruppen voneinander trennt. Hat man allerdings mehr als zwei Gruppen oder sind zwei Gruppen speziell angeordnet reicht eine Gerade nicht mehr aus um diese zu trennen. In diesem Fall fügt man dem Netz mehr Schichten hinzu und hat somit mehr Geraden zur Verfügung.

![Nichtliniare Separierbarkeit](https://github.com/rausc-daniel/INH17GAbschlussklausuren/blob/master/BNK_und_IVN/img/multiple_layers.png)

## XML

XML steht für Extensible Markup Language und ist eine Sprache zur Darstellung von Daten in hierarchischen Strukturen. XML kann sowohl von Menschen, als auch von Maschinen gut *verstanden* werden. XML erlaubt es mehrere verschiedene Dialekte im gleichen Dokument zu haben, sofern jeder mit einem eindeutigen Prefix ausgewiesen wird.

### Generelles

```xml
    <!-- Jede XML-Datei sollte diesen Header haben -->
    <?xml version="1.0" encoding="utf-8"?>
    <!-- Namespace des Dokuments und sein Prefix -->
    <c:Namespace xmlns:c="namespace">
        <!-- Daten, die die Datei hält -->
        <c:Node attribute="value">
            Text
        </c:Node>
    </c:Namespace>
```

### SVG

SVG steht für Scalable Vector Graphics und ist ein XML-Dialekt, der zur Definition von 2D Vektorgrafiken genutzt wird.

### SMIL

SMIL steht für Synchronized Multimedia Integration Language und ist ein XML-Dialekt, mit dem man zeitsynchron Multimediainhalte (Bilder, Videos, Ton etc.) animieren kann.

### XSD

XSD steht für XML Schema Definition und wird dazu genutzt, den Aufbau einer XML-Datei, sowie die Datentypen ihrer Attribute zu validieren.

```xml
    <!-- Namespace -->
    <schema xmlns="http://www.w3.org/2001/XMLSchema">
```

#### Einfache Typen

Einfache Typen sind atomare Datentypen. Dies bedeutet hier, dass sie keine Elemente unter sich haben können (Leaf Nodes)

```xml
    <simpleType name="monat"></simpleType>
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

Elemente sind die eigentlichen XML-Nodes, die der Nutzer in der XML-Datei verwenden kann. Sie können von einem vordefinierten Typen sein, müssen sonst aber einem Typen zugewiesen werden

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
    <!-- Namespace -->
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

    <!-- Aufruf -->
    <assert test="x=$name">Nachricht, wenn der Test fehlschlägt</assert>
```

### XSLT

XSLT steht für Extensible Stylesheet Language Transformations und ist ein XML-Dialekt, der es erlaubt jede belibige XML-Datei wie XHTML zu behandeln.

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

### DTD

DTD steht für Document Type Definition und wird genutzt um die Struktur, die Verschachtelung und den Inhalt von XML-Dokumenten zu definieren. Es deklariert somit einen wiederverwendbaren Dokumenttypen.

### XPath XLink XQuery

#### XPath

XPath ist eine Abfragesprache, die dazu dient Elemente in einem XML-Dokument zu addressieren und auszuwerten.

```xml
    <Root>
        <Element attr="attribute">
            Text
        </Element>
    </Root>

    <!-- Root -->
    <element xpath="/">

    <!-- Kindelemt(-e) eines Tags, kann Text sein-->
    <element xpath="/Root/Element">

    <!-- Attribute -->
    <element xpath="/Root/Element[@attr]">
```

#### XLink

Mit XLink lassen sich Verlinkungen zu anderen Dateien oder Websites in XML-Dokumente einbinden.

#### XQuery

XQuery ist eine Abfragesprache für XML-Dateien, die syntaktisch und inhaltlich SQL ähnelt.

### Ajax

Ajax steht für Asynchronous JavaScript and XML und ermöglicht es asynchrone Anfragen an einen Webserver zu senden und die aktuelle HTML-Seite zu verändern ohne sie neu zu laden.

## Verschiedenes

### Vim

*Vim* ist ein mit Plugins erweiterbarer Texteditor, der in den 1980ern entwickelt wurde. *Vim* ist auf allen Unix-Systemen (Linux, MacOS) vorinstalliert und läuft sowohl als eigenständiges Programm als auch in der Kommandozeile und über SSH-Verbindungen.
