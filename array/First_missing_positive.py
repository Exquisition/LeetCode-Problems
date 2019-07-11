class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        UniqueNums = set(nums)
        length = len(nums)

        if length == 0:
            return 1

        for i in range(1, length + 2):
            if i not in UniqueNums:
                return i
