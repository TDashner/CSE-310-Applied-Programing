using System;
using System.IO;

namespace TicTacToeGame
{
    class TicTacToe : Game
    {
        private Board board;
        private char currentPlayer;
        private int turnCount;

        public TicTacToe()
        {
            board = new Board();
            currentPlayer = 'X';
            turnCount = 0;
        }

        public override void PlayGame()
        {
            while (true)
            {
                board.DisplayBoard();
                Console.WriteLine($"\nPlayer {currentPlayer}, enter a number (1-9) to place your mark:");
                
                string input = Console.ReadLine();
                if (int.TryParse(input, out int move) && move >= 1 && move <= 9)
                {
                    if (PlaceMark(move))
                    {
                        turnCount++;
                        if (CheckWin())
                        {
                            board.DisplayBoard();
                            Console.WriteLine($"\nPlayer {currentPlayer} wins!");
                            SaveGameResult($"Player {currentPlayer} won!\n");
                            break;
                        }
                        if (turnCount == 9)
                        {
                            board.DisplayBoard();
                            Console.WriteLine("\nIt's a draw!");
                            SaveGameResult("It's a draw!\n");
                            break;
                        }
                        SwitchPlayer();
                    }
                    else
                    {
                        Console.WriteLine("Invalid move! The spot is already taken.");
                    }
                }
                else
                {
                    Console.WriteLine("Invalid input! Please enter a number between 1 and 9.");
                }
            }
        }

        private bool PlaceMark(int move)
        {
            int row = (move - 1) / 3;
            int col = (move - 1) % 3;

            if (board.grid[row, col] != 'X' && board.grid[row, col] != 'O')
            {
                board.grid[row, col] = currentPlayer;
                return true;
            }
            return false;
        }

        private void SwitchPlayer()
        {
            currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
        }

        private bool CheckWin()
        {
            for (int i = 0; i < 3; i++)
            {
                if (board.grid[i, 0] == currentPlayer && board.grid[i, 1] == currentPlayer && board.grid[i, 2] == currentPlayer)
                    return true;
                if (board.grid[0, i] == currentPlayer && board.grid[1, i] == currentPlayer && board.grid[2, i] == currentPlayer)
                    return true;
            }
            if (board.grid[0, 0] == currentPlayer && board.grid[1, 1] == currentPlayer && board.grid[2, 2] == currentPlayer)
                return true;
            if (board.grid[0, 2] == currentPlayer && board.grid[1, 1] == currentPlayer && board.grid[2, 0] == currentPlayer)
                return true;
            return false;
        }

        private void SaveGameResult(string result)
        {
            string filePath = "game_results.txt";
            File.AppendAllText(filePath, result);
        }
    }
}

