class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = {}
        for letter in s:
            if not(letter in temp):
                temp[letter] = 1
            else:
                temp[letter] += 1

        for letter in t:
            if not(letter in temp):
                return False
            else:
                temp[letter] -= 1
        
        for value in temp.values():
            if value != 0:
                return False
        return True
        