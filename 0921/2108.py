from sys import stdin
import sys
from collections import Counter

n=int(stdin.readline())
numbers=[]
for _ in range(n):
    num=int(stdin.readline())
    numbers.append(num)

numbers.sort()
total=0
for i in numbers:
    total+=i

cnt = Counter(numbers)
mode = cnt.most_common(2)
if(len(mode)==2):
    if(mode[0][1]==mode[1][1]):
        mode=mode[1]
    else:
        mode=mode[0]
else:
    mode=mode[0]
mid=int(n/2)
average=round(total/n) #산술평균
middle=numbers[mid] #중앙값
frequent=mode[0] #최빈값
scale=int(numbers[-1]-numbers[0]) #범위
print(average)
print(middle)
print(frequent)
print(scale)

