
# Data Structures & Systems Design Assignment

Python solutions for a Software Engineering Intern assessment.

## Overview

This repository contains implementations of:

1. **LRU Cache** using a hash map and doubly linked list.
2. **Event Scheduler** to detect meeting conflicts and calculate the minimum number of meeting rooms.

The project also includes test cases, complexity analysis, and system-design considerations.

## Project Structure

```text
DSA-Systems-Design-Assignment/
├── lru_cache.py
├── event_scheduler.py
├── main.py
├── README.md
└── .gitignore
```

## Requirements

- Python 3.9 or later
- No external dependencies

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/DSA-Systems-Design-Assignment.git
cd DSA-Systems-Design-Assignment
```

Run the test examples:

```bash
python main.py
```

## Problem 1: LRU Cache

### Approach

The LRU Cache combines two data structures:

- **Hash map:** Maps keys to linked-list nodes for average O(1) lookup.
- **Doubly linked list:** Maintains recency order and supports O(1) insertion, removal, and reordering.

The most recently used entry is stored near the head, while the least recently used entry is stored near the tail.

### Operations

- `get(key)`: Returns the value if present; otherwise returns `-1`.
- `put(key, value)`: Inserts or updates an entry and evicts the least recently used entry when necessary.

### Complexity

| Operation | Time Complexity |
|---|---|
| Initialization | O(1) |
| get | O(1) average |
| put | O(1) average |

Total cache storage: O(C), where C is the cache capacity.

## Problem 2: Event Scheduler

### can_attend_all(events)

Sorts events by start time and checks adjacent intervals for overlap.

If the previous event ends after the next event starts, the function returns `False`.

Adjacent meetings are allowed because an end time equal to the next start time is not an overlap.

### min_rooms_required(events)

Sorts start and end times independently and processes them with two pointers.

A room is released when a meeting ends at or before the next meeting's start time. The maximum number of simultaneously active meetings determines the minimum number of rooms required.

### Complexity

| Function | Time | Auxiliary Space |
|---|---|---|
| can_attend_all | O(n log n) | O(n) |
| min_rooms_required | O(n log n) | O(n) |

## Design Discussion

### Why combine a hash map and doubly linked list?

A hash map offers fast key lookup but does not maintain recency order. A linked list maintains the order but cannot find an arbitrary key quickly. Combining them provides average O(1) cache operations.

### How can rooms be assigned specific names?

Sort meetings by start time and use two min-heaps: one for occupied rooms ordered by end time, and another for available room IDs. Release rooms when meetings finish, reuse them where possible, and assign a new room only when necessary.

### How can the cache become thread-safe?

Protect each complete `get` and `put` operation with a lock. The lock must also cover `get`, because reading an entry changes its recency order. For distributed systems, additional coordination may be required.

## Edge Cases Tested

- Empty event list
- Adjacent meetings
- Overlapping meetings
- Multiple simultaneous meetings
- LRU eviction
- Updating an existing cache key
- Zero-capacity cache
- Invalid event intervals

## Author

Upendra Chauhan

Software Engineering | AI/ML | Data Structures & Algorithms
