# 4gewinnt

Hier finden Sie die 4Gewinnt Umsetzung im Rahmen der Lehrveranstaltung Softwareentwicklungsmodelle 1 von Kevin Herunter und Oliver Tanzer.
Vier Gewinnt sollte für jeden ein Begriff sein. Falls Sie die Spielerklärung aber benötigen finden Sie diese unter:
<https://www.spielregeln-spielanleitungen.de/spiel/vier-gewinnt/>.

Ziel dieses Projektes ist aber nicht nur die Umsetzung der Anwendung, sondern vielmehr der Prozess um die Software zu erstellen. Sprich man sollte nach der Erstellung dieses Projektes mehr Praxiswissen im Bereich Softwareentwicklungsmodelle besitzen und dieses anwenden können. Im genaueren bedeuted dies, dass man sich mit Git, Dokumentation, Klassendiagrammen und Unit Tests genauer auseinandersetzen muss. Außerdem wird ein Software Design Pattern und pro Teammitglied ein Design Pattern genauer beschrieben. Diese findet man unter Dokumentation


## Spielerklärung

Um zu spielen, wird die Datei **connectfour.py** ausgeführt. Danach kann man zwischen zwei Spielmodi auswählen:
- **PVP**: Um zwei Spieler gegeneinander antreten zu lassen, wählen Sie den Spielmodus *PVP* aus (alles in Großbuchstaben)
- **PCV**: Um gegen einen Computer zu spielen, wählen Sie den Spielmodus *PCV* aus (alles in Großbuchstaben)

Um das Spiel zu verlassen, geben Sie **Exit** ein (Exit muss diesesmal und auch infolge immer mit einem großen E am Anfang eingegeben werden)

Die Spielsteine werden mithilfe der Symbole **X** und **O** dargestellt, während ein leeres Feld mit **-** dargestellt wird.

### PVP-Spielmodus
Wenn Sie sich für den Spieler gegen Spieler Modus entschieden haben, werden am Anfang des Spiels die Namen der beiden Spieler abgefragt. Diese kann man beliebig wählen. Sollte sich einer der beiden Spieler noch gegen das Spiel entschieden haben, kann das Spiel mittels der Eingabe von *Exit* und der Bestätigung durch *Enter* beendet werden.
Nachdem beide Spieler einen Namen gewählt haben, mit dem sie während des Spiels angesprochen werden möchten, wird das Spielfeld angezeigt und der erste Spieler beginnt mit seinem ersten Zug:
- Um einen Spielstein zu werfen, wählen Sie eine Spalte aus, die nicht voll ist. Das können Sie machen, indem Sie eine Zahl zwischen 1 und 7 auswählen und danach mit *Enter* bestätigen. (Die Nummer der Spalte wird über dem Spielfeld eingeblendet)
- Um die Runde zu beenden, geben Sie *Exit* ein. Um das Spiel komplett zu beenden, danach erneut *Exit* eingeben.
- Auf die Spielregeln von Vier Gewinnt wird in dieser Spielererklärung nicht genauer eingegangen. Sollten diese nicht bekannt sein, bitte unter dem Link im ersten Absatz dieses Files nachlesen.

Sobald der Spieler seinen Zug mit *Enter* bestätigt hat, wird das Spielfeld erneut ausgegeben, natürlich jetzt mit dem zuvor geworfenen Spielstein.
Danach ist der andere Spieler am Zug. Das geschieht so lange bis *Exit* eingegeben wird, ein Spieler das Spiel gewonnen hat oder das Spielfeld voll mit Steinen ist und das Spiel mit Unentschieden endet. Bei einem Sieg wird der Gewinner ausgegeben und das Spiel beendet. Bei einem Unentschieden wird ausgegeben, dass das Spiel mit einem Unentschieden endet und das Spiel wird beendet.
Bei allen drei Möglichkeiten (Sieg, Unentschieden und *Exit*) gelangt man zurück zur Auswahl des Spielmodus und man kann wieder entweder *PVP* oder *PVC* auswählen oder das Spiel mittels *Exit* ganz verlassen.

### PCV-Spielmodus
Sollten Sie sich für das Spiel gegen einen Computer entschieden haben, wird am Anfang des Spiels der Name des Spielers abgefragt. Dieser kann beliebig gewählt werden. Sollte man sich noch gegen das Spiel entschieden haben, kann es mit *Exit* beendet werden.
Nachdem der Spieler seinen Nickname gewählt hat, kann man den Schwierigkeitsgrad des Computergegners wählen. (auch hier kann das Spiel mittels *Exit* noch beendet werden) Der Schwierigkeitsgrad muss zwischen 1 und 7 liegen, wobei 1 den einfachsten Gegner darstellt und 7 den am schwersten zu besiegenden Gegner (eine genauere Beschreibung des Computergegners befindet sich im Dokumentationsordner).
Nach der Auswahl des Schwierigkeitsgrades gelangt man zum eigentlichen Spiel:
Zuerst wird das Spielfeld ausgegeben, es beginnt danach der menschliche Spieler.
- Dieser wählt mittels eingabe einer Zahl zwischen 1 und 7 eine nicht volle Spalte aus. (Die Spaltennummer wird über dem Spielbrett angezeigt)
- Mittels *Exit* kann die aktuelle Runde beendet werden. Um komplett aus dem Spiel hinauszugelangen, erneut *Exit* eingeben.

Danach ist der Computergegner an der Reihe. Dieser wählt seine Spalte je nach Schwierigkeitsgrad zufällig oder nicht zufällig und wirft dort seine Spielsteine hinein.
Danach wird das Spielfeld wieder (mit dem soeben vom Computer geworfenen Spielstein) ausgegeben und der menschliche Spieler ist wieder an der Reihe.
Das wiederholt sich so lange, bis das Spiel von einem Spieler gewonnen wird, das Spielfeld voll ist (und das Spiel somit Unentschieden endet) oder der menschliche Spieler *Exit* eingibt.
Bei allen drei Möglichkeiten (Sieg, Unentschieden und *Exit*) gelangt man zurück zur Auswahl des Spielmodus und man kann wieder entweder *PVP* oder *PVC* auswählen oder das Spiel mittels *Exit* ganz verlassen.

Wir hoffen, Sie haben Spaß mit unserem Spiel!
