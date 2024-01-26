def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    print(f"--- Begin report of {path}")
    print (f"{word_count}\n")
    for character in character_count:
        if character[0].isalpha():
            print(f"The '{character[0]}' character was found {character[1]} times")
    print("\n--- End report ---")
    


    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    count = len(words)
    return f"{count} words were found in the document"

def get_character_count(text):
    characters = {}
    for character in text.lower():
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    characters = list(characters.items())
    characters.sort(reverse= True, key=lambda a: a[1])
    return characters
    


main()


