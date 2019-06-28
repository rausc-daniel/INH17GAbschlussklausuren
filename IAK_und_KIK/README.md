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
  * [Allgemein wichtige Attribute](#allgemein-wichtige-attribute)
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
            <input type="checkbox" name="" id="" value="true">
            <input type="radio" name="radio" id="" value="1" checked>
            <input type="radio" name="radio" id="" value="2">
            <input type="radio" name="radio" id="" value="3">
            <input type="submit" name="" id="" value="Abschicken">
        </fieldset>
    </form>
```

<form action="#" method="get|post">
    <fieldset>
        <input type="text" name="" id="" placeholder="Text" autofocus> <br />
        <input type="email" name="" id="" placeholder="E-Mail"> <br />
        <input type="tel" name="" id="" placeholder="Telefonnummer"> <br />
        <input type="password" name="" id="" placeholder="Passwort"> <br />
        <input type="date" name="" id=""> <br />
    </fieldset>
    <fieldset>
        <label>Checkbox <input type="checkbox" name="" id=""></label> <br />
        <label>Radio Button 1<input type="radio" name="radio" id="" checked></label> <br />
        <label>Radio Button 2<input type="radio" name="radio" id=""></label> <br />
        <label>Radio Button 3<input type="radio" name="radio" id=""></label> <br />
        <input type="submit" name="" id="" value="Abschicken">
    </fieldset>
</form>

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

### Selektoren

### Allgemein wichtige Attribute

### Positionierung

### Pseudoklassen

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
