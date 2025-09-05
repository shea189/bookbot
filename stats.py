
def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text: str) -> dict:
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_chatacters(char_dict: dict) -> list:
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    def sort_on(item):
        return item["num"]
    
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

