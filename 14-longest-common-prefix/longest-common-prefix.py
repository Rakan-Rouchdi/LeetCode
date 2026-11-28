class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""  # store the prefix we've matched so far
        shortestWord = min(strs, key=len)  # every word has at least this many characters

        for i, char in enumerate(shortestWord):  # get each index and character in the shortest word
            for word in strs:
                if word[i] != char:  # does this word have a different character at index i?
                    return prefix  # one mismatch is enough to stop
            prefix += char  # every word matched at index i, so add this character

        return prefix  # the whole shortest word matched
        
        