"""
Development Exercises - L8
Board class for the Tic Tac Toe game
"""

from tictactoe_ai import tictactoe_brain

class tictactoe_board:
    def __init__(self, player_selection: str):
        self.player_selection = player_selection
        self.computer_selection = ''
        if self.player_selection == 'X':
            self.computer_selection = 'O'
        else:
            self.computer_selection = 'X'

        # the ai will play the computer selection
        self.ai = tictactoe_brain(self.computer_selection)

        self.board = [' ']*10

    def draw_board(self):
        """
        Draws the board to the standard output
        """
        board = self.board
        print(board[7] + '|' + board[8] + '|' + board[9])
        print('-+-+-')
        print(board[4] + '|' + board[5] + '|' + board[6])
        print('-+-+-')
        print(board[1] + '|' + board[2] + '|' + board[3])

    def player_won(self) -> bool:
        """
        Return true if the player has won, false otherwise
        """
        if not self.get_winning_moves(self.player_selection):
            return False
        else:
            return True
        # return self.check_victory(self.player_selection)

    def ai_won(self) -> bool:
        """
        Return true if the ai has won, false otherwise
        """
        if not self.get_winning_moves(self.computer_selection):
            return False
        else:
            return True
        # return self.check_victory(self.computer_selection)

    def tied(self) -> bool:
        if len(self.get_valid_moves()) == 0:
            return True
        else:
            return False

    def get_winning_moves(self, selection: str):
        """
        Evaluates the board, to check if the given selection has won the match
        """
        board = self.board
        
        # check for rows
        for i in range(3):
            i += 1
            value = i*3
            if ((board[value] == board[value-1]) and
                (board[value-1] == board[value-2])):
                if board[value] == selection:
                    return [value-2, value-1, value]

        #check for columns
        for i in range(3):
            i += 1
            value = i
            if ((board[value] == board[value+3]) and
                (board[value+3] == board[value+6])):
                if board[value] == selection:
                    return [value, value+3, value+6]

        # check the diags
        if ((board[1] == board[5]) and 
            (board[5] == board[9])):
                if board[1] == selection:
                    return [1, 5, 9]

        if ((board[7] == board[5]) and 
            (board[5] == board[3])):
                if board[7] == selection:
                    return [3,5,7]

        return []
    
    def get_valid_moves(self) -> list:
        """
        Return a list with all the Valid Moves.
        A valid move is when there is a " " in the board
        """
        valid_moves = []
        iterboard = iter(self.board) # Get Iterator for Board
        next(iterboard)         # Skip the first position 0
        # iterate on all empty spaces
        for i, space in enumerate(iterboard):
            i += 1  # incremet one, because we ignore the 0
            if self.board[i] == ' ':
                valid_moves.append(i)
        return valid_moves

    def is_move_valid(self, move: int) -> bool:
        """
        Check if the move is empty in the list
        """
        valid_move = False
        if self.board[move] == ' ':
            valid_move = True
        return valid_move

    def do_player_move(self, move: int):
        """
        Receives where the players wants to move and perform the move
        """
        if self.is_move_valid(move):
            self.board[move] = self.player_selection
    
    def do_ai_move(self):
        best_move = self.ai.BestMove(self.board)
        if self.is_move_valid(best_move):
            self.board[best_move] = self.computer_selection