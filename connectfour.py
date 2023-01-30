class Player:
    def __init__(self):
        pass


class Field:
    rows = 6
    columns = 7

    def create_board(self) -> list:
        board = list()
        content = list()
        for i in range(self.columns):
            content.append("-")
        for i in range(self.rows):
            board.append(content)

        return board

    def show_field(self, board: list):
        for x in board:
            print(x)


if __name__ == '__main__':
    f1 = Field
    gameboard = f1.create_board(f1)
    f1.show_field(f1, gameboard)
