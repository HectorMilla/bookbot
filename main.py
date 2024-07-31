def main():
   book_path = "books/frankenstein.txt"
   text = get_book_text(book_path)
   wordcount = get_word_count
   char_list = get_char_count(text)
   print(char_list)
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
    
    
main()