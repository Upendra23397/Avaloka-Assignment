
def can_attend_all(events):
    """
    Return True if all events can be attended without overlap.

    Adjacent events are allowed.
    Time: O(n log n)
    Space: O(n)
    """
    if not events:
        return True

    sorted_events = sorted(events, key=lambda event: event[0])

    for i in range(1, len(sorted_events)):
        previous_end = sorted_events[i - 1][1]
        current_start = sorted_events[i][0]

        if previous_end > current_start:
            return False

    return True


def min_rooms_required(events):
    """
    Return the minimum number of rooms needed.

    Uses sorted start/end times and two pointers.
    Time: O(n log n)
    Space: O(n)
    """
    if not events:
        return 0

    for start, end in events:
        if start > end:
            raise ValueError("Event start time cannot exceed end time")

    starts = sorted(start for start, end in events)
    ends = sorted(end for start, end in events)

    start_pointer = 0
    end_pointer = 0

    current_rooms = 0
    max_rooms = 0
    n = len(events)

    while start_pointer < n:
        # Release rooms before processing an event
        # that starts at or after the earliest end time.
        if starts[start_pointer] >= ends[end_pointer]:
            current_rooms -= 1
            end_pointer += 1
        else:
            current_rooms += 1
            max_rooms = max(max_rooms, current_rooms)
            start_pointer += 1

    return max_rooms
