from sys import stdin
import sys
from itertools import combinations
'''
n=int(stdin.readline())
answers=list(map(str, stdin.readline().split()))
submit=list(map(str, stdin.readline().split()))
index=[]

for i in range(n):
    index.append(i)

com=list(combinations(index, 2))
score=0

for c in com:
    if(answers.index(submit[c[0]]) <answers.index(submit[c[1]])):
        score+=1

print(score,'/',len(com))
#시간 초과
'''

n = int(stdin.readline())
ans = stdin.readline().split() #정답
d = {} #각 해전의 상대적인 순서 딕셔너리
for i in range(n):
    d[ans[i]] = i #해당 정답 = key , 인덱스 = value
inp = input().split() #입력값
score = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if d[inp[i]] < d[inp[j]]: #지금 입력된 값의 딕셔너리 value를 통해서 올바른 순서인지 비교
            score += 1
print(f"{score}/{n * (n - 1) // 2}")
