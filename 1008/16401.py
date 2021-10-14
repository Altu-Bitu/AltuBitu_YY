from sys import stdin
import itertools
import sys

m, n=map(int, sys.stdin.readline().split())
snack=list(map(int, sys.stdin.readline().split()))

left = 1 #최소 크기
right = max(snack) #최대 크기
answer= 0 #다 나눠줄 수 없는 경우
while(left <= right): #이분탐색 기저조건
    mid=int((left + right)/2)
    count = 0
    for s in snack:
        if(s < mid):
            continue
        else:
            count+=int(s/mid)
    if(count >= m): #다 나눠줄 수 있는 경우 더 큰 수 탐색
        answer = mid
        left = mid + 1
    else:
        right = mid -1
print(answer)



