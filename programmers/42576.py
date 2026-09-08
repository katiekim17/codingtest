# 프로그래머스 - 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    answer = ''
    ppl = {}
    for person in participant:
        
        if person in ppl:
            ppl[person] += 1 # 동명이인이면 숫자가 1 추가됨     
        else:
            ppl[person] = 1 # 'leo'라는 이름표를 붙이고 숫자 1을 넣음
        
    for person in completion:
        ppl[person] -= 1
    
    for person in ppl:
        print(ppl[person])
        if ppl[person] > 0:
            answer = person
        
    return answer