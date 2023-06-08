# We assign nums2 to nums1[m:], replacing the elements after the original m
# elements in nums1 with the elements from nums2. This effectively merges the
# two arrays.
# We then call the sort() method on nums1 to sort the merged array in-place.

def merge(nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()
    return nums1
