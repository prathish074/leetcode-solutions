class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Step 1: Place each number in its correct position
        # Example: 3 should go to index 2 (because index = num - 1)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] to its correct position
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # Step 2: Find the first place where index+1 != value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # Step 3: If all numbers are in place, missing number is n + 1
        return n + 1
