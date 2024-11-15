class Player:
    def __init__(self, color):
        self.name = color
        self.pieces = []

# The base of every piece. Has a name, unique symbol and other useful stuff.
class Piece:
    def __init__(self, character, value, coordinates):
        self.symbol = character
        self.color = value
        self.square = coordinates
        self.line_of_sight = []
        self.name = self.symbol + self.square
        self.supported = False

    def __str__(self):
        return self.symbol

    def move(self, coordinates):
        self.square = coordinates
    
    def getLineOfSight(self, board):
        self.line_of_sight = self.getPossibleMoves(board)

    def getPossibleMoves(self, board):
        pass


# The pawn piece
class Pawn(Piece):
    # The pawn also needs to know which way it's going, and the squares it can move to aren't the ones it covers
    def __init__(self, character, value, coordinates, direction):
        Piece.__init__(self, character, value, coordinates)
        self.orientation = 1 if direction == "up" else -1
        self.en_passant = False

    # Movement for the pawn is different, so we need a function separate from line of sight
    def getPossibleMoves(self, board):
        possible_moves = []
        current_row = int(self.square[1])
        current_column = self.square[0]

        # Checks for a free space in front of the pawn
        if board[current_column + str(current_row + self.orientation)] == " ":
            possible_moves.append(current_column + str(current_row + self.orientation))

            # Checks for the next free space, if the pawn hasn't moved yet
            if current_row == 2 and self.orientation == 1 or current_row == 7 and self.orientation == -1:
                if board[current_column + str(current_row + 2 * self.orientation)] == " ":
                    possible_moves.append(current_column + str(current_row + 2 * self.orientation))

        return possible_moves

    # Line of sight are the squares the pieces cover, it's different from possible moves for pawns
    def getLineOfSight(self, board):
        covered_squares = []
        current_row = int(self.square[1])
        current_column = self.square[0]

        # Checks the squares to the left and right of the pawn
        for i in [-1, 1]:
            # Checks if the side column is within the boundaries of the board
            side_column = chr(ord(current_column) + i)
            if not ord("a") <= side_column <= ord("h"):
                continue

            next_row = current_row + self.orientation

            # Checks the squares in front of the pawn for free spaces or enemy pieces
            if board[side_column + str(next_row)] == " ":
                covered_squares.append(side_column + str(next_row))
            elif board[side_column + str(next_row)].color != self.color:
                covered_squares.append(side_column + str(next_row))
            else:
                board[side_column + str(next_row)].supported = True

            # Checks the squares adjacent to the pawn for en_passant
            try:
                if board[side_column + str(current_row)].en_passant and board[side_column + str(current_row)].color != self.color:
                    covered_squares.append(side_column + str(current_row))
            except:
                pass

        self.line_of_sight = covered_squares

class Knight(Piece):
    def getPossibleMoves(self, board):
        covered_squares = []
        current_row = int(self.square[1])
        current_column = self.square[0]
        
        # Checks for the Ls up, down, left and right:
        for l in [[-1, 2], [1, 2], [-1, -2], [1, -2], [-2, 1], [-2, -1], [2, 1], [2, -1]]:
            # Checks if the side column is within the boundaries of the board
            column = chr(ord(current_column) + l[0])
            if not ord("a") <= column <= ord("h"):
                continue

            # Checks if the row is inbounds
            row = current_row + l[1]
            if not 1 <= row <= 8:
                continue

            # Checks the squares to be free or occupied by enemy pieces
            if board[column + str(row)] == " ":
                covered_squares.append(column + str(row))
            elif board[column + str(row)].color != self.color:
                covered_squares.append(column + str(row))
            else:
                board[column + str(row)].supported = True

        return covered_squares

class Bishop(Piece):
    def getPossibleMoves(self, board):
        covered_squares = []
        current_row = int(self.square[1])
        current_column = self.square[0]

        # Checks the for diagonals until it goes out of bounds or hits a piece
        for i in [[1, 1], [-1, -1], [-1, 1], [1, -1]]:
            for j in range(1, 8):
                # Checks if the given coordinates are in bounds
                row = current_row + j * i[0]
                column = chr(ord(current_column) + j * i[1])
                if not 1 <= row <= 8 or not ord("a") <= ord(column) <= ord("h"):
                    break

                if board[column + str(row)] == " ":
                    covered_squares.append(column + str(row))
                elif board[column + str(row)].color != self.color:
                    covered_squares.append(column + str(row))
                    break
                else:
                    board[column + str(row)].supported = True
                    break
    
        return covered_squares

class Rook(Piece):
    # The rook can't be used for castling if it's moved
    def __init__(self, character, value, coordinates):
        Piece.__init__(self, character, value, coordinates)
        self.moved = False

    def getPossibleMoves(self, board):
        covered_squares = []
        current_row = int(self.square[1])
        current_column = self.square[0]

        for i in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            for j in range(1, 8):
                # Checks if the given coordinates are in bounds
                row = current_row + j * i[0]
                column = chr(ord(current_column) + j * i[1])
                if not 1 <= row <= 8 or not ord("a") <= ord(column) <= ord("h"):
                    break

                # Checks if hit the edges of the board or a piece
                if board[column + str(row)] == " ":
                    covered_squares.append(column + str(row))
                elif board[column + str(row)].color != self.color:
                    covered_squares.append(column + str(row))
                    break
                else:
                    board[column + str(row)].supported = True
                    break

        return covered_squares

class Queen(Piece):
    def getPossibleMoves(self, board):
        covered_squares = []
        current_row = int(self.square[1])
        current_column = self.square[0]

        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(1, 8):
                    if j == i == 0:
                        continue

                    # Checks if the given coordinates are in bounds
                    row = current_row + k * i
                    column = chr(ord(current_column) + k * j)
                    if not 1 <= row <= 8 or not ord("a") <= ord(column) <= ord("h"):
                        break

                    # Checks if hit the edges of the board or a piece
                    if board[column + str(row)] == " ":
                        covered_squares.append(column + str(row))
                    elif board[column + str(row)].color != self.color:
                        covered_squares.append(column + str(row))
                        break
                    else:
                        board[column + str(row)].supported = True
                        break

        return covered_squares

class King(Piece):
    # The King can't castle if it's moved, also, we need to keep track of it's status
    def __init__(self, character, value, coordinates):
        Piece.__init__(self, character, value, coordinates)
        self.moved = False
        self.checked = False
        self.checkmated = False
        self.dangerous_squares = []

    # Checks the squares the king can't go to because they're covered
    def getDangerousSquares(self, board):
        self.dangerous_squares = []

        for piece in board.values():
            try:
                if piece.color != self.color:
                    self.dangerous_squares.append(piece.line_of_sight)

                    if self.square in piece.line_of_sight:
                        self.checked = True
            except:
                pass

        if self.checked:
            self.checkCheckmate(board)

    def getPossibleMoves(self, board):
        covered_squares = []
        current_row = int(self.square[1])
        current_column = self.square[0]

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue

                # Checks if the coordinates are in bounds
                row = current_row + i
                column = chr(ord(current_column) + j)
                if not 1 <= row <= 8 or not ord("a") <= ord(column) <= ord("h"):
                    break

                # Checks if the square is free, occupied by an enemy piece, or covered by an enemy
                if column + str(row) in self.dangerous_squares:
                    continue
                elif board[column + str(row)] == " ":
                    covered_squares.append(column + row)
                elif board[column + str(row)].color != self.color:
                    if not board[column + str(row)].supported:
                        covered_squares.append(column + str(row))
                else:
                    board[column + str(row)].supported = True
        
        return covered_squares

    # Analises the king's situation
    def checkCheckmate(self, board):
        current_row = int(self.square[1])
        current_column = self.square[0]

        # Checks legal moves for the king
        self.getPossibleMoves(board)
        if self.line_of_sight != []:
            return

        # Checks how many pieces are attacking the king
        checking_pieces = []
        for piece in board.values():
            try:
                if self.square in piece.line_of_sight:
                    checking_pieces.append()
            except:
                continue

        # If more than one piece are checking the king and in can't move, that's checkmate
        if len(checking_pieces) > 1:
            self.checkmated = True
            return

        
        # Searches for a piece that can capture the checking piece
        checking_piece = checking_pieces[0]
        for piece in board.values():
            if checking_piece in piece.line_of_sight:
                return

        
        # It's impossible to block a knight
        if checking_piece.symbol == "N":
            self.checkmated = True
            return

        # Searches for a piece that can block the check
        lesser_row = min(current_row, int(checking_piece.square[1]))
        greater_row = max(current_row, int(checking_piece.square[1]))

        lesser_column = min(ord(current_column), ord(checking_piece.square[0]))
        greater_column = max(ord(current_column), ord(checking_piece.square[0]))

        line = [sqr for sqr in checking_piece.line_of_sight if lesser_column < ord(sqr[0]) < greater_column and lesser_row < sqr[1] < greater_row]
        
        for piece in board.values():
            try:
                if piece.color == self.color and len([sqr for sqr in piece.line_of_sight if sqr in line]) > 0:
                    return
            except:
                continue

        # If no piece can block either, the king was checkmated
        self.checkmate = True
        return
   