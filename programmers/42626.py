# 프로그래머스 - 더맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

# 처음에 for을 생각했으나, 꺼내서 확인하고 다시 넣는 건데 길이가 바뀌므로 while로 바꿈. pop, push를 써야하나 했는데, push는 없었고. append를 써야 했었음. 
# 실제적으로 실행했지만, 효율성에서 떨어졌음. heapq라는 것을 알게 되었음. 
# 가장 작은 수부터 넣어야 하므로 sort가 필요하다는 것도 인지하게 되었음

import heapq

def solution(scoville, K):
    answer = 0    
    heapq.heapify(scoville)
    while scoville[0] < K:
        
        if len(scoville) < 2:
            answer = -1
            break
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        sco = first + (second *2)
        
        heapq.heappush(scoville, sco)
    
        answer += 1

    return answer