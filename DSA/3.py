class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        l=0
        result=0

        for r in range(len(s)):
            #Add right remove left and add l+1
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])

            #Choose max
            result = max(result, r-l+1)
        return result
        
