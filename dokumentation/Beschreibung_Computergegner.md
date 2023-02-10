# Beschreibung des Computergegners
Im Rahmen unseres Vier-Gewinnt Spiels, bei dem man auch gegen einen Computergegner spielen kann, wurde der Computergegner (auch "Bot" genannt) von uns verbesster, damit es nicht ganz so leicht ist, gegen diesen zu gewinnen.
Dabei wurde das Hauptaugenmerk darauf gelegt, dass der Computergegner einerseits selbst erkennt, wenn er dass Spiel gewinnen kann und andererseits so gut es geht verhindert, dass sein Gegner das Spiel gewinnt.
Es gibt 7 verschiedene Schwierigkeitsstufen, wobei der Computergegner mit der Schwierigkeisstufe 1 am leichtesten und der Computergegner mit der Schwierigkeitsstufe 7 am schwierigsten zu besiegen ist. Es ist aber auch gegen den Bot Level 7 durchaus möglich zu gewinnen. Eine genauere Beschreibung der einzelnen Schwierigkeitsstufen befindet sich unten.

Mit der Methode **choose_difficulty()** wird zu beginn des Spiels der Schwierigkeitsgrad des Computergegners initialisiert und in Folge im Attribut **difficulty_level** des Computerspieler-Objekts gespeichert.
Danach wird jedes mal, wenn der Computergegner an der Reihe ist, die Methode **throw_token()** des Computergegner-Objekts aufgerufen. In dieser Methode wird zuerst festgelegt, in welche Spalten es überhaupt möglich ist zu werfen (volle Spalten werden ausgenommen). Danach hängt die Auswahl der Spalte, in der er den Spielstein wirft, vom zuvor festgelegtem Schwierigkeitsgrad ab, wobei ab Schwierigkeitsstufe 2 die in der vorangegangenen Schwierigkeitsstufe festgelegten Bedingungen weiterhin zählen (Beispiel: Schwierigkeitsstufe 5 kann alles was Schwierrigkeitsstufe 4 kann, und mehr):

## Schwierigkeitsstufe 1
Der Computergegner mit der Schwierigkeitsstufe 1 wählt die Spalte, in die er seinen nächsten Spielstein wirft, zufällig aus den nicht vollen Spalten aus (dies passiert mithilfe des Moduls **random**). Er speichert die Spalte dann auf der Variable **column** und wirft den Stein mithilfe der for-Schleife ans untere Ende der ausgewählten Spalte.

## Schwierigkeitsstufe > 1
Ab Schwierigkeitsstufe 2 wird die Spalte, in die der Stein geworfen wird, anhand verschiedener Bedingungen festgelegt. Die ausgwählte Spalte wird auf der Variable **column** gespeichert und nach Prüfung aller Bedingungen mithilfe einer for-Schleife ans untere Ende der ausgewählten Spalte geworfen.
## Schwierigkeitsstufe 2
Bei der Schwierigkeitsstufe 2 wird zuerst mithilfe von zwei verschachtelten for-Schleifen und mehreren verketteten Bedingungen überprüft, ob der Computer bereits drei Steine in einer Reihe hat, zumindest eine Spalte daneben (links oder rechts) in der gleichen Reihe frei ist und der Platz unter dem freien Platz nicht frei ist (also, dass darunter entweder der Boden des Spielfelds oder ein beliebiger Spielstein ist, damit der Stein auch in der gewollten Reihe stehen bleibt). Trifft dies zu, wird die Spalte, in der sich dieser "freie Platz" zum Gewinnen befindet, unter der Variable **column** gespeichert.

Trifft das nicht zu, wird in der nächsten Bedingung wieder mithilfe von zwei verschachtelten for-Schleifen das gesamte Spielbrett überprüft, ob der Computer in einer Spalte gewinnen kann: 

