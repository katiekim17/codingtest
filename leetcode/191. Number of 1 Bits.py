# https://leetcode.com/problems/number-of-1-bits/description

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n = n & (n - 1)
            count += 1

        return count