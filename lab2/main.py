import math

class LinearGenerator:
    def __init__(self, a, c, m):
        self.a=a
        self.c=c
        self.m=m
        self.state = 15

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state % self.m

    def sequence(self, N):
        return [self.next() for _ in range(N)]




def shift_register_generator(seed, negated_bits):
    register = seed.copy()
    output = []

    for _ in range(100):
        feedback = 0
        for bit in negated_bits:
            feedback ^= register[bit]
        output.append(register[-1])


        for i in range(len(register) - 1, 0, -1):
            register[i] = register[i - 1]


        register[0] = feedback

    return output[-31:]





def number_classification(data, M):
    classific = {'0':0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for numb in data:
        res = (numb*10)//M
        if res == 0:
            classific['0'] = classific['0']+1
        elif res == 1:
            classific['1'] = classific['1']+1
        elif res == 2:
            classific['2'] = classific['2']+1
        elif res == 3:
            classific['3'] = classific['3']+1
        elif res == 4:
            classific['4'] = classific['4']+1
        elif res == 5:
            classific['5'] = classific['5']+1
        elif res == 6:
            classific['6'] = classific['6']+1
        elif res == 7:
            classific['7'] = classific['7']+1
        elif res == 8:
            classific['8'] = classific['8']+1
        elif res == 9:
            classific['9'] = classific['9']+1

    return classific


def binary_to_decimal(bits):
    binary_string = ''.join(map(str, bits))  # Konwersja listy zer i jedynek na string
    decimal = int(binary_string, 2)  # Konwersja stringa binarnego na liczbę dziesiętną
    return decimal


if __name__ == "__main__":

    a, c, m = 69069, 1, 2**31
    generator = LinearGenerator(a, c, m)
    N=100000
    data = generator.sequence(N)

    classific = number_classification(data, m)

    print(classific)


    #2
    seed = [1,0,0,1,1,0,1]
    taps = [6,2] # Pozycje, z których bierzemy bity do XOR (licząc od 0)


    N = 100000
    data2 =[]
    numb = 0
    for _ in range(100000):

        bits = shift_register_generator(seed, taps)

        numb = binary_to_decimal(bits)


        data2.append(numb)
        seed = bits[-7:]

    classific = number_classification(data2, m)

    print(classific)




