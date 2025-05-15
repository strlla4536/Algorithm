import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = re.sub('[-=+,#/\?:;^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’· _\{\}]', '',s).lower()
        s = re.sub('\W', '', s).lower()
        s = re.sub('[_]','',s)
        print(s)

        if len(s)==0: return True
        
        start, end = 0, len(s)-1
        
        while s[start] == s[end]:
            
            start += 1
            end -= 1
            
            if start >= end:
                return True
            
            
        return False
        