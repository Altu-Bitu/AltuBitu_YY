def solution(stones, k):
    answer=0
    left = 0
    right = max(stones)
    while(left <= right): #기저조건
        mid = int((left+right)/2)
        count=0
        mcount=0
        flag = False 
        for s in stones:
            if(s <= mid and flag == False): #최초로 나온 mid이하의 수
                count=1
                flag= True
            elif(s <= mid and flag == True): #연속되는 mid이하의 수 갯수 세기
                count+=1
            else:
                mcount = max(mcount,count) #mid 보다 큰 경우이므로 지나갈 수 있음 이전에 셌던 count값과 mcount 비교해서 max 값을 담아줌
                count=0 #앞으로 연속된 것 또 세주기 위해서 초기화
                flag=False #초기화
        mcount = max(mcount,count)
        if(mcount < k): #k번 미만 mid 이하인 연속된 수가 나옴
            left = mid + 1 #더 큰 수 탐색
        else:
            answer = mid #k번 이상 mid 이하인 연속된 수가 나옴
            right = mid -1 # 더 작은 수 탐색
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))