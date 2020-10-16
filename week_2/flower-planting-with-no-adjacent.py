from collections import defaultdict
from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)

        output = [1]

        all_types = {1, 2, 3, 4}

        for i in range(2, n+1):
            seen_types = set()
            neighbours = graph[i]

            for garden in neighbours:
                if garden > i:
                    continue
                seen_types.add(output[garden-1])

            popped_val = (all_types.difference(seen_types)).pop()
            output.append(popped_val)

        return output
