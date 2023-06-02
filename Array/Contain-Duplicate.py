# Approach: Use a set to check for duplicate elements

def containsDuplicate(nums):
    return len(set(nums)) != len(nums)
