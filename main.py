def read_book(file):
    with open(file) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

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
    print("Reading Frankenstein")
    book = 'books/frankenstein.txt'
    text = read_book(book)
    num_words = get_num_words(text)
    letters = get_num_letters(text)
    print(f"Report of {book}")
    print(f"There are {num_words} in the document")
    letter_list = []
    for c in letters:
        if c.isalpha():
            letter_list.append((c, letters[c]))
    letter_list.sort()
    for l in letter_list:
        print(f"The letter {l[0]} was used {l[1]} times in {book}.")
