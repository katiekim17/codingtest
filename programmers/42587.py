# 프로그래머스 - 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    answer = 0   # 몇 번째로 인쇄되는지 세어줄 변수
    # 다시 집어 넣어야 하니까, for는 쓸 수 없고, while을 써야 함
    # 다시 집어 넣었을 때 위치를 알아야 하니까. 우선순위와 처음위치를 묶어서 저장해야함
    queue = []
    for i in range(len(priorities)):
        queue.append([priorities[i], i])

    while len(queue) > 0:
        # 1. 대기열 맨 앞(0번)에서 문서를 하나 꺼냅니다.
        current = queue.pop(0) 
        has_higher = False  # 나보다 우선순위가 높은 문서가 있는지 체크하는 깃발
    
        for doc in queue:
            # doc[0]은 대기열에 남은 문서의 우선순위, current[0]은 방금 꺼낸 문서의 우선순위
            if doc[0] > current[0]:
                has_higher = True  # 나보다 센 놈을 발견했다!
                break              # 하나라도 찾았으면 더 볼 필요 없으니 중단!
                    
        if has_higher:
            queue.append(current)  # 뒤로 밀려남
        else:
            answer += 1  # 인쇄 성공!
            if current[1] == location:  # 내가 찾던 문서라면?
                return answer  # 정답 반환    
    
    return answer