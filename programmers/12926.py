# 프로그래머스 - 시저 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/12926

import string
def solution(s, n):
    answer = ''
    lower = string.ascii_lowercase + string.ascii_lowercase
    upper = string.ascii_uppercase + string.ascii_uppercase
    
    for char in s: # 한 글자씩 검사하기
        if char == ' ':
            answer += ' '
        elif char.isupper():
            start_idx = upper.index(char)
            answer += upper[start_idx + n]
        elif char.islower():
            start_idx = lower.index(char)
            answer += lower[start_idx + n]

    return answer
