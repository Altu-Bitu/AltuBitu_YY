from sys import stdin
import heapq
#heapq 는 기본적으로 최소힙

n, m = map(int, stdin.readline().split()) #첫줄 입력 카드 n개로 m번 수행

# heap 생성
c = []
card_list = [int(x) for x in stdin.readline().split()] #둘째 줄 입력

for card in card_list: #모든카드에 대해서
    heapq.heappush(c, card) #힙에 삽입

for _ in range(m): #m번 수행
    card1 = heapq.heappop(c) 
    card2 = heapq.heappop(c) #가장 작은 두개를 pop해서 꺼냄

    heapq.heappush(c, card1 + card2) #둘을 더한 값을 2번 삽입
    heapq.heappush(c, card1 + card2)

print(sum(c)) # 모든 원소를 더한 결과