from sys import stdin
import sys

n=int(stdin.readline())

numbers=[]
for _ in range(n):
    num=int(stdin.readline())
    numbers.append(num)

flag=[]
for i in numbers:
    tmp=[]
    j=1
    while(j*(j+1)/2<=i):
        tmp.append(j*(j+1)/2) #i까지의 삼각수를 모두 저장
        j+=1
    f=0
    for t in tmp:
        for t2 in tmp:
            for t3 in tmp:
                if(t+t2+t3==i): #세개의 삼각수로 표현 가능한 경우
                    f=1
    flag.append(f)
for f in flag:
    print(f)
            