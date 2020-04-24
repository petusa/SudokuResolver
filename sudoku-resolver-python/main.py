from random import randrange

print('SudokuResolver')

def create_board(size=9):
    board = []
    for _ in range(size):
        row = [0]*size
        board.append(row)
    return board

def select_random_indices(num, size):
    random_indices = []
    while len(random_indices)!=num:
        selected_index = randrange(size)
        if selected_index not in random_indices:
            random_indices.append(selected_index)
    return random_indices

def generate_board(num_of_cells=9):
    board  = create_board(9)
    random_indices = select_random_indices(num_of_cells, 9*9)
    for random_index in random_indices:
        row = random_index // 9
        col = random_index % 9
        val = randrange(1,10)
        while not is_valid(val, row, col, board):
            val = randrange(1, 10)
        board[row][col] = val
    return board

def print_board(board):
    for row in range(9):
        if row % 3==0:
            print("-"*31)
        for col in range(9):
            if col % 3==0:
                print("|", end="")
            print(" ", end="")
            print(board[row][col], end="")
            print(" ", end="")
        print("|")
    print("-"*31)

def in_division(num, row, col, board):
    div_row = row // 3
    div_col = col // 3
    for r in range(div_row*3, div_row*3 + 3):
        for c in range(div_col*3, div_col*3 + 3):
            if num == board[r][c]:
                return True
    return False

def in_column(num, col, board):
    for row in board:
        if row[col] == num:
            return True
    return False

def is_valid(num, row, col, board):
    return num not in board[row] and not in_column(num, col, board) and not in_division(num, row, col, board)

if __name__ == "__main__":
    board = generate_board(38)
    print_board(board)
