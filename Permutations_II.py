class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        result = []

        for i in range(len(nums)):
            x = nums[i]
            xs = nums[:i] + nums[i + 1:]
            for p in self.permuteUnique(xs):
                if [x] + p not in result:
                    result.append([x] + p)
        return result
