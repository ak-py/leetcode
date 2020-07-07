from typing import List

'''

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.


8:03 = 8 mins into the prompt. Can't figure out the brute force. Looks like a trick question. 

9:00 = Interesting solution. I was off from the right track. 

14:00 = Read it thoroughly for 5-10 mins. Try to reproduce on my own now.

29:00 = Looked up documentation for using "else" with "for" loop in python language.

35:00 = Done. Leetcode passed.

'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_indexes = {char: index for index, char in enumerate(order)}

        for pivot in range(len(words)-1):

            curr = words[pivot]
            nxt = words[pivot+1]

            for i in range(min(len(curr), len(nxt))):

                # verify order on first distinct character seen
                if curr[i] != nxt[i]:
                    if order_indexes[curr[i]] > order_indexes[nxt[i]]:
                        return False
                    break

            # for loop completed with iteration
            # the case is such that curr = "face" and nxt = "facebook"
            # verify length of the words
            else:
                if len(curr) > len(nxt):
                    return False

        return True
