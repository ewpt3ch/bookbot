import sys
from stats import get_num_words

def read_book(file):
    with open(file) as f:
        return f.read()

def get_num_letters(text):
    letter_freq = {}
    for c in text:
        c = c.lower()
        if c in letter_freq:
            letter_freq[c] += 1
        else:
            letter_freq[c] = 1
    return letter_freq


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book = sys.argv[1]
    text = read_book(book)
    num_words = get_num_words(text)
    letters = get_num_letters(text)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print(f"----------- Word Count ----------")
    print(f"There are {num_words} words found in the document")
    print(f"--------- Character Count -------")
    letter_list = []
    for c in letters:
        if c.isalpha():
            letter_list.append((c, letters[c]))
    letter_list.sort()
    for l in letter_list:
        print(f"{l[0]}: {l[1]}")
    print(f"============= END ===============")
