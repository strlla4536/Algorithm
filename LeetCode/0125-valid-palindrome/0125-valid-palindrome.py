import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = [i for i in s.lower() if i.isalnum()]
        return new == new[::-1]