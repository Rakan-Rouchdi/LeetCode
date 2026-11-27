class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
        left = 0
        for right in range(len(needle)-1, len(haystack)):
            if haystack[left:right+1] == needle:
                return left
            left += 1
        return -1



        