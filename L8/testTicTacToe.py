#Unittesting for tic tac toe game
import io
import sys
import unittest
import ticTacToe2 as ttt

class TestUM(unittest.TestCase):

    def test_drawBoard(self):
        theBoard = [' '] * 10
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], theBoard)


    def test_inputPlayerLetter(self):
        letter_to_be_tested = 'X'
        playerLetter, computerLetter = ttt.inputPlayerLetter()
        self.assertEqual(playerLetter, letter_to_be_tested)

    def whoGoesFirstTest(self):
        pass

    def playAgainTest(self):
        pass

    def makeMoveTest(self):
        pass

    def isWinnerTest(self):
        self.b = ticTacToe2.boar

    def getBoardCopyTest(self):
        pass

    def isSpaceFreeTest(self):
        pass

    def getPlayerMoveTest(board):
        pass

    def chooseRandomMoveFromListTest(self):
        pass

    def getComputerMoveTest(self):
        pass

    def isBoardFullTest(self):
        pass







