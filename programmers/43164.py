# 프로그래머스 - 여행경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 전혀 생각도 못함. 티켓 사용 여부도 확인하지 않았고,
# 2차 배열 함수에 머리가 아팠음

def solution(tickets):
    answer = []
    tickets.sort()
    
    # 2. 티켓 사용 여부를 기록할 리스트 만들기 (티켓 개수만큼 False로 초기화)
    visited = [False] * len(tickets)  # visited = [False, False, False]
    
    # 3. DFS 함수(또는 재귀 함수) 정의하기
    def dfs(now_airport, path):
        # 만약 path에 담긴 공항 수가 (티켓 수 + 1)과 같다면? 모든 티켓을 쓴 것!
        if len(path) == len(tickets) + 1:
            return path
    
        # 지금 공항(now_airport)에서 출발하는 티켓을 tickets에서 찾기
        for i in range(len(tickets)):
            # 아직 안 쓴 티켓이고, 출발지가 현재 공항과 같다면?
            if not visited[i] and tickets[i][0] == now_airport:
                visited[i] = True # 티켓 사용 처리
                
                # 다음 공항으로 이동 (재귀 호출)
                result = dfs(tickets[i][1], path + [tickets[i][1]])
                if result: 
                    return result # 경로를 찾았다면 그대로 끝까지 반환
                
                visited[i] = False # (중요!) 이 길로 가니 실패했다면, 다시 티켓을 안 쓴 걸로 되돌리기(백트래킹)

    
    # 항상 "ICN"에서 시작합니다.
    return dfs("ICN", ["ICN"])

        
    return answer
