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
