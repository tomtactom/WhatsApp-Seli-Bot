# WhatsApp Bot
> Eine API für WhatsApp zum Benutzen in externen Programmen. Das Programm basiert auf Python, mit Verwendung von Selenium.
<!--
[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]
-->
[WhatsApp](https://www.whatsapp.com/) stellt [nur für Firmen](https://www.facebook.com/business/m/whatsapp/business-api) eine API zur Verfügung. Hobbyentwickler bekommen leider keinen Zugriff darauf. Dieses Repository hilft dir dabei WhatsApp automatisiert, plattformübergreifend und mich viel mehr Möglichkeiten zu Nutzen. Dafür wird eine Brücke über [WhatsApp Web](https://web.whatsapp.com) aufgebaut und die Daten werden über [Selenium](https://www.seleniumhq.org/) abgerufen und es werden Handlungen ausgeführt.

![](https://repository-images.githubusercontent.com/194916303/125f1b00-9d09-11e9-8244-14ebb274543b)

## Installation
!!!Achtung!!!
*Es kann sein, dass das Tool noch nicht funktioniert, oder noch gar nicht vorhanden ist, da es momentan noch entwickelt wird.*

OS X & Linux: -


Windows: -


Manuell: 
1. Lade die Zip-Datei herunter und entpacke sie in gewünschten Verzeichnis
2. Installiere einige Module
```
pip install urllib
pip install pil
pip install requests
pip install io
pip install json
pip install time
pip install selenium
```
3. Lade dir die neuste Version von Google Chrome oder Chromium herunter
4. Lade dir die neuste Version von Chromedriver herunter
5. Führe die `whatsapp-bot.py` aus
```
python whatsapp-bot.py
```
## Anwendungsbeispiel

Momentan ist das Programm noch in der Entwicklungsphase, weshalb es zu Fehlern führen kann.
Es wird noch nicht empfolen es zu benutzen, da Fehler auftreten können.

## Entwicklungssetup

Lade das Repository als Zip-Datei herunter und führe es über die Konsole aus.

```
python whatsapp-bot.py
```
Scanne den QR-Code.
Wenn der QR-Code abgelaufen ist, drücke ENTER
<!--
## Version Verlauf

* 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`
* 0.1.1
    * FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
* 0.1.0
    * The first proper release
    * CHANGE: Rename `foo()` to `bar()`
* 0.0.1
    * Work in progress

## Weitere Daten

12tom12 – [](https://twitter.com/) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/12tom12](https://github.com/12tom12/)

## Contributing

1. Fork it (<https://github.com/12tom12/whatsapp-bot/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
-->
