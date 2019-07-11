class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for x in nums:
            subsets = [subset + [x] for subset in res if subset + [x] not in res]

            res.extend(subsets)
        return res
