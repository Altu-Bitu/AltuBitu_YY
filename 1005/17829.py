from sys import stdin
import itertools
import sys

n = int(sys.stdin.readline())
board=[]

for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    board.append(l)

k=int(n/2)
while(k>0):
    new_b=[]
    for i in range(k):
        ml=[]
        for j in range(k):
            m=[board[2*i][2*j],board[2*i+1][2*j],board[2*i][2*j+1],board[2*i+1][2*j+1]] #배열화
            m.sort()
            ml.append(m[2]) #두번째로 큰 값
            #print(m , k)
        new_b.append(ml)
    board=new_b
    k=int(k/2)


print(board[0][0])
    