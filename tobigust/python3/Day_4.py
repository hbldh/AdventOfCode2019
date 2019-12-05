import re
"""
Input: 387638-919123
"""

def getcodes(start, stop):
    count = 0
    for a in range(start, stop+1):
        a = str(a)
        if not re.search(r'(.)\1', a): # no double, skip to next sequence
            continue
        if re.search(r'(.)\1{2,}', a):  #if three or more characters are equal
            p = re.search(r'(.)\1{2,}', a)
            b = a[:p.span()[0]] + a[p.span()[1]:]   #remove triplets (or quadruplets)
            if re.search(r'(.)\1{2,}', b) or not re.search(r'(.)\1', b):  #is there any doubles left? otherwise skip to next seq
                continue
        for n, i in enumerate(a):
            if n < len(a)-1:
                if int(i) > int(a[n+1]):
                    handbrake = True
                    break
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    getcodes(387638, 919123)