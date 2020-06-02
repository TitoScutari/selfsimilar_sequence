import matplotlib.pyplot as plt
import random
import wave
import struct

class Word:

    init = []
    sequence = []
    lvl = 0
    species = "none"

    def __init__(self, seq):
        self.init = seq
        self.sequence = seq

   
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
    for x in array:
        a.append(x/m)
    return a

def wav_write(array, name):
    sound = wave.open(name, 'wb')

    sound.setnchannels(1)
    sound.setsampwidth(2)
    sound.setframerate(48000)

    BinStr = bytes()
    for i in array:
        BinStr = BinStr + struct.pack('h',round(i*20000))

    sound.writeframes(BinStr)
    sound.close()


x = []
for i in range(4):
    x.append(random.random()*2)

a = Mult_Word(x)
for i in range(8):
    a.step()

print(x)

w = normalize(a.sequence)
rounded = normalize(soften(w, 4))

wav_write(w, "sharp.wav")
wav_write(rounded, "rounded.wav")


plt.plot(range(len(w)), w)
#plt.plot(range(len(rounded)), rounded)
plt.show()
