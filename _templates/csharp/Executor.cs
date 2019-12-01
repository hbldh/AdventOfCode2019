using System;
using System.IO;
using System.Net.Http;

namespace AOC2019
{
    public class Executor
    {
        private readonly string sessionToken;

        public Executor(string sessionToken)
        {
            this.sessionToken = sessionToken;
        }

        public void Run(int? day)
        {
            if (day is null)
            {
                // Run all!
                ExecuteDay(1);
            }
            else
            {
                // Run specified day.
                ExecuteDay((int)day);
            }
        }

        private void ExecuteDay(int day)
        {
            EnsureData((int)day);
            Type t = Type.GetType($"AOC2019.Day{day}");
            IDay dayObj = (IDay)Activator.CreateInstance(t);
            var solutions = dayObj.Solve();
            Console.WriteLine($"Day {day}:");
            Console.WriteLine($"Part 1: {solutions.Item1}");
            Console.WriteLine($"Part 2: {solutions.Item2}");
            Console.WriteLine($"---------------------------");
        }

        private bool EnsureData(int day)
        {
            var aocFolder = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "AOC2019");
            Directory.CreateDirectory(aocFolder);
            if (!File.Exists(Path.Combine(aocFolder, $"input{day.ToString().PadLeft(2, '0')}.txt")))
            {
                using HttpClient client = new HttpClient();
                client.DefaultRequestHeaders.Add("Cookie", $"session={this.sessionToken}");
                var resp = client.GetAsync($"https://adventofcode.com/2019/day/{day}/input").ConfigureAwait(false).GetAwaiter().GetResult();
                var data = resp.Content.ReadAsStringAsync().ConfigureAwait(false).GetAwaiter().GetResult();
                File.WriteAllText(Path.Combine(aocFolder, $"input{day.ToString().PadLeft(2, '0')}.txt"), data);
            }
            return true;
        }
    }
}
