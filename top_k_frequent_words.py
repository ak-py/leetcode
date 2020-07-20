import collections
import heapq
from typing import List


class FreqWord:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return other.word < self.word
        return self.freq < other.freq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)

        heap = []

        for word, count in counts.items():
            heapq.heappush(heap, FreqWord(word, count))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap).word)

        result.reverse()

        return result
