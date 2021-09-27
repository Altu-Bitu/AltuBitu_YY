from sys import stdin
import sys
'''
n=int(stdin.readline())
schedule=[] #스케줄을 담은 배열
for _ in range(n):
    t,p=map(int,stdin.readline().split())
    schedule.append((t,p))

profit=[]

for s in range(len(schedule)):
    if(len(profit)==0):
        profit.append((s+schedule[s][0]-1,schedule[s][1]))
    else:
        if(s >= profit[0][0]):
            if(s+schedule[s][0]<n):
                t,p=map(int,profit[0])
                profit[0]=((s+schedule[s][0],p+schedule[s][1]))
        else:
            if(s+schedule[s][0]<n):
                profit.append((s+schedule[s][0],schedule[s][1]))
    print(profit)
'''

import sys
readline = sys.stdin.readline

N = int(sys.stdin.readline())
T, P = [], []
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t) #기간 저장
    P.append(p) #금액 저장

d = [0] * (N+1) #최대 금액 저장

for i in range(N - 1, -1, -1): #n-1 부터 0까지 -1씩 하면서 진행 (0부터 n-1까지 거꾸로)
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않음
    if i + T[i] > N:
        d[i] = d[i+1] # 이전의 값을 대입
    else:
        # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
        d[i] = max(d[i+1], P[i] + d[i + T[i]]) #이전의 최대금액과 상담을 했을 경우의 시간에서의 최대금액 + 해당 상담 금액을 더한 값 비교하여 더 큰 값 대입

print(d[0])





