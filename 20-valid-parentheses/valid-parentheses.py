class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"} # hash map
        stack = [] # empty stack

        for c in s: # for every character in the string
            if c in closeToOpen: # if its a closing bracket
                if stack and stack[-1] == closeToOpen[c]: # check if stack is not empty and the top of the stack is its matching opening bracket
                    stack.pop()
                else: # otherwise either if its empty or its not matching
                    return False
            else: # if its another consecutive opening bracket 
                stack.append(c) # add it to the stack
        
        return True if not stack else False