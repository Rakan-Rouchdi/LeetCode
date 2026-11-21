class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        results = defaultdict(list) # that means any new key created in this dictionary will have a default value of an empty list automatically
        for string in strs:
            count = [0] * 26 # a - z 26 possible characters, a is index 0 and z is index 25
            for character in string:
                count[ord(character) - ord('a')] += 1
            results[tuple(count)].append(string)
        return list(results.values())
        
                
        