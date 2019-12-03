const fs = require('fs');

fs.readFile('Day1data.txt', 'utf8', (err, data) => {

        if (err) throw err;

        const massArr = data.split("\n");
        const calcFuel = (n) => Math.floor(parseInt(n) / 3 - 2);
        
        const sum1 = massArr.map(x => calcFuel(x)).reduce((acc, curr) => acc + curr);
        
        console.log(sum1);
        
        const calcFuelR = (x) => {
          const fuel = calcFuel(x);
          if (fuel <= 0) {
             return 0;
          } else {
             return fuel + calcFuelR(fuel);
          }
        }
        
        const sum2 = massArr.map(x => calcFuelR(x)).reduce((acc, curr) => acc + curr);
        
        console.log(sum2);
});