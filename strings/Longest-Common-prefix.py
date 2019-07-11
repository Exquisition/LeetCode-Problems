class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Exception if strs empty
        if not strs:
            return ''

        # Getting smallest string length
        min_size = float('inf')
        for string in strs:
            min_size = min(min_size, len(string))

        # Iterating till the smallest string length
        for index in range(min_size):
            # Assigning character of first string
            char = strs[0][index]

            # Checking if it is the same for all strings
            for string in strs:
                if string[index] != char:
                    # returning trimmed string till the current index
                    return string[:index]

        # Returning smallest string
        return strs[0][:min_size]
