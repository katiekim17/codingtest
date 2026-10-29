# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        result = []

        def backtrack(remain, comb, start):
            if remain == 0:
                result.append(list(comb))
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                # 숫자를 무한정 사용할 수 있으므로 i를 그대로 넘김
                backtrack(remain - candidates[i], comb, i)
                comb.pop()  # 백트래킹 (원상복구)

        backtrack(target, [], 0)
        return result
