import unittest
from unittest import mock

# * sollte eigentlich nicht verwendet werden, wird hier aber verwendet, da alle Klassen und Methoden getestet werden
# sollen.
from vier_gewinnt.connectfour import *


class ConnectFourTestCase(unittest.TestCase):

    def setUp(self) -> None:
        """Initialisierung der Variablen für Testzwecke"""
        self.p1 = Player("O")
        self.p2 = Player("X")
        self.emptyboard = [['-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-']]
        self.verticalwin = [['-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-'],
                           ['X', 'X', 'X', 'X', '-', '-', '-']]
        self.horizontalwin = [['-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', 'O', '-', '-'],
                           ['-', '-', '-', '-', 'O', '-', '-'],
                           ['-', '-', '-', '-', 'O', '-', '-'],
                           ['-', '-', '-', '-', 'O', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-']]
        self.diagonalwin = [['-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', '-'],
                           ['-', '-', '-', '-', '-', '-', 'Y'],
                           ['-', '-', '-', '-', '-', 'Y', '-'],
                           ['-', '-', '-', '-', 'Y', '-', '-'],
                           ['-', '-', '-', 'Y', '-', '-', '-']]
        self.diagonalwin2 = [['-', '-', '-', '-', '-', '-', '-'],
                            ['-', '-', '-', '-', '-', '-', '-'],
                            ['Y', '-', '-', '-', '-', '-', '-'],
                            ['-', 'Y', '-', '-', '-', '-', '-'],
                            ['-', '-', 'Y', '-', '-', '-', '-'],
                            ['-', '-', '-', 'Y', '-', '-', '-']]
        self.gameboard_draw = [ ['X', 'X', 'X', 'O', 'X', 'X', 'X'],
                                ['O', 'O', 'O', 'X', 'O', 'O', 'O'],
                                ['X', 'X', 'X', 'O', 'X', 'X', 'X'],
                                ['O', 'O', 'O', 'X', 'O', 'O', 'O'],
                                ['X', 'X', 'X', 'O', 'X', 'X', 'X'],
                                ['O', 'O', 'O', 'X', 'O', 'O', 'O']]
        self.h1 = Human("O", "Oliver")
        self.h2 = Human("X", "Kevin")
        self.bot = Bot("B", 1)


    def test_player_init(self):
        """Test Konstruktor Player"""
        self.assertEqual(self.p1.symbol, "O")
        self.assertEqual(self.p2.symbol, "X")
        self.assertIsNot(self.p1.symbol, "ABC")

    def test_human_init(self):
        """Test Konstruktor Human"""
        self.assertEqual(self.h1.name, "Oliver")
        self.assertEqual(self.h1.symbol, "O")
        self.assertIsNot(self.h2.symbol, "O")
        self.assertEqual(self.h2.name,"Kevin")

    def test_create_board(self):
        """Test leere Boarderstellung"""
        self.assertEqual(self.emptyboard, Field.create_board(Field))

    def test_show_field(self):
        """Test Spielfeldanzeige"""
        empty2 = Field.create_board(Field)
        self.assertEqual(self.emptyboard, empty2)
        self.assertIsNot(self.emptyboard, self.horizontalwin)

    def test_win_condition(self):
        """Test Gewinnermittlung"""
        self.assertEqual(True, Field.check_win(Field, self.verticalwin))
        self.assertEqual(True, Field.check_win(Field, self.horizontalwin))
        self.assertEqual(True, Field.check_win(Field, self.diagonalwin))
        self.assertEqual(True, Field.check_win(Field, self.diagonalwin2))
        self.assertEqual(False, Field.check_win(Field, self.emptyboard))
        self.assertEqual(False, Field.check_win(Field, self.gameboard_draw))

    def test_draw_condition(self):
        """Test für Unentschieden Erkennung"""
        self.assertEqual(False, Field.check_draw(Field, self.verticalwin))
        self.assertEqual(False, Field.check_draw(Field, self.horizontalwin))
        self.assertEqual(False, Field.check_draw(Field, self.diagonalwin))
        self.assertEqual(False, Field.check_draw(Field, self.emptyboard))
        self.assertEqual(True, Field.check_draw(Field, self.gameboard_draw))

    def test_throw_token_human(self):
        """Test Spielzug Spieler"""
        # hier wird UserInput mithilfe von mock generiert
        empty = Field.create_board(Field)
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: "Exit"
        self.assertEqual(True, self.h1.throw_token(self.emptyboard))
        mock.builtins.input = original_input
        mock.builtins.input = lambda _: "4"
        self.assertEqual(None, self.h1.throw_token(self.emptyboard))
        self.assertIsNot(self.emptyboard, empty)
        if self.emptyboard[5][3] == "O":
            self.assertEqual(True, True)
            print("Stein wurde erfolgreich gelegt")
        mock.builtins.input = original_input

    def test_init_bot(self):
        """Test Konstruktor Klasse Bot"""
        self.assertEqual(self.bot.symbol, "B")
        self.assertEqual(self.bot.difficulty_level, 1)
        self.assertIsNot(self.bot.symbol, "X")

    def test_throw_token_bot(self):
        """Test Spielzug Computer"""
        empty = Field.create_board(Field)
        self.bot.throw_token(self.emptyboard, 3)
        self.assertIsNot(empty, self.emptyboard)
        self.bot.throw_token(empty,3)
        self.assertEqual(empty, self.emptyboard)

    def test_choose_difficulty(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: "Exit"
        self.assertEqual(True, self.bot.choose_difficulty())
        mock.builtins.input = original_input
        mock.builtins.input = lambda _: "1"
        self.bot.choose_difficulty()
        self.assertEqual(self.bot.difficulty_level, 1)
        mock.builtins.input = original_input
        mock.builtins.input = lambda _: "3"
        self.bot.choose_difficulty()
        self.assertEqual(self.bot.difficulty_level, 3)


if __name__ == '__main__':
    unittest.main()
