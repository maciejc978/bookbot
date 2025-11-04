import sys
from stats import get_num_words, get_character_count, sort_character_counts


def get_book_text(path):
    """Opens a text file and returns its content as a string."""
    with open(path, 'r', encoding='utf-8') as file:
        contents = file.read()
    return contents


def main():
    """Analyzes a book file provided via command-line argument and prints a report."""
    # Check that the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    # Read and analyze the book
    try:
        book_content = get_book_text(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'.")
        sys.exit(1)

    num_words = get_num_words(book_content)
    char_counts = get_character_count(book_content)
    sorted_chars = sort_character_counts(char_counts)

    # Word count section
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character count section
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
