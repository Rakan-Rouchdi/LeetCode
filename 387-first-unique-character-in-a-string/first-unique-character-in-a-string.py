class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}

        # First pass: count how many times each character appears.
        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1

        # Second pass: check the characters in their original order.
        # enumerate gives us both the index i and the character c.
        for i, c in enumerate(s):
            if counts[c] == 1:
                # This is the first character that appears only once.
                return i

        # Every character repeats, so there is no unique character.
        return -1

        # Time: O(n) because we scan the string at most twice.
        # Extra space: O(1) because counts stores at most 26 lowercase letters.