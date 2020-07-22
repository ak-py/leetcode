"""

URL = https://leetcode.com/problems/longest-palindromic-substring/

Have done this question about an year ago. Still remember the optimal approach on high level.

Took me about 15 mins to code. Did dry run on notebook.

Tested few edge cases on leetcode. Everything went fine, then finally submitted it.

Scored among top 25% of solutions. Has optimal runtime and space complexity.

Although I can improve on the return value of the helper function and eliminate the tuple completely.

I implement the other solution as on leetcode solutions page. Took me about 20 mins.
Mostly took me 15 mins to figure out how to set start and end variables.
Performance gains minimal. Maybe by 0.5% at most. Not worth the headache and reduced readability.

"""

class Solution:
    def longestPalindrome_smaller_call_stack(self, s: str) -> str:

        if not s or len(s) == 1:
            return s

        start = end = 0
        max_len = 1

        def expand_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            length = right - left - 1

            return length

        for i in range(len(s)):

            odd = expand_center(i, i)
            even = expand_center(i, i+1)

            iter_best = max(odd, even)

            if iter_best > max_len:
                max_len = iter_best
                start = i - (iter_best-1)//2
                end = i + iter_best//2

        return s[start:end+1]

    def longestPalindrome(self, s: str) -> str:

        if not s or len(s) == 1:
            return s

        max_str = (0, 1)
        max_len = 1

        def expand_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            length = right - left - 1
            str_range = (left + 1, right)

            return length, str_range

        for i in range(1, len(s)):

            odd = expand_center(i - 1, i + 1)
            even = expand_center(i - 1, i)

            iter_best = odd if odd[0] > even[0] else even

            if iter_best[0] > max_len:
                max_len = iter_best[0]
                max_str = iter_best[1]

        return s[max_str[0]:max_str[1]]