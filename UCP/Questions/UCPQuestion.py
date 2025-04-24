# import requests
# import mysql.connector
# import pandas as pd

'''
Given an array of integers, return the number of unique triplets that sum to zero.
Example
Input: [8, 2, 3, 5, -2, 1, -1, 3]
Output: 2 (Triplets are (-2, -1, 3), (-2, -1, 3))

Input: [5, 0, -5, -2, 4, 1, -3, 6]
Output: 3 (Triplets are (5, 0, -5), (5, -2, -3), (-5, 4, 1))
'''

'''

'''
def getUniqueTriplets(nums)->int:
    if not nums:
        return 0

    nums.sort()
    ans = 0

    numCount = {}
    for num in nums:
        numCount[num] = numCount.get(num, 0) + 1

    tripletsUsed = set()
    for idx, num in enumerate(nums):
        left, right = idx + 1, len(nums) - 1

        while left < right:
            if (num, nums[left], nums[right]) not in tripletsUsed and (num + nums[left] + nums[right]) == 0:
                tripletsUsed.add((num, nums[left], nums[right]))
                if num == nums[left] and num == nums[right]:
                    ans += ((numCount[num] * (numCount[nums[left]]  - 1) * (numCount[nums[right]] - 2)) // 6)
                elif num == nums[left]:
                    ans += ((numCount[num] * (numCount[nums[left]] - 1 )* numCount[nums[right]]) // 6)
                elif num == nums[right] or nums[right] == nums[left]:
                    ans += ((numCount[num] * numCount[nums[left]] * (numCount[nums[right]] - 1)) // 6)
                else:
                    ans += ((numCount[num] * numCount[nums[left]] * numCount[nums[right]]) // 6)
                left += 1
            elif num + nums[left] + nums[right] > 0:
                right -= 1
            else:
                left += 1

        return ans

#T = O(n^2)
#S = O(N)

nums = [8, 2, 3, 5, -2, 1, -1, 3]
nums = [-2, -2, 0, 0, 2, 2, 2]
nums = [5, 0, -5, -2, 4, 1, -3, 6]
nums = [0,0, 0, 0, 0, 0, 0, 0, 0]

print(getUniqueTriplets(nums))