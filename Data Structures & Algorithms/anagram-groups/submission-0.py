class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seenAnagram = {}
        groups= []

        i=0
        
        for word in strs:
            temp = [0 for i in range(26)]
            
            for letter in word:
                temp[ord(letter)-97] += 1
            key = tuple(temp)
            if not (key in seenAnagram):
                seenAnagram[key] = []
            seenAnagram[key].append(i)
            i+=1

        for group in seenAnagram.values():
            newGroup = []
            for index in group:
                newGroup.append(strs[index])
            groups.append(newGroup)
            
        return groups
            