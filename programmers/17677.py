# 프로그래머스 - [1차] 뉴스 클러스터링 (자카드 유사도) 
# https://school.programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    answer = 0
    group1 = []
    group2 = []

    str1 = str1.upper()
    str2 = str2.upper()
        
    for i in range(0, len(str1), 1):
        ja1 = str1[i:i+2]
        if len(ja1) > 1 and ja1.isalpha():
            group1.append(ja1)
    for j in range(0, len(str2), 1):
        ja2 = str2[j:j+2]
        if len(ja2) > 1 and ja2.isalpha():
            group2.append(ja2)
    
    # 3. 빈 집합 예외 처리 (ZeroDivisionError 방지)
    if not group1 and not group2:
        return 65536
    
#     num = 0
#     # 교집합
#     for k in group1:
#         for l in group2:
#             print(f"k: {k}, l: {l}")
#             if k == l:
#                 num += 1
#     #numa = set(group1) & set(group2)
#     #print(len(numa))
#     # print(num)
    
#     #합집합
#     # numb = set(group1) | set(group2)
#     # print(len(numb))
#     hop = []
#     for k in group1:
#         hop.append(k)
#     for l in group2:
#         if l not in hop:
#             hop.append(l)
#     print(len(hop))       
    
#     answer = (num / len(hop)) * 65536
    
        # ------------------ [수정 1] 교집합 계산 방식 변경 ------------------
    # 중복 카운트를 막기 위해 group2를 복사해서 사용합니다.
    group2_copy = group2.copy()
    num = 0
    for k in group1:
        # 중첩 for문 대신 'in'을 쓰면 매칭되는 게 있는지 바로 찾습니다.
        if k in group2_copy:
            num += 1
            # 짝이 맞춰진 글자는 리스트에서 제거하여 중복 매칭을 방지합니다.
            group2_copy.remove(k) 
    # -----------------------------------------------------------------
    
    # ------------------ [수정 2] 합집합 계산 방식 변경 ------------------
    # 다중집합의 합집합 크기는 공식이 정해져 있습니다.
    # 공식: (A의 개수 + B의 개수) - 교집합의 개수
    len_hop = len(group1) + len(group2) - num
    # -----------------------------------------------------------------
    
    # ------------------ [수정 3] 정수 변환(소수점 버림) 추가 -----------
    # 자카드 유사도 결과는 소수점 아래를 버려야 하므로 int()를 씌워줍니다.
    answer = int((num / len_hop) * 65536)
    # -----------------------------------------------------------------
            
        
            
    return answer
