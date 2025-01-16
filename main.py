def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = get_word_count(text)
    char_list = get_char_count(text)
    sorted_char_list = get_sorted_char_list(char_list)
    print(f"-- Begin report of {book_path} ---")
    print(f"{wordcount} words foind in the document/n/n")
    for char in sorted_char_list:
        if not char["char"].isalpha():
            continue
        else:
            print(f"The '{char['char']}' character was found {char['num']} times")
    print("Thank you for using bookbot!")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    text = text.split()
    return len(text)


def get_char_count(text):
    text = text.lower()
    char_list = {}
    for char in text:
        if char in char_list:
            char_list[char] += 1
        else:
            char_list[char] = 1
    return char_list


def sort_on(d):
    return d["num"]


def get_sorted_char_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
