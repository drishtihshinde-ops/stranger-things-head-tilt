characters = {
    "Eleven": 0,
    "Mike": 0,
    "Dustin": 0,
    "Will": 0,
    "Max": 0
}

def add_score(chars):
    for char in chars:
        if char in characters:
            characters[char] += 1

def get_result():
    max_score = max(characters.values())
    result = [char for char, score in characters.items() if score == max_score]
    return result[0]  # pick first if tie
