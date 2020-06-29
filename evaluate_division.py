from typing import List

from collections import defaultdict, deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)

        for index in range(len(equations)):
            (num, den) = equations[index]
            value = values[index]
            graph[num].append((den, value))
            graph[den].append((num, 1 / value))

        output = []

        for start, end in queries:
            self.bfsHelper(graph, start, end)
            # output.append(res)

        return output

    def bfsHelper(self, dic, start, end):

        if start not in dic or end not in dic:
            return -1.0

        queue = deque()
        queue.append((start, 1.0))
        visited = set()

        while queue:

            cur_node, cur_val = queue.popleft()
            visited.add(cur_node)

            if cur_node == end:
                return cur_val

            for neighbor_node, neighbor_val in dic[cur_node]:
                if neighbor_node not in visited:
                    queue.append((neighbor_node, cur_val * neighbor_val))

        return -1.0
