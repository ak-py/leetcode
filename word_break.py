from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        self.lexicon = set(wordDict)

        return self.wb_helper(s, 0, cache={})

    def wb_helper(self, s, start, cache):

        if start == len(s):
            return True

        if start in cache:
            return cache[start]

        for end in range(start+1, len(s)+1):

            word = s[start:end]
            if word in self.lexicon and self.wb_helper(s, end+1, cache):
                cache[start] = True
                return True

        cache[start] = False
        return False

    def wordBreak_old(self, s: str, wordDict: List[str]) -> bool:

        lexicon = set(wordDict)

        return self.wb_helper_old(s, lexicon, cache={})

    def wb_helper_old(self, s, lexicon, cache):

        if len(s) == 0:
            return True

        if s in cache:
            return cache[s]

        for index in range(len(s)):

            word = s[0:index + 1]

            if word in lexicon:
                if self.wb_helper(s[index + 1:], lexicon, cache):
                    cache[s] = True
                    return True

        cache[s] = False
        return False
