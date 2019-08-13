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
  * [Constructor Functions](#constructor-functions)
  * [Intervalle](#intervalle)
* [jQuery](#jquery)
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

#### Relative Einheiten

Anstatt Positionen und Größen in Pixel anzugeben empfiehlt sich relative Enheiten zu nutzen. Diese sind Prozent (%) Viewport-Width (vw) bzw. Viewport-Height (vh). Prozent bezieht sich auf das Elternelement, während vw und vh vom gesamten Bildschirm des Gerätes abhängen.

#### Grid

```html
    <div class="grid-container">
        <div class="item" id="1"></div>
        <div class="item" id="2"></div>
        <div class="item" id="3"></div>
        <div class="item" id="4"></div>
    </div>
```

```css
    .grid-container {
        display: grid;
        grid-template-rows: 200px 1fr 1fr;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        grid-row-gap: 10px;
        grid-column-gap: 20px;
        /* grid-gap: row col */
    }

    .item {
        background: grey;
    }

    #1 {
        grid-column-start:1;
        grid-column-end:5;
        grid-row-start:1;
        grid-row-end:2;
    }

    #2 {
        grid-column-start:1;
        grid-column-end:4;
        grid-row-start:2;
        grid-row-end:3;
    }

    #3 {
        grid-column-start:4;
        grid-column-end:5;
        grid-row-start:2;
        grid-row-end:3;
    }

    #4 {
        grid-column-start:1;
        grid-column-end:5;
        grid-row-start:3;
        grid-row-end:4;
    }
```

![Grid](https://github.com/rausc-daniel/INH17GAbschlussklausuren/blob/master/IAK_und_KIK/img/grid.png)

#### Media Queries

Wenn sich Elemente bei verschiedenen Bildschirmbreiten anders verhalten sollen nutzt man sogenannte Media-Queries.

```css
    /* Alle Geräte deren Bildschirm kleiner als 1140px ist */
    @media screen (max-width: 1440px) {
        /* Style Rules */
    }
```

Es empfiehlt sich die folgenden Media-Queries zu implementieren.

```css
    @media screen (max-width: 599px) {
        /* Style Rules */
    }

    @media screen (min-width: 600px) {
        /* Style Rules */
    }

    @media screen (min-width: 980px) {
        /* Style Rules */
    }

    @media screen (min-width: 1260px) {
        /* Style Rules */
    }
```

## JavaScript

### Constructor Functions

Constructor Functions sind (neben Klassen) eine Möglichkeit Objekte vorzudefinieren.

```js
function Person(first_name, last_name, age) {
    this.first_name = first_name;
    this.last_name = last_name;
    this.age = age;

    this.increaseAge = function() {
        this.age++;
    }
}

john = new Person("John", "Doe", 24);
john.increaseAge();

// John ist jetzt 25
```

### Intervalle

Intervalle können mit einer festen Rate folgendermaßen deklariert werden.

```js
    var sleepTime = 16.667; // Zeit zwischen den Intervallen in ms (60fps)
    setInterval(function() {
        // Was im Intervall passieren soll
    }, sleepTime)
```

Soll ein Intervall so oft wie möglich ausgeführt werden kann die *requestAnimationFrame*-Methode rekursiv genutzt werden.

```js
    // time ist die aktuelle Uhrzeit in ms, als int
    function step(time) {
        window.requestAnimationFrame(step);
    }

    window.requestAnimationFrame(step);
```

## jQuery

jQuery ist eine JavaScript Bibliothek, die häufig zusammen genutzte Befehle in Funktionen bündelt und somit DOM-Manipulation erleichtert und schneller macht.
jquery kann entweder im *&lt;head&gt;* oder am Ende des *&lt;body&gt;* Tags eingebunden werden. Wird es im *&lt;head&gt;* eingebunden muss darauf gewartet werden, dass die komplette Website geladen ist.

```js
    $(document).ready(function(){
        /* Hier der jQuery-Code */
    });

    // Kurzschreibweise
    $(() => {
        /* Hier der jQuery-Code */
    });
```

### Objekte Selektieren

Um DOM-Objekte zu selektieren und in JQuery-Objekte zu transformieren nutzt man die *$*-Funktion;

```js
    var obj = $("css-Selektor");

    // Fenster
    var win = $(window);

    // sichtbarer Inhalt
    var doc = $(document)

    // Wenn es von einem Elemt mehrere gibt kann über die Liste iteriert werden
    $("element").each((index) => {
        var current = $(this);
    })
```

### Seiteninhalt und Style modifizieren

```js
    // HTML auslesen
    var html = $("element").html();
    // HTML setzen
    $("element").html("text");

    // Elemente dynamisch erzeugen
    var elem = $("<tag></tag>");
    // Element anhängen
    $("body").prepend(elem);
    $("body").append(elem);

    // Style auslesen
    var style = $("element").css("rulename");
    // Eine Style-Rule setzen
    $("element").css("rulename", "rulewert");
    // Mehrere Style-Rules setzen
    $("element").css({
        "rulename": "rulewert",
        "rulename": "rulewert"
        });
```

### Maus und Tastaturinput

```js
    // Maus auf einem Element
    $("element").click(() => { });
    $("element").dblclick(() => { });

    $("element").mousedown(() => { });
    $("element").mouseup(() => { });

    $("element").mousemove(() => { });

    $("element").mouseover(() => { });
    $("element").mouseout(() => { });

    // Tastatur
    $(document).keydown(e => { });
    $(document).keypress(e => { });
    $(document).keyup(e => {
        var keyCode = e.which;
    });
```

### Attribute und Klassen

```js
    // Attribut auslesen
    var attr = $("element").attr("attributname")
    // Ein Attribut setzen
    $("element").attr("attributname", "attributwert")
    // Mehrere Attribute setzen
    $("element").attr({
        "attributname": "attributwert",
        "attributname": "attributwert"
        });
    // Das value-Attribut hat einen shorhand
    var val = $("element").val();

    // Klasse hinzufügen
    $("element").addClass("klassenname");
    // Klasse entfernen
    $("element").removeClass("klassenname");
    // Klasse togglen
    $("element").toggleClass("klassenname");
```

### Formulare auslesen

```js
    $("input[type=text]").val();
    $("select").val();
    $("input[type=radio]:checked").val();
    $("input[type=checkbox]:checked").each(() => {
        text += $(this).val() + " ";
    });
```

## Canvas

Um die Canvas nutzen zu können ist mindestens folgendes HTML-Dokument von Nöten (jQuery kann vermieden werden).

```html
    <head>
        <script href="jQuery.js"></script>
    </head>
    <body>
        <canvas width="" height=""></canvas>
        <script href="canvas.js"></script>
    </body
```

Das Setup für eine responsive Canvas sieht folgendermaßen aus.

```js
    // canvas.js

    $(() => {
        const win = $(window);

        const canvasPercentage = {
            x: 0.5,
            y: 0.5
        };

        const canvas = $("canvas");
        const context = canvas[0].getContext("2d");

        // wird jeden Frame ausgeführt
        function renderLoop() {
            // Code zum Rendern
        }

        // Größe der Canvas setzen
        canvas.attr("width", win.width() * canvasPercentage.x);
        canvas.attr("height", win.height() * canvasPercentage.y);

        // Größe der Canvas anpassen, wenn das Fenster vergrößert wird
        win.resize(() => {
            canvas.attr("width", win.width() * canvasPercentage.x);
            canvas.attr("height", win.height() * canvasPercentage.y);
        });

        // 16.667ms timeout jeden Aufruf sind 60fps
        setInterval(renderLoop, 16.667);
    });
```

### Formen

```js
    function toRadians(angle) {
        return angle * Math.PI / 180;
    }

    function renderLoop() {
        // rect(x, y, w, h)
        context.fillRect(100, 100, 50, 50);
        context.strokeRect(100, 200, 50, 50);

        // arc(x, y, r, start_angle, end_angle, clockwise?)
        // jeder neue arc muss begonnen werden
        context.beginPath();
        // Winkel müssen im Bogenmaß angegeben werden (pi = 180° = 1/2 Kreis)
        context.arc(200, 100, 25, 0, Math.PI * 2);
        // jeder arc muss einzeln gefüllt werden
        context.fill();

        context.beginPath();
        context.arc(200, 200, 25, 0, Math.PI, false);
        context.stroke();

        // moveTo(x, y) und lineTo(x, y)
        context.beginPath();
        // moveTo bewegt den cursor, zeichnet aber keine Linie
        context.moveTo(275, 75);
        context.lineTo(250, 125);
        context.lineTo(300, 125);
        // closePath verbindet den letzten Punkt mit dem Ersten
        context.closePath();
        context.fill();
    }
```

### Sprites

#### Animationen

#### Tilemap

### Prallaxeffekt

### Collisionsabfrage

### Objekte um Pivot rotieren
