import weirdvector as wv
import reaperautoops as rpr 

def main():
    seed1 = [0.7, 0.4, 1, 0.2]
    revseed1 = seed1.copy().reverse()

    seq1 = seed1.copy()
    revseq1 = revseed1.copy()

    for i in range (5):
        seq1 = wv.fractalize_mult(seq1, seed1)
        revseq1 = wv.fractalize_mult(revseq1, revseed1)

if __name__ == "__main__":
    main()

