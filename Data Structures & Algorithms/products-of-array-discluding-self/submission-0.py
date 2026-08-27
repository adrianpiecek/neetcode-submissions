class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        prevNum = nums[0]

        for i in range(1,len(nums)):
            prefix[i] = prevNum*prefix[i-1]
            prevNum=nums[i]
        
        prevNum = nums[len(nums)-1]
        
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = prevNum*suffix[i+1]
            prevNum=nums[i]
        
        result=[]
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[i])
        
        return result
            

        