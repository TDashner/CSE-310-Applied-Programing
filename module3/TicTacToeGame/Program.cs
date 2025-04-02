using System;

namespace TicTacToeGame
{    
    abstract class Game
    {
        public abstract void PlayGame();
    }

    class Program
    {
        static void Main(string[] args)
        {
            TicTacToe game = new TicTacToe();
            game.PlayGame();
            Console.WriteLine("\nGame over. Press any key to exit.");
            Console.ReadKey();
        }
    }
}
