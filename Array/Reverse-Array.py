# we use two pointers (start and end) initially pointing to the first and last elements of the array, respectively.
# We swap the elements at these pointers and move the pointers towards the center until they meet or cross each other, effectively reversing the array in-place.

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
