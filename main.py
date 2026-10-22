
from lru_cache import LRUCache
from event_scheduler import can_attend_all, min_rooms_required


def test_lru_cache():
    cache = LRUCache(2)

    cache.put(1, 100)
    cache.put(2, 200)

    assert cache.get(1) == 100

    cache.put(3, 300)  # Evicts key 2

    assert cache.get(2) == -1
    assert cache.get(3) == 300

    cache.put(4, 400)  # Evicts key 1

    assert cache.get(1) == -1
    assert cache.get(3) == 300
    assert cache.get(4) == 400

    # Updating an existing key.
    cache.put(4, 450)
    assert cache.get(4) == 450

    # Zero-capacity cache.
    empty_cache = LRUCache(0)
    empty_cache.put(1, 100)
    assert empty_cache.get(1) == -1

    print("LRU Cache: All tests passed!")


def test_event_scheduler():
    events_1 = [(9, 10), (10, 11), (11, 12)]

    assert can_attend_all(events_1) is True
    assert min_rooms_required(events_1) == 1

    events_2 = [(9, 11), (10, 12), (10, 13), (13, 14)]

    assert can_attend_all(events_2) is False
    assert min_rooms_required(events_2) == 3

    # Empty input.
    assert can_attend_all([]) is True
    assert min_rooms_required([]) == 0

    # All events happen simultaneously.
    events_3 = [(9, 12), (9, 12), (9, 12)]
    assert min_rooms_required(events_3) == 3

    # Invalid intervals.
    try:
        min_rooms_required([(12, 9)])
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid event should raise ValueError")

    print("Event Scheduler: All tests passed!")


def main():
    test_lru_cache()
    test_event_scheduler()

    events = [(9, 10), (10, 11), (11, 12)]

    print("\nExample scheduler results:")
    print("Events:", events)
    print("Can attend all:", can_attend_all(events))
    print("Minimum rooms:", min_rooms_required(events))


if __name__ == "__main__":
    main()
