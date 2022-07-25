class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        items = list(set(nums))
        if len(items) != len(nums):
            return True
        return False
