"""
take its mass, divide by three, round down, and subtract 2

part 2:
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583
"""

def load_data(filename):
    ires = 0
    with open(filename) as inp:
        for i in inp:
            ires += calc(int(i))
    return ires

def calc(modweight):
    result = 0
    while modweight > 0:
        fuel = int(modweight/3)-2
        if fuel > 0:
            result += fuel
        modweight = fuel
    return result


if __name__ == "__main__":
    print(load_data("inp.txt"))
