from sys import stdin
import sys
from itertools import permutations
import itertools

n, m = map(int, sys.stdin.readline().split())
numbers = list(set(list(map(int, sys.stdin.readline().split()))))

answer =  list(set(list(itertools.product(numbers, repeat=m)))) #모든 경우의 수 repeat=m -> m번 중복 허용
answer.sort()
for a in answer:
    s=''
    for b in a:
        s=s+str(b)+' '
    print(s)
