class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_palindrome(arr, l, r, error_allowed):

            while l < r:
                if arr[l] != arr[r] and not error_allowed:
                    return False

                if arr[l] != arr[r] and error_allowed:
                    return check_palindrome(arr, l+1, r, False) or check_palindrome(arr, l, r-1, False)
                l += 1
                r -= 1

            return True

        return check_palindrome(s, 0, len(s)-1, True)
