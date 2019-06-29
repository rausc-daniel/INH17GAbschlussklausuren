# IAK und KIK Lernzettel

## Inhalt

* [HTML](#html)
  * [Aufbau einer HTML-Datei](#aufbau-einer-html-datei)
  * [Einbinden von Dateien](#einbinden-von-dateien)
  * [Allgemein wichtige Tags](#allgemein-wichtige-tags)
  * [Formulare](#formulare)
  * [Semantische Container](#semantische-container)
* [CSS](#css)
  * [Selektoren](#selektoren)
  * [Allgemein wichtige Regeln](#allgemein-wichtige-regeln)
  * [Positionierung](#positionierung)
  * [Pseudoklassen](#pseudoklassen)
  * [Responsives Design](#responsives-design)
* [JavaScript](#javascript)
  * [Generelle Syntax](#generelle-syntax)
  * [Arrays und Objekte](#arrays-und-objekte)
  * [Constructor Functions](#constructor-functions)
  * [Intervalle](#intervalle)
* [JQuery](#jquery)
  * [Objekte Selektieren](#objekte-selektieren)
  * [Seiteninhalt und Style modifizieren](#seiteninhalt-und-style-modifizieren)
  * [Maus und Tastaturinput](#maus-und-tastaturinput)
  * [Attribute und Klassen](#attribute-und-klassen)
  * [Formulare auslesen](#formulare-auslesen)

## HTML

### Aufbau einer HTML-Datei

Eine HTML-Datei besteht aus zwei Teilen, dem *head* und dem *body*. Der *head* enthält Meta-Informationen und zusätzliche Dateien, die die Seite benötigt. Er kann außerdem Style-Attribute haben.
Der *body* besteht aus den sichtbaren Informationen der Website.

```html
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Beispiel Dokument</title>
    <style>
        * {
            
        }
    </style>
</head>
<body>
    <h1>Beispiel Dokument</h1>
</body>
</html>
```

### Einbinden von Dateien

Websites benötigen oft Daten, die nicht in HTML abgebildet werden können. In HTML-Dateien können deshalb andere Dateien und deren Inhalt eingebunden werden.

```html
    <!-- statische Dateien -->
    <link src="" rel="" type="" />
    <!-- <link src="css/style.css" rel="stylesheet" type=""text/css /> -->

    <!-- Skripte -->
    <script href=""></script>
```

### Allgemein wichtige Tags

#### Text

```html
    <!-- Überschriften -->
    <h1>Hauptüberschrift</h1>
    <h2>Unterüberschrift</h2>
    <h3>Unterüberschrift</h3>
    <h4>Unterüberschrift</h4>
    <h5>Unterüberschrift</h5>
    <h6>Unterüberschrift</h6>

    <!-- Website Inhalt -->
    <p>Text</p>

    <!-- Text formattieren -->
    <b>Fett</b>
    <i>Kursiv</i>
    <s>Durchgestrichen</s>

    <!-- Zeilenumbruch -->
    <br />
```

#### Container

```html
    <!-- Container, der über die gamze Seite geht -->
    <div></div>

    <!-- Container, der sich der Länge des Inhalts anpasst -->
    <span></span>
```

#### Links

```html
    <a href=""></a>
    <!-- <a href="https://www.google.com">Google</a> -->
```

#### Bilder

```html
    <img src="" alt="">
    <!-- <img src="img/image.jpg" alt="Das Bild konnte nicht angezeigt werden"> -->
```

#### Verschiedenes

```html
    <!-- Horizontale Linie -->
    <hr />
```

#### Listen

```html
    <!-- Geordnet -->
    <ol>
        <li>Item</li>
        <li>Item</li>
    </ol>

    <!-- Ungeordnet -->
    <ul>
        <li>Item</li>
        <li>Item</li>
    </ul>
```

#### Tabellen

```html
    <table>
        <!-- Überschriften -->
        <thead>
            <tr>
                <td>Überschrift Spalte 1</td>
                <td>Überschrift Spalte 2</td>
                <td>Überschrift Spalte 3</td>
            </tr>
        </thead>
        <!-- Zellen -->
        <tbody>
            <tr>
                <td>Zeile 1 - Spalte 1</td>
                <td>Zeile 1 - Spalte 2</td>
                <td>Zeile 1 - Spalte 2</td>
            </tr>
            <tr>
                <td>Zeile 2 - Spalte 1</td>
                <td>Zeile 2 - Spalte 2</td>
                <td>Zeile 2 - Spalte 3</td>
            </tr>
        </tbody>
    </table>
```

### Formulare

```html
    <form action="#" method="get|post">
        <fieldset>
            <input type="text" name="" id="" placeholder="Text" autofocus>
            <input type="email" name="" id="" placeholder="E-Mail">
            <input type="tel" name="" id="" placeholder="Telefonnummer">
            <input type="password" name="" id="" placeholder="Passwort">
            <input type="date" name="" id="">
        </fieldset>
        <fieldset>
            <label>Checkbox<input type="checkbox" name="" id="" value="true"></label>
            <label>Radio Button 1<input type="radio" name="radio" id="" value="1" checked></label>
            <label>Radio Button 2<input type="radio" name="radio" id="" value="2"></label>
            <label>Radio Button 3<input type="radio" name="radio" id="" value="3"></label>
            <input type="submit" name="" id="" value="Abschicken">
        </fieldset>
    </form>
```

![Form](https://github.com/rausc-daniel/INH17GAbschlussklausuren/blob/master/IAK_und_KIK/img/form.png)

### Semantische Container

Für bestimmte Container, die häufig genutzt werden gibt es spezielle Tags.

```html
    <header>
        <nav></nav>
    </header>
    <section></section>
    <article></article>
    <aside></aside>
    <footer></footer>
```

![Semantische Container](https://github.com/rausc-daniel/INH17GAbschlussklausuren/blob/master/IAK_und_KIK/img/semantic_container.png)

## CSS

CSS oder Cascading Stylesheet kann genutzt werden um das Aussehen und Teile des Verhaltens (z.B. simple Animationen) einer Website zu beeinflussen.

### Selektoren

```css
    /* Alle Elemente im Body */
    * {

    }

    /* Ein Element */
    name {

    }

    /* Alle Elemente mit dieser Klasse */
    .class {

    }

    /* Das Element mit dieser ID */
    #id {

    }

    /* Alle Elemente, die in einem bestimmten Element sind */
    element tochterElement {

    }

    /* Mehrere verschiedene Elemente */
    element1, element2, element3 {

    }

    /* Alle Elemente, deren Attribut ein bestimmtes Value hat */
    element[attr=value] {

    }
```

### Allgemein wichtige Regeln

CSS hat das sog. Box-Modell, was bedeutet, dass alle Elemente automatisch um ihren Rahmen, ihr Padding und ihre Border größer sind.
Alle Elemente haben außerdem einen vordefinerten Margin und ein vordefiniertes Padding.

```css
    element {
        /* Box-Modell ausschalten */
        box-sizing: border-box;

        /* Größe */
        widht: breite;
        min-width: minimale breite;
        max-width: maximale breite;

        height: höhe;
        min-height: minimale höhe;
        max-height: maximale höhe;

        /* Platzierung */
        margin: rundrum;
        margin: oben/unten rechts/links;
        margin: oben rechts unten links;

        padding: rundrum;
        padding: oben/unten rechts/links;
        padding: oben rechts unten links;

        /* Text */
        font-family: schriftart;
        font-size: größe;
        font-weight: dicke;
        font-style: style;
        text-decoration: stil der line;
        text-aling: ausrichtung;
        color: textfarbe;
        line-height: zeilenabstand;

        /* Umrandungen */
        border: width style color;
        border-collapse: collapse;

        /* Hintergründe */
        background-color: farbe;

        background-image: url(url);
        background-position: x y;
        background-repeat: repeat | repeat-x | repeat-y;
        background-size: größe | (x y);

        background: farbe | (url(url) repeat size);
    }
```

### Positionierung

```css
    element {
        /* absolute: Objekt kann frei positioniert werden */
        /* relative: Element ist der Referenzpunkt für alle Kindelemente */
        position: absolute | relative;
        left: abstand vom linken rand;
        right: abstand vom rechten rand;
        top: abstand vom oberen rand;
        bottom: abstand vom unteren rand;

        /* Das Objekt liegt am linken bzw. rechten Rand des Referenzobjektes */
        float: left | right;

        /* Beide Methoden sorgen dafür, dass das Element keinen Platz mehr im Dokument einnimmt und über allen anderen Objekten liegt */

        z-index: wie weit hinten das Objekt liegt;

        /* Mittig im Container */
        margin: auto;
        text-align: center;
    }
```

### Pseudoklassen

```css
    element:first {
        /* Das erste Element dieses Typs */
    }

    element:last-of-type {
        /* Das letzt Element dieses Typs */
    }

    element:first-child {
        /* Das erste Child dieses Element */
    }

    element:last-child {
        /* Das letzte Child dieses Element */
    }

    element:nth-child(n) {
        /* Das n'te Child dieses Element */
        /* nth-child(1) -> das erste */
        /* nth-child(2n | even) -> alle gerade */
        /* nth-child(2n + 1 | odd) -> alle ungeraden */
    }

    element:before {
        /* Content, der vor dem Element angezeigt wird */
        /* oft Bilder, Icons oder Anführungszeichen */
    }

    element:after {
        /* Content, der nach dem Element angezeigt wird */
    }

    element:hover {
        /* Wenn die Maus über dem Element ist */
    }

    element:checked {
        /* Wenn eine Checkbox oder ein Radio-Button ausgewählt ist */
    }

```

### Responsives Design

## JavaScript

### Generelle Syntax

### Arrays und Objekte

### Constructor Functions

### Intervalle

## JQuery

### Objekte Selektieren

### Seiteninhalt und Style modifizieren

### Maus und Tastaturinput

### Attribute und Klassen

### Formulare auslesen
