def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_dict = get_character_count(text)
    char_report = get_char_report(char_dict, book_path, word_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text_in):
    return len(text_in.split())

def get_character_count(text_in):
    lower_text_in = text_in.lower()
    new_dict = {}
    for char in lower_text_in:
        if char not in new_dict:
            new_dict[char] = 1
        else:
            new_dict[char] += 1
    return new_dict

def get_char_report(dict, path, count):
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document")
    print("")

    for i in dict:
        num = dict[i]
        print(f"The '{i}' character was found {num} times")

    print("--- End report ---")

main()
