class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)

        return [left, right]

    def binSearch(self, nums, target, leftBias):
        l = 0
        r = len(nums) - 1
        ans = -1

        while l <= r:
            mid = (l + r) // 2

            if target > nums[mid]:
                l = mid + 1

            elif target < nums[mid]:
                r = mid - 1

            else:
                ans = mid

                if leftBias:
                    r = mid - 1
                else:
                    l = mid + 1

        return ans
