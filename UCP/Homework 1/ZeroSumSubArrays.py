# Given an array of integers, count the number of subarrays that sum to zero.

def zeroSumSubArrays(nums: list[int]) -> int:
    curSum, ans = 0, 0
    prefixSums = {0 : 1}
    for num in nums:
        curSum += num
        if curSum in prefixSums:
            ans += prefixSums.get(curSum)
        prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
    return ans

nums = [4, 5, 2, -1, -3, -3, 4, 6, -7]
print(zeroSumSubArrays(nums))

nums = [1, 8, 7, 3, 11, 9]
print(zeroSumSubArrays(nums))

nums =  [8, -5, 0, -2, 3, -4]
print(zeroSumSubArrays(nums))
