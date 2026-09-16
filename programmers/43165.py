# 프로그래머스 - 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    # 0에서 시작합니다.
    leaves = [0]
    
    for num in numbers:
        temp = []
        for leaf in leaves:
            # 기존 값에 현재 숫자를 더한 것과 뺀 것을 모두 추가합니다.
            temp.append(leaf + num)
            temp.append(leaf - num)
        # 다음 단계를 위해 업데이트합니다.
        leaves = temp
        
    # 최종 결과물 중에서 target의 개수를 세어서 반환합니다.
    return leaves.count(target)
