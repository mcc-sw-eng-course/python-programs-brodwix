"""
Development Exercises - L8
MinMax Algorithm for choosing the best move, and optimized with AB pruning.
"""

class tictactoe_brain:

    def __init__(self, player_selection: str):
        self.player_selection = player_selection
        self.computer_selection = ''
        if self.player_selection == 'X':
            self.computer_selection = 'O'
        else:
            self.computer_selection = 'X'

    def Evaluate(self, board: list) -> int:
        """
        Evaluate function for a Tic Tac Toe Game.
        The Board var: (position 0 is ignored, we always add one to the loop)
        board = ["0", "1","2","3",
                      "4","5","6",
                      "7","8","9"]
        Numbers are position in the array, and we will matche them for X or O.
        When  we detect a win, if it is an X we return 10, if it is an O we return -10
        When no one will win, we return 0.
        """
        player_selection = self.player_selection
        computer_selection = self.computer_selection
        # Check if there is a win in any row of the board
        for i in range(3):
            i += 1
            value = i*3
            if ((board[value] == board[value-1]) and
                (board[value-1] == board[value-2])):
                if board[value] == player_selection:
                    return 10
                elif board[value] == computer_selection:
                    return -10

        # Check if there is a win in any column in the board
        for i in range(3):
            i += 1
            value = i
            if ((board[value] == board[value+3]) and
                (board[value+3] == board[value+6])):
                if board[value] == player_selection:
                    return 10
                elif board[value] == computer_selection:
                    return -10

        # check win in any diagonal in the board
        if ((board[1] == board[5]) and 
            (board[5] == board[9])):
                if board[1] == player_selection:
                    return 10
                elif board[1] == computer_selection:
                    return -10

        if ((board[7] == board[5]) and 
            (board[5] == board[3])):
                if board[7] == player_selection:
                    return 10
                elif board[7] == computer_selection:
                    return -10
        # no one has won!
        return 0

    def MovesLeft(self, board: list) -> bool:
        """
        Checks if there are possible moves within the board.
        An empty space in a position is a Move Left.
        Position 0 must be Ignored.
        board = [" ", " ","X","X",
                      "O","X","O",
                      "O","O","X"]
        In this example board there is 1 move left to do.
        """
        iterboard = iter(board) # Get Iterator for Board
        next(iterboard)         # Skip the first position 0
        for space in iterboard:
            if space == ' ':
                return True
        return False

    def Minmax(self, board: list, depth: int, isMax: bool, alpha: int, beta: int) -> int:
        """
        MinMax function. Consider all possibilities of the Tic Tac Toe Game
        and return the value of the given board
        """
        score = self.Evaluate(board)

        player_selection = self.player_selection
        computer_selection = self.computer_selection

        # Max has won the Game
        if score == 10:
            return score

        # Min has won the Game
        if score == -10:
            return score

        # The game is a tie when there are no moves left
        if self.MovesLeft(board) == False:
            return 0

        # if it's Max turn
        if True == isMax:
            best = -1000
            iterboard = iter(board) # Get Iterator for Board
            next(iterboard)         # Skip the first position 0
            # iterate on all empty spaces
            for i, space in enumerate(iterboard):
                i += 1  # incremet one, because we ignore the 0
                if space == ' ': # space is empty
                    board[i] = player_selection  # make the move with Max
                    # recursively call Minmax
                    best = max(best, self.Minmax(board, depth + 1, not isMax, alpha, beta))
                    alpha = max(best, alpha)
                    board[i] = ' '  # undo the move to have a clean board
                    if beta <= alpha:
                        break
            return best
        # Min turn
        else:    
            best = 1000
            iterboard = iter(board) # Get Iterator for Board
            next(iterboard)         # Skip the first position 0
            # iterate on all empty spaces
            for i, space in enumerate(iterboard):
                i += 1  # incremet one, because we ignore the 0
                if space == ' ': # space is empty
                    board[i] = computer_selection  # make the move with Max
                    # recursively call Minmax
                    best = min(best, self.Minmax(board, depth + 1, not isMax, alpha, beta))
                    beta = min(best, beta)
                    board[i] = ' '  # undo the move to have a clean board
                    if beta <= alpha:
                        break
            return best

    def BestMove(self, board: list) -> int:
        """
        Find the best move available fot the AI opponent.
        Iterate all cell, evaluate MinMax function for all empty cells.
        Return the cell with optimal value
        """
        best_value = -1000
        best_move = -1

        iterboard = iter(board) # Get Iterator for Board
        next(iterboard)         # Skip the first position 0
        # iterate on all empty spaces
        for i, space in enumerate(iterboard):
            i += 1  # incremet one, because we ignore the 0
            if space == ' ': # space is empty
                board[i] = self.player_selection
                move_value = self.Minmax(board, 0, False, -1000, 1000)
                board[i] = ' '  # undo the move to have a clean board

                if move_value > best_value:
                    best_move = i
                    best_value = move_value
        return best_move