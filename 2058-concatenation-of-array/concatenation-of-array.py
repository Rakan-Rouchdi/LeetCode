class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Create enough space for two copies of nums.
        ans = [0] * 2 * len(nums)

        for i in range(len(nums)):
            # Put the number at the same index in the first copy.
            ans[i] = nums[i]

            # Move forward by one full copy to fill the second half.
            ans[i + len(nums)] = nums[i]

        return ans
        