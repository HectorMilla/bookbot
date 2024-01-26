def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_word_count(text)
    print(text)
    print (word_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    count = len(words)
    return count
main()


