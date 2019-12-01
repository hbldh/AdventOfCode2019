using System;
using System.IO;
using System.Net;
using System.Net.Http;

namespace AOC2019
{
   
    class Day1 : IDay
    {

        private readonly string data;

        public Day1()
        {
            var aocFolder = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "AOC2019");
            this.data = File.ReadAllText(Path.Combine(aocFolder, "input01.txt"));
        }

        public string SolvePartOne()
        {
            throw new NotImplementedException();
        }

        public string SolvePartTwo()
        {
            throw new NotImplementedException();
        }
    }
}
