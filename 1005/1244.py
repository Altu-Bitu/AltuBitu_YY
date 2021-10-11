from sys import stdin
import itertools
import sys

s = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
p = int(sys.stdin.readline())

people=[]
for i in range(p):
    fm, n = map(int, sys.stdin.readline().split())
    people.append((fm, n))

for j in people:
    if(j[0]==1):
        now=j[1]

        while(now <= s):
            if(switch[now-1]==1):
                switch[now-1]=0
            else:
                switch[now-1]=1
            now=now+j[1] #배수 확인을 위해 더해줌
    else:
        now=j[1]
        if(switch[now-1]==1): #일단 본인 바꿔줌
                switch[now-1]=0
        else:
            switch[now-1]=1
        same=1
        i=1
        while(same==1):
            if(((now-1-i) >=0 and (now-1+i) < s) and (switch[now-1-i]==switch[now-1+i])): #범위 안에 있는 양옆 한 쌍씩 홛인
                if(switch[now-1-i]==1):
                    switch[now-1-i]=switch[now-1+i]=0
                    i+=1
                elif(switch[now-1-i]==0):
                    switch[now-1-i]=switch[now-1+i]=1
                    i+=1
            else:
                same=0
state=''
'''
switch=str(switch).replace('[', '').replace(']', '').replace(',', '')
for ss in range(len(switch)):
    if(ss%20==19 or ss==len(switch)-1):
        state+=switch[ss]
        print(state)
        state=''
    else:
        state+=switch[ss]+' '
'''
for ss in range(len(switch)):
    if(ss%20==19 or ss==len(switch)-1):
        state+=str(switch[ss])
        print(state)
        state=''
    else:
        state+=str(switch[ss])+' '

