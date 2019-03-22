"""
Development Exercises - L8
Unit Testing for TicTacToe board class
"""

import unittest

from tictactoe_board import tictactoe_board

class test_tictactoe_board(unittest.TestCase):
    def setUp(self):
        self.b = tictactoe_board('X')

    def tearDown(self):
        self.b = None

    def test_player_victory_row1(self):
        board = [" ", "X","X","X",
                      " "," "," ",
                      " "," "," "]
        self.b.board = board
        self.assertEqual(True, self.b.player_won())

    def test_player_victory_row2(self):
        board = [" ", "X","O","X",
                      "X","X","X",
                      " "," "," "]
        self.b.board = board
        self.assertEqual(True, self.b.player_won())

    def test_player_victory_row3(self):
        board = [" ", "X","O","X",
                      " "," ","O",
                      "X","X","X"]
        self.b.board = board
        self.assertEqual(True, self.b.player_won())

    def test_player_not_won(self):
        board = [" ", "X","O","X",
                      " ","O","O",
                      "X"," ","X"]
        self.b.board = board
        self.assertEqual(False, self.b.player_won())

    def test_player_victory_col1(self):
        board = [" ", "X","O","X",
                      "X","O","O",
                      "X"," ","X"]
        self.b.board = board
        self.assertEqual(True, self.b.player_won())

    def test_player_victory_col2(self):
        board = [" ", "X","X","X",
                      " ","X","O",
                      " ","X","X"]
        self.b.board = board
        self.assertEqual(True, self.b.player_won())

    def test_player_victory_col3(self):
        board = [" ", "X","O","X",
                      " ","O","X",
                      " "," ","X"]
        self.b.board = board
        self.assertEqual(True, self.b.player_won())

    def test_player_victory_diag1(self):
        board = [" ", "X","O","O",
                      " ","X","O",
                      "X"," ","X"]
        self.b.board = board
        self.assertEqual(True, self.b.player_won())

    def test_player_victory_diag2(self):
        board = [" ", "O","O","X",
                      " ","X","O",
                      "X"," ","X"]
        self.b.board = board
        self.assertEqual(True, self.b.player_won())

    def test_ai_victory(self):
        board = [" ", "O","O","O",
                      " ","X","O",
                      "X"," ","X"]
        self.b.board = board
        self.assertEqual(True, self.b.ai_won())

    def test_ai_not_victory(self):
        board = [" ", "O"," ","O",
                      " ","X","O",
                      "X"," ","X"]
        self.b.board = board
        self.assertEqual(False, self.b.ai_won())

    def test_game_tied(self):
        board = [" ", "O","X","O",
                      "O","X","O",
                      "X","O","X"]
        self.b.board = board
        self.assertEqual(True, self.b.tied())

    def test_game_not_tied(self):
        board = [" ", "O","X","O",
                      "O"," ","O",
                      "X","O","X"]
        self.b.board = board
        self.assertEqual(False, self.b.tied())

    def test_get_valid_moves(self):
        board = [" ", " "," ","O",
                      "O"," ","O",
                      "X","O","X"]
        self.b.board = board
        self.assertListEqual([1,2,5], self.b.get_valid_moves())

    def test_is_move_valid_true(self):
        board = [" ", " "," ","O",
                      "O"," ","O",
                      "X","O","X"]
        self.b.board = board
        self.assertEqual(True, self.b.is_move_valid(5))

    def test_is_move_valid_false(self):
        board = [" ", " "," ","O",
                      "O"," ","O",
                      "X","O","X"]
        self.b.board = board
        self.assertEqual(False, self.b.is_move_valid(3))

    def test_player_move_valid(self):
        board = [" ", " "," ","O",
                      "O"," ","O",
                      "X","O","X"]
        self.b.board = board
        self.b.do_player_move(5)
        self.assertListEqual([" ", " "," ","O",
                                   "O","X","O",
                                   "X","O","X"], self.b.board)

    def test_player_move_invalid(self):
        board = [" ", " "," ","O",
                      "O"," ","O",
                      "X","O","X"]
        self.b.board = board
        self.b.do_player_move(6)
        self.assertListEqual([" ", " "," ","O",
                                   "O"," ","O",
                                   "X","O","X"], self.b.board)

    def test_player_move_invalid(self):
        board = [" ", "X","O","X",
                      "O","O","X",
                      " "," "," "]
        self.b.board = board
        self.b.do_ai_move()
        self.assertListEqual([" ", "X","O","X",
                                   "O","O","X",
                                   " ","O"," "], self.b.board)

    pass

if __name__ == '__main__':
    unittest.main()