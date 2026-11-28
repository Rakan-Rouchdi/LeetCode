class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        shortestWord = min(strs, key=len)
        for i, char in enumerate(shortestWord):
            for word in strs:
                if word[i] != char:
                    return prefix
            prefix += char
        return prefix
        
        