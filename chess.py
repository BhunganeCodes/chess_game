def parse_fen(board: str) -> list:
    pieces, color, castling, enpassant, halfmove, fullmove = board.split()
    pieces = pieces.split("/")

    board_repr = []
    for row in pieces:
        for piece in row:
            if piece.isdigit():
                piece = ["."] * int(piece)
                board_repr.extend(piece)
            else:
                board_repr.append(piece)
    return board_repr

print(parse_fen("rnbqkb1r/pppppppp/8/8/8/8/PPPPPPPP/RNBQKB1R w KQkq - 0 1"))