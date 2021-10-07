from sys import stdin
import itertools
import sys

n = int(sys.stdin.readline())

triangle = []

num=[]
for i in range(n):
    i = int(sys.stdin.readline())
    num.append(i)

result=-1
num.sort(reverse=True)
if(num[0]<num[1]+num[2]):
    result=num[0]+num[1]+num[2] #바로 만들어지는 경우
else:
    for t in range(1,len(num)-2):
        if(num[t]<num[t+1]+num[t+2]):
            result=num[t]+num[t+1]+num[t+2]
            break

print(result)








