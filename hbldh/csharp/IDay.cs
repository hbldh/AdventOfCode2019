using System;
using System.IO;

namespace AOC2019
{
    public interface IDay
    {
        public Tuple<string, string> Solve()
        {
            return Tuple.Create(SolvePartOne(), SolvePartTwo());
        }

        string SolvePartOne();
        string SolvePartTwo();
    }
}
