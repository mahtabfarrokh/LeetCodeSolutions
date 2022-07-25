class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
            
        output = sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]
        
        return [i[0] for i in output] 
