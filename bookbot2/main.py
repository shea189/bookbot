from stats import get_num_words

with open("books/frankenstein.txt") as f:
    text = f.read()

count = get_num_words(text)
print(f"{count} words found in the document")
