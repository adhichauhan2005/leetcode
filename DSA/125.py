import re
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower().strip()
        s = s.replace(" ", "")
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        return s == s[::-1]            
