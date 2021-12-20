import random
import wave
import struct

# this one is probably useless

class Word:

    init = []
    sequence = []
    lvl = 0

    def __init__(self, seq):
        self.init = seq
        self.sequence = seq

#set_level(int) should be much better than step 
class Add_Word(Word):

    def step(self):

        self.lvl += 1
        seq = []

        for j in self.sequence:
            for i in self.init:
                seq.append(j+i)
        
        self.sequence = seq

class Mult_Word(Word):

     def step(self):

        self.lvl += 1
        seq = []

        for j in self.sequence:
            for i in self.init:
                seq.append(j*i)
        
        self.sequence = seq

def summation(array):
    a = []
    for i in range(len(array)):
        a.append(sum(array[:i]))
    return a
# some kind of inverse of summation is probably a good idea, like a highpass filter

def soften(array, amount):
    a = []
    amount = amount*2
    for i in range(len(array)):
        start = i - int(amount/2)
        end = i + int(amount/2)
        if start < 0:
            start = 0
        if end > len(array)-1:
            end = len(array)-1
        a.append(sum(array[start:end])/amount)
    return a

def normalize(array):
    a = []
    m = max(array)
    if m < abs(min(array)):
        m = abs(min(array))
    for x in array:
        a.append(x/m)
    return a

def octdown(array):
    a = []
    for x in array:
        a.append(x)
        a.append(x)
    return a

def zero_sum_factor(array):
    return -1*sum(array)

def automation_write(filename, length, array, type):
    filename += ".ReaperAutoItem"
    f = open(filename, "w")
    f.write("SRCLEN "+ str(length*2) + "\n")

    space = round(2*length/len(array), 5)
    i = 0
    for x in array:
        f.write("PPT "+ str(i) + " "+ str(x)+" " +str(type)+" 0\n")
        i+= space
    
    f.close()

def scramble(array):
    a = list(array)
    for i in range(len(array)-1):
        bi = random.randint(i+1, len(a)-1)
        b = a[bi]
        a[bi]=a[i]
        a[i]=b
    return a


def wav_write(array, name):
    sound = wave.open(name, 'w')

    sound.setnchannels(1)
    sound.setsampwidth(2)
    sound.setframerate(48000)

    arr = []
    for x in array:
        arr.append(int(round(x*32000)))

    BinStr = struct.pack( str(len(array))+'h', *arr)

    sound.writeframes(BinStr)
    sound.close()