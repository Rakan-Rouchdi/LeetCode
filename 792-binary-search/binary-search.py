class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # consider the whole array
        l = 0 # start at the beginning of the array
        r = len(nums) - 1 # start the end of the array

        while l <= r: # run until they cross each other 
            mid = (l + r) // 2 # calculate the midpoint
            if nums[mid] > target: # if mid is bigger than target
                r = mid - 1 # we need a smaller number so update the right pointer to get smaller numbers
            elif nums[mid] < target: # if mid is less than target
                l = mid + 1 # need a bigger number update left pointer
            else: # that means they are equal and we found the target
                return mid # return the index

        return -1 # target is not in the array

        # Time complexity O(logn)
        # Space complexity O(1)