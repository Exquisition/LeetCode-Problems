class Solution:
    def maxSubArray(self, A):
        """
        :type nums: List[int]
        :rtype: int

        max subarray using Kadane's Algorithm
        """
        max_ending_here = max_so_far = A[0]
        for x in A[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
