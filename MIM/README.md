# MIM Lernzettel

* [Was ist C++](#was-ist-c++)
  * [Use Cases](#use-cases)
  * [Engines](#engines)
  * [IDEs](#ides)
  * [Vergleich zu C#](vergleich-zu-c#)
* [C++](#c++)
  * [Generelle Syntax](#generelle-syntax)
  * [Collections](#collections)
  * [Klassen, Structs und Vererbung](#klassen-structs-und-vererbung)
  * [Pointer](#pointer)
  * [std](#std)

## Inhalt

## Was ist C++

C++ ist eine ISO-genormte Programmiersprache, die eine Erweiterung von C darstellt. C++ ermöglicht die maschinennahe und damit besonders effiziente Programmierung kann aber gleichzeitig ein hohes Abstraktionsniveau haben.

### Use Cases

C++ wird hauptsächling in der Systemprogrammierung und der Anwendungsprogrammierung eingesetzt und zählt in beiden Feldern zu den beliebtesten Programmiersprachen. Im Bereich der Systemprogrammierubg kommt C++ zum Einsatz wenn es einen hohen Anspruch an Effizienz gibt z.B. bei Betriebssydteme, Treiber, virtuelle Maschinen etc. Im Bereich der Anwendungsprogrammierung gilt das gleiche, allerding verliert C++ hier an Bedeutung und wurde mit der Zeit von C# und Java verdrängt.

### Engines

Im Bereich der Anwendungsprogrammierung ist C++ allerdings noch beliebt bei der Entwicklung von Engines und Spielen. Beispiele hierfür sind Unity und die Unreal Engine.

### IDEs

Die meisten großen IDEs unterstützen mittlerweile C++, so zum Beispiel

* MS Visual Studio
* MS Visual Studio Code
* Jetbrains CLion
* Netbeans
* Vim
* etc.

### Vergleich zu C#

Der größte Unterschied zu C++ ist das Fehlen eines Garbage Collectors, sodass man sich selst um Speicher-Management kümmern muss. Anders als bei C# hat man außerdem die Möglichkeit Pointer zu benutzen, die man allerdins selbst managen muss.
In C++ ist man zudem nicht an Objektorientierte Programmierung gebunden und kann prozedurale Programme erstellen.
Da beide Sprachen von C abstammen sind Syntax und Programmaufbau vergleichbar.

## C++

### Generelle Syntax

#### Preprocessor Directives

Wie C# auch hat C++ einen sogenannten Preprocessor, der vor dem Kompilieren das Programm analysiert und somit entscheidet welche Teile überhaupt kompilert werden.

```cpp
    // häufig genutzte Anweisungen (Directives)
    #include <modul>

    #define name "wert"

    #if WINDOWS
        ...
    #elif LINUX
        ...
    #else
        ...
    #edif
```

#### Module importieren

Alle Dateien, die nicht Teil des aktuellen Projektes sind müssen importiert werden. Dies kann in Form von Modulen oder einzelnen Dateien geschehen.

```cpp
    // <> wenn das Modul im global installiert ist
    #include <modul/datei>
    // "" wenn das Modul im Projekt liegt
    #include "modul/datei"
```

#### Variablen

```cpp
    int my_int = 1;
    float my_float = 1.0f;
    const char* my_string = "string";

    auto my_double = 1.0
```

#### Funktionen

```cpp
    // <rückgabetyp><name>(<parameter>) {...}

    // pass by value
    int add(int a, int b) {
        return a + b;
    }

    // pass by reference
    int sub(int &a, int &b) {
        return a - b;
    }
```

#### Abfragen und Schleifen

```cpp
    if 1 == true {}
    if 0 == false {}

    if 1 != false {}

    if 1 == true && 0 == false {}

    if 1 == true || 0 == false {}

    for(auto i = 0; i < limit; i++) {}

    for(auto x : arr) {}

    while true {}
```

### Collections

Alle Collections, die keine Arrays sind müssen importiert werden.

```cpp
    // Array
    int arr_empty[4];
    int arr_filled[] = {1, 2, 3, 4};

    // Array iterieren
    for(int i : arr_filled) {
        int x = i;
    }

    for(int i = 0; i < sizeof arr_filled / sizeof *arr_filled; i++) {
        int x = arr_filled[i];
    }

    // Listen
    #include <vector>
    using namespace std;

    vector<int> vec_empty = vector<int>(4);
    vector<int> vec_filled = {1, 2, 3, 4};

    // Liste iterieren
    for(int i : vec_filled) {
        int x = i;
    }

    for(int i = 0; i < vec_filled.size(); i++) {
        int x = vec_filled[i];
    }

    for(vector<int>::iterator it = vec_filled.begin(); it != vec_filled.end(); it++) {
        int x = *it;
    }

    // Liste manipulieren
    vec_filled.push_back(5); // {1, 2, 3, 4, 5}
    vec_filled[4] = 6; // {1, 2, 3, 4, 6}
    vec_filled.erase(6); // {1, 2, 3, 4}
```

### Klassen, Structs und Vererbung

In C++ gibt es classes und structs. Deren einziger Unterschied ist aber, dass Felder in Klassen standardmäßig private sind und Felder in structs standardmäßig public sind.

```cpp
    class Base {
    public:
        int x;
        Base() {
            // Base objekt wird mit dem default constructor erstellt
        }

        Base(int _x) {
            x = _x;
            // Base objekt wird mit einem parametrisierten constructor erstellt
        }

        // Kurzschreibweise
        // Base(int _x) : x(_x) { }
    };

    class Derived : Base {
        // x ist hier private
    public:
        Derived() : Base() {
            // Derived objekt wird mit dem default constructor der Base Klasse erstellt
        }

        Derived(int _x) : Base(_x) {
            // Derived objekt wird mit einem parametrisierten constructor der Base Klasse erstellt
        }

        // Deconstructor, wird aufgerufen wenn die Referenz (Pointer zu dem Objekt) aus dem Memory gelöscht wird
        ~Derived {}
    };

    struct Derived : Base {
        // x ist hier public
    }
```

Es ist möglich die implizit privat vererbten Felder als public zu vererben (nur bei Klassen)

```cpp
    class Base {
    public:
        int x;
    };

    class Derived : public Base {
        // x ist nun eine public Variable
    }
```

### Pointer

Pointer sind Adressen im Arbeitsspeicher, an denen Objekte liegen.

```cpp
    // Objekt
    int i;
    // Pointer
    int *j;

    // um den Pointer von einem Objekt zu erhalten nutzt man den reference operator
    j = &i;

    // um den Wert an einem Pointer zu erhalten nutzt man den dereferce operator
    i = *j;

    // Um einen Pointer nicht immer derefernzieren zu müssen wenn man auf Funktionen oder Felder zugreifen will gibt es hierfür einen extra Operator
    p->Method();

    // mit pointern kann man außerdem durch den Arbeitsspeicher springen
    j += 4;          // z.B. 0x00000010 -> 0x00000014
    j -= sizeof int; // z.B. 0x00000014 -> 0x00000010

    // Pointer müssen gelöscht werden, wenn sie nicht mehr gebraucht werden
    delete j;
```

Die verschiedenen Arten von Pointern werden im Abschnitt [std->memory](#memory) behandelt.

### std

*std* ist die Standardbibliothek von C++ die aus vielen verschiedenen Modulen besteht. Alle Klassen und Funktionen sind unter dem Namespace std zusammengefasst.

#### string

*string* ist eine Möglichkeit Zeichenketten zu verwenden, wie man sie aus z.B. C# kennt. Ohne *string* müsste man strings selbst über ein char-Array abbilden.

```cpp
    #include <string>

    std::string name = "Peter";

    char P = name[0];

    std::string eter = name.substr(1,4);

    std::string PeterMeier = name + "Meier";
```

#### stdio

*stdio* bietet die Möglichkeit über die Standard Input/Output Konsole mit dem Nutzer zu interagieren.

```cpp
    #include <stdio>

    // Ausgeben
    std::cout << "Nachricht";

    // Ende der Zeile (\n)
    std::endl;

    // Eingabe
    std::string name;
    std::cin >> name;
    std::cout << "Hallo " << name << "!" << std::endl;
```

#### memory

*memory* enthält Klassen, die das Speichermanagement erweitern und teilweise vereinfachen, indem sie unter Anderem neue Arten von Pointern einführen, die sog. smart pointer.

##### Shared Pointer

Diese Pointer räumen sich automatisch auf, sobald ihr sog. reference couter auf 0 steht, also wenn kein anderes Objekt mehr auf sie Zugreift. Dies kann das Ende einer Funktion oder einer Klasse sein. Er kann außerdem beliebig viele Referenzen zum gleichen Objekt speichern.

```cpp
    #include <memory>

    class Example {
    public:
        Example(int i, int j) {}
    };

    int main() {
        // Die Parameter der Funktion make_shared sind automatisch die des Constructors der Klasse.
        std::shared_ptr<Example> example = std::make_shared<Example>(1, 2);
        std::shared_ptr<Example> example2 = example; // Es gibt nun zwei Referenzen zu dem gleichen Objekt
    } // <- Das Objekt wird hier automatisch gelöscht, da example und example2 hiernach nicht mehr gültig sind
```

##### Unique Pointer

Wie Shared Pointer räumen sich Unique Pointer automatisch auf, sobald ihr reference counter auf 0 steht. Der Unterschied ist allerdings, dass der reference counter maximal auf 1 stehen kann, es also nur eine Referenz zu jedem Objekt geben kann.

```cpp
    #include <memory>

    class Example {
    public:
        Example(int i, int j) {}
    };

    int main() {
        // Die Parameter der Funktion make_unique sind automatisch die des Constructors der Klasse.
        std::unique_ptr<Example> example = std::make_unique<Example>(1, 2);
        std::unique_ptr<Example> example2 = example; // Fehler, da es bereits eine Referenz zu dem Objekt gibt (example) und es nur eine geben darf
    } // <- Das Objekt wird hier automatisch gelöscht, da example hiernach nicht mehr gültig ist
```

##### Weak Pointer

#### function
