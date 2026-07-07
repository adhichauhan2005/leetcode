class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2):
            return False

        s1_count = {}
        window_count = {}

        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1

        left = 0

        for right in range(len(s2)):
            ch = s2[right]
            window_count[ch] = window_count.get(ch, 0) + 1

            if right - left + 1 > len(s1):
                left_ch = s2[left]
                window_count[left_ch] -= 1

                if window_count[left_ch] == 0:
                    del window_count[left_ch]

                left += 1

            if window_count == s1_count:
                return True

        return False
