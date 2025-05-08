# We need a board to work on, so that is step 1
# We need pieces to work with, so that is step 2
# We have to implement the turns to be taken by the players, so that is step 3
# We need to implement the moves of the pieces by the players, so that is step 4


def parse_fen(fen):
    # create an 8x8 matrix
    board = [0] * 8
    for i in range(len(board)):
        board[i] = ["__"] * 8

    for row in board:
        for col in row:
            print(col, end = " ")
        print("")
# (0, 0) => a8 .. So we want our co-ordinates to be updated
    for i, row in enumerate(board):
        print(8 - i, end = ": ")
        for j, col in enumerate(row):
            print(col, end = " ")
        print("\n")
    print(" " * 3 + "a" + " " * 2 + "b" + " " * 2 + "c" + " " * 2 + "d" + " " * 2 + "e" + " " * 2 + "f" + " " * 2 + "g" + " " * 2 + "h")

    # hash table for pieces
    white_pieces = {
        "P": [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
        "N": [(7, 1), (7, 6)],
        "B": [(7, 2), (7, 5)],
        "R": [(7, 0), (7, 7)],
        "Q": [(7, 3)],
        "K": [(7, 4)]
    }

    black_pieces = {
        "p": [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
        "n": [(0, 1), (0, 6)],
        "b": [(0, 2), (0, 5)],
        "r": [(0, 0), (0, 7)],
        "q": [(0, 3)],
        "k": [(0, 4)]
    }

    col_map = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
    }


    # Now we are putting the white pieces on the board
    for piece, squares in white_pieces.items():     # we are looping through the pieces
        for square in squares:                      # we are looping thrqough the squares
            x, y = square[0], square[1]          # we are getting the x and y coordinates
            board[x][y] = piece                  # we are putting the piece on the board

    # Now we are putting the black pieces on the board
    for piece, squares in black_pieces.items():     # we are looping through the pieces
        for square in squares:                      # we are looping thrqough the squares
            x, y = square[0], square[1]          # we are getting the x and y coordinates
            board[x][y] = piece                  # we are putting the piece on the board

parse_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

    


def generate_moves(board):
    raise NotImplementedError("This function is not implemented yet.")


def apply_move(board, move):
    raise NotImplementedError("This function is not implemented yet.")