"""
25 pixels wide and 6 pixels tall
"""
from collections import Counter

def load8_1(filename):
    with open(filename) as f:
        rawimg = str(f.read())
        return rawimg

def imgdecode(pixels, width, height):
    layers = {}
    row = []
    start = 0
    for h in range(int(len(pixels)/width)):
        row.append(pixels[start:start+width])
        start += width
    start = 0
    for j in range(int(len(row)/height)):
        layers[j] = row[start:start+height]
        start += height
    return layers

def imgrender(image):
    # 0=black, 1=white, 2=transp
    rendered = [list(p) for p in image[0]]
    for nl, layer in enumerate(image.items()):
        for nr, row in enumerate(layer[1]):
            for np, pix in enumerate(row):
                if rendered[nr][np] == '2':
                    rendered[nr][np] = pix
    for i in rendered:
        for j in i:
            if j == '0':
                print(' ', end='')
            else:
                print('M', end='')
        print()


def find_code(image):
    maxz = 999
    code = 0
    for layer in image.items():
        c = Counter(''.join(layer[1]))
        if c['0'] < maxz:
            maxz = c['0']
            code = c['1'] * c['2']
    return code

if __name__ == "__main__":
    r = load8_1('inp_d8.txt')
    img = imgdecode(r, 25, 6)
    imgrender(img)