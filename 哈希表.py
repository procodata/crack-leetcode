#%% 1 Two Sum 
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
"""
### Problem: In Dict, decide what to put as key or as value?
### Solution: Index needs to be found, index should be the value instead of key. 

### Problem: Nested loop results in redundent checking. 2+7 and 7+2 are redundent
### Solution: hash
from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    temp = dict()
    for i in range(len(nums)):
        if nums[i] not in temp.keys():
            temp.update({target - nums[i]: i})
        else:
            return (i, temp[nums[i]])

#%% 217 Contains Duplicate      
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""      
def containsDuplicate(nums: List[int]) -> bool:
    hash_map = set()
    for num in nums:
        if num not in hash_map:
            hash_map.add(num)
        else:
            return True
    return False

#%% 594 Longest Harmonious Subsequence
"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

nums = [1,3,2,2,5,2,3,7] The longest harmonious subsequence is [3,2,2,2,3].
"""
def findLHS(nums: List[int]) -> int:
    hash_map = {}
    for num in nums:
        # if num not in hash_map:
        #     hash_map[num] = 1
        # else:
        #     hash_map[num] += 1
        hash_map[num] = hash_map.get(num, 0) + 1 ### Deal with cases when item is not in dict
    max_len = 0
    for k, v in hash_map.items():
        if hash_map.get(k+1, 0) != 0:
            max_len = max(max_len, hash_map.get(k+1)+v) ### find max
    return max_len

#%% 349 两个数组的交集 
"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    res = []
    set1 = set(nums1)
    for num in nums2:
        if num in set1 and num not in res:
            res.append(num)
    return res

#%% 350 两个数组的交集 II
"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""
### Problem: 
#   * 遍历 without replacement, 用过一次就要拿掉
#   * 统计出现的次数
### Solution: map
    
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    count = {}
    # hashmap1 = dict.fromkeys(nums1, 0)

    res = []
    # set1 = set(nums1)
    for num in nums1:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    for num in nums2:
        if num in count and count[num] >= 1:
            res.append(num)
            count[num] -= 1
        else:
            continue
    return res

#%% 242 有效的字母异位词  Valid Anagram
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Input: s = "anagram", t = "nagaram"
Output: true
"""
def isAnagram(s: str, t: str) -> bool:
    map1 = dict.fromkeys(list(s), 0)
    map2 = dict.fromkeys(list(t), 0)
    for char in s:
        map1[char] += 1
    for char in t:
        map2[char] += 1
    return map1 == map2

#%% 202. Happy Number
"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

"""
### Problem: Decide if it will end eventually or loop forever
### Solution: 
#   * Prove endless loop won't happen
#   * find when/on what condition loop will happen

class Solution:
    def isHappy(n: int) -> bool:
        def get_next(n):
            n = sum([int(num)**2 for num in str(n)])
            return n
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1

#%% 205. Isomorphic Strings 同构字符串
"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""
### Problem: one-to-one mapping, bidirectional
### Solution: 
#   * maintain two maps
#   * Use one map, but use set(keys) == set(values) to check if it's one-to-one mapping
def isIsomorphic(s: str, t: str) -> bool:
    hashmap1 = {}
    hashmap2 = {}
    for i, j in zip(s, t):
        if i not in hashmap1:
            hashmap1[i] = j
        else:
            if hashmap1[i] != j:
                return False
        if j not in hashmap2:
            hashmap2[j] = i
        else:
            if hashmap2[j] != i:
                return False
    return True
