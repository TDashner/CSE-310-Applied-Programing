using System;

namespace TicTacToeGame
{
    struct Board
    {
        public char[,] grid;  // 3x3 grid
        public Board()
        {
            grid = new char[3, 3] { { '1', '2', '3' }, { '4', '5', '6' }, { '7', '8', '9' } };
        }

        public void DisplayBoard()
        {
            Console.Clear();
            Console.WriteLine("Tic-Tac-Toe Game");
            Console.WriteLine($" {grid[0, 0]} | {grid[0, 1]} | {grid[0, 2]} ");
            Console.WriteLine("---+---+---");
            Console.WriteLine($" {grid[1, 0]} | {grid[1, 1]} | {grid[1, 2]} ");
            Console.WriteLine("---+---+---");
            Console.WriteLine($" {grid[2, 0]} | {grid[2, 1]} | {grid[2, 2]} ");
        }
    }
}