class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        dictionary = {}
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
                
        sorted_x = sorted(dictionary.items(), key = lambda x: x[1], reverse=True)
        
        return [x[0] for x in sorted_x][:k]
        