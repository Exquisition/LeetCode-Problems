class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        d = {}
        if len(nums) < 3:
            return []

        nums = sorted(nums)
        for i, num in enumerate(nums):
            l = i + 1  # left pointer
            r = len(nums) - 1  # right pointer
            while l < r and nums[l] != nums[r]:
                # 2 conditions, left pointer and right pointer are not pointing to same element,
                # AND values aren't equal (otherwise we won't get 3sum = 0)
                s = nums[i] + nums[l] + nums[r]
                if s < 0:  # if sum < 0, increment the left pointer to increase the sum
                    l += 1
                elif s > 0:  # if sum > 0, decrement the right pointer to decrease the sum
                    r -= 1
                else:
                    t = (nums[i], nums[l], nums[r])
                    if t not in d:
                        d[t] = 1  # sum = 0, so add this tuple to the dictionary

                    l += 1  # move towards the middle of array
                    r -= 1
        return d.keys()
