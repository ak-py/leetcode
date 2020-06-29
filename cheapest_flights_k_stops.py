from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        # [[0,1,100],[1,2,100],[0,2,500]]

        graph = defaultdict(list)
        for src_city, dst_city, price in flights:
            graph[src_city].append((dst_city, price))

        # { 0 : (1,100)

        queue = [(src, 0, 0)]

        res = []

        while queue:
            city, stops, price = queue.pop(0)

            if stops > K:
                continue

            if city == dst:
                res.append(price)

            for connected_city, travel_price in graph[city]:
                queue.append((connected_city, stops+1, price + travel_price))

        return min(res)
