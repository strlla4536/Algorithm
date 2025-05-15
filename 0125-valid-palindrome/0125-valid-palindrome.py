import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = re.sub('[-=+,#/\?:;^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’· _\{\}]', '',s).lower()
        s = re.sub('\W', '', s).lower()
        s = re.sub('[_]','',s)
        print(s)

        if len(s)==0: return True
        
        start, end = 0, len(s)-1
        i = 1
        while s[start] == s[end]:
            print(f"{i}번째")
            print(f"update 전 start : {start}, end: {end}")
            start += 1
            end -= 1
            print(f"update 후 start : {start}, end: {end}")
            if start >= end:
                return True
            i += 1
            
        return False
        