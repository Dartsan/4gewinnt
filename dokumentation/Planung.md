# Planung
## Klassendiagramm
In unserem Vier-Gewinnt-Spiel werden wir vermutlich folgende Klassen benötigen:

Die abstrakte Klasse ***Player*** welche alle Spieler darstellen soll. Das Attribut **symbol** initialisiert das Symbol, mit welchem die Spielsteine am Spielfeld dargestellt werden, wir haben uns für die Symbole "X" und "O" entschieden. Das Attribut **win** gibt an, ob der Spieler gewonnen hat oder nicht, dieser wird auf True gesetzt, sobald der Spieler gewonnen hat. Das Attribut **nr_wins** gibt die Anzahl der Siege des Spielers an, dieses Attribut wird bei jedem Sieg des Spielers um eins erhöht. Die Methode **throw_token** wird verwendet, um einen Spielstein des Spielers in das Spielfeld zu werfen. Die Methode **add_win()** erhöht die Variable **nr_wins** bei einem Sieg des Spielers.

Die Klasse **Human** leitet sich von der ***Player***-Klasse ab und ist für alle menschlichen Spieler. Dieser initialisiert seinen Namen (oder einen Username) unter dem Attribut **name**. Mit der Methode **end_game()** wird das Spiel auf Wunsch des Spielers beendet. Ansonsten besitzt die Klasse natürlich auch die vererbten Attribute und Methoden der ***Player***-Klasse.

Die Klasse **Bot** leitet sich ebenfalls von der ***Player***-Klasse ab und wird für einen nicht-menschlichen (Computer-)Spieler verwendet. Das Attribut **activated** wird auf True gesetzt, wenn gegen einen Computer gespielt wird. Das Attribut **difficulty_level** gibt den Schwierigkeitsgrad des Bots an. Ansonsten werden auch hier die Attribute und Methoden der ***Player*** Klasse vererbt.

Die Klasse **Field** wird verwendet um das Spielfeld zu erstellen. Diese enthält zwei bereits im Vorhinein bekannte Attribute, wobei **rows** für die Anzahl der Reihen steht (6) und **columns** für die Anzahl der Spalten am Spielfeld (7). Die Methode **show_field()** wird verwendet, um das aktuelle Spielfeld auszugeben, die Methode **clear_field()** leert das Spielfeld nach jeder abgeschlossenen Runde. Die Methode **create_field()** wird am Anfang verwendet, um das Spielfeld zu erstellen.
