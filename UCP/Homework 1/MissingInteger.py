#Given an integer n and a sorted array of integers of size n-1 which contains all but one of the integers in the range 1-n, find the missing integer.

def missingInteger(nums: list[int], k: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if mid + 1 == nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    return left + 1
        




nums = [1, 2, 3, 4, 6, 7]
print(missingInteger(nums, 7))

nums = [1]
print(missingInteger(nums, 2))

nums =  [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
print(missingInteger(nums, 12))