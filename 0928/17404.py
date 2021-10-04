from sys import stdin
import itertools
import sys

n = int(sys.stdin.readline())

cost=[]
for i in range(1,n+1):
    r, g, b = map(int, sys.stdin.readline().split())
    cost.append([r,g,b])


result = float('inf')

# 첫 번째 색깔에 따라 각 비용을 계산한다.
for idx in range(3):
	#dp행렬을 3 * n으로 구성
    dp = [[0] * n for _ in range(3)]
    for i in range(3): #i는 색의 번호를 의미
        if i == idx:
            dp[i][0] = cost[0][i] #색과 순서가 cost와 반대로 매칭된 dp
            continue
        dp[i][0] = result #무한대 대입시켜놓음
	
    # 비용 계산
    for i in range(1, n):
        dp[0][i] = cost[i][0] + min(dp[1][i - 1], dp[2][i - 1])
        dp[1][i] = cost[i][1] + min(dp[0][i - 1], dp[2][i - 1])
        dp[2][i] = cost[i][2] + min(dp[0][i - 1], dp[1][i - 1])
	
    # 마지막 색과 첫 번째 고른 색이 같은 경우를 제외하고 최솟값을 갱신한다.
    for i in range(3):
        if i == idx: #i는 색의 번호를 의미 같은색일때는 제외 시켜야함
            continue
        result = min(result, dp[i][-1]) #같은 색이 아닌경우 result와 현재 값을 비교하여 최솟값 구함
print(result)