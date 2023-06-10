# we can use a two-pointer approach to find a subarray with a given sum in a given array.

def subarrayWithGivenSum(arr, target_sum):
    start = end = curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        while curr_sum > target_sum:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == target_sum:
            end = i
            return [start, end]
    return [-1, -1]
