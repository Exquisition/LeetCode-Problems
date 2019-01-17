class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]

        for x in nums:
            subsets = [subset + [x] for subset in res]
            res.extend(subsets)
        return res