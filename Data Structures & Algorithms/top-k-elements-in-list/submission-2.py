class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        groups = [[] for _ in range(len(nums)+1)]
        for num, frequency in freq.items():
            groups[frequency].append(num)
        
        count = 0
        result = []
        for group in reversed(groups):
            for num in group:
                result.append(num)
                count += 1
            if count == k:
                break
                
        return result

        