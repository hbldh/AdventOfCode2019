using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using AOC2019.Shared;

namespace AOC2019
{
    class Day2 : IDay
    {
        private readonly string data;
        private List<int> values;

        public Day2()
        {
            var aocFolder = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "AOC2019");
            this.data = File.ReadAllText(Path.Combine(aocFolder, "input02.txt"));
            this.values = this.data.Split(',',options:StringSplitOptions.RemoveEmptyEntries).ToList().ConvertAll(int.Parse);
        }

        public string SolvePartOne()
        {
            var computer = new IntCodeComputerDay2(this.values, 12, 2);
            computer.Process();
            return computer.memory[0].ToString();
        }

        public string SolvePartTwo()
        {
            for (int i = 0; i < 100; i++)
            {
                for (int j = 0; j <= i; j++)
                {
                    var computer = new IntCodeComputerDay2(this.values, i, j);
                    computer.Process();
                    if (computer.memory[0] == 19690720)
                    {
                        return (100 * i + j).ToString();
                    }
                }
            }
            return "0";
        }
    }
}
