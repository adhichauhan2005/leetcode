class Solution(object):
    def reverse(self, x):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x != 0:
            #digit 
            digit = x % 10
            #adding digit behind
            rev = rev * 10 + digit
            #obtain rightmost digit
            x = x // 10

        rev = rev * sign

        if rev < INT_MIN or rev > INT_MAX:
            return 0

        return rev
