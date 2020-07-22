"""
bad implementation -> pythonic and too polarizing, might not work well for large integers
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        result = []

        for i in reversed(range(n)):

            if a[i] == "1":
                carry += 1

            if b[i] == "1":
                carry += 1

            if carry % 2 == 1:
                result.append("1")
            else:
                result.append("0")

            carry = carry // 2

        if carry == 1:
            result.append("1")

        result.reverse()

        return "".join(result)
