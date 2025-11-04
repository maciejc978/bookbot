def get_num_words(book_text: str) -> int:
    """
    Count the number of words in the given text.
    """
    words = book_text.split()
    return len(words)


def get_character_count(book_text: str) -> dict[str, int]:
    """
    Count how many times each character appears in the text.
    Converts characters to lowercase to avoid duplicates.
    """
    book_text = book_text.lower()
    char_count = {}

    for char in book_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_character_counts(char_dict: dict[str, int]) -> list[dict[str, int]]:
    """
    Convert a dictionary of character counts into a sorted list of dictionaries.
    Only include alphabetical characters. Sort from highest to lowest count.
    """
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():  # include only alphabetic characters
            sorted_list.append({"char": char, "num": count})

    def sort_on(dict_item):
        return dict_item["num"]

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

