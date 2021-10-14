from sys import stdin
import itertools
import sys

n, m=map(int, sys.stdin.readline().split())


fight=[]
for i in range(n):
    f = list(map(str, sys.stdin.readline().split()))
    fight.append(f)

character=[]

for i in range(m):
    c = int(sys.stdin.readline())
    left= 0
    right= n-1
    while(left <= right):
        mid=int((left+right)/2)
        #print(c , int(fight[mid][1]))
        if(c > int(fight[mid][1])):
            left=mid+1
        else:
            right=mid-1
    print(fight[left][0])


'''
for c in character:
    left= 0
    right= n-1
    while(left <= right):
        mid=int((left+right)/2)
        #print(c , int(fight[mid][1]))
        if(c > int(fight[mid][1])):
            left=mid+1
        else:
            right=mid-1
    print(fight[left][0])
'''