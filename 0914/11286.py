import sys
m = int(sys.stdin.readline())
S = set() #중복을 제거하고 검색을 하기위해 set 사용 

for _ in range(m):
    temp = sys.stdin.readline().strip().split() #시간복잡도를 줄이기 위해 사용
    
    if len(temp) == 1:
        if temp[0] == "all": #all인 경우
            S = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        else:
            S = set() #empty인 경우  빈 set으로 정의
    
    else:
        func, x = temp[0], temp[1]
        x = int(x)
        if func == "add":
            S.add(x) #set S에 추가 - set이 알아서 중복 없게 처리해주므로 확인할 필요 X
        elif func == "remove":
            S.discard(x) #set S에서 삭제
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)