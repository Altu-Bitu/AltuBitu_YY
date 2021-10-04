from sys import stdin
import itertools
from collections import deque

n,m=map(int,input().split())
start=[deque(), deque()]
temp=[deque(),deque()]

for i in range(n):
    a,b=map(int,input().split())
    start[0].appendleft(a)
    start[1].appendleft(b)

t=0
for _ in range(m):
    temp[t].appendleft(start[t].popleft()) #가장 위에 있는 카드 뽑음
    if not start[t]:#둘 중 하나라도 카드 덱이 0이 되면 종료 상대방 승리
        break
    win=-1 # 초기화
    for i in [0,1]:
        if temp[i] and temp[i][0]==5: # 둘중 하나가 5
            win=0 #도도가 이김 
    if temp[0] and temp[1] and temp[0][0]+temp[1][0]==5: #두 카드의 합이 5
            win=1 #수연이가 이김 
    if win!=-1:#종 치는 경우 
        for i in [1-win,win]: #누구 카드를 먼저 가져오는지 - 상대방의 그라운드 먼저
            while temp[i]: #현재 그라운드
                start[win].append(temp[i].pop()) #이긴사람의 덱에 temp 전부 합침 pop으로 오른쪽부터 뽑아줌
    t=1-t #도도와 수연이 번갈아서 카드를 뽑음

if len(start[0])>len(start[1]):
    print('do')
elif len(start[1])>len(start[0]):
    print('su')
else:
    print('dosu')



