# 🎮 Tic Tac Toe Game 🕹️

Hey there! Welcome to my first Python project — **Tic Tac Toe Game**! 😎  
You can play with a friend (2-player mode) or challenge the bot (single-player mode). Enjoy! 🎉

## 🌟 Features
- Play as 'X' or 'O' ✖️⭕
- 1 Player (vs. Bot 🤖) or 2 Player modes 🙋‍♂️🙋‍♀️
- Game board that updates after every move 🔄
- Auto-detects win 🏆 or draw ✋
- Allows users to start a new match or stop playing 🔄❌
- Error handling for invalid inputs ❌
- Console based game.

## 🎮 How to Play

1. **Choose Game Mode:**
   - **Single Player**: Play against the bot 🤖.
   - **Two Players**: Play with a friend 👯‍♂️.

2. **Gameplay:**
   - The board is a 3x3 grid (numbers 1-9 represent cells). 🟥🟦🟩🟨🟪🟩🟦🟩🟨
   - Players take turns placing their symbol ('X' or 'O') on the board.
   - The first to align 3 of their symbols in a row, column, or diagonal wins! 🏅
   - After the game ends, you can either start a **New match** or **Stop playing**. 🔄❌

3. **Error Handling:**
   - Invalid inputs (like selecting an already occupied cell or non-numeric input) are caught, and the player is asked to choose a valid option. 🚫

4. **End Game:**
   - The game ends with a win 🏆 or a draw 😬.

## 💻 Code Breakdown

- **check_winner(board)**: Checks if there's a winner (3 symbols in a row) 🏆
- **is_draw(board)**: Checks if the game ended in a draw ✋
- **switch_player(current_player)**: Switches players between 'X' and 'O' 🔄
- **reset_board()**: Resets the board for a new game ♻️
- **print_board(board)**: Prints the game board for you to see 🔲
- **map_input_to_indices(cell)**: Maps the cell numbers (1-9) to actual board positions 🎲

## 🙏 Credits

Made with ❤️ by **HARSHINI R.** 😅!  
Hope you like it and give me feedback! 💬

---

Thanks for checking it out! Let's see who wins first: you or the bot? 😜
