class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            length = len(word)
            result += str(length) + "#" + word
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        length = ""
        word = ""
        isNumber = True
        count = 0
        wordNo = 0
        for letter in s:
            if letter != "#" and count == 0:
                length += letter
                continue
            elif count == 0:
                count = int(length)
                if count == 0:
                    result.append("")
                length = ""
                continue
            word += letter
            count -= 1
            if count == 0:
                result.append(word)
                word = ""
        
        return result
            
            

                



            
