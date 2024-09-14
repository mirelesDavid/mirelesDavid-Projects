#Kadane's Algorithm Modificado para Conseguir los Numeros del MaxSubarray
"""
   class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        currentMax = 0

        for n in nums:
            currentMax = max(n, currentMax + n)
            result = max(result, currentMax)
        
        return result
 
"""


def maxSubArray(numbers):
    currentMax, res = 0, 0
    startIdx, tempStartIdx, endIdx = 0, 0, 0
    for idx, num in enumerate(numbers):
        if currentMax + num > num:
            currentMax += num
        else:
            currentMax = num
            tempStartIdx = idx
        
        if currentMax > res:
            res = currentMax
            startIdx = tempStartIdx
            endIdx = idx
            
    return numbers[startIdx:endIdx + 1]
    
print(maxSubArray([-3, 10, -2, 4]))



