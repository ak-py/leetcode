class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        removal = set()

        for index, val in enumerate(s):

            if val not in "()":
                continue

            if val == ")":
                if not stack:
                    removal.add(index)
                else:
                    stack.pop()

            if val == "(":
                stack.append(index)

        removal = removal.union(set(stack))

        out_str = ""

        for index, char in enumerate(s):
            if index not in removal:
                out_str += char

        return out_str