class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1
        
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i

        return -1
