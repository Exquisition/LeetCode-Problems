class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        dicti = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        oldlist = []
        currentlist = list(dicti[digits[0]])

        for bit in digits[1:]:
            oldlist = currentlist
            currentlist = []
            for letter in dicti[bit]:
                # each letter possible
                currentlist += [x + letter for x in oldlist]

        return currentlist
