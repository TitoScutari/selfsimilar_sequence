from word import *

def main():
    x = []
    for i in range(3): #increasing this can slow down everything by a lot
        x.append(random.random()*2-1)

    x.insert(round(len(x)/2), zero_sum_factor(x))
    x = normalize(x)

    a = Mult_Word(x)
    for i in range(11): #increasing this can slow down everything by a lot
        a.step()

    print(x)

    w = normalize(a.sequence)

    #plt.plot(range(len(w)), w)
    #plt.show()

    wav_write(normalize(soften(w, 4)), "sound.wav")

if __name__ == "__main__":
    main()