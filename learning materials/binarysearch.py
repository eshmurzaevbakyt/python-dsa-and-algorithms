def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

# Improved version 1
def locate_card1(cards, query):
    lo, hi = 0, len(cards) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        print(f"lo: {lo}, hi: {hi}, mid: {mid}, value: {cards[mid]}")
        if cards[mid] == query:
            result = mid
            hi = mid - 1
        elif cards[mid] < query:
            hi = mid - 1
        else:
            lo = mid + 1
    return result
cards = [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
query = 6
for x, y in enumerate(cards):
    print(f"Index: {x}, Value: {y}")
location = locate_card(cards, query)
print(location)

# Version for increasing list
def binary_search_leftmost_ascending(arr, target):
    lo, hi = 0, len(arr) - 1
    ans = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            ans = mid
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

# Version using bisect
import bisect

def locate_leftmost(arr, target):
    i = bisect.bisect_left(arr, target)
    if i != len(arr) and arr[i] == target:
        return i
    return -1

