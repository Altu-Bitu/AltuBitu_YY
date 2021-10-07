from sys import stdin
import itertools
import sys

n, c=map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

box=[]
for _ in range(m):
    a, b, d =map(int, sys.stdin.readline().split())
    box.append([a,b,d]) #박스에 대한 배열

box=sorted(box, key=lambda x:x[1]) #받는 마을 기준으로 정렬
answer=0
remain = [c] * (n + 1)  # 각 위치에 남은 공간 / 일단 전부 남은 공간으로 초기화 / 0~n번 마을까지 봐줄것이므로 n+1만큼 만들어줌

for i in range(m):
    temp = c  #최대로 초기화
    for j in range(box[i][0], box[i][1]): #보내는 마을 부터 받는 마을까지
        temp = min(temp, remain[j]) #현재 값과 초기화된 값 중 작은 값(최대로 올릴 수 있는 값)을 고름
    temp = min(temp, box[i][2]) #가장 많이 채운 (즉 가장 작은 temp값) 상태와 올릴 수 있는 박스 갯수 중 더 작은 값 골라서 temp에 저장(여유 칸 보다 박스 갯수가 작을 경우 박스 다 채우고 아닌 경우 여유 공간 만큼만 채우게됨)
    for j in range(box[i][0], box[i][1]):  #보내는 마을 부터 받는 마을까지
        remain[j] -= temp # 차에 올리는 경우 (남는 공간이 줄어듦)
    answer += temp #정답에 올렸던 박스 수 더해줌

print(answer)