class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in nums:
                L = 1
                while n + 1 in nums:
                    L += 1
                    n += 1
                longest = max(longest, L)
        return longest
