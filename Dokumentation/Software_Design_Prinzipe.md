# Software Design Prinzipe

## Aufgabenstellung
Sie beginnen als EntwicklerIn in einem neuen Unternehmen und bekommen die Verantwortung für
ein Modul. Das Modul ist über eine lange Zeit hinweggewachsen und besteht nur aus sehr wenigen
Klassen. Die Methoden dieser Klassen sind meist sehr lange, oftmals einige hundert Zeilen oder
länger, und sie sind auch eher spärlich dokumentiert. Was für Nachteile ergeben sich für Sie durch
diesen Code? Welche grundlegenden Software Design Prinzipien werden evtl. nicht eingehalten?

## Problemlösung
Ein grundlegendes Problem ergibt sich aufgrund der eher nicht so detaillierten Dokumentation. Der Source Code ist 
ohne Dokumentation schwieriger nachvollziehen als ein Source Code mit sinnvoller Dokumentation. Dies erschwert es, wenn 
neue EntwicklerInnen an diesem Projekt weiterarbeiten müssen, da sie viel Zeit investieren müssen, um den Source Code zu
verstehen. Dadurch wird die Wartbarkeit der Software schwieriger und komplexer. Ein weiteres Problem ist, dass die 
Klassen meist sehr lange sind. Dies verletzt das "Single Responsibility" Prinzip. Dies besagt, dass eine Klasse nur eine
Aufgabe und einen Grund zur Veränderung haben soll. Dadurch hat man weniger Testfälle und kann diese leichter abdecken. 
Aufgrund dieses Prinzip gibt es auch weniger Abhängigkeiten von Klassen da weniger Funktionalitäten umgesetzt werden.
Außerdem ist der Quellcode leichter zu lesen und zu organisieren. Dieses Prinzip kann man auch für Interfaces anwenden.
Interface Segregation ist der Name dieses Prinzips. Es kann auch vorgekommen sein, dass keine Design-Pattern verwendet 
worden sind. Design Pattern sind Muster, die verwendet werden, wenn immer Probleme immer wieder vorkommen. Es gibt
drei Arten von Design Pattern:
1. Verhaltensmuster (Behavioral Pattern)
2. Erzeugungsmuster (Creational Pattern)
3. Strukturmuster (Structural Pattern)

Da wir die genaue Umsetzung aber nicht wissen, können wir nicht sagen ob eine Anwendung dieser Pattern sinnvoll gewesen
wäre.