Während unserer Arbeit am Projekt haben wir folgende Veränderungen an unserer Planung und am Klassendiagramm vorgenommen:

Wir haben uns dazu entschlossen, die Attribute **win** und **nr_wins** aus der abstrakten Basisklasse ***Player*** zu entfernen, da wir die Gewinnerkennung über die **Field**-Klasse implementiert haben und den Sieger dann direkt in der Spiellogik bekanntgeben (und somit auch die Anzahl der Siege pro Spieler nicht mitzählen).
Da wir die Siege nicht mitzählen, wird auch die Methode **add_win()** nicht mehr benötigt.

Aus der **Human**-Klasse wurde die **end_game()**-Methode entfernt, da diese Funktion ebenfalls direkt in der Spiellogik implementiert wurde.

Bei der Klasse **Bot** wurde das Attribut **activated** entfernt, da direkt in der Spiellogik festgelegt wird, ob gegen einen Computer gespielt wird und es somit nicht nötig ist, in der Klasse zu speichern, ob dieser aktiviert ist. Das Attribut **schwierigkeitsgrad** haben wir nur unbenannt in **difficulty_level**, welches die Wert 1, 2 oder 3 annehmen kann.
Wir benötigen in der **Bot**-Klasse nun die Methode **choose_difficulty()**, um den Schwierigkeitsgrad zu initialisieren.

In der **Field**-Klasse sind die beiden Methoden **check_win()** und **check_draw()** hinzugekommen, um das aktive Spielfeld auf ein mögliches Ende des Spiels zu überprüfen.

Eine Übersicht über das aktualisierte Klassendiagramm befindet sich im Dokumentationsordner unter **Klassendiagramm_aktualisiert_6.2.2023**
