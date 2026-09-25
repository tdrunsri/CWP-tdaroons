PIECES = "KQRBP"


def check_line(board, king_row, king_col, row_move, col_move, attackers):
    size = len(board)

    row = king_row + row_move
    col = king_col + col_move

    while 0 <= row < size and 0 <= col < size:
        square = board[row][col]

        if square in PIECES:
            return square in attackers

        row += row_move
        col += col_move

    return False


def checkmate(board):
    if not isinstance(board, str):
        return
    rows = board.splitlines()
    size = len(rows)

    if size == 0:
        return

    for row in rows:
        if len(row) != size:
            return

    king_row = -1
    king_col = -1
    king_count = 0

    for row in range(size):
        for col in range(size):
            if rows[row][col] == "K":
                king_row = row
                king_col = col
                king_count += 1

    if king_count != 1:
        return

    # Pawn
    pawn_row = king_row + 1

    if pawn_row < size:
        left = king_col - 1
        right = king_col + 1

        if left >= 0 and rows[pawn_row][left] == "P":
            print("Success")
            return

        if right < size and rows[pawn_row][right] == "P":
            print("Success")
            return

    # Rook / Queen
    straight_directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for row_move, col_move in straight_directions:
        if check_line(
            rows,
            king_row,
            king_col,
            row_move,
            col_move,
            "RQ"
        ):
            print("Success")
            return

    # Bishop / Queen
    diagonal_directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for row_move, col_move in diagonal_directions:
        if check_line(
            rows,
            king_row,
            king_col,
            row_move,
            col_move,
            "BQ"
        ):
            print("Success")
            return

    print("Fail")
