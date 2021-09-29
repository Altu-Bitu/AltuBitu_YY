from sys import stdin
import itertools
import sys
 
 
def squre(x, y):
    return (x//3)*3 + y//3 #몇번째 스퀘어인지 출력

def dfs(n): #좌표의 값을 1개로만 받아서 9로 나누어 x와 y값을 구함
    if n == 81: #모든 칸이 완성 되면 출력
        for i in B:
            print(' '.join(map(str, i)))
        return True
    x = n // 9 #9로 나눈 몫 -> x좌표
    y = n % 9 #나머지 -> y좌표
    if B[x][y] != 0:
        return dfs(n+1) #0이 아니면 그냥 다음 칸 실행 
    else: #0인경우
        for i in range(1, 10):
            if c1[x][i] == False and c2[y][i] == False and c3[squre(x, y)][i] == False: # 전부 false인 경우 
                c1[x][i] = c2[y][i] = c3[squre(x, y)][i] = True #다 true로 바꿔주고 값 대입
                B[x][y] = i #해당하는 값 대입
                if dfs(n+1): #다음 칸이 True를 리턴하면 ->마지막이면
                    return True  #종료
                B[x][y] = 0 #다음 칸이 False를 리턴하면 다음에 다시 고려할 수 있게끔 다시 0으로 변경
                c1[x][i] = c2[y][i] = c3[squre(x, y)][i] = False #다시 고려할 수 있게 false로 세팅
    return False

B = [list(map(int, input().split())) for _ in range(9)] #입력값
c1 = [[False]*10 for _ in range(9)] #가로에 1-9까지 숫자가 있는지 없는지 체크 
c2 = [[False]*10 for _ in range(9)] #세로에 1-9까지 숫자가 있는지 없는지 체크 
c3 = [[False]*10 for _ in range(9)] # n번째 3*3 사각형 안에 1-9까지 숫자가 있는지 없는지 체크 
for i in range(9):
    for j in range(9):
        if B[i][j] != 0:
            c1[i][B[i][j]] = True #있는 것들 True로 값 변경
            c2[j][B[i][j]] = True #있는 것들 True로 값 변경
            c3[squre(i, j)][B[i][j]] = True #있는 것들 True로 값 변경
dfs(0)
            











