from sys import stdin
import itertools
import sys

N = int(sys.stdin.readline())
'''
schedule=[]

for i in range(1,n+1):
    t, p = map(int, sys.stdin.readline().split())
    if(i+t-1>n):
        continue
    else:
        schedule.append((i,i+t-1,p))

schedule=sorted(schedule, key=lambda x:x[1])
#print(schedule)

cost = 0 #가치
#넣은 경우와 넣지 않은 경우 중 더 큰 경우로 최댓값 설정
ans=[]
ans.append(schedule[0]) #처음 일단 대입
cost=schedule[0][2]

for s in schedule[1:]:
    if(ans[-1][1] >= s[0]): #앞의것의 종료 시작보다 빨리 시작 할때
        if(cost-ans[-1][2]+s[2] > cost): #앞의 것을 빼고 넣는 것이 더 나을때
            cost= cost-ans[-1][2]+s[2]
            ans.remove(ans[-1])
            ans.append(s)     
    else: #앞의 것 종료시작과 같거나 더 늦게 시작
        ans.append(s)
        cost+=s[2]

print(cost)

시간초과    '''

day = N
T, P = [], []
dp = [0]*(N+1)

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    T.append(temp[0])
    P.append(temp[1])


for i in range(0, N):
    if i + T[i] <= N: #n일 이전에 끝나는 경우에는
        dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i]) #dp배열의 해당 수행이 끝나는 시간에 수행한 가치, 수행하지 않았을때의 원래 가치 중 큰 값을 대입 
    dp[i+1] = max(dp[i+1], dp[i]) #dp배열의 다음 값에 이전의 값과 현재 존재하는 값을 비교하여 더 큰 것 대입(다음순서에서의 비교를 위해)

print(dp[N])



