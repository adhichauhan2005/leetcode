class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue

                path.append(num)
                backtrack()
                path.pop()

        backtrack()
        return res
