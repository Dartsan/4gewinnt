[Bild_Problem]:https://refactoring.guru/images/patterns/content/observer/observer-comic-1-en-2x.png
[Bild_echte_Welt]:https://refactoring.guru/images/patterns/content/observer/observer-comic-2-en-2x.png
# Design Patter Tanzer
## Spectator Design Patter
Dieses Design Patter ist unter den Name Listener oder Event-Subscriber auch bekannt.
### Vorhaben
Der Sinn dieses Design Patter ist es, dass man einen abonniert Status erreichen will, sprich man will mitbekommen, 
wenn etwas bei einem anderen Objekt verändert wird. Was man mit dieser Information dann weitergehend macht, liegt an der 
Realisierung.
### Problem
Es gibt bei diesem Design zwei Hauptprobleme.
1. Man muss als Abonnent immer wieder überprüfen, ob sich bei der abonnierten Klasse etwas geändert hat.
2. Es kann vorkommen, dass man Abonnenten etwas mitteilt, dass sie nicht interessiert, sprich man erzeugt Spam.

Nachfolgendes Bild beschreibt dieses Verhalten mithilfe der Analogie von einem Kunden, welcher sich ein neues Handy
kaufen will:
![Problem][Bild_Problem]

### Lösung
Man bezeichnet die Ressource, auf welche man zugreifen will meistens als subject. Der Benachrichtiger von diesem subject 
wird oft publisher genannt und die Objekte, welche auf die Ressource zugreifen wollen werden, subscriber genannt.
Das Observer Pattern besagt, dass man entweder abonnieren oder das Abo kündigen kann. 
Die technische Umsetzung sieht meistens so aus:
1. Ein Array, damit man die Referenzen auf das Objekt speichern kann
2. öffentliche Methoden um Abonnenten hinzufügen oder entfernen zu können

Wenn etwas Wichtiges passiert, benachrichtigt der publisher alle subscriber. 

### Analogie aus der echten Welt
Das beste Beispiel aus der echten Welt ist das Abo-System für Zeitungen. Sobald man eine Zeitung abonniert hat muss 
man nicht mehr in den Laden fahren, um zu schauen, ob die Zeitung verfügbar ist. Entweder erhält man eine Mail, wenn die
nächste Ausgabe verfügbar ist, oder die nächste Aufgabe wird direkt vor die Haustüre geliefert. Der Zeitungshersteller 
weiß dadurch genau, wer die Zeitung abonniert hat und die LeserInnen haben jederzeit die Möglichkeit diesen Newsletter
zu abonnieren beziehungsweise dieses Abo zu kündigen. Dieses Bild zeigt dieses Verhalten:
![Analogie_aus_der_echten_Welt_Bild][Bild_echte_Welt]

### Ablauf und Struktur

Hier wird oft das Wort Event verwendet. Als Event bezeichnet man, wenn sich Zustände ändern oder gewisse Methoden
aufgerufen werden.

1. Der Publisher teilt Ressourcen, welche er teilen will. Dies wird realisiert, wenn ein Event auftritt. 
Außerdem enthält er ein Interface, damit Benutzer kündigen oder abonnieren können.
2. Wenn ein Event auftritt, werden mithilfe des Interfaces alle Endbenutzer benachrichtigt.
3. Das subscriber Interface beschreibt die Update-Methode für die Endbenutzer. Es können außerdem zusätzliche 
Informationen mithilfe dieser Methode den Endbenutzer mitgeteilt werden.
4. Concret Subscriber ist eine weitere Klasse. Diese wird verwendet, um Aktionen durchzuführen, wenn das Update 
Interface aufgerufen wird. Der Publisher ist nicht mit dieser Klasse verbunden.
5. Der Endbenutzer braucht meistens zusätzliche Informationen, damit er die update-Methode durchführen kann. Diese
Informationen erhält er meistens vom Publisher. 
6. Der Endbenutzer initialisiert publisher und subscriber Klassen getrennt und registriert die subscriber für zukünftige
Änderungen, welche beim publisher passieren.

### Anwendungsbereiche

- Verwendung bei Ketten von Veränderungen. Wenn ein User zum Beispiel einen Button auf einer Website benutzt, sollen
viele Klassen aktualisiert werden, oder benachrichtigt werden, wenn dieser Button benutzt wurde.
- Verwendung wenn Klassen Beziehungen nur für gewissen Zeitraum aufgebaut werden sollen. Dies wird mithilfe diesem 
Pattern realisiert, da man dynamisch abonnieren oder kündigen kann.

### Vorteile

- Open/Closed Prinzip. Man muss keinen publisher Code verändern, wenn man neue Abonnenten hinzufügen will.
- Man kann Beziehungen zwischen Klassen parallel zur Laufzeit herstellen 

### Nachteile

- Abonnenten werden zufällig benachrichtigt

Quelle: <https://refactoring.guru/design-patterns/observer/>
