class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [] # list of lists containing the unique triplets
        nums.sort() # sort the array so duplicate numbers will be next to each other in the array

        for i, a in enumerate(nums): # for loop to find the first number in the triplet (a)
            if i > 0 and a == nums[i-1]: # check to see if it is a duplicate (element a) as we don't want the same solution
                continue # skip the iteration completely move to the next i
            l = i+1 # start the left pointer at one position more than the first number (a)
            r = len(nums) - 1 # start the right pointer at the last element of the nums list
            while l < r: # keep running until the pointers meet or cross each other
                threeSum = a + nums[l] + nums[r] # add the 3 numbers
                if threeSum < 0: # if result is less than 0 it is too small
                    l += 1 # shift left pointer for a bigger number
                elif threeSum > 0: # if result is not less than 0 and is bigger than 0 it is too big
                    r -= 1 # shift right pointer for a lower number
                else: # if both conditions not true then the result is equal to 0
                    res.append([a,nums[l],nums[r]]) # add the triplets as we have found a solution
                    l += 1 # update the left pointer move it to the right to check for more solutions
                    while nums[l] == nums[l-1] and l < r: # check for duplicates on the left pointer and make sure it doesn't cross bounds
                        l += 1 # skip until we don't see a duplicate and once we do that the right pointer will move itself
        return res
                



        