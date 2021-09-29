from sys import stdin
import itertools
import sys
from itertools import combinations
from itertools import product

l, c = map(int, sys.stdin.readline().split())
alphabets = list(map(str, sys.stdin.readline().split()))

vowel=[]
consonant=[]
for a in alphabets:
    if a in ['a','e','i','o','u']:
        vowel.append(a)
    else:
        consonant.append(a)

pos=l-3
num=[]
if pos==0:
    num=[(0,0)]
else:
    for i in range(pos+1):
        num.append((i,pos-i))
can=[]
for n in num:
    vow=list(combinations(vowel,n[0]+1))
    con=list(combinations(consonant,n[1]+2))
    for v in vow:
        for c in con:
            tmp=list(c+v)
            tmp.sort()
            can.append(tmp)
can.sort()
for c in can:
    s=''
    for c1 in c:
        s+=c1
    print(s)

