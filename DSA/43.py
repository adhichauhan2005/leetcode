class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                digit1 = ord(num1[i]) - ord("0")
                digit2 = ord(num2[j]) - ord("0")

                mul = digit1 * digit2

                pos1 = i + j
                pos2 = i + j + 1

                total = mul + res[pos2]

                res[pos2] = total % 10
                res[pos1] += total // 10

        ans = ""

        for digit in res:
            if not (ans == "" and digit == 0):
                ans += str(digit)

        return ans
