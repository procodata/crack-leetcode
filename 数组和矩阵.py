#%% 283 Move Zeroes
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
### Problem: 遍历 while list itself could change
### Solutio: 快慢指针
from typing import List
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    fast, slow = 0, 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            fast += 1
            slow += 1
        else:
            fast += 1
    while slow <= len(nums) - 1:
        nums[slow] = 0
        slow += 1

#%% 566. Reshape the Matrix
"""
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
"""
def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    # output = [[None]*c]*r ### matrix will keep having the same value since reference is saved. cannot change individual value separately
    output = [[0]*c for _ in range(r)]
    m = len(mat)
    n = len(mat[0])
    if m*n != r*c:
        return mat
    for i in range(r):
        for j in range(c):
            index = i*c + j
            mat_r = index//n 
            mat_c = index%n
            output[i][j] = mat[mat_r][mat_c]
    return output

#%% 485 Max Consecutive Ones
"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""
def findMaxConsecutiveOnes(nums: List[int]) -> int:
    res = 0
    seg = 0
    for i in nums:
        if i == 1:
            seg += 1
            res = max(res, seg)
        else:
            seg = 0
    return res

#%% 645 Set Mismatch
"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Input: nums = [1,2,2,4]
Output: [2,3]
"""
def findErrorNums(nums: List[int]) -> List[int]:
    set_num = set(nums)
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            dul = nums[i]
    for i in range(1, len(nums)+1):
        if i not in set_num:
            missing = i
    return [dul, missing]

#%% 697 Degree of an Array
"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
"""
### Problem: Find the key of dict based on the condition of values
### Solution: 遍历
def findShortestSubArray(nums: List[int]) -> int:
    count = dict.fromkeys(nums, 0)
    for i in nums:
        count[i] += 1
    max_count = max(count.values())
    max_num = [key for key in count.keys() if count[key] == max_count]
    

    min_len = len(nums)
    for max_num_ in max_num:
        start = 0; end = len(nums)-1
        while nums[start] != max_num_:
            start += 1
        while nums[end] != max_num_:
            end -= 1
        min_len = min(min_len, (end-start+1))
    return min_len

### 一次loop，count同时找到value第一次和最后一次出现的位置
def findShortestSubArray(nums: List[int]) -> int:
        left, right = dict(), dict()
        counter = collections.Counter()
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            counter[num] += 1
        degree = max(counter.values())
        res = len(nums)
        for k, v in counter.items():
            if v == degree:
                res = min(res, right[k] - left[k] + 1)
        return res

#%% 766 Toeplitz Matrix
"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
"""
def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r-1):
        for j in range(c-1):
            current = matrix[i][j]
            lower_right = matrix[i+1][j+1]
            if current != lower_right:
                return False
            else:
                continue
    return True

