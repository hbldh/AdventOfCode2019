def load_data(filename):
    with open(filename) as inp:
        orbmap = [o.strip() for o in inp]
        #orbmap = None
    return orbmap

def linkorbit(orbmap):
    orblink = {o.split(')')[1]: o.split(')')[0] for o in orbmap}  #tree leaves will be unique, suitable for dictionary key then
    #print('Orblink: ', orblink)
    return orblink

def newcount(orblink, node):
    #'Walk' from start position to COM by using the dict value as key in next iteration of recursion.
    path = []
    def recount(node):
        if orblink[node] == 'COM':
            return 1
        else:
            path.append(node)           # Append the planet you currently orbiting for every step towards COM to make a trace
            return 1 + recount(orblink[node])  #until COM is reached
    return recount(node), path

def tracenodes(node1, node2, indata):
    m = load_data(indata)
    #print(m)
    om = linkorbit(m)
    crossing = []
    for o in om:
        edges = 0
        if o == node1 or o == node2:       #if any of two start nodes is found (e.g. 'YOU' & 'SAN')
            edge, trail = newcount(om, o)
            crossing.append(trail)         #will contain trails of the two nodes path to com
            edges += edge                  #only used in part 1
            #print(edges)
    #print(crossing)
    steps = 0
    for n, c in enumerate(crossing):
        for na, a in enumerate(crossing[n]):    #iterate through each trail
            if a in crossing[(n+1)%2]:          #until finding the first orbit where the other node been to
                steps += na-1                   #Added no of steps for each node to common orbit = total orbit transitions between nodes
                #print(f'Cross at {a}, steps from start = {na-1}')
                break
        #print(n, crossing[n])
    return steps

if __name__ == "__main__":
    print(tracenodes('YOU', 'SAN', 'inp_d6.txt'))