import numpy as np

def update_board(boards, number):
    updated_boards = []
    for board in boards:
        board =  np.where(board == number, "X", board)

        updated_boards.append(board)        

    return updated_boards

def win_check(boards):
    for board in boards:
        board_t = board.transpose()
        for i, row in enumerate(board_t):
            if np.count_nonzero(board[i] == "X") == 5 or np.count_nonzero(board_t[i] == "X") == 5:
                return [True, board]
    return [False]

def calculate_win(board, number):
    total = 0
    for row in board:
        row_numbers = [int(x) for x in row if x != "X"]
        
        total += sum(row_numbers)

    return(total * int(number))

with open("input.txt", "r") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

    for i, line in enumerate(lines):
        line = line.replace("  ", " ")
        line = line.split(" ")        
        lines[i] = line   

    numbers = lines[0][0].split(",")
    numbers.insert(0, "100") 

    boards = []

    for i in range(2, len(lines), 6):
        board = lines[i: i +5]
        for i, line in enumerate(board):
            line = [int(x) for x in line if x != ""]
            board[i] = line
        board_arr = np.array(board)
        boards.append(board_arr)

    for number in numbers:
        boards = update_board(boards, number)
        check = win_check(boards)
        if check[0]:
            winning_board = check[1]
            print(calculate_win(winning_board, number))
            break




        




        

        
   
