from sys import stdin
import heapq
import sys

n = int(sys.stdin.readline())
total=[]
for _ in range(n):
    s, t = map(int, stdin.readline().split())
    total.append([s,t])

total.sort() #시작시간 기준 정렬
room=[]
heapq.heappush(room,total[0][1]) #첫 종료 시간 힙에 삽입
for i in range(1,len(total)): #전체 리스트에 대해서 
    if total[i][0] < room[0]: #종료시간보다 먼저 시작하는 수업의 겨우
        heapq.heappush(room, total[i][1]) #종료 보다 먼저 시작하는 수업의 종료시간을 힙에 삽입
    else: #종료시간 이후에 시작하는 수업
        heapq.heappop(room) #현재 들어가 있던 종료 시간을 빼고
        heapq.heappush(room, total[i][1]) # 지금 수업의 종료 시간을 새로 삽입

print(len(room))