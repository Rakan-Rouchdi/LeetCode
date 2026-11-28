class TrieNode(): # create a new class for nodes in the tree 
    def __init__(self): # for every node object/character
        self.children = {} # they're going to have their children
        self.endOfWord = False # and a marker if they mark the end of a word

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root # start at the root
        for c in word: # for every character in the word
            if c not in current.children: # check if the character exists as a child node
                current.children[c] = TrieNode() # create the child node character if it does not exist
            current = current.children[c] # update the current pointer
        current.endOfWord = True # mark the last character as the end of the word
        # now the whole string is inserted
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root # start at the root
        for c in word: # for every character in the word
            if c not in current.children: # if the character is not a child 
                return False # the word was not inserted
            current = current.children[c] # update the pointer to the next character node
        return current.endOfWord # if the last character of the word is marked as the end return true
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root # start at the root
        for c in prefix: # loop through every character
            if c not in current.children: # if character not in the hash map of its children nodes
                return False # the prefix does not exist, no words start with that prefix
            current = current.children[c] # update the pointer to the next character
        return True # there exists at least 1 word with that prefix
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)