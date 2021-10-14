from sys import stdin
import itertools
import sys
from itertools import combinations

n, m=map(int, sys.stdin.readline().split())
classes = list(map(int, sys.stdin.readline().split()))
'''
com=list(combinations(classes, m-1))
group=[]
for c in com:
    temp=0
    if(classes[0:c[0]]==[] or classes[c[-1]:]==[]):
        continue
    else:
        temp=sum(classes[0:c[0]])
        for i in range(m-2):
            if(temp < sum(classes[c[i]:c[i+1]])):
                temp = sum(classes[c[i]:c[i+1]])
        if(temp < sum(classes[c[-1]:])):
            temp = sum(classes[c[-1]:])
        group.append(temp)
print(min(group))
#메모리초과
''' 
left=max(classes) #최소 블루레이 크기
right=sum(classes) #최대 블루레이 크기
while (left<=right): #이분탐색 기저조건
    mid=int((left+right)/2)
    limit = 0 #블루레이 크기
    div = 1 #블루레이 갯수
    for i in range(n):
        limit+= classes[i]
        if limit > mid: #블루레이 누적 값이 블루레이 크기보다 크다면 
            div+=1 #블루레이 갯수를 하나 늘리고
            limit = classes[i] #새로운 블루레이에 해당 값을 넣어줌 
    if div <= m:
        answer = mid #블루레이 갯수가 요구된 갯수 이하라면 정답에 현재 크기 대입
        right = mid-1
    else:
        left = mid+1 #블루레이 갯수가 요구된 갯수보다 많으면 블루레이의 크기를 늘림 
print(answer)
#출처 https://icymingu.tistory.com/6