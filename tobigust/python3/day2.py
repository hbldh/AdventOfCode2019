"""
intcode[0] command 1=add, [1-3] position (1,2 input, 3, result)
command: 1=add, 2=multi, 99=halt

1,9,10,3,2,3,11,0,99,30,40,50


testdata
1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
"""

def halt():
    return False

def add(f, s):
    return f + s

def mult(f, s):
    return f * s

def runintc(pfile):
    with open(pfile) as prog:
        p = [int(i) for i in prog.read().split(',')]
    for v in range(100):
        for n in range(100):
            mres = cal(p)
            if mres[0] == 19690720:
                print('------', mres[1],',', mres[2], 100*mres[1]+mres[2], '------')


def cal(inind):
    ind = inind.copy()
    commands = {1:add, 2:mult, 99:halt}
    compos = 0
    com = 100
    it = 0
    while com != 99:
        command = commands[ind[compos]]
#        comname = commands[ind[compos]].__name__
        verb = ind[compos+1]
        verbval = ind[verb]
        noun = ind[compos+2]
        nounval = ind[noun]
        newpos = ind[compos+3]
        #tempr = commands[ind[compos]](ind[ind[compos+1]], ind[ind[compos+2]])
        tempr = command(verbval, nounval)
        #print(f'@{compos}: {comname} {verb}({verbval}) and {noun}({nounval}) = {tempr}, replace at {newpos}')
        ind[ind[compos+3]] = tempr
        compos = compos+4
        com = ind[compos]
        it += 1
    return ind


if __name__ == "__main__":
    runintc("inp_d2.txt")
#   t1=[1,0,0,0,99] # =2
#   t2=[2,3,0,3,99] # =6
#   t3=[2,4,4,5,99,0] # =9801
#   t4=[1,1,1,4,99,5,6,0,99] # =30
#   cal(t4)
