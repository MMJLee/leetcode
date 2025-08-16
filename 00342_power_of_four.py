# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

 

# Example 1:

# Input: n = 16
# Output: true
# Example 2:

# Input: n = 5
# Output: false
# Example 3:

# Input: n = 1
# Output: true
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?

# same thing as power of two, but if not divisible by 3, then it's also divisible by 4
# since powers of four will only be a single bit as '1'
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n % 3 == 1 and not (n & (n - 1))