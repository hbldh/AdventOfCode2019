using System.Net;

namespace AOC2019
{
    partial class Program
    {
        static void Main(string[] args)
        {
            // Specify Day here!
            int day = 1;
            // Get the session Cookie Value from your browser and paste it here!
            string sessionToken = "";

            Executor aoc = new Executor(sessionToken);
            aoc.Run(day);
        }
    }
}
