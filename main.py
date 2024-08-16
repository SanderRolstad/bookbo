def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num = get_num(text)
    letters_dict = str_to_int(text)
    sorted_list = sort(letters_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num} words found in the document")
    print()
    for char, count in sorted_list:
        print(f"The '{char}' character was found {count} times")
    print()
    print("--- End report ---")


def book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_num(text):
    words = text.split()
    return len(words)

def str_to_int(text):
    letters = {}
    lower_string = text.lower()
    for char in lower_string:
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters

def sort(letters):
    return sorted(letters.items(), key=lambda item: item[1], reverse=True)


main()