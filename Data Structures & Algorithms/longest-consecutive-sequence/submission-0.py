class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            nums_set.add(num)

        max_length = 0
        curr_length = 0
        curr_set = set()

        for num in nums_set:
            if num-1 in nums_set:
                continue
            else:
                i=0
                while(num+i in nums_set):
                    i+=1
                if i>max_length:
                    max_length=i

        return max_length



        