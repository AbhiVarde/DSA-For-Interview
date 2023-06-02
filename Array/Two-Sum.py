# Approach: Use a hash table to store the difference between the target and each element.
# If the difference is found later in the array, return the indices.

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []
