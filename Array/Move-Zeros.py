# The moveZeroes function uses two pointers, i and j, to iterate through the array nums.
# Whenever a non-zero element is encountered at index j, it is swapped with the element at index i, and i is incremented by 1.

def moveZeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
