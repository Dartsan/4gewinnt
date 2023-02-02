import abc
import random


class Player:

    def __init__(self, symbol: str):
        self.symbol = symbol

    @abc.abstractmethod
    def throw_token(self, gameboard):
        pass


class Field:
    rows = 6
    columns = 7
    board = list()

    def create_board(self) -> list:
        for i in range(self.rows):
            self.board.append(list())
            for j in range(self.columns):
                self.board[i].append("-")

        return self.board

    def show_field(self, board: list):
        print([str(y) for y in range(1, 8)])
        print()
        for x in board:
            print(x)

    def check_win(self, gameboard: list[list[str]]) -> bool:
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
        # von links oben nach rechts unten: (haut hin)
        for i in range(Field.rows - 3):
            for j in range(Field.columns - 3):
                if (gameboard[i][j] != "-") and (
                        gameboard[i][j] == gameboard[i + 1][j + 1] == gameboard[i + 2][j + 2] == gameboard[i + 3][
                        j + 3]):
                    win = True
        return win

    def check_draw(self, gameboard: list[list[str]]) -> bool:
        draw = False
        if "-" not in gameboard[0]:
            draw = True
        return draw


class Human(Player):
    def __init__(self, symbol: str, name: str):
        super().__init__(symbol)
        self.name = name

    def throw_token(self, gameboard: list):
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
        super().__init__(symbol)
        self.difficulty_level = difficulty_level

    def throw_token(self, gameboard: list[list[str]], column: int):
        if self.difficulty_level == 1:
            for i in range(Field.rows - 1, -1, -1):
                if gameboard[i][column] == "-":
                    gameboard[i][column] = self.symbol
                    break
        elif self.difficulty_level == 2:
            pass
        else:
            pass

    def choose_difficulty(self):
        difficulty = input("Geben Sie den Schwierigkeitsgrad des Computers an. "
                           "Dieser kann zwischen 1 (sehr einfach) und 3 (schwierig) liegen: ")
        if difficulty == "Exit":
            print("Das Spiel wurde erfolgreich beendet!")
            return True
        elif difficulty.isnumeric():
            self.difficulty_level = int(difficulty)
            while self.difficulty_level not in range(1, 4):
                difficulty = input("Das ist leider nicht möglich! "
                                   "Bitte wählen Sie eine Schwierigkeit zwischen 1 und 3: ")
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
    # f1 = Field
    # gameboard = f1.create_board(f1)
    # f1.show_field(f1, gameboard)
    # h1 = Human("X", "Hannes")
    # h1.throw_token(gameboard)
    # f1.show_field(f1, gameboard)
    # h1.throw_token(gameboard)
    # f1.show_field(f1, gameboard)

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
                if player1.throw_token(pvpgameboard):
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
                if player2.throw_token(pvpgameboard):
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
            if player2.choose_difficulty():
                print("Das Spiel wurde erfolgreich beendet!")
                break
            possible_numbers = [i for i in range(0, Field.columns)]
            while True:
                print("------------Spielfeld--------------")
                pvcgame.show_field(pvcgame, pvcgameboard)
                print()
                if player1.throw_token(pvcgameboard):
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
                for i in possible_numbers:
                    if pvcgameboard[0][i] != "-":
                        possible_numbers.remove(i)
                column = random.choice(possible_numbers)
                player2.throw_token(pvcgameboard, column)
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
