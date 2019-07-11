class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        if digits[-1] != 9:
            return digits[0:n-1] + [digits[-1]+1]    #just add one to the element
        elif n>1:
            return self.plusOne(digits[0:n-1]) + [0]    #recursive call
        else:
            return [1,0]                                #base case