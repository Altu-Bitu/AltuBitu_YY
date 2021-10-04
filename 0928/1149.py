from sys import stdin
import itertools
import sys

n = int(sys.stdin.readline())

cost=[]
for i in range(1,n+1):
    r, g, b = map(int, sys.stdin.readline().split())
    cost.append([r,g,b])

for i in range(1,n): # 이전의 값에서 같은 색이 아닌 값 중 작은 값과 현재 색의 가치를 더한 값으로 대입 
    cost[i][0]=cost[i][0]+min(cost[i-1][1],cost[i-1][2])
    cost[i][1]=cost[i][1]+min(cost[i-1][0],cost[i-1][2])
    cost[i][2]=cost[i][2]+min(cost[i-1][0],cost[i-1][1]) 

print(min(cost[n-1]))