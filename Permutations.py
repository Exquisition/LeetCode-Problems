import itertools


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]

        else:
            l = []
            for i in range(len(nums)):
                x = nums[i]
                xs = nums[:i] + nums[i + 1:]
                for p in self.permute(xs):
                    l.append([x] + p)
            return l

