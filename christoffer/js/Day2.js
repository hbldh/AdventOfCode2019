const fs = require('fs');

fs.readFile('Day2data.txt', 'utf8', (err, data) => {
    const dataArr = data.split(',');

    const memory = getMemory(dataArr, '12', '2');
    const part1 = memory[0];

    console.log(part1);
    
    let noun = 0;
    let part2 = 0;
    
    while(noun <= 100) {
        let verb = 0;
        while(verb <= 100) {
            if (getMemory(dataArr, noun, verb)[0] == 19690720) {
                part2 = 100 * noun + verb;
                break;
            }
            verb++;
        }
        noun++;
    }

    console.log(part2);
    
});

function getMemory(inputArr, noun, verb) {
    const dataArr = [...inputArr];
    for(let index = 0; index < dataArr.length; index += 4) {
        dataArr[1] = noun;
        dataArr[2] = verb;

        const item = dataArr[index];
        const code = parseInt(item);
        const firstVal = parseInt(dataArr[dataArr[index + 1]]);
        const secondVal = parseInt(dataArr[dataArr[index + 2]]);
        
        if (code === 1) {
            dataArr[dataArr[index + 3]] = firstVal + secondVal;
        } else if (code === 2) {
            dataArr[dataArr[index + 3]] = firstVal * secondVal;
        } else if (code === 99) {
            break;
        } else {
            throw new Error("Unrecognized instruction alert");
        }
    }
    
    return dataArr;
}