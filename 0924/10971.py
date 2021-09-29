from sys import stdin
import sys
from itertools import permutations
import itertools
n = int(stdin.readline())
cost=[]
num=[]
for i in range(n):
    cost1 = list(map(int, sys.stdin.readline().split()))
    cost.append(cost1)
    num.append(i)

answer = list(itertools.permutations(num, n)) #모든 경우의 수
min_cost=1000000*n #최댓값 설정

for a in answer:
    now = 0
    for i in range(n):
        if(i==(n-1)): #마지막인 경우
            if(cost[a[i]][a[0]]!=0 and now + cost[a[i]][a[0]] <min_cost): #최솟값인 경우
                min_cost=now + cost[a[i]][a[0]]
                #print(a)
        else:
            if(cost[a[i]][a[i+1]]==0): #길이 없는 경우
                break
            if( now + cost[a[i]][a[i+1]] > min_cost): #이미 최솟값이 아닌 경우
                break
            now = now + cost[a[i]][a[i+1]]

print(min_cost)







