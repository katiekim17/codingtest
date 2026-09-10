# 프로그래머스 - 짝지어 제거하기

# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 스택 문제였는 데, 스택을 쓰지 못했고, 처음에 인덱스를 증가 시키면서 각각의 값을 비교하려고 하니, 삭제시 문제가 됐음.


def solution(s):
    answer = -1
    stack = []
    
    for char in s:
        
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
        if len(stack) == 0:
            answer = 1
        else:
            answer = 0


    return answer