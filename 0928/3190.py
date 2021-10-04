from sys import stdin
import itertools
import sys

dx = [0,1,0,-1] #상 우 하 좌 시계방향으로 돌아가는 좌표
dy = [1,0,-1,0]

def change(d, c):
    if(c == "L"):
        d = (d-1)%4 #왼쪽으로 90도 회전하면 상은 좌가 되고 우는 상이 되고 하는 좌가 됨
    else:
        d = (d+1)%4 #오른쪽으로 90도 회전하면 상은 우가 되고 우는 하가 되고 좌는 상이 됨 
    return d
        
def start():
    cnt = 0
    # 뱀 위치 표시
    x = 0
    y = 0
    arr[x][y] = 3
    d = 0 #맨 위 맨 좌측에서 시작하므로 처음에 오른쪽을 향한다는 것은 일반 좌표에서 상 방향으로 향한다는 의미
    idx = 0
    # 뱀의 꼬리 ~ 머리까지의 정보를 q에 담기
    q = []
    q.append((x,y))
    while(True):
        # 몇초에 방향 전환 하는지
        if(game[idx][0] == cnt): #방향전환하는 시간일때
            d = change(d, game[idx][1]) #방향 전환
            idx += 1 #다음 game을 봐주기 위해 idx+1
        nx = x + dx[d] #다음칸 좌표
        ny = y + dy[d]
        # 범위안에 있고, 자기자신이 아니라면
        if(0<=nx<n and 0<=ny<n and arr[nx][ny] != 3):
            # 사과를 먹으면 꼬리는 그대로
            if(arr[nx][ny] == 1): #사과가 있을 때
                arr[nx][ny] = 3 #지나갔음을 표시
                q.append((nx,ny))
            # 사과를 못먹으면 꼬리 하나 떼기
            elif(arr[nx][ny] == 0):
                arr[nx][ny] = 3 #현재 위치
                q.append((nx,ny)) #일단 추가
                tx, ty = q.pop(0) #0번 인덱스 위치의 좌표 떼어줌
                arr[tx][ty] = 0 #뺀 자리 0으로 지나갔으니까
            x = nx #현재 위치 x,y에 저장
            y = ny
            cnt += 1
        else:
            cnt += 1 #범위 안에 없을때 -> 벽에 부딪힌 것이므로 종료
            break
    return cnt

n= int(sys.stdin.readline())
k= int(sys.stdin.readline())
arr = [[0]*n for _ in range(n)] #0으로 초기화
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = 1 # 사과 좌표 저장
l = int(input())
game = [[0,0]]*10000 #초기환
for i in range(l):
    x, c = input().split()
    game[i] = [int(x), c] #방향전환 정보
res = start() #게임 시작
print(res)
