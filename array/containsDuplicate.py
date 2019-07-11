class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashmap = {}
        
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                return True
        return False
        