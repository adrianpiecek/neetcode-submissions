class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if not (num in freq):
                freq[num] = 1
            else:
                freq[num] += 1

        groups = [[] for _ in range(len(nums))]
        for key,value in freq.items():
            groups[value-1].append(key)
        
        count = 0
        result = []
        for group in reversed(groups):
            if len(group) > 0:
                for num in group:
                    result.append(num)
                    count += 1
                if count == k:
                    break
                
        return result

        