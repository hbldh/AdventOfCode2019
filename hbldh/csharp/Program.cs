﻿using System.Net;

namespace AOC2019
{
    partial class Program
    {
        static void Main(string[] args)
        {
            int day = 2;
            string sessionToken = "";

            Executor aoc = new Executor(sessionToken);
            aoc.Run(day);
        }
    }
}
