from math import cos, sin, pi
"""
A vertical line can only intersect with a horizontal line

A line is vertical if it has U or D
A line is horizontal if it has R or L

Calculate coords of all lines, keep UDRL.
Sort by vert or horiz
compare vert of wire 1 w horiz of wire 2

On intersection, measure distance.
Compare and find closest
"""

#inp1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
inp1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
def load_data(filename):
    with open(filename) as inp:
        i = inp.read()
    return i

def cal_coord(wire):
    #vec = [[0, 1], [0, 0]]
    angle = {'R':0, 'U':pi/2, 'L': pi, 'D':(3*pi)/2}
    wires = [w for w in wire.split()]
    wires_c = {'h1':[], 'v1':[], 'h2':[], 'v2':[]} #sort vertical/horizontal for each wire and store i a collection
    #print(wires[0])
    for n,w in enumerate(wires):
        x0, y0 = 0, 0  #central port
        for seg in w.split(','):
            xs, ys = round(x0 + int(seg[1:])*cos(angle[seg[0]])), round(y0 + int(seg[1:])*sin(angle[seg[0]]))  #calculate end coordinates
            coord = [(x0, y0), (xs, ys)]
            if x0 == xs:        #x coord did not change, this must be a vertical line place it accordingly
                wires_c[f'v{n+1}'].append(coord)
            else:               #anything else must be a horizontal line place it accordingly
                wires_c[f'h{n+1}'].append(coord)
            x0, y0 = xs, ys     #end position will be start position for next line segment
    return wires_c

def cal_inter(wires):
    inters_dist = []
    for h in wires['h1']:       #for every horizontal line segment in wire 1
        for v in wires['v2']:   #for every vertical
            if min(h[0][0], h[1][0]) <= v[0][0] <= max(h[0][0], h[1][0]) and min(v[0][1], v[1][1]) <= h[0][1] <= max(v[0][1], v[1][1]):
                dist = abs(0 - v[0][0]) + abs(0 - h[0][1])
                #print(f'w1 intersect with w2 @ {v[0][0]}, {h[0][1]}\n at a distance from origin of {dist}')
                if dist>0:
                    inters_dist.append(dist)
    for h in wires['h2']:
        for v in wires['v1']:
            if min(h[0][0], h[1][0]) <= v[0][0] <= max(h[0][0], h[1][0]) and min(v[0][1], v[1][1]) <= h[0][1] <= max(v[0][1], v[1][1]):
                dist = abs(0 - v[0][0]) + abs(0 - h[0][1])
                if dist>0:#print(f'w1 intersect with w2 @ {v[0][0]}, {h[0][1]}\n at a distance from origin of {dist}')
                    inters_dist.append(dist)
            #print(one, two)

    return min(inters_dist)

if __name__ == '__main__':
    data = load_data('inp.txt')
    wirecollection = cal_coord(data)
    print(cal_inter(wirecollection))
