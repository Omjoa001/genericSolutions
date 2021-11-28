# Description https://leetcode.com/problems/search-insert-position/
from typing import List

"""class Solution(object):
    def searchInsert(self, nums, target):

        :type nums: List[int]
        :type target: int
        :rtype: int
 
 Note to self: Python is weird, python3 below:
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            n = len(nums)
            for i in range(n):
                if (nums[i] > target):                
                    return i
            return n
            
            
            
nums = [1,3,5,6]
#target = 5
#target = 2
#target = 7
target = 0
#nums, target = [1], 0

solution = Solution()
solution.searchInsert(nums, target)
