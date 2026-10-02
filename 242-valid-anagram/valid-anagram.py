class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Time: O(n), where n is the length of either string.
        # Space: O(1), since each dictionary stores at most
        # 26 distinct lowercase English letters.

        # Anagrams must have the same length.
        if len(s) != len(t):
            return False
        
        # Store character frequencies for each string.
        countS, countT = {}, {}

        # Visit the same position in both strings.
        for i in range(len(s)):
            # Get the current count (0 if new), then add 1.
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Check that both dictionaries have identical letters and counts.
        if countS == countT:
            return True

        # Different character counts mean they aren't anagrams.
        return False
        