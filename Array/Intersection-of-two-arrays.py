# Approach: We convert the arrays to sets, use the bitwise AND operator to find the common elements,
# and convert the result to a list. This succinct approach effectively removes duplicates and returns the intersection.

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
