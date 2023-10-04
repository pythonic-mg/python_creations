from urllib.request import urlretrieve
import re

url = "https://www.gutenberg.org/ebooks/71779.txt.utf-8"

book_txt = "book_txt.txt"

urlretrieve(url, book_txt)

with open(book_txt, "r", encoding="utf8") as fileref:
    book = fileref.readlines()

# remove beginning commentary
book[:26] = []

# remove ending commentary
book[10885:] = []

list_of_lists_of_words = []

for line in book:
    list_of_lists_of_words.append(line.split())

print(list_of_lists_of_words[:5])

book_dictionary = {}

for lst in list_of_lists_of_words:
    if lst == []:
        pass
    else:
        for word in lst:
            word = re.sub(r'[^\w]', "", word)
            word = word.lower()
            book_dictionary[word] = 0

for lst in list_of_lists_of_words:
    if lst == []:
        del lst
    else:
        for word in book_dictionary:
            if book_dictionary[word]:
              book_dictionary[word] = book_dictionary[word] + 1

print(book_dictionary["flowers"])

with open("book_dictonary", "w") as fileref:
    for thing in book_dictionary:
       fileref.write(f"{thing}")








