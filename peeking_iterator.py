# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


"""

        { 1 }

curr          ^
value =  1
has_next = F 


hasNext = F 
peek = error
next = error
"""


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator

        # empty list
        if not self.it.hasNext():
            raise ValueError()

        self.value = self.it.next()
        self.has_next = True

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.has_next:
            raise IndexError()

        return self.value

    def next(self):
        """
        :rtype: int
        """
        if not self.has_next:
            raise IndexError()

        temp = self.value   # 1

        if self.it.hasNext():
            self.value = self.it.next()
        else:
            self.has_next = False

        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_next



# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
