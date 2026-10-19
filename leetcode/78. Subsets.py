class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # Start with the empty set
        result = [[]]
        
        for num in nums:
            # Create new subsets by adding the current number to all existing subsets
            result += [curr + [num] for curr in result]
            
        return result