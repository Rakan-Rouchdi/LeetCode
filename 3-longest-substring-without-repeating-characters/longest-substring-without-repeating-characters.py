class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set() # create a set to keep track of seen characters
        l = 0 # set left pointer to 0 
        result = 0 # return longest substring length
        for r in range(0, len(s)): # use the right pointer to iterate through the whole string
            while s[r] in charSet: # check for duplicates in the set and keep checking until all duplicates are removed
                charSet.remove(s[l]) # remove the duplicate character from the set 
                l += 1 # increment the left pointer by 1 and shrink the window
            # once all duplicates have been removed and it is safe to add a new character to the set
            charSet.add(s[r])
            result = max(result, r - l + 1) # update the result and check if it is greater
        return result
        # Time Complexity -  O(N) as we 1 loop through string
        # Space Complexity - O(N) as we created a new set 
        