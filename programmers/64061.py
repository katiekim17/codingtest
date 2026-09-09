# 프로그래머스 - 크레인 인형뽑기 게임

# https://school.programmers.co.kr/learn/courses/30/lessons/64061
# 너무 어려웠음. 일단 행열에서 열이 고정되기때문에 m-1로 해야한다는것과, 열부터 시작되어야 한다는 걸 이해하지 못헀고 맨 위에껄빼는 방법도 몰랐음.

def solution(board, moves):
    answer = 0
    basket = [] # 딕셔너리 대신 리스트를 추천해요!
    
    # 1. moves에 있는 번호를 하나씩 꺼냅니다.
    for m in moves:
        # 주의: moves의 번호는 1부터 시작하지만, board의 인덱스는 0부터 시작합니다!
        col = m - 1 
                
        # 2. 고정된 열(col)에서 위에서 아래로(행 번호 0부터 순서대로) 탐색합니다.
        # board의 행 개수만큼 반복하는 코드가 필요합니다.
        for row in range(len(board)):
            # 3. 만약 board[row][col]에 인형(0이 아닌 값)이 있다면?
            # - 바구니의 맨 위 인형과 비교하기
            # - 터뜨리거나 바구니에 넣기
            # - board[row][col]을 0으로 만들기
            # - 인형을 하나 뽑았으니 이 열의 탐색은 break로 멈추기
            if board[row][col] > 0:
                doll = board[row][col]  # 잠시 손에 쥐어주기
                top = 0 # 0으로 시작
                if basket: #인형이 있으면 맨 위에꺼 꺼내기
                    top = basket.pop(-1)
                if top == doll: # 꺼냈더니, 같으면 펑! 점수만 올려주고
                    answer += 2
                else : # 다르면 다시 집어 넣기
                    if top != 0:
                        basket.append(top)
                    basket.append(doll)
                
                board[row][col] = 0
                break
            
            
    return answer

