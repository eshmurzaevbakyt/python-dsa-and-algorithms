def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return f"Found at position {position}"
        position += 1
    return -1

def locate_card1(cards, query):
    for position in range(len(cards)):
        if cards[position] == query:
            return f"Found at position {position}"
        position += 1
    return -1

def locate_card3(cards, query):
    for index, value in enumerate(cards):
        if value == query:
            return f"Found at index {index}"
    return -1
