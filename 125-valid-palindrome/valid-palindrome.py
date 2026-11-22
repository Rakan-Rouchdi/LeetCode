class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0 # left pointer starting at the first character of string
        r = len(s) - 1 # right pointer starting at last character of string
        
        while l < r: # while loops keeps going until both pointers are in the same position if odd (length of string) or they cross each other if even
            while l < r and not s[l].isalnum(): # Skip non-alphanumeric characters on the left until the pointers meet
                l += 1 # skip the character
            while r > l and not s[r].isalnum(): # Skip non-alphanumeric characters on the right until the pointers meet
                r -= 1 # skip the character
            if s[l].lower() != s[r].lower(): # convert to lower and compare characters
                return False 
            l += 1 # move pointer up 
            r -= 1 # move pointer down
        return True

        