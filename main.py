def main():
   book_path = "books/frankenstein.txt"
   text = get_book_text(book_path)
   wordcount = get_word_count
   print(text, f"{wordcount} words found in this document")
def get_book_text(path):
   with open(path) as f:
      return f.read()

def get_word_count(text):
       text = text.split()
       return len(text)
  
    
main()