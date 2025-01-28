import random

def check_winner(board):
    # Case 1: Criss-cross (diagonals)
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    # Case 2: Vertical
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Case 3: Horizontal
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            return True

    return False

def is_draw(board):
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def switch_player(current_player):
    return "O" if current_player == "X" else "X"

def reset_board():
    return [[" "] * 3 for _ in range(3)]

def print_board(board):
    cell_mapping = [str(i) if cell == " " else cell for i, cell in enumerate(sum(board, []), 1)]
    for i in range(0, 9, 3):
        print(" | ".join(cell_mapping[i:i+3]))
        if i < 6:
            print("-" * 9)

def map_input_to_indices(cell):
    mapping = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    return mapping.get(cell, (-1, -1))

def main():
    print("Welcome to Tic Tac Toe!")
    mode = input("Choose mode: (1) Single Player (2) Two Players: ")

    while mode not in ["1", "2"]:
        print("Invalid choice. Please choose 1 or 2.")
        mode = input("Choose mode: (1) Single Player (2) Two Players: ")

    is_single_player = mode == "1"

    board = reset_board()
    current_player = "X" if random.choice([True, False]) else "O"
    print(f"\nStarting player: {current_player}\n")
    is_game_over = False

    while not is_game_over:
        print_board(board)
        if is_single_player and current_player == "O":
            print("\nBot's turn")
            available_cells = [i for i in range(1, 10) if board[map_input_to_indices(i)[0]][map_input_to_indices(i)[1]] == " "]
            cell = random.choice(available_cells)
            print(f"Bot chooses cell {cell}\n")
        else:
            print(f"\nPlayer {current_player}'s turn")
            try:
                cell = int(input("Enter cell number (1-9): "))
                row, col = map_input_to_indices(cell)
                if row == -1 or board[row][col] != " ":
                    print("Invalid or already taken cell, choose a different one.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

        row, col = map_input_to_indices(cell)
        board[row][col] = current_player

        if check_winner(board):
            print_board(board)
            print(f"***Player {current_player} wins!***")
            is_game_over = True
        elif is_draw(board):
            print_board(board)
            print("\n---It's a draw!---")
            is_game_over = True
        else:
            current_player = switch_player(current_player)

    print("\nOptions: (1) New Match (2) Stop Match\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        main()
    elif choice == "2":
        print("---Thanks for playing!---")

if __name__ == "__main__":
    main()
