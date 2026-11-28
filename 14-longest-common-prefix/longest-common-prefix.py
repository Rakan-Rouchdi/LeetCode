#class TrieNode:
#    def __init__(self):
#        self.children = {}


#class Trie:
#    def __init__(self):
#        self.root = TrieNode()
#    
#    def add(str):
#        current = self.root
#           if c not in current.children:
#                current.children[c] = TrieNode()
#            current = current.children[c]
#    
#    def starts

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        shortestWord = min(strs, key=len)
        flag = True
        for i, char in enumerate(shortestWord):
            for word in strs:
                if word[i] != char:
                    flag = False
            if flag:
                prefix += char
        return prefix

        
        