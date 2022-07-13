class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # e.g. nums = [0, 1, 2, 5, 3, 3, 0]
        # A reverse function that reverses the elements specified
        def reverse(nums, l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # Take right index
        right =  len(nums)-1

        # Iterate till non-increasing elements are present
        while right > 0 and nums[right] <= nums[right-1]:
            right -= 1

        # If right == 0
        # Array is descending
        # Just return the array in ascending order
        if right == 0:
            return nums.reverse()

        # Take a pivot which the element previous to the non-decresing elements
        # nums = [0, 1, 2, 5, 3, 3, 0] pivot = 2
        pivot = right - 1

        # Initialise a successor element and find the successor which is greater than a pivot element
        # in the array 
        successor = 0
        for i in range(len(nums)-1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break
        
        # nums = [0, 1, 2, 5, 3, 3, 0] pivot = 2, successor = 3
        # Swap the successor and pivot
        nums[pivot], nums[successor] = nums[successor], nums[pivot]

        # nums = [0, 1, 3, 5, 3, 2, 0]

        # Reverse the elements from pivot till last element
        reverse(nums, pivot+1, len(nums)-1)
        # nums = [0, 1, 3, 0, 2, 3, 5]

        return nums

s = Solution()
print(s.nextPermutation([3, 2, 1]))