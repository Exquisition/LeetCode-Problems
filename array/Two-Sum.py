class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False

        dicti = {}
        for i, num in enumerate(nums):
            if num in dicti.keys():
                return [dicti[num], i]

            else:
                dicti[target - num] = i


"""
dicti[7] = 0

Idea: We make a single pass through the array. For each element we store target-element as the key and the index of the element as the value. If at some point we see a number that is a key in the dictionary, we have found the second number. 

We return the index of the number we are currently at (i) , and the index of the num in the dictionary which is dicti[num]


"""
