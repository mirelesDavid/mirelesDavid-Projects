# import requests
# import mysql.connector
# import pandas as pd

# Problem
# Determine if an array has a majority element (element that appears > n/2 times, where n is the length of the array).

# Function Definition
# has_majority_element(arr) -> int
# arr: array of integers
# int: integer element in arr

# Example Input/Output
# Input 1: [2, 4, 2, 5, 2, 2, 4]
# Output 2

# Input 2: [2, 2, 5, 2, 2, 4]
# Output 2

# Input 3: [4, 2, 5, 2, 2, 4, 3]
# Output NULL

# Input 4: [2, 4, 5, 3, 2, 4]
# Output NULL

def has_majority_element(arr):
    hsahMap = collections.defaultdict(int)
    
    for num in arr:
        hashMap[num] += 1
    
    biggestNum, countNum = 0, 0
    for val, count in hashMap.items():
        if count > countNum:
            biggestNum = val
            countNum = count
        
    return biggestNum if countNum > len(arr) / 2 else None
"""
{
    2 : 4
    4 : 2
    5:  1
}

2, 4

"""
# Determine if an array has a plurality element (element that appears more than any other element).

# Function Definition
# has_plurality_element(arr) -> int
# arr: array of integers
# int: integer element in arr

# Input 1: [2, 4, 2, 5, 2, 3, 4]
# Output 1: 2

# Input 2: [2, 4, 1, 5, 2, 3, 4]
# Output 2: NULL

# Input 3: [4, 2, 5, 2, 2, 4]
# Output 3: 2

# Input 4: [4, 2, 4, 2, 2, 4]
# Output 4: NULL
def has_majority_element(arr):
    hashMap = collections.defaultdict(int)
    for num in arr:
        hashMap[num] += 1
    
    biggestNum, countNum = 0, 0
    repeated = False
    for val, count in hashMap.items():
        if count > countNum:
            biggestNum = val
            countNum = count
            repeated = False
        elif count == countNum:
            repeated = True
        
    
    return None if repeated else biggestNum

"""
# Input 4: [4, 2, 4, 2, 2, 4]

{
    2:3
    4:3
}

0, 0, False
2, 3, False
2, 3 True

"""
# Determine if an array has an equilibrium index (index where the sum of all elements to the left equals the sum of all elements to the right).

# Function Definition
# has_equilibrium_index(arr) -> int
# arr: array of integers
# int: integer index in arr

# Example Input/Output
# Input 1: [1, 4, 2, 5, 2, 3, 2]
# Output 1: 3
# Input 2: [1, 4, 2, 2, 3, 2]
# Output 2: NULL
# Input 3: [8, 2, 3, 1, 5, 4]
# Output 3: 2
# Input 4: [6]
# Output 4: 0

def has_equilibrium_index(arr):
    if len(arr) == 1:
        return 0
    
    prefixSums = []
    total = 0
    for num in arr:
        total += num
        prefixSums.append(total)
    
    for idx, num in enumerate(prefixSums):
        leftSum = num - arr[idx]
        rightSum = prefixSums[-1] - num
        
        if rightSum == leftSum:
            return idx
    
    return None
    
"""
# Input 1: [1, 4, 2, 5, 2, 3, 2]
# Output 1: 3

[1, 5, 7, 12, 14, 17, 19]

1.
1 - arr[0] =  1- 1 = 0
19 - 1 = 18

2.
5 - arr[1] = 5 - 4 = 1
19 - 5 = 14

3.
7 - arr[2] = 7 - 2 = 5
19 - 7 = 12

4.
12 - arr[3] = 12 - 5 = 7
19 - 12 = 7

"""
