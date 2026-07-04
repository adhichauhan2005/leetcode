class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}

        for ele in nums:
            count[ele] = count.get(ele, 0) + 1

        res = sorted(count.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in res[:k]]
