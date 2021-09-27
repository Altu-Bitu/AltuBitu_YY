from sys import stdin
import sys

N,K = map(int,stdin.readline().split()) #입력 받은 n,k
ngs = list(map(int, stdin.readline().split())) #내구성

robot=[0]*N #일단 다 0을 넣은 로봇의 위치 배열
step=0 #몇단계인지

while(ngs.count(0)<K): #내구성이 0인 것이 k개보다 작게있는 동안 수행
    step+=1 #한번 수행할때마다 내구성 +1
    
    a=ngs.pop() #내구성 내부의 가장 오른쪽 값 pop
    ngs.insert(0,a)  #0번째자리에 a 삽입 - 한칸 회전

    robot.pop() #로봇 내의 제일 오른쪽 값 pop
    robot.insert(0,0) #로봇 0번째 자리에 0 삽입 -한칸 회전

    robot[N - 1] = 0 #N-1번째는 내려주는 위치

    for i in range(N-2,0,-1):
        if robot[i] and ngs[i+1] and (not robot[i+1]): #다음칸이 비어있으면서 내구성 값이 0이 아니고 해당 위치 로봇값이 1일때
            robot[i]=0 # 현재 위치는 0 없는 것으로
            robot[i+1]=1 #다음 위치는 1 있는 것으로 표시
            ngs[i+1] = max(0,ngs[i+1]-1) #내구성을 -1해줌 (-1한 것이 0보다 작을때는 그냥 0 표시)

    robot[N - 1] = 0  #N-1번째는 내려주는 위치 즉시 내려줌
    if ngs[0] and (not robot[0]): #내구성의 첫번째 값이 0이 아니면서 첫번째 자리에 로봇이 없을때
        robot[0]=1 #로봇을 올려줌
        ngs[0] = max(0,ngs[0]-1) #내구성을 -1해줌 

print(step)