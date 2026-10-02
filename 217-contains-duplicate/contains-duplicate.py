class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Create an empty set to remember numbers we've already seen.
        hashset = set()

        # Visit each number in nums. Here, n is a value, not an index.
        for n in nums:
            # Check BEFORE adding: is this number from an earlier iteration?
            if n in hashset:
                # We've seen it before, so a duplicate exists.
                # Return immediately, ending the function.
                return True

            # This number is new. Remember it for future checks.
            hashset.add(n)

        # All numbers were checked without finding a duplicate.
        return False