class Solution:
    def expandFromCenter(self, s, l, r):
        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        if self.maxlen < r - l - 1:
            self.maxlen = r - l - 1
            self.start = l + 1

    def longestPalindrome(self, s):
        self.maxlen = 0
        self.start = 0

        for i in range(len(s)):
            self.expandFromCenter(s, i, i)
            self.expandFromCenter(s, i, i + 1)
        return s[self.start:self.start + self.maxlen]


'''
expand at a position with left and right pointers. 
for each character in s, expand with l and r
the substring from start to start+maxlen is the longest palindrome

b a b a d

  r
  l

b a b a d

l   r
0   2

maxlen = r-l

'''