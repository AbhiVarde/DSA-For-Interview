# The "removeElement" function uses two pointers, i and j, to iterate through the array nums
# Whenever a non-val element is encountered at index j, it is assigned to the position i in the array, and i is incremented by 1.

def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
