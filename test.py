import weirdvector as wv
from svgpathtools import Path, Line, wsvg, disvg

s = [0, 0.5, 0.8, 0.3, 1]
s = wv.fractalize_mult(s,s)
s = wv.fractalize_mult(s,s)

path = [Line(100+100j, 200+200j)]
for i in range(len(s)):
    path.push(Line(i*100+s[i]*2000j, (i+1)*100+s[i]*2000j)

disvg(path, filename="svgtest.svg")