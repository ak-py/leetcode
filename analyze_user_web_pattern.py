"""
URL - https://leetcode.com/problems/analyze-user-website-visit-pattern/

Status - REDO - short-term

Could not come up with a solution within 15 mins. Looked at other submissions to get an idea.
Need to practice more on Array + Hash Table + Graph problems.

Time Complexity = O(N log(N))
Space Complexity = O(N)
 where N is the number of records

 Time taken - 40 mins

"""
import collections
import itertools
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        graph = collections.defaultdict(list)

        for t, u, w in sorted(zip(timestamp, username, website)):
            graph[u].append(w)

        seen_combs = collections.Counter()

        for u, route in graph.items():
            for combination in set(itertools.combinations(route, 3)):
                seen_combs[combination] += 1

        pattern = None
        max_count = 0

        for comb, count in seen_combs.items():

            # highest count combination is picked
            if count > max_count:
                pattern = comb
                max_count = count

            # if tie then pick lexicographically smaller combination
            elif count == max_count and pattern > comb:
                pattern = comb

        return pattern
