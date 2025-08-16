# https://leetcode.com/problems/power-of-two/description/
# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?

# n has one '1' in binary format, but not in the one's place (since that would be 1)
# bitwise & operator needs all '1's in binary
# since power of 2 would be 0000...0000 with one '1'
# we do n - 1, flipping every single bit from 0 to 1 and 1 to 0
# so, we do n & (n - 1) to see if ALL bits are not matching

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1))