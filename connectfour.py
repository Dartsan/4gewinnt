import abc


class Player:
    win = False
    nr_wins = 0

    def __init__(self, symbol: str):
        self.symbol = symbol

    @abc.abstractmethod
    def throw_token(self, gameboard):
        pass

    @abc.abstractmethod
    def add_win(self):
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
        for x in board:
            print(x)


class Human(Player):
    def __init__(self, symbol: str, name: str):
        super().__init__(symbol)
        super().win
        super().nr_wins
        self.name = name

    def throw_token(self, gameboard: list):
        inputstring = input(f"{self.name}: Bitte wähle eine Spalte aus, in den du deinen Stein werfen willst, indem du eine Zahl "
                           "zwischen 1 und 7 wählst")
        if inputstring.isnumeric():
            column = int(inputstring)
            while column not in range(1, 8):
                column = int(input("Das ist leider nicht möglich. Wähle eine Zahl zwischen 1 und 7"))
            for i in range(Field.rows-1, -1, -1):
                if gameboard[i][column - 1] == "-":
                    gameboard[i][column - 1] = self.symbol
                    break
        else:
            self.throw_token(gameboard)

    def add_win(self):
        self.nr_wins += 1

    def end_game(self):
        pass


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
    print("Bitte geben Sie an ob Sie Spieler gegen Spieler(PVP) oder Spieler gegen Computer(PVC) spielen wollen!")
    while True:
        gamemode = input()
        if gamemode == "PVP":
            pvpgame= Field
            pvpgameboard = pvpgame.create_board(pvpgame)
            exit = False
            name1 = input("Geben Sie den Name des ersten Spielers an")
            player1 = Human("X", name1)
            name2 = input("Geben Sie den Name des zweiten Spielers an")
            player2 = Human("O", name2)
            while True:
                player1.throw_token(pvpgameboard)
                print()
                print("------------Spielfeld--------------")
                pvpgame.show_field(pvpgame, pvpgameboard)
                print()
                player2.throw_token(pvpgameboard)
                print()
                print("------------Spielfeld--------------")
                pvpgame.show_field(pvpgame, pvpgameboard)
                print()

        elif gamemode == "PVC":
            pass
        elif gamemode == "Exit":
            break
        else:
            print("Bitte geben Sie PVP oder PVC an")