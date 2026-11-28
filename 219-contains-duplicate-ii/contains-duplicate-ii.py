class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashMap = {} # key : value (number : index)
        for i, num in enumerate(nums):
            if num in hashMap:
                if k >= abs(i - hashMap[num]):
                    return True
            hashMap[num] = i
        return False

        