#Description https://leetcode.com/problems/first-bad-version/

import math
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n: int) -> int:
       # introducing the problem, a bad way of doing this is the following
       for i in range(n+1):
           if isBadVersion(i):
               return i

        #TODO: halve the n to avoid looping through

        # if isBadVersion(math.floor(n/2)):
        #     for i in range(n):
        #         if isBadVersion(i):
        #             return i

        # else:
        #     for i in range(math.floor(n/2), n):
        #         if isBadVersion(i):
        #             return i


def isBadVersion(i):
    if i >= 4:
        return True


