class Node:
    def __init__(self, key, value, next_node=None, prev_node=None):
        self.val = value
        self.key = key
        self.next = next_node
        self.prev = prev_node


class LRUCache:

    def __init__(self, capacity: int):
        if capacity == 0:
            raise RuntimeError("Cannot supply capacity = 0")

        self.cap = capacity
        self.length = 0
        self.map = {}  # key -> node

        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            value = node.val

            self.remove_node(node)
            self.add_node(key, value)

            return value
        return -1

    def put(self, key: int, value: int) -> None:

        # remove old value
        if key in self.map:
            node = self.map[key]
            self.remove_node(node)

        # remove the last used key, value pair
        if self.length == self.cap:
            last = self.tail.prev
            self.remove_node(last)

        #  add the node next to head
        self.add_node(key, value)

    def remove_node(self, node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

        del self.map[node.key]
        self.length -= 1

        return node

    def add_node(self, key, value):

        head = self.head
        first = head.next

        node = Node(key, value, next_node=first, prev_node=head)

        head.next = node
        first.prev = node

        self.map[key] = node
        self.length += 1

        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
