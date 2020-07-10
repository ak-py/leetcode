"""

Took about 10 mins to crack it.

13 more mins to code it up finally without any bugs.

Leetcode tested it and successful in first try at 23 min mark.

Looking at the solutions, I can write it cleaner and more concise code.


"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removal_indexes = set()
        for i, curr in enumerate(s):

            if curr not in "()":
                continue

            if not stack and curr == ")":
                removal_indexes.add(i)

            elif curr == "(":
                stack.append(i)

            elif curr == ")":
                stack.pop()

        removal_indexes = removal_indexes.union(set(stack))
        string_arr = []

        for index, char in enumerate(s):
            if index not in removal_indexes:
                string_arr.append(char)

        return "".join(string_arr)


sol = Solution()

test_1 = "()"
test_2 = ")"
test_3 = "("
test_4 = "))(("
test_5 = "lee(t(c)o)de)"
test_6 = "a)b(c)d"

print(sol.minRemoveToMakeValid(test_1))
print(sol.minRemoveToMakeValid(test_2))
print(sol.minRemoveToMakeValid(test_3))
print(sol.minRemoveToMakeValid(test_4))
print(sol.minRemoveToMakeValid(test_5))
print(sol.minRemoveToMakeValid(test_6))

