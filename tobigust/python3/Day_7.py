from itertools import permutations

maxamp = 0
maxphase = 0

def gen_perm(seq):
    for p in permutations(seq):
        yield ''.join(p)

def load_8_1(progfile):
        with open(progfile) as pf:
            program = [int(p) for p in pf.read().split(',')]
        return program

class amplifier():
    def __init__(self, phase, inpsig, name='ampN'):
        self.running = True
        self.params = []
        self.params.append(inpsig)
        if 0 <= phase <= 4:
            self.params.append(phase)
            self.phase = phase
        self.inpsig = inpsig
        self.program = []
        self.name = name

    def amp_input(self, insignal):
        self.params.append(insignal)

    def calculate(self, program):
        data = program
        opcode = 00
        adrpntr = 0
        while opcode != '99':
            opcode = str(data[adrpntr]).rjust(5, '0')
            if opcode[-2:] == '01':
                #add
                if opcode[2] == '0':
                    verb = data[data[adrpntr+1]]
                else:
                    verb = data[adrpntr+1]

                if opcode[1] == '0':
                    noun = data[data[adrpntr+2]]
                else:
                    noun = data[adrpntr+2]
                data[data[adrpntr+3]] = verb + noun
                adrpntr += 4
            elif opcode[-2:] == '02':
                #multiply
                if opcode[2] == '0':
                    verb = data[data[adrpntr+1]]
                else:
                    verb = data[adrpntr+1]

                if opcode[1] == '0':
                    noun = data[data[adrpntr+2]]
                else:
                    noun = data[adrpntr+2]
                data[data[adrpntr+3]] = verb * noun
                adrpntr += 4
            elif opcode[-2:] == '03':
                #store
                if len(self.params) > 0:
                    storeval = self.params.pop()
                sp = data[adrpntr+1]
                data[sp] = storeval
                adrpntr += 2
            elif opcode[-2:] == '04':
                #get
                if opcode[2] == '0':
                    response = data[data[adrpntr+1]]
                else:
                    response = data[adrpntr+1]
                adrpntr += 2
                return response

            elif opcode[-2:] == '05':
                #jump if true
                if opcode[2] == '0':
                    verb = data[data[adrpntr+1]]
                else:
                    verb = data[adrpntr+1]

                if opcode[1] == '0':
                    noun = data[data[adrpntr+2]]
                else:
                    noun = data[adrpntr+2]
                if int(verb) != 0:
                    adrpntr = noun
                else:
                    adrpntr += 3

            elif opcode[-2:] == '06':
                # jump if false
                if opcode[2] == '0':
                    verb = data[data[adrpntr+1]]
                else:
                    verb = data[adrpntr+1]

                if opcode[1] == '0':
                    noun = data[data[adrpntr+2]]
                else:
                    noun = data[adrpntr+2]
                if int(verb) == 0:
                    adrpntr = noun
                else:
                    adrpntr += 3

            elif opcode[-2:] == '07':
                #LessThan (3 params)
                if opcode[2] == '0':
                    verb = data[data[adrpntr+1]]
                else:
                    verb = data[adrpntr+1]

                if opcode[1] == '0':
                    noun = data[data[adrpntr+2]]
                else:
                    noun = data[adrpntr+2]
                
                if int(verb) < int(noun):
                    data[data[adrpntr+3]] = 1
                else:
                    data[data[adrpntr+3]] = 0
                adrpntr += 4

            elif opcode[-2:] == '08':
                #Equals (3 params)
                if opcode[2] == '0':
                    verb = data[data[adrpntr+1]]
                else:
                    verb = data[adrpntr+1]

                if opcode[1] == '0':
                    noun = data[data[adrpntr+2]]
                else:
                    noun = data[adrpntr+2]
                
                if int(verb) == int(noun):
                    data[data[adrpntr+3]] = 1
                else:
                    data[data[adrpntr+3]] = 0
                adrpntr += 4

            else:
                #Unknown opcode
                break


if __name__ == '__main__':
    prog = load_8_1('inp_d7.txt')
    insig = 0
    for r in gen_perm('01234'):
        for n, p in enumerate(r):
            program = prog.copy()
            amp = amplifier(int(p), insig, 'A' + str(n))
            o = amp.calculate(program)
            if amp.name == 'A4':
                if o > maxamp:
                    maxamp = o
                    maxphase = r
                insig = 0
                break
            if o == None:
                insig = 0
                break
            insig = o
    print(f'Maxphase: {maxamp}, @ phase seq {maxphase}')