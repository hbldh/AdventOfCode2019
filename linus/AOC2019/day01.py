import math
import traceback


def solve(data):
    return solve_part_1(data), solve_part_2(data)

def fuel_calc(value):
    return math.floor(int(value) / 3) - 2

#The first tired attempt that you just want to work.
def nonrecursive_fuel_calc(value):    
    fuel = fuel_calc(value)    
    sum = fuel
    while True:
        fuel = fuel_calc(fuel)
        if fuel < 0:
            break
        sum += fuel          
    return sum 

def recursive_fuel_calc(tSum, value):    
    new_value = fuel_calc(value) 
    if new_value < 0:
        return tSum, 0
    else:
        tSum += new_value
        return recursive_fuel_calc(tSum, new_value)
    
def solve_part_1(data):
    values = data.splitlines()
    sum = 0
    for value in values:
        sum += fuel_calc(value.strip())      
    return sum

def solve_part_2(data):
    values = data.splitlines()
    sum = 0
    for value in values:        
        a,b = recursive_fuel_calc(0, value)
        sum +=a                     
    return sum

if __name__ == '__main__':
    from AOC2019 import run_solver
    run_solver(solve, __file__)
