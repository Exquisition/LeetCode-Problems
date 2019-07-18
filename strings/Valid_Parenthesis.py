class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        stack = []
        
        for char in s:
            if char == '(' or char == '{' or char == "[":
                stack.append(char)
            else:
                if len(stack) > 0:
                    char_popped = stack.pop()
                    if char_popped == '(':
                        opposite = ')'
                    elif char_popped == '{':
                        opposite = '}'
                    else:
                        opposite = "]"

                    if opposite != char: 
                        return False
                else:
                    return False
                
        if len(stack) > 0:
            return False
                
            
        return True