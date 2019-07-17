class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        output = ""

        index = 0
        for char in strs[0]:
            for i in range(1, len(strs)):
                if index > len(strs[i]) - 1 or char != strs[i][index]:
                    return output

            output += char
            index += 1

        return output

