class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1 for i in range(len(nums))]
        after = [1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            before[i]= before[i-1] * nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            after[i]= after[i+1] * nums[i+1]
            

        output = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            output[i]=before[i]*after[i]
            
        return output
            
