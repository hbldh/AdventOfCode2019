using System;
using System.Diagnostics;
using System.IO;

namespace AOC2019
{
    public interface IDay
    {
        public Tuple<string, string> Solve()
        {
            Stopwatch t = new Stopwatch();
            t.Start();
            var x = SolvePartOne();
            t.Stop();
            var t1 = t.Elapsed.ToString("g");
            t.Reset();
            t.Start();
            var y = SolvePartTwo();
            t.Stop();
            var t2 = t.Elapsed.ToString("g");
            Console.WriteLine($"Time taken for part 1: {t1}");
            Console.WriteLine($"Time taken for part 2: {t2}");
            return Tuple.Create(x, y);
        }

        string SolvePartOne();
        string SolvePartTwo();
    }
}
