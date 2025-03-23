#Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.
'''
Input Array: [4, 5, -3, 2, 6, 1]
Input k = 2
Output: 4.5
'''

def maxMeanSubArray(nums: list[int], k: int) -> float:
    if not nums:
        return None

    left, right = 0, k - 1
    curSum = ans = sum(nums[:right + 1])
    right += 1
    
    while right < len(nums):
        curSum += nums[right] - nums[left]
        ans = max(curSum, ans)
        left += 1
        right += 1
    
    return ans / k 

nums = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
k = 5
print(maxMeanSubArray(nums, k))