class Solution:
    def search(self, a, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int



        Perform binary search to find pivot

        """

        left = 0
        right = len(a) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == a[mid]:  # base case
                return mid

            elif a[left] <= a[mid]:  # if left element < middle element
                if target >= a[left] and target < a[
                    mid]:  # pivot is somewhere between left and mid. But since target > left
                    right = mid - 1  # target cannot be on the right side of the array, reduce right
                else:
                    left = mid + 1

            else:
                if target <= a[right] and target > a[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

