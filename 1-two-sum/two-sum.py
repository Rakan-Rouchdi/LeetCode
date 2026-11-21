class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]cc
        """
        # most efficient way is to make a hash map of every 
        # value in the input array to instanly check if the value exists
        prevMap = {} # value : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i