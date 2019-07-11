class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num = sorted(nums)
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j = i + 1
            k = len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:  # if less than target, increase sum by incrementing right pointer
                    j += 1
                elif sum > target:
                    k -= 1

        return result