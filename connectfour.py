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
        #content = list()
        #for i in range(self.columns):
            #content.append("-")
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
        column = int(input("Bitte wähle eine Spalte aus, in den du deinen Stein werfen willst, indem du eine Zahl zwischen 1 und 7 wählst"))
        while column not in range(1, 8):
            column = int(input("Das ist leider nicht möglich. Wähle eine Zahl zwischen 1 und 7"))
        for i in range(5, -1, -1):
            if gameboard[i][column - 1] == "-":
                gameboard[i][column - 1] = self.symbol
                break

    def add_win(self):
        self.nr_wins += 1

    def end_game(self):
        pass


if __name__ == '__main__':
    f1 = Field
    gameboard = f1.create_board(f1)
    f1.show_field(f1, gameboard)
    h1 = Human("X", "Hannes")
    h1.throw_token(gameboard)
    f1.show_field(f1, gameboard)
    h1.throw_token(gameboard)
    f1.show_field(f1, gameboard)