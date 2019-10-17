import unittest


class TicTacToe:
    """This is game Tic-Tac-Toe"""
    def __init__(self):
        self.__field = [[" "] * 3 for _ in range(3)]
        self.__move = 0
        self.__symb_x = "X"
        self.__symb_o = "O"
        self.__symb_empty = " "
        self.__win_x = "X"
        self.__wins_o = "O"
        self.__draw = "draw"
        self.__ongoing = "ongoing"
        self.__chars = [self.__symb_x, self.__symb_o]
        self.__game_status = self.__ongoing

    def __str__(self):
        """Returns string - game in table view"""
        string = ""
        for i in range(3):
            string += "|"
            string += "|".join(self.__field[i])
            string += "|\n"
        return string

    def __is_valid(self, i, j):
        """Returns boolean - checks if move in cell (i, j) is valid"""
        if not (0 <= i <= 2 and 0 <= j <= 2):
            return False
        return not self.is_finished() and self.__field[i][j] == self.__symb_empty

    def make_move(self, i, j):
        """Makes move in cell (i, j) and updates game status

        Returns True - if move is successful
        False else
        """
        i, j = i - 1, j - 1
        if not self.__is_valid(i, j):
            return False
        self.__field[i][j] = self.__chars[self.__move]
        self.__move = 1 - self.__move
        self.__update_status(i, j)
        return True

    def __update_status(self, i, j):
        """Updates status after move in cell (i, j)"""
        if all(self.__field[i][k] == self.__symb_x for k in range(3)):
            self.__game_status = self.__win_x
            return
        if all(self.__field[k][j] == self.__symb_o for k in range(3)):
            self.__game_status = self.__wins_o
            return
        if i == j:
            if all(self.__field[k][k] == self.__symb_x for k in range(3)):
                self.__game_status = self.__win_x
                return
            if all(self.__field[k][k] == self.__symb_o for k in range(3)):
                self.__game_status = self.__wins_o
                return
        if i + j == 2:
            if all(self.__field[k][2 - k] == self.__symb_x for k in range(3)):
                self.__game_status = self.__win_x
                return
            if all(self.__field[k][2 - k] == self.__symb_o for k in range(3)):
                self.__game_status = self.__wins_o
                return

        if not any(self.__field[i][j] == self.__symb_empty for i in range(3) for j in range(3)):
            self.__game_status = self.__draw


    def is_finished(self):
        """Returns boolean - if game is finished"""
        return self.__game_status != self.__ongoing

    def get_status(self):
        """Returns string - status"""
        return self.__game_status

    def whose_move(self):
        """Returns string - whose move is now"""
        return self.__chars[self.__move]

    def status_ongoing(self):
        """Returns ongoing status value"""
        return self.__ongoing

    def get_status_draw(self):
        """Returns draw status value"""
        return self.__draw

    def get_status_wins_x(self):
        """Returns wins X status value"""
        return self.__win_x

    def get_status_wins_o(self):
        """Returns wins O status value"""
        return self.__wins_o

    def get_symbol_x(self):
        """Returns symbol of X"""
        return self.__symb_x

    def get_symbol_o(self):
        """Returns symbol of O"""
        return self.__symb_o


class TestTicTacToe(unittest.TestCase):
    """Class to test game TicTacToe"""
    def setUp(self):
        """Initiates first moves of game"""
        self.game = TicTacToe()
        self.game.make_move(1, 1)
        self.game.make_move(3, 2)
        self.game.make_move(1, 2)
        self.game.make_move(3, 4)

    def test_make_move(self):
        """Test make_move method"""
        self.game.make_move(1, 1)
        self.assertEqual(str(self.game), "|X|X| |\n| | | |\n| |O| |\n")

    def test_str(self):
        """Test string convertion"""
        self.game.make_move(3, 4)
        self.assertEqual(str(self.game), "|X|X| |\n| | | |\n| |O| |\n")

    def test_is_finished(self):
        """Test is_finished method"""
        self.game.make_move(2, 2)
        self.assertEqual(self.game.is_finished(), False)
        self.game.make_move(1, 3)
        self.assertEqual(self.game.is_finished(), True)

    def test_get_status(self):
        """Test get_status method"""
        self.assertEqual(self.game.get_status(), self.game.status_ongoing())

    def test_whose_move(self):
        """Test whose_move method"""
        self.assertEqual(self.game.whose_move(), self.game.get_symbol_o())
        self.game.make_move(3, 3)
        self.assertEqual(self.game.whose_move(), self.game.get_symbol_x())

    def test_get_status_ongoing(self):
        """Test get_status_ongoing method"""
        self.assertEqual(self.game.status_ongoing(), "ongoing")

    def test_get_status_draw(self):
        """Test get_status method"""
        self.assertEqual(self.game.get_status_draw(), "draw")

    def test_get_status_wins_x(self):
        """Test get_status_wins_x method"""
        self.assertEqual(self.game.get_status_wins_x(), "X")

    def test_get_status_wins_o(self):
        """Test get_status_wins_o method"""
        self.assertEqual(self.game.get_status_wins_o(), "O")

    def test_get_symbol_x(self):
        """Test get_symbol_x method"""
        self.assertEqual(self.game.get_symbol_x(), "X")

    def test_get_symbol_o(self):
        """Test get_symbol_o method"""
        self.assertEqual(self.game.get_symbol_o(), "O")




if __name__ == "__main__":
    unittest.main()
