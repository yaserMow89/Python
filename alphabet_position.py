#give the index number of each alphabet char in a string

from string import ascii_lowercase

LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}


def alphabet_position(text):
    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return ' '.join(numbers)


print(alphabet_position("abc"))
