class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        
        
        i, j = 0, len(people) - 1
        ans = 0
        
        while i <= j:
            
            # take the heaviest person only
            ans += 1
            
            
            #if we can take the light person as well
            if people[i] + people[j] <= limit:
                i += 1
                
            j -= 1
           
        return ans