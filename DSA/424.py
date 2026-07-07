class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        left = 0
        maxFreq = 0
        ans = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            maxFreq = max(maxFreq, count[s[right]])

            window_size = right - left + 1

            if window_size - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
