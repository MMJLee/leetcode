# You are given an integer array nums.

# You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:

# All elements in the subarray are unique.
# The sum of the elements in the subarray is maximized.
# Return the maximum sum of such a subarray.

 

# Example 1:

# Input: nums = [1,2,3,4,5]

# Output: 15

# Explanation:

# Select the entire array without deleting any element to obtain the maximum sum.

# Example 2:

# Input: nums = [1,1,0,1,1]

# Output: 1

# Explanation:

# Delete the element nums[0] == 1, nums[1] == 1, nums[2] == 0, and nums[3] == 1. Select the entire array [1] to obtain the maximum sum.

# Example 3:

# Input: nums = [1,2,-1,-2,1,0,-1]

# Output: 3

# Explanation:

# Delete the elements nums[2] == -1 and nums[3] == -2, and select the subarray [2, 1] from [1, 2, 1, 0, -1] to obtain the maximum sum.

# Constraints:

# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100

# seems like a sliding window problem again
# we will always be removing negatives since they don't contribute to the uniqueness of the subarray at all
# keep track of the lagging pointer to slide the window until no dupes when leading pointer encounters a dupe

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = max(nums)
        count = 0
        num_stack = []

        for num in nums:
            while num in num_stack:
                count -= num_stack.pop(0)
            if num > 0:
                num_stack.append(num)
                count += num
                ans = max(ans, count)
        return ans

# not exactly a sliding window since you can ignore dupes
# better to use a set?

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        tmp = set(num for num in nums if num > 0)
        if len(tmp) == 0: return max(nums)
        return sum(tmp)
