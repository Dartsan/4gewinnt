import abc
import random


class Player(abc.ABC):
    def __init__(self, symbol: str):
        """
        Konstruktor der abstrakten Klasse Player

        Parameters
        ----------
        symbol: str
            Spielsteinsymbol des Spielers
        """
        self.symbol = symbol

    @abc.abstractmethod
    def throw_token(self, gameboard: list[list]):
        """
        Realisierung, Spielsteine zu setzen

        Parameters
        ----------
        gameboard: list[list]
            aktuelles Spielfeld, mit dem gespielt wird
        """
        pass


class Field:
    """
    Diese Klasse stellt das Spielfeld dar

    Attributes
    ----------
    rows: int
        Anzahl der Reihen, die das Spielfeld besitzt (festgelegt auf 6)
    columns: int
        Anzahl der Spalten, die das Spielfeld besitzt (festgelegt auf 7)
    board: list
        leere Liste, mithilfe der das Spielfeld erstellt wird
    """
    rows = 6
    columns = 7
    board = []

    def create_board(self) -> list[list[str]]:
        """
        Erstellung ein leeres Spielfeld mit dem Symbol '-' als Platzhalter

        Returns
        -------
        list of lists of str
            leeres Spielfeld mit den Namen board
        """
        self.board.clear()
        for i in range(self.rows):
            self.board.append(list())
            for j in range(self.columns):
                self.board[i].append("-")
        return self.board

    def show_field(self, board: list[list[str]]):
        """
        Zeigt das aktuelle Spielfeld an

        Parameters
        ----------
        board: list[list[str]]
            auszugebendes Spielfeld
        """
        print([str(y) for y in range(1, 8)])
        print()
        for x in board:
            print(x)

    def check_win(self, gameboard: list[list[str]]) -> bool:
        """
        Überprüfung, ob ein Spieler gewonnen hat

        Parameters
        ----------
        gameboard: list[list[str]]
            zu überprüfendes Spielfeld

        Returns
        -------
        win: bool
            bei True: es gibt einen Gewinner, die aktuelle Runde ist zu Ende
        """
        win = False
        # jede Spalte überprüfen:
        for i in range(Field.rows - 1, -1, -1):
            for j in range(0, Field.columns - 3):
                if (gameboard[i][j] != "-") and (
                        gameboard[i][j] == gameboard[i][j + 1] == gameboard[i][j + 2] == gameboard[i][j + 3]):
                    win = True
        # jede Zeile überprüfen:
        for j in range(Field.columns):
            for i in range(Field.rows - 4, -1, -1):
                if (gameboard[i][j] != "-") and (
                        gameboard[i][j] == gameboard[i + 1][j] == gameboard[i + 2][j] == gameboard[i + 3][j]):
                    win = True
        # Diagonale überprüfen:
        # von links unten nach rechts oben:
        x = Field.rows
        for i in range(Field.rows - 3):
            x -= 1
            for j in range(Field.columns - 3):
                if (gameboard[x][j] != "-") and (
                        gameboard[x][j] == gameboard[x - 1][j + 1] == gameboard[x - 2][j + 2] == gameboard[x - 3][
                        j + 3]):
                    win = True
        # von links oben nach rechts unten:
        for i in range(Field.rows - 3):
            for j in range(Field.columns - 3):
                if (gameboard[i][j] != "-") and (
                        gameboard[i][j] == gameboard[i + 1][j + 1] == gameboard[i + 2][j + 2] == gameboard[i + 3][
                        j + 3]):
                    win = True
        return win

    def check_draw(self, gameboard: list[list[str]]) -> bool:
        """
        Überprüft, ob das Spiel Unentschieden endet

        Parameters
        ----------
        gameboard: list[list[str]]
            zu überprüfendes Spielfeld

        Returns
        -------
        draw: bool
            bei True: Unentschieden, das Spiel ist zu Ende
        """
        draw = False
        if "-" not in gameboard[0]:
            draw = True
        return draw


class Human(Player):
    def __init__(self, symbol: str, name: str):
        """
        Konstruktor Klasse Human

        Parameters
        ----------
        symbol: str
            Spielsteinsymbol des Spielers
        name: str
            Nickname des Spielers
        """
        super().__init__(symbol)
        self.name = name

    def throw_token(self, gameboard: list[list[str]]) -> bool:
        """
        Realisierung Spielzug für eine Person

        Parameters
        ----------
        gameboard: list[list[str]]
            aktuelles Spielfeld, in welches der Stein geworfen werden soll

        Returns
        -------
        exit: bool
            liefert True bei der Eingabe von "Exit" zurück, um das Verlassen des Spiels nach jedem Spielzug zu
            ermöglichen
        """
        exit = False
        inputstring = input(
            f"{self.name}: Bitte wählen Sie eine Spalte aus, in den Sie Ihren Stein werfen wollen, indem Sie eine Zahl "
            "zwischen 1 und 7 wählen: ")
        if inputstring.isnumeric():
            column = int(inputstring)
            while column not in range(1, 8):
                possiblenumber = input("Das ist leider nicht möglich. Wählen Sie eine Zahl zwischen 1 und 7: ")
                if possiblenumber.isnumeric():
                    column = int(possiblenumber)
                elif possiblenumber == "Exit":
                    exit = True
                    break
                else:
                    continue
            if gameboard[0][column - 1] != "-":
                print("Diese Spalte ist voll! Wähle eine andere Spalte!")
                self.throw_token(gameboard)
            if exit:
                return True
            else:
                for i in range(Field.rows - 1, -1, -1):
                    if gameboard[i][column - 1] == "-":
                        gameboard[i][column - 1] = self.symbol
                        break

        elif inputstring == "Exit":
            return True
        else:
            self.throw_token(gameboard)


class Bot(Player):
    def __init__(self, symbol: str, difficulty_level: int):
        """
        Konstruktor Klasse Bot

        Parameters
        ----------
        symbol: str
            Spielsteinsymbols des Computers
        difficulty_level: int
            Schwierigkeitsstufe des Computers, kann die Werte 1-7 annehmen
        """
        super().__init__(symbol)
        self.difficulty_level = difficulty_level

    def throw_token(self, gameboard: list[list[str]]):
        """
        Realisierung Spielzug für den Computer

        Parameters
        ----------
        gameboard: list[list[str]]
            aktuelles Spielfeld, in das der Spielstein geworfen werden soll
        """
        possible_numbers = [i for i in range(0, Field.columns)]
        for i in possible_numbers:
            if gameboard[0][i] != "-":
                possible_numbers.remove(i)
        if self.difficulty_level == 1:
            column = random.choice(possible_numbers)
            for i in range(Field.rows - 1, -1, -1):
                if gameboard[i][column] == "-":
                    gameboard[i][column] = self.symbol
                    break
        # ab hier beginnt der Computer, seine Züge nicht mehr ganz zufällig zu wählen,
        # eine genaue Beschreibung des Computergegners befindet sich im Dokumentationsordner
        else:
            column = None
            # überprüfen, ob Computer in einer Reihe fertig werden kann
            for i in range(Field.rows - 1, -1, -1):
                for j in range(0, Field.columns - 2):
                    if j == (Field.columns - 3):
                        if gameboard[i][j] == "O":
                            if (gameboard[i][j + 1] == "O") and (gameboard[i][j + 2] == "O"):
                                if i == (Field.rows - 1):
                                    if gameboard[i][j - 1] == "-":
                                        column = j - 1
                                elif (gameboard[i + 1][j - 1] != "-") and (gameboard[i][j - 1] == "-"):
                                    column = j - 1
                    elif gameboard[i][j] == "O":
                        if (gameboard[i][j + 1] == "O") and (gameboard[i][j + 2] == "O"):
                            if i == (Field.rows - 1):
                                if gameboard[i][j + 3] == "-":
                                    column = j + 3
                                elif j > 0:
                                    if gameboard[i][j - 1] == "-":
                                        column = j - 1
                            elif (gameboard[i + 1][j + 3] != "-") and (gameboard[i][j + 3] == "-"):
                                column = j + 3
                            elif j != 0:
                                if (gameboard[i + 1][j - 1] != "-") and (gameboard[i][j - 1] == "-"):
                                    column = j - 1
            # überprüfen, ob Computer in einer Spalte fertig werden kann (wenn nicht in einer Reihe möglich)
            if column == None:
                for i in range(Field.rows - 1, Field.rows - 3, -1):
                    for j in range(0, Field.columns):
                        if gameboard[i][j] == "O":
                            if (gameboard[i - 1][j] == "O") and (gameboard[i - 2][j] == "O") and \
                                    (gameboard[i - 3][j] == "-"):
                                column = j
            # überprüfen, ob Gegner in einer Reihe fertig werden kann, wenn Computer nicht selbst fertig wird
            if column == None:
                for i in range(Field.rows - 1, -1, -1):
                    for j in range(0, Field.columns - 2):
                        if j == (Field.columns - 3):
                            if gameboard[i][j] == "X":
                                if (gameboard[i][j + 1] == "X") and (gameboard[i][j + 2] == "X"):
                                    if i == (Field.rows - 1):
                                        if gameboard[i][j - 1] == "-":
                                            column = j - 1
                                    elif (gameboard[i + 1][j - 1] != "-") and (gameboard[i][j - 1] == "-"):
                                        column = j - 1
                        elif gameboard[i][j] == "X":
                            if (gameboard[i][j + 1] == "X") and (gameboard[i][j + 2] == "X"):
                                if i == (Field.rows - 1):
                                    if gameboard[i][j + 3] == "-":
                                        column = j + 3
                                    elif j > 0:
                                        if gameboard[i][j - 1] == "-":
                                            column = j - 1
                                elif (gameboard[i + 1][j + 3] != "-") and (gameboard[i][j + 3] == "-"):
                                    column = j + 3
                                elif j != 0:
                                    if (gameboard[i + 1][j - 1] != "-") and (gameboard[i][j - 1] == "-"):
                                        column = j - 1
            # wenn noch keine Reihe gefunden -> überprüfen, ob Gegner in einer Spalte fertig werden kann
            if column == None:
                for i in range(Field.rows - 1, Field.rows - 3, -1):
                    for j in range(0, Field.columns):
                        if gameboard[i][j] == "X":
                            if (gameboard[i - 1][j] == "X") and (gameboard[i - 2][j] == "X") and \
                                    (gameboard[i - 3][j] == "-"):
                                column = j
            if (self.difficulty_level >= 3) and (column == None):
                # überprüfen, ob Computer über Diagonale fertig werden kann
                # von links unten nach rechts oben:
                x = Field.rows
                for i in range(Field.rows - 2):
                    x -= 1
                    for j in range(Field.columns - 2):
                        if gameboard[x][j] == "O":
                            if (gameboard[x - 1][j + 1] == "O") and (gameboard[x - 2][j + 2] == "O"):
                                if (x == Field.rows - 1) or (j == 0):
                                    if (x != Field.rows - 4) and (j != Field.columns - 3):
                                        if (gameboard[x - 3][j + 3] == "-") and (gameboard[x - 2][j + 3] != "-"):
                                            column = j + 3
                                elif (x == Field.rows - 4) or (j == Field.columns - 3):
                                    if (x != Field.rows - 1) and (j != 0):
                                        if (gameboard[x + 1][j - 1] == "-") and (gameboard[x + 2][j - 1] != "-"):
                                            column = j - 1
                                else:
                                    if (gameboard[x - 3][j + 3] == "-") and (gameboard[x - 2][j + 3] != "-"):
                                        column = j + 3
                                    elif (gameboard[x + 1][j - 1] == "-") and (gameboard[x + 2][j - 1] != "-"):
                                        column = j - 1
                # von links oben nach rechts unten:
                for i in range(Field.rows - 2):
                    for j in range(Field.columns - 2):
                        if gameboard[i][j] == "O":
                            if (gameboard[i + 1][j + 1] == "O") and (gameboard[i + 2][j + 2] == "O"):
                                if (i == 0) or (j == 0):
                                    if (i != Field.rows - 3) and (j != Field.columns - 3):
                                        if (gameboard[i + 3][j + 3] == "-") and (gameboard[i + 4][j + 3] != "-"):
                                            column = j + 3
                                elif (i == Field.rows - 3) or (j == Field.columns - 3):
                                    if (i != 0) and (j != 0):
                                        if (gameboard[i - 1][j - 1] == "-") and (gameboard[i][j - 1] != "-"):
                                            column = j - 1
                                else:
                                    if (gameboard[i + 3][j + 3] == "-") and (gameboard[i + 4][j + 3] != "-"):
                                        column = j + 3
                                    elif (gameboard[i - 1][j - 1] == "-") and (gameboard[i][j - 1] != "-"):
                                        column = j - 1
                # überprüfen, ob Gegner über Diagonale fertig werden kann:
                # von links unten nach rechts oben:
                if column == None:
                    x = Field.rows
                    for i in range(Field.rows - 2):
                        x -= 1
                        for j in range(Field.columns - 2):
                            if gameboard[x][j] == "X":
                                if (gameboard[x - 1][j + 1] == "X") and (gameboard[x - 2][j + 2] == "X"):
                                    if (x == Field.rows - 1) or (j == 0):
                                        if (x != Field.rows - 4) and (j != Field.columns - 3):
                                            if (gameboard[x - 3][j + 3] == "-") and (gameboard[x - 2][j + 3] != "-"):
                                                column = j + 3
                                    elif (x == Field.rows - 4) or (j == Field.columns - 3):
                                        if (x != Field.rows - 1) and (j != 0):
                                            if (gameboard[x + 1][j - 1] == "-") and (gameboard[x + 2][j - 1] != "-"):
                                                column = j - 1
                                    else:
                                        if (gameboard[x - 3][j + 3] == "-") and (gameboard[x - 2][j + 3] != "-"):
                                            column = j + 3
                                        elif (gameboard[x + 1][j - 1] == "-") and (gameboard[x + 2][j - 1] != "-"):
                                            column = j - 1
                    # von links oben nach rechts unten:
                    for i in range(Field.rows - 2):
                        for j in range(Field.columns - 2):
                            if gameboard[i][j] == "X":
                                if (gameboard[i + 1][j + 1] == "X") and (gameboard[i + 2][j + 2] == "X"):
                                    if (i == 0) or (j == 0):
                                        if (i != Field.rows - 3) and (j != Field.columns - 3):
                                            if (gameboard[i + 3][j + 3] == "-"):
                                                if i == Field.rows - 4:
                                                    column = j + 3
                                                elif (gameboard[i + 4][j + 3] != "-"):
                                                    column = j + 3
                                    elif (i == Field.rows - 3) or (j == Field.columns - 3):
                                        if (i != 0) and (j != 0):
                                            if (gameboard[i - 1][j - 1] == "-") and (gameboard[i][j - 1] != "-"):
                                                column = j - 1
                                    else:
                                        if (gameboard[i + 3][j + 3] == "-"):
                                            if i == Field.rows - 4:
                                                column = j + 3
                                            elif gameboard[i + 4][j + 3] != "-":
                                                column = j + 3
                                        elif (gameboard[i - 1][j - 1] == "-") and (gameboard[i][j - 1] != "-"):
                                            column = j - 1
            if (self.difficulty_level >= 4) and (column == None):
                # Einbeziehen des Falles der aufgespaltenen Reihe, in der der Computer fertig werden kann
                for i in range(Field.rows):
                    for j in range(Field.columns - 3):
                        if gameboard[i][j] == "O":
                            if i == Field.rows - 1:
                                if (gameboard[i][j + 1] == "O") and \
                                        (gameboard[i][j + 2] == "-") and (gameboard[i][j + 3] == "O"):
                                    column = j + 2
                                elif (gameboard[i][j + 1] == "-") and \
                                        (gameboard[i][j + 2] == "O") and (gameboard[i][j + 3] == "O"):
                                    column = j + 1
                            else:
                                if (gameboard[i][j + 1] == "O") and (gameboard[i][j + 2] == "-") and \
                                        (gameboard[i + 1][j + 2] != "-") and (gameboard[i][j + 3] == "O"):
                                    column = j + 2
                                elif (gameboard[i][j + 1] == "-") and (gameboard[i + 1][j + 1] != "-") and \
                                        (gameboard[i][j + 2] == "O") and (gameboard[i][j + 3] == "O"):
                                    column = j + 1
                # Einbeziehen des Falles der aufgespaltenen Diagonalen, in der der Computer fertig werden kann,
                # von links unten nach rechts oben:
                x = Field.rows
                for i in range(Field.rows - 3):
                    x -= 1
                    for j in range(Field.columns - 3):
                        if gameboard[x][j] == "O":
                            if (gameboard[x - 1][j + 1] == "O") and (gameboard[x - 2][j + 2] == "-") and \
                                    (gameboard[x - 1][j + 2] != "-") and (gameboard[x - 3][j + 3] == "O"):
                                column = j + 2
                            elif (gameboard[x - 1][j + 1] == "-") and (gameboard[x][j + 1] != "-") and \
                                    (gameboard[x - 2][j + 2] == "O") and (gameboard[x - 3][j + 3] == "O"):
                                column = j + 1
                # von links oben nach rechts unten:
                for i in range(Field.rows - 3):
                    for j in range(Field.columns - 3):
                        if gameboard[i][j] == "O":
                            if (gameboard[i + 1][j + 1] == "O") and (gameboard[i + 2][j + 2] == "-") and \
                                    (gameboard[i + 1][j + 2] != "-") and (gameboard[i + 3][j + 3] == "O"):
                                column = j + 2
                            elif (gameboard[i + 1][j + 1] == "-") and (gameboard[i][j + 1] != "-") and \
                                    (gameboard[i + 2][j + 2] == "O") and (gameboard[i + 3][j + 3] == "O"):
                                column = j + 1
                if column == None:
                    # Einbeziehen des Falles der aufgespaltenen Reihe, in der der Gegner fertig werden kann
                    for i in range(Field.rows):
                        for j in range(Field.columns - 3):
                            if gameboard[i][j] == "X":
                                if i == Field.rows - 1:
                                    if (gameboard[i][j + 1] == "X") and \
                                            (gameboard[i][j + 2] == "-") and (gameboard[i][j + 3] == "X"):
                                        column = j + 2
                                    elif (gameboard[i][j + 1] == "-") and \
                                            (gameboard[i][j + 2] == "X") and (gameboard[i][j + 3] == "X"):
                                        column = j + 1
                                else:
                                    if (gameboard[i][j + 1] == "X") and (gameboard[i][j + 2] == "-") and \
                                            (gameboard[i + 1][j + 2] != "-") and (gameboard[i][j + 3] == "X"):
                                        column = j + 2
                                    elif (gameboard[i][j + 1] == "-") and (gameboard[i + 1][j + 1] != "-") and \
                                            (gameboard[i][j + 2] == "X") and (gameboard[i][j + 3] == "X"):
                                        column = j + 1
                    # Einbeziehen des Falles der aufgespaltenen Diagonalen, in der der Gegner fertig werden kann,
                    # von links unten nach rechts oben:
                    x = Field.rows
                    for i in range(Field.rows - 3):
                        x -= 1
                        for j in range(Field.columns - 3):
                            if gameboard[x][j] == "X":
                                if (gameboard[x - 1][j + 1] == "X") and (gameboard[x - 2][j + 2] == "-") and \
                                        (gameboard[x - 1][j + 2] != "-") and (gameboard[x - 3][j + 3] == "X"):
                                    column = j + 2
                                elif (gameboard[x - 1][j + 1] == "-") and (gameboard[x][j + 1] != "-") and \
                                        (gameboard[x - 2][j + 2] == "X") and (gameboard[x - 3][j + 3] == "X"):
                                    column = j + 1
                    # von links oben nach rechts unten:
                    for i in range(Field.rows - 3):
                        for j in range(Field.columns - 3):
                            if gameboard[i][j] == "X":
                                if (gameboard[i + 1][j + 1] == "X") and (gameboard[i + 2][j + 2] == "-") and \
                                        (gameboard[i + 1][j + 2] != "-") and (gameboard[i + 3][j + 3] == "X"):
                                    column = j + 2
                                elif (gameboard[i + 1][j + 1] == "-") and (gameboard[i][j + 1] != "-") and \
                                        (gameboard[i + 2][j + 2] == "X") and (gameboard[i + 3][j + 3] == "X"):
                                    column = j + 1
            if (self.difficulty_level >= 5) and (column == None):
                # zwei Gewinnmöglichkeiten für Computer erschaffen
                # zwei Steine nebeneinander in einer Reihe:
                for i in range(Field.rows):
                    for j in range(Field.columns - 3):
                        if (gameboard[i][j] == "-") and (gameboard[i][j + 1] == "O") and (gameboard[i][j + 2] == "O") \
                                and (gameboard[i][j + 3] == "-"):
                            if i == Field.rows - 1:
                                column = j
                            elif (gameboard[i + 1][j] != "-") and (gameboard[i + 1][j + 3] != "-"):
                                column = j
                # zwei Steine getrennt voneinander in einer Reihe:
                for i in range(Field.rows):
                    for j in range(Field.columns - 4):
                        if (gameboard[i][j] == "-") and (gameboard[i][j + 1] == "O") and \
                                (gameboard[i][j + 2] == "-") and (gameboard[i][j + 3] == "O") and \
                                (gameboard[i][j + 4] == "-"):
                            if i == Field.rows - 1:
                                column = j + 2
                            elif gameboard[i + 1][j + 2] != "-":
                                column = j + 2
                # zwei Steine nebeneinander in einer Diagonalen:
                # von links unten nach rechts oben:
                x = Field.rows
                for i in range(Field.rows - 3):
                    x -= 1
                    for j in range(Field.columns - 3):
                        if (gameboard[x][j] == "-") and (gameboard[x - 1][j + 1] == "O") and \
                                (gameboard[x - 2][j + 2] == "O") and (gameboard[x - 3][j + 3] == "-") and \
                                (gameboard[x - 2][j + 3] != "-"):
                            if x == Field.rows - 1:
                                column = j
                            elif gameboard[x + 1][j] != "-":
                                column = j
                # von links oben nach rechts unten:
                for i in range(Field.rows - 4):
                    for j in range(Field.columns - 4):
                        if (gameboard[i][j] == "-") and (gameboard[i + 1][j] != "-") and \
                                (gameboard[i + 1][j + 1] == "O") and (gameboard[i + 2][j + 2] == "O") and \
                                (gameboard[i + 3][j + 3] == "-"):
                            if i == Field.columns - 4:
                                column = j
                            elif gameboard[i + 4][j + 3] != "-":
                                column = j
                if column == None:
                    # vorhersehen, dass nicht zwei Gewinnmöglichkeiten für Gegner entstehen
                    # zwei Steine nebeneinander in einer Reihe:
                    for i in range(Field.rows):
                        for j in range(Field.columns - 3):
                            if (gameboard[i][j] == "-") and (gameboard[i][j + 1] == "X") and \
                                    (gameboard[i][j + 2] == "X") and (gameboard[i][j + 3] == "-"):
                                if i == Field.rows - 1:
                                    column = j
                                elif (gameboard[i + 1][j] != "-") and (gameboard[i + 1][j + 3] != "-"):
                                    column = j
                    # zwei Steine getrennt voneinander in einer Reihe:
                    for i in range(Field.rows):
                        for j in range(Field.columns - 4):
                            if (gameboard[i][j] == "-") and (gameboard[i][j + 1] == "X") and \
                                    (gameboard[i][j + 2] == "-") and (gameboard[i][j + 3] == "X") and \
                                    (gameboard[i][j + 4] == "-"):
                                if i == Field.rows - 1:
                                    column = j + 2
                                elif gameboard[i + 1][j + 2] != "-":
                                    column = j + 2
                    # zwei Steine nebeneinander in einer Diagonalen:
                    # von links unten nach rechts oben:
                    x = Field.rows
                    for i in range(Field.rows - 3):
                        x -= 1
                        for j in range(Field.columns - 3):
                            if (gameboard[x][j] == "-") and (gameboard[x - 1][j + 1] == "X") and \
                                    (gameboard[x - 2][j + 2] == "X") and (gameboard[x - 3][j + 3] == "-") and \
                                    (gameboard[x - 2][j + 3] != "-"):
                                if x == Field.rows - 1:
                                    column = j
                                elif gameboard[x + 1][j] != "-":
                                    column = j
                    # von links oben nach rechts unten:
                    for i in range(Field.rows - 4):
                        for j in range(Field.columns - 4):
                            if (gameboard[i][j] == "-") and (gameboard[i + 1][j] != "-") and \
                                    (gameboard[i + 1][j + 1] == "X") and (gameboard[i + 2][j + 2] == "X") and \
                                    (gameboard[i + 3][j + 3] == "-"):
                                if i == Field.columns - 4:
                                    column = j
                                elif gameboard[i + 4][j + 3] != "-":
                                    column = j
            if (self.difficulty_level >= 6) and (column == None):
                # den Sieg für den Gegner nicht unabsichtlich ermöglichen
                # Reihe:
                for i in range(Field.rows - 1):
                    for j in range(Field.columns - 3):
                        if (gameboard[i + 1][j] == "-") and (gameboard[i][j + 1] == "X") and \
                                (gameboard[i][j + 2] == "X") and (gameboard[i][j + 3] == "X"):
                            if i == Field.rows - 2:
                                possible_numbers.remove(j)
                            elif gameboard[i + 2][j] != "-":
                                possible_numbers.remove(j)
                        if (gameboard[i][j] == "X") and (gameboard[i + 1][j + 1] == "-") and \
                                (gameboard[i][j + 2] == "X") and (gameboard[i][j + 3] == "X"):
                            if i == Field.rows - 2:
                                possible_numbers.remove(j + 1)
                            elif gameboard[i + 2][j + 1] != "-":
                                possible_numbers.remove(j + 1)
                        if (gameboard[i][j] == "X") and (gameboard[i][j + 1] == "X") and\
                                (gameboard[i + 1][j + 2] == "-") and (gameboard[i][j + 3] == "X"):
                            if i == Field.rows - 2:
                                possible_numbers.remove(j + 2)
                            elif gameboard[i + 2][j + 2] != "-":
                                possible_numbers.remove(j + 2)
                        if (gameboard[i][j] == "X") and (gameboard[i][j + 1] == "X") and (gameboard[i][j + 2] == "X") \
                                and (gameboard[i + 1][j + 3] == "-"):
                            if i == Field.rows - 2:
                                possible_numbers.remove(j + 3)
                            elif gameboard[i + 2][j + 3] != "-":
                                possible_numbers.remove(j + 3)
                # Diagonale:
                # von links unten nach rechts oben:
                x = Field.rows
                for i in range(Field.rows - 3):
                    x -= 1
                    for j in range(Field.columns - 3):
                        if x == Field.rows - 1:
                            if (gameboard[x][j] == "X") and (gameboard[x][j + 1] == "-") and \
                                    (gameboard[x - 2][j + 2] == "X") and (gameboard[x - 3][j + 3] == "X"):
                                possible_numbers.remove(j + 1)
                            if (gameboard[x][j] == "X") and (gameboard[x - 1][j + 1] == "X") and \
                                    (gameboard[x - 1][j + 2] == "-") and (gameboard[x][j + 2] != "-") and \
                                    (gameboard[x - 3][j + 3] == "X"):
                                possible_numbers.remove(j + 2)
                            if (gameboard[x][j] == "X") and (gameboard[x - 1][j + 1] == "X") and \
                                    (gameboard[x - 2][j + 2] == "X") and (gameboard[x - 2][j + 3] == "-") and \
                                    (gameboard[x - 1][j + 3] != "-"):
                                possible_numbers.remove(j + 3)
                        else:
                            if (gameboard[x + 1][j] == "-") and (gameboard[x - 1][j + 1] == "X") and \
                                    (gameboard[x - 2][j + 2] == "X") and (gameboard[x - 3][j + 3] == "X"):
                                if x == Field.rows - 2:
                                    possible_numbers.remove(j)
                                elif gameboard[x + 2][j] != "-":
                                    possible_numbers.remove(j)
                            if (gameboard[x][j] == "X") and (gameboard[x][j + 1] == "-") and \
                                    (gameboard[x + 1][j + 1] != "-") and (gameboard[x - 2][j + 2] == "X") and \
                                    (gameboard[x - 3][j + 3] == "X"):
                                possible_numbers.remove(j + 1)
                            if (gameboard[x][j] == "X") and (gameboard[x - 1][j + 1] == "X") and \
                                    (gameboard[x - 1][j + 2] == "-") and (gameboard[x][j + 2] != "-") and \
                                    (gameboard[x - 3][j + 3] == "X"):
                                possible_numbers.remove(j + 2)
                            if (gameboard[x][j] == "X") and (gameboard[x - 1][j + 1] == "X") and \
                                    (gameboard[x - 2][j + 2] == "X") and (gameboard[x - 2][j + 3] == "-") and \
                                    (gameboard[x - 1][j + 3] != "-"):
                                possible_numbers.remove(j + 3)
                # von links oben nach rechts unten:
                for i in range(Field.rows - 3):
                    for j in range(Field.columns - 3):
                        if i == Field.rows - 4:
                            if (gameboard[i + 1][j] == "-") and (gameboard[i + 2][j] != "-") and \
                                    (gameboard[i + 1][j + 1] == "X") and (gameboard[i + 2][j + 2] == "X") and \
                                    (gameboard[i + 3][j + 3] == "X"):
                                possible_numbers.remove(j)
                            if (gameboard[i][j] == "X") and (gameboard[i + 2][j + 1] == "-") and \
                                    (gameboard[i + 3][j + 1] != "-") and (gameboard[i + 2][j + 2] == "X") and \
                                    (gameboard[i + 3][j + 3] == "X"):
                                possible_numbers.remove(j + 1)
                            if (gameboard[i][j] == "X") and (gameboard[i + 1][j + 1] == "X") and \
                                    (gameboard[i + 3][j + 2] == "-") and (gameboard[i + 3][j + 3] == "X"):
                                possible_numbers.remove(j + 2)
                        else:
                            if (gameboard[i + 1][j] == "-") and (gameboard[i + 2][j] != "-") and \
                                    (gameboard[i + 1][j + 1] == "X") and (gameboard[i + 2][j + 2] == "X") and \
                                    (gameboard[i + 3][j + 3] == "X"):
                                possible_numbers.remove(j)
                            if (gameboard[i][j] == "X") and (gameboard[i + 2][j + 1] == "-") and \
                                    (gameboard[i + 3][j + 1] != "-") and (gameboard[i + 2][j + 2] == "X") and \
                                    (gameboard[i + 3][j + 3] == "X"):
                                possible_numbers.remove(j + 1)
                            if (gameboard[i][j] == "X") and (gameboard[i + 1][j + 1] == "X") and \
                                    (gameboard[i + 3][j + 2] == "-") and (gameboard[i + 4][j + 2] != "-") and \
                                    (gameboard[i + 3][j + 3] == "X"):
                                possible_numbers.remove(j + 2)
                            if (gameboard[i][j] == "X") and (gameboard[i + 1][j + 1] == "X") and (gameboard[i + 2][j + 2] == "X") and (gameboard[i + 4][j + 3] == "-"):
                                if i == Field.rows - 5:
                                    possible_numbers.remove(j + 3)
                                elif gameboard[i + 5][j + 3] != "-":
                                    possible_numbers.remove(j + 3)
            if (self.difficulty_level >= 7) and (column == None):
                # auf zwei eigene Steine werfen, wenn vorhanden
                for i in range(Field.rows - 2):
                    for j in range(Field.columns):
                        if (gameboard[i][j] == "-") and (gameboard[i + 1][j] == "O") and (gameboard[i + 2][j] == "O"):
                            column = j
                # auf einen eigenen Stein werfen, wenn vorhanden
                if column == None:
                    for i in range(Field.rows - 1):
                        for j in range(Field.columns):
                            if (gameboard[i][j] == "-") and (gameboard[i + 1][j] == "O"):
                                column = j
            if column == None:
                column = random.choice(possible_numbers)
            # Werfen des Steins an sich:
            for i in range(Field.rows - 1, -1, -1):
                if gameboard[i][column] == "-":
                    gameboard[i][column] = self.symbol
                    break

    def choose_difficulty(self) -> bool:
        """
        Realisierung zur Auswahl des Schwierigkeitsgrades des Computers

        Returns
        -------
        bool/None
            liefert True bei der Eingabe von "Exit" zurück, um das Verlassen des Spiels nach jedem Spielzug zu
            ermöglichen, ansonsten ist der Return None
        """
        difficulty = input("Geben Sie den Schwierigkeitsgrad des Computers an. "
                           "Dieser kann zwischen 1 (sehr einfach) und 7 (schwierig) liegen: ")
        if difficulty == "Exit":
            print("Das Spiel wurde erfolgreich beendet!")
            return True
        elif difficulty.isnumeric():
            self.difficulty_level = int(difficulty)
            while self.difficulty_level not in range(1, 8):
                difficulty = input("Das ist leider nicht möglich! "
                                   "Bitte wählen Sie eine Schwierigkeit zwischen 1 und 7: ")
                if difficulty.isnumeric():
                    self.difficulty_level = int(difficulty)
                elif difficulty == "Exit":
                    print("Das Spiel wurde erfolgreich beendet!")
                    return True
                else:
                    continue
        else:
            self.choose_difficulty()


if __name__ == '__main__':
    print("Willkommen bei 4 Gewinnt von Kevin Herunter und Oliver Tanzer!")
    print("Mit Exit können Sie das Spiel jederzeit beenden!")
    print("Bitte geben Sie an, ob Sie Spieler gegen Spieler(PVP) oder Spieler gegen Computer(PVC) spielen wollen!")
    while True:
        gamemode = input()
        if gamemode == "PVP":
            pvpgame = Field
            pvpgameboard = pvpgame.create_board(pvpgame)
            name1 = input("Geben Sie den Name des ersten Spielers an ")
            if name1 == "Exit":
                print("Das Spiel wurde erfolgreich beendet!")
                break
            player1 = Human("X", name1)
            name2 = input("Geben Sie den Name des zweiten Spielers an ")
            if name2 == "Exit":
                print("Das Spiel wurde erfolgreich beendet!")
                break
            player2 = Human("O", name2)
            print()
            print("------------Spielfeld--------------")
            pvpgame.show_field(pvpgame, pvpgameboard)
            print()
            while True:
                if player1.throw_token(pvpgameboard):  # bei der throw_token Methode wird True bei der Eingabe von
                    # "Exit" zurückgeliefert
                    print("Das laufende Spiel wurde erfolgreich abgebrochen!")
                    pvpgameboard.clear()
                    break
                print()
                print("------------Spielfeld--------------")
                pvpgame.show_field(pvpgame, pvpgameboard)
                print()
                if pvpgame.check_win(pvpgame, pvpgameboard) or pvpgame.check_draw(pvpgame, pvpgameboard):
                    if pvpgame.check_win(pvpgame, pvpgameboard):
                        print(f"{player1.name} hat gewonnen! ")
                    else:
                        print("Es sind alle Spalten voll, es ist kein Zug mehr möglich!")
                        print("Das Spiel endet Unentschieden!")
                    pvpgameboard.clear()
                    print()
                    print("Um erneut ein Spiel zu starten geben Sie wieder PVP oder PVC an!")
                    break
                if player2.throw_token(pvpgameboard):  # liefert True bei Eingabe "Exit"
                    print("Das laufende Spiel wurde erfolgreich abgebrochen!")
                    pvpgameboard.clear()
                    break
                print()
                print("------------Spielfeld--------------")
                pvpgame.show_field(pvpgame, pvpgameboard)
                print()
                if pvpgame.check_win(pvpgame, pvpgameboard) or pvpgame.check_draw(pvpgame, pvpgameboard):
                    if pvpgame.check_win(pvpgame, pvpgameboard):
                        print(f"{player2.name} hat gewonnen!")
                    else:
                        print("Es sind alle Spalten voll, es ist kein Zug mehr möglich!")
                        print("Das Spiel endet Unentschieden!")
                    pvpgameboard.clear()
                    print()
                    print("Um erneut ein Spiel zu starten geben Sie wieder PVP oder PVC an!")
                    break
        elif gamemode == "PVC":
            pvcgame = Field
            pvcgameboard = pvcgame.create_board(pvcgame)
            name1 = input("Geben Sie den Name des Spielers an ")
            if name1 == "Exit":
                print("Das Spiel wurde erfolgreich beendet!")
                break
            player1 = Human("X", name1)
            player2 = Bot("O", None)
            if player2.choose_difficulty():  # liefert True bei Eingabe von "Exit"
                print("Das Spiel wurde erfolgreich beendet!")
                break
            while True:
                print("------------Spielfeld--------------")
                pvcgame.show_field(pvcgame, pvcgameboard)
                print()
                if player1.throw_token(pvcgameboard):  # liefert True bei Eingabe von "Exit"
                    print("Das laufende Spiel wurde erfolgreich abgebrochen!")
                    pvcgameboard.clear()
                    break
                if pvcgame.check_win(pvcgame, pvcgameboard) or pvcgame.check_draw(pvcgame, pvcgameboard):
                    print("------------Spielfeld--------------")
                    pvcgame.show_field(pvcgame, pvcgameboard)
                    print()
                    if pvcgame.check_win(pvcgame, pvcgameboard):
                        print(f"{player1.name} hat gewonnen! ")
                    else:
                        print("Es sind alle Spalten voll, es ist kein Zug mehr möglich!")
                        print("Das Spiel endet Unentschieden!")
                    pvcgameboard.clear()
                    print()
                    print("Um erneut ein Spiel zu starten geben Sie wieder PVP oder PVC an!")
                    break
                player2.throw_token(pvcgameboard)
                if pvcgame.check_win(pvcgame, pvcgameboard) or pvcgame.check_draw(pvcgame, pvcgameboard):
                    print("------------Spielfeld--------------")
                    pvcgame.show_field(pvcgame, pvcgameboard)
                    print()
                    if pvcgame.check_win(pvcgame, pvcgameboard):
                        print(f"Der Computer hat gewonnen! ")
                    else:
                        print("Es sind alle Spalten voll, es ist kein Zug mehr möglich!")
                        print("Das Spiel endet Unentschieden!")
                    pvcgameboard.clear()
                    print()
                    print("Um erneut ein Spiel zu starten geben Sie wieder PVP oder PVC an!")
                    break
        elif gamemode == "Exit":
            print("Das Spiel wurde erfolgreich beendet!")
            break
        else:
            print("Bitte geben Sie PVP oder PVC an")
