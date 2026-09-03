# 프로그래머스 - 시저 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    result = []
    for c in s:
        if c == " ":
            result.append(" ")
        elif c.isupper():
            result.append(chr((ord(c) - ord("A") + n) % 26 + ord("A")))
        else:
            result.append(chr((ord(c) - ord("a") + n) % 26 + ord("a")))
    return "".join(result)
