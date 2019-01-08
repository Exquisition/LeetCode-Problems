class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        solution using sliding window

        """
        # body is a set storing all non-repeating elements in the current consideration
        body = set()
        # l is leftmost element
        # r is right most element
        # maxl is max length we've seen so far
        l = r = maxl = 0
        while r < len(s):
            cur = s[r]
            # if current element is in the set already,
            # we move left boundary until the element and then move 1 more to move past it
            # e.g. d a b c a
            #      l     r
            # we need to move l to 1 past a which is b and get
            # d a b c a
            #     l   r
            # set contains b c a, size of the set is the maxl for the current set of elements
            if cur in body:   #if we see a character already in the set
                while l < r and s[l] != cur:   #remove all characters up until cur
                    body.remove(s[l])
                    l += 1
                l += 1
            body.add(cur)  #add to current longest substring
            maxl = max(maxl, len(body))   #update max length
            r += 1              #go to the next character
        return max(maxl, len(body))
        # or we can just return maxl