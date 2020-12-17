import numpy as np
import random as rnd

def fractalize_add(array, shape):
    a = []
    for j in array:
        for i in shape:
            a.append(j+i)    
    return a

def fractalize_mult(array, shape):
    a = []
    for j in array:
        for i in shape:
            a.append(j*i)    
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
    m = max(array)
    if m < abs(min(array)):
        m = abs(min(array))
    return [a/m for a in array]

def octdown(array):
    a = []
    for x in array:
        a.append(x)
        a.append(x)
    return a

def zero_sum_factor(array):
    return -1*np.cumsum(array)

def zero_sumify(array):
    mean = np.cumsum(array)/len(array)
    return [a-mean for a in array]

def random_ones(length, onesnumber):
    a = [0]*length
    while onesnumber>0:
        i = rnd.randint(0, length)
        if a[i] == 0:
            a[i]=1
            onesnumber-=1
    return a

def scramble(array):
    a = list(array)
    for i in range(len(array)-1):
        bi = rnd.randint(i+1, len(a)-1)
        b = a[bi]
        a[bi]=a[i]
        a[i]=b
    return a