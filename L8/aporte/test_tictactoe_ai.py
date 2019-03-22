"""
Development Exercises - L8
Unit Testing for MinMax Algorithm
"""

import unittest

from tictactoe_ai import tictactoe_brain

class test_tictactoe_ai(unittest.TestCase):

    def setUp(self):
        self.b = tictactoe_brain('X')
        self.MIN = -1000
        self.MAX = +1000

    def tearDown(self):
        self. b = None

    # Testing Evaluate Function
    def test_evaluate_first_row(self):
        board = [" ", "X","X","X",
                      " "," "," ",
                      " "," "," "]
        self.assertEqual(10, self.b.Evaluate(board))
        board = [" ", "O","O","O",
                      " "," "," ",
                      " "," "," "]
        self.assertEqual(-10, self.b.Evaluate(board))

    def test_evaluate_middle_row(self):
        board = [" ", " "," "," ",
                      "X","X","X",
                      " "," "," "]
        self.assertEqual(10, self.b.Evaluate(board))
        board = [" ", " "," "," ",
                      "O","O","O",
                      " "," "," "]
        self.assertEqual(-10, self.b.Evaluate(board))

    def test_evaluate_last_row(self):
        board = [" ", " "," "," ",
                      " "," "," ",
                      "X","X","X"]
        self.assertEqual(10, self.b.Evaluate(board))
        board = [" ", " "," "," ",
                      " "," "," ",
                      "O","O","O"]
        self.assertEqual(-10, self.b.Evaluate(board))

    def test_evaluate_first_col(self):
        board = [" ", "X"," "," ",
                      "X"," "," ",
                      "X"," "," "]
        self.assertEqual(10, self.b.Evaluate(board))
        board = [" ", "O"," "," ",
                      "O"," "," ",
                      "O"," "," "]
        self.assertEqual(-10, self.b.Evaluate(board))

    def test_evaluate_middle_col(self):
        board = [" ", " ","X"," ",
                      " ","X"," ",
                      " ","X"," "]
        self.assertEqual(10, self.b.Evaluate(board))
        board = [" ", " ","O"," ",
                      " ","O"," ",
                      " ","O"," "]
        self.assertEqual(-10, self.b.Evaluate(board))

    def test_evaluate_last_col(self):
        board = [" ", " "," ","X",
                      " "," ","X",
                      " "," ","X"]
        self.assertEqual(10, self.b.Evaluate(board))
        board = [" ", " "," ","O",
                      " "," ","O",
                      " "," ","O"]
        self.assertEqual(-10, self.b.Evaluate(board))

    def test_evaluate_first_diag(self):
        board = [" ", "X"," "," ",
                      " ","X"," ",
                      " "," ","X"]
        self.assertEqual(10, self.b.Evaluate(board))
        board = [" ", "O"," "," ",
                      " ","O"," ",
                      " "," ","O"]
        self.assertEqual(-10, self.b.Evaluate(board))

    def test_evaluate_second_diag(self):
        board = [" ", " "," ","X",
                      " ","X"," ",
                      "X"," "," "]
        self.assertEqual(10, self.b.Evaluate(board))
        board = [" ", " "," ","O",
                      " ","O"," ",
                      "O"," "," "]
        self.assertEqual(-10, self.b.Evaluate(board))

    def test_evaluate_no_winner(self):
        board = [" ", "X","O","X",
                      "O","O","X",
                      "X","X","O"]
        self.assertEqual(0, self.b.Evaluate(board))

    # Testing MoveLeft Function
    def test_MovesLeft_true(self):
        board = [" ", " ","X","X",
                      "O","X","O",
                      "O","O","X"]
        self.assertEqual(True, self.b.MovesLeft(board))

    def test_MovesLeft_false(self):
        board = [" ", "X","X","X",
                      "O","X","O",
                      "O","O","X"]
        self.assertEqual(False, self.b.MovesLeft(board))

    # Testing MinMax Function
    def test_minmax_MaxWin(self):
        board = [" ", "X","O","X",
                      "O","O","X",
                      " "," "," "]
        self.assertEqual(10, self.b.Minmax(board, 0, True, self.MIN, self.MAX))
    
    def test_minmax_MinWin(self):
        board = [" ", "X","O","X",
                      "O","O","X",
                      " "," "," "]
        self.assertEqual(-10, self.b.Minmax(board, 0, False, self.MIN, self.MAX))

    def test_minmax_BestMove_O(self):
        self.b = tictactoe_brain('O')
        board = [" ", "X","O","X",
                      "O","O","X",
                      " "," "," "]
        self.assertEqual(8, self.b.BestMove(board))

    def test_minmax_BestMove_X(self):
        self.b = tictactoe_brain('X')
        board = [" ", "X","O","X",
                      "O","O","X",
                      " "," "," "]
        self.assertEqual(9, self.b.BestMove(board))

if __name__ == '__main__':
    unittest.main()