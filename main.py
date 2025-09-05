import sys
from stats import get_num_words
from stats import count_characters, sort_chatacters


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

with open(book_path, "r") as f:
    text = f.read()

count = get_num_words(text)
print(f"Found {count} total words")


char_counts = count_characters(text)
sorted_chars = sort_chatacters(char_counts)

for item in sorted_chars:
    print(f"{item['char']}: {item['num']}")


