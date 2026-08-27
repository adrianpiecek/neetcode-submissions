class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i=0
        for num in nums:
            result = target - num
            if (result in seen):
                return [seen.get(result),i]
            else:
                seen[num] = i
            i+=1
        return []