"""
bad implementation -> pythonic and too polarizing, might not work well for large integers
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b, 2)

        total = int_a + int_b
        return bin(total)[2::]