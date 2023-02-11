# Beschreibung des Computergegners
Im Rahmen unseres Vier-Gewinnt Spiels, bei dem man auch gegen einen Computergegner spielen kann, wurde der Computergegner (auch "Bot" genannt) von uns verbesster, damit es nicht ganz so leicht ist, gegen diesen zu gewinnen.
Dabei wurde das Hauptaugenmerk darauf gelegt, dass der Computergegner einerseits selbst erkennt, wenn er dass Spiel gewinnen kann und andererseits so gut es geht verhindert, dass sein Gegner das Spiel gewinnt. Das heißt er agiert nicht selbst und kreiert keine eigenen Spielzüge, um zu gewinnen, sondern reagiert lediglich auf das aktuelle Spielgeschehen.
Es gibt 7 verschiedene Schwierigkeitsstufen, wobei der Computergegner mit der Schwierigkeisstufe 1 am leichtesten und der Computergegner mit der Schwierigkeitsstufe 7 am schwierigsten zu besiegen ist. Es ist aber auch gegen den Bot Level 7 durchaus möglich zu gewinnen. Eine genauere Beschreibung der einzelnen Schwierigkeitsstufen befindet sich unten.

Mit der Methode **choose_difficulty()** wird zu beginn des Spiels der Schwierigkeitsgrad des Computergegners initialisiert und in Folge im Attribut **difficulty_level** des Computerspieler-Objekts gespeichert.
Danach wird jedes mal, wenn der Computergegner an der Reihe ist, die Methode **throw_token()** des Computergegner-Objekts aufgerufen. In dieser Methode wird zuerst festgelegt, in welche Spalten es überhaupt möglich ist zu werfen (volle Spalten werden ausgenommen). Diese Spalten werden in der Liste **possible_numbers** gespeichert. Danach hängt die Auswahl der Spalte, in der er den Spielstein wirft, vom zuvor festgelegtem Schwierigkeitsgrad ab, wobei ab Schwierigkeitsstufe 2 die in der vorangegangenen Schwierigkeitsstufe festgelegten Bedingungen weiterhin zählen (Beispiel: Schwierigkeitsstufe 5 kann alles was Schwierrigkeitsstufe 4 kann, und mehr):

## Schwierigkeitsstufe 1
Der Computergegner mit der Schwierigkeitsstufe 1 wählt die Spalte, in die er seinen nächsten Spielstein wirft, zufällig aus den nicht vollen Spalten aus (dies passiert mithilfe des Moduls **random**). Er speichert die Spalte dann auf der Variable **column** und wirft den Stein mithilfe der for-Schleife ans untere Ende der ausgewählten Spalte.

## Schwierigkeitsstufe > 1
Ab Schwierigkeitsstufe 2 wird die Spalte, in die der Stein geworfen wird, anhand verschiedener Bedingungen festgelegt. Die ausgwählte Spalte wird auf der Variable **column** gespeichert und nach Prüfung aller Bedingungen mithilfe einer for-Schleife ans untere Ende der ausgewählten Spalte geworfen.

## Schwierigkeitsstufe 2
Bei der Schwierigkeitsstufe 2 wird zuerst mithilfe von zwei verschachtelten for-Schleifen und mehreren verketteten Bedingungen überprüft, ob der Computer bereits drei Steine in einer Reihe hat, zumindest eine Spalte daneben (links oder rechts) in der gleichen Reihe frei ist und der Platz unter dem freien Platz nicht frei ist (also, dass darunter entweder der Boden des Spielfelds oder ein beliebiger Spielstein ist, damit der Stein auch in der gewollten Reihe stehen bleibt). Trifft dies zu, wird die Spalte, in der sich dieser "freie Platz" zum Gewinnen befindet, unter der Variable **column** gespeichert.

Trifft das nicht zu, wird in der nächsten Bedingung wieder mithilfe von zwei verschachtelten for-Schleifen das gesamte Spielbrett (Listen in einer Liste) überprüft, ob der Computer in einer Spalte gewinnen kann: Es wird überprüft, ob drei Spielsteine des Computers übereinander in einer Spalte liegen und, ob der Platz darüber frei ist (also, ob die Liste zuvor in der Spielfeldliste an derselben Position das Zeichen "-" enthält). Trifft dies zu, wird diese Spalte unter der Variable **column** gespeichert.

Sollte der Computer in keiner Reihe oder Spalte eine Gewinnmöglichkeit finden, wird mit demselben System und in derselben Reihenfolge überprüft, ob der menschliche Gegner gewinnen könnte. Um das zu verhindern, wird dann die Spalte, in der der Gegner gewinnen könnte, unter der Variable **column** gespeichert.

## Schwierigkeitsstufe 3
Bei Schwierigkeitsstufe 3 wird zuerst wieder überprüft, ob der Computer mit dem nächsten Wurf gewinnen kann, diesmal über den Weg der beiden Diagonalen (die Bedingungen werden nur überprüft, wenn noch keine Reihe oder Spalte aus Schwierigkeitsstufe 2 gefunden wurden). Dazu werden sich die beiden Diagonalen getrennt angeschaut: Es wird wieder mithilfe von zwei verschachtelten for-Schleifen das ganze Spielfeld (alle Listen in der Liste) überprüft, ob bereits drei Spielsteine (also "O"-Symbole) Diagonal nebeneinander liegen und es möglich ist, entweder links oder rechts daneben, die Diagonale zu vervollständigen (sollte beides möglich sein, wird der Spielstein zuerst rechts daneben hineingeworfen; sollten zwei verschiedene Diagonalen zum vervollständigen vorhanden sein, also eine von links unten nach rechts oben und eine von links oben nach rechts unten, wird die Diagonale von links oben nach rechts unten vervollständigt, da diese nach der anderen überprüft wird, und somit den Wert der Variable ***column** zuletzt überschreibt).

Sollte es für den Computer nicht möglich sein, das Spiel über eine Diagonale zu gewinnen, wird wieder mit demselben System und in derselben Reiehnfolge überprüft, ob der Gegner über eine Diagonale gewinnen könnte. Um das zu verhindern, wird diese Spalte dann wieder unter **column** gespeichert.

## Schwierigkeitsstufe 4
Wenn noch keine Reihe, Spalte oder Diagonale des Computers oder des Gegner zum Gewinnen gefunden wurde, wird bei Schwierigkeitsstufe 4 der Fall miteinbezogen, dass eine Reihe oder eine Diagonale auch aufgespaltet sein könnte und somit zum Sieg führen könnte. 
Beispiel: "O" "O" "-" "O" -> der Spieler mit dem Symbol "O" könnte in diesem Fall in der dritten Spalte das Spiel gewinnen. Dasselbe könnte bei einer Diagonalen auftreten. Diese Fälle werden bei den Schwierigkeitsstufen 2 und 3 noch ignoriert, während ab Schwierigkeitsstufe 4 darauf acht genommen wird.

Es wird hier zuerst überprüft, ob der Computer selbst über eine solche aufgespaltenen Reihe gewinnen kann, danach, ob er über eine aufgespaltene Diagonale gewinnen kann, wobei zuerst die Diagonale von links unten nach rechts oben überprüft wird und danach von links oben nach rechts unten (treffen alle drei Möglichkeiten zu: Diagonale von unten nach oben überschreibt das **column** von der aufgespaltenen Reihe - Diagonale von oben nach unten überschreibt **column** der anderen Diagonale).

Treffen alle drei Möglichkeiten nicht zu, wird danach mit dem gleichen Prozedere überprüft, ob der Gegner so gewinnen könnte. Wenn eine Möglichkeit gefunden wurde, wird diese Spalte wieder unter **column** gespeichert.

## Schwierigkeitsstufe 5
Bei Schwierigkeitsstufe 5 und höher, wenn zuvor noch keine passende Spalte gefunden wurde, versucht der Computer zuerst, mit diesem Zug zwei verschiedene Gewinnmöglichkeiten für den nächsten Zug zu schaffen. Er versucht also eine Ausgangslage zu schaffen, in der der Gegner den Sieg des Computers nicht mehr verhindern kann.

Dazu wird als erstes das ganze Spielfeld überprüft, ob irgendwo zwei Steine nebeneinander sind, wobei auch überprüft wird, ob die Plätze links und rechts neben den beiden Steinen frei sind (und die beiden Plätze darunter nicht, um den Stein darauf werfen zu können) und auf mindestens einer Seite noch ein weiterer Platz daneben frei ist (und der Platz darunter nicht). Denn nur wenn alle diese Bedingungen erfüllt sind, können zwei Gewinnmöglichkeiten erschafft werden. Es wird dann die Spalte direkt neben den beiden Steinen, auf jener Seite auf der zwei Plätze daneben frei sind, unter **column** gespeichert.
Beispiel: "-" "-" "O" "O" "-" -> es wird in die zweite Spalte geworfen, da dann links und rechts eine Viererreihe erzeugt werden kann.

Als nächstes wird überprüft, ob sich zwei Steine des Computers mit einem Platz getrennt voneinander in einer Reihe befinden, wobei der Platz zwischen den Steinen frei ist (und der darunter nicht) und die beiden Plätze links und rechts neben den beiden Steinen frei sind (und die beiden Plätze darunter nicht). Sollte das der Fall sein, wird die Spalte zwischen den beiden Steinen unter **column** gespeichert.
Beispiel: "-" "O" "-" "O" "-" -> es wird in die mittlere Spalte geworfen, da dann links und rechts eine Viererreihe erzeugt werden kann.

Danach wird überprüft, ob sich in den Diagonalen bereits zwei Steine des Computers nebeneinander befinden, und die beiden Plätze diagonal daneben frei sind (und die beiden Plätze jeweils darunter nicht). Ist das der Fall, wird der Stein immer links diagonal zu den beiden bereis vorhandenen Steinen geworfen (also die dazugehörige Spalte unter **column** gespeichert). Es wird wieder zuerst die Diagonale von unten nach oben und danach von oben nach unten überprüft.

Beim Zutreffen von mehreren der zuvor beschriebenen Bedingungen der Schwierigkeitsstufe 5 gilt wieder: das später eintreffende Ereignis überschreibt die Variable **column** zuletzt und trifft somit ein.

Sollten sich dadurch keine zwei Gewinnmöglichkeiten für den Computer ergeben, wird durch dasselbe System und in derselben Reihenfolge überprüft, ob sich für den Gegner zwei Gewinnmöglichkeiten für den nächsten Zug ergeben könnten. Um das zu verhindern, wird die jeweilige Spalte wieder unter **column** gespeichert.

## Schwierigkeitsstufe 6
Ab dieser Schwierigkeitsstufe 6 folgen lediglich noch Optimierungen des Computergegners. Sollte der Computer durch die vorherigen Schwierigkeitsstufen noch keine optimale Spalte für seinen Stein gefunden haben, wird bei dieser Schwierigkeitsstufe darauf acht genommen, dass nicht unabsichtlich durch zufälliges Werfen des Steins der Sieg des Gegners ermöglicht wird:
Es wird dazu das Spielfeld überprüft, ob sich ein Sieg für den Gegner ergeben könnte, wenn der Gegner auf den nächsten geworfenen Stein des Computers wirft. Alle Spalten, bei denen das der Fall ist, werden aus der Liste **possible_numbers** entfernt und werden somit nicht mehr für die Auswahl der Spalte herangezogen. Da das mit Worten möglicherweise schwer nachvollziehbar ist, hier ein Beispeil:
"X" "-" "X" "X"
"O" "-" "X" "O"
Computer -> "O", Gegner -> "X"
Wenn in diesem Fall in die zweite Spalte geworfen wird, wird dem Gegner der Sieg auf dem Silvertablett serviert. Um das zu verhindern wird diese Spalte aus **possible_numbers** entfernt, um auszuschließen, dass in diese Spalte geworfen wird.

## Schwierigkeitsstufe 7
Bei Schwierigkeitsstufe 7 folgt eine weitere Optimierung, um zu verhindern, dass der Stein fortlaufen in unnötige Spalten geworfen wird, wenn zuvor keine optimale Spalte gefunden wurde. Dazu wird beachtet, dass der Computer wenn möglich zumindest auf seine eigenen Steine wirft. Sollten sich zwei seiner Steine übereinander befinden und der Platz darüber ist frei, wird diese Spalte unter **column** gespeichert, sollte das nicht der Fall sein, aber es befindet sich ein einzelner Stein des Computers am Feld, wird diese Spalte under **column** gespeichert. (Da das Spielfeld von links nach rechts überprüft wird, überschreibt eine Spalte weiter rechts immer die Spalte weiter links).

Der Sinn hinter dieser Optimierung ist es, einerseits dass fortlaufend unnötige Platzieren des Computersteins zu verhindern und somit andererseits den Gegner ein wenig unter druck zu setzen und ihm sozusagen eine Zug "wegzunehmen", da er bei einem Dreierstapel einen Stein darauf werfen muss, um den Sieg des Computers zu verhindern.

## Weiteres
Sollte durch die verschiedenen Bedingungen in den Schwierigkeitsstufen noch keine optimale Spalte gefunden worden sein, wird aus den möglichen Spalten aus der liste **possible_number** mithilfe des Moduls random zufällig eine Spalte ausgewählt und unter der Variable **column** gespeichert. Zur Erinnerung: aus dieser Liste wurden die vollen Spalten sowie bei Schwierigkeitsgrad >= 6 die Spalten, die einen Sieg für den Gegner ermöglichen, entfernt.

Danach wird der Spielstein in die ausgewählte Spalte, die in **column** gespeichert ist, mit einer for-Schleife ans untere Ende der Spalte geworfen.

Wie bereits erwähnt, sind die Schwierigkeitsstufen ab Level 2 aufeinander aufbauend. Das bedeutet, dass bei Schwierigkeitsstufe 7 auch alle Schwierigkeitsstufen von 2 bis 6 enthalten sind. Die Bedingungen von Schwierigkeitsgrad 7 kommen nur dann zur Verwendendung, wenn davor noch keine Spalte gefunden wurde.
