# def is_anagram_aux(string: str):
#     if string == "":
#         return ""
#     else:
#         letters = list(string.lower())
#         length = len(string)
#         for i in range(length):
#             for letter in range(0, length - i - 1):
#                 if letters[letter] > letters[letter + 1]:
#                     letters[letter], letters[letter + 1] = (
#                         letters[letter + 1],
#                         letters[letter])
#         return "".join(letters)

def is_anagram_aux(string: str):
    letters = list(string.lower())
    new_string = []
    for i in string:
        letter = min(letters)
        new_string.append(letter)
        letters.remove(letter)
    return "".join(new_string)


def is_anagram(first_string, second_string):
    first_text = is_anagram_aux(first_string)
    second_text = is_anagram_aux(second_string)
    if first_text == "" or second_text == "":
        return (first_text, second_text, False)
    return (first_text, second_text, first_text == second_text)


if __name__ == "__main__":
    print(is_anagram("PEDRA", "perda"))

# def is_anagram_aux(string: str):
#     letters = list(string.lower())
#     new_string = []
#     for i in string:
#         letter = min(letters)
#         new_string.append(letter)
#         letters.remove(letter)
#     return "".join(new_string)


# def is_anagram(first_string, second_string):
#     first_text = is_anagram_aux(first_string)
#     second_text = is_anagram_aux(second_string)
#     if first_text == "" or second_text == "":
#         return (first_text, second_text, False)
#     return (first_text, second_text, first_text == second_text)


# if __name__ == "__main__":
#     print(is_anagram("PEDRA", "perda"))
