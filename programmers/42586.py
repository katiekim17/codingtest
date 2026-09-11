# 프로그래머스 - 기능 개발

# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 왜 이렇게 되나요? 
#(원리 이해하기)파이썬의 // 연산자는 소수점을 버리는 내림(Floor) 연산자입니다. 이를 반대로 올림으로 바꾸기 위해, 나누기 전에 (나누는 수 - 1)을 분자에 더해주는 수학적 트릭을 사용하는 것입니다. 예를 들어 남은 진도가 70이고 속도가 30일 때 (70 / 30 = 2.33...이므로 올림 하면 3이 되어야 함):
# 1. 단순 // 사용 시: 70 // 30 ➔ 2 (버림이 되어 배포일이 부족해짐 ❌)
# 2. 올림 공식 적용 시: (70 + 30 - 1) // 30 ➔ 99 // 30 ➔ 3 (정확히 올림 성공! ⭕)
# 만약 딱 떨어지는 수라면(남은 진도 60, 속도 30):(60 + 30 - 1) // 30 ➔ 89 // 30 ➔ 2 (나머지가 있어도 기존 몫을 넘지 않아 딱 떨어짐 ⭕)


def solution(progresses, speeds):
    answer = []
    count = 0
    days = []
    for i in range(len(progresses)):
        day = (100 - progresses[i] + speeds[i] -1)//speeds[i]
        days.append(day)
        print(day)
    
     # 1. 첫 번째 작업이 끝나는 날을 '기준일'로 잡습니다.
    target_day = days[0]
    count = 1  # 첫 번째 작업은 무조건 포함되므로 1부터 시작합니다.
    
     # 2. 두 번째 작업(인덱스 1)부터 마지막 작업까지 순서대로 확인합니다.
    for j in range(1, len(days)):
        if days[j] <= target_day:
            count += 1
            
        else:
            answer.append(count)  # 지금까지 모인 기능들을 배포!
            target_day = days[j]  # 새로운 작업일을 기준일로 변경!
            count = 1             # 새로운 팀의 카운트를 1부터 다시 시작! 
        
        
    answer.append(count) 
                
    
    return answer