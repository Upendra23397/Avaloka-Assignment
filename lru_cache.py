
class Node:
    """A node in the doubly linked list."""

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """Least Recently Used (LRU) Cache."""

    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")

        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail nodes.
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove a node from the linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        """Insert a node immediately after the head."""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node):
        """Mark a node as recently used."""
        self._remove(node)
        self._add_to_front(node)

    def get(self, key):
        """Return the value or -1 if the key is missing."""
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_front(node)

        return node.value

    def put(self, key, value):
        """Insert or update an entry and evict if necessary."""
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        if len(self.cache) > self.capacity:
            # The node before the tail is least recently used.
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]
