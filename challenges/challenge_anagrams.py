def is_anagram(first_string, second_string):
    array = list('abcdefghijklmnopqrstuvwxyz')
    first_letters = list(first_string.lower())
    second_letters = list(second_string.lower())
    first_text = "".join([i * first_letters.count(i)
                          for i in array if i in first_letters])
    second_text = "".join([i * second_letters.count(i)
                           for i in array if i in second_letters])
    if first_text == "" or second_text == "":
        return (first_text, second_text, False)
    return (first_text, second_text, first_text == second_text)


if __name__ == "__main__":
    print(is_anagram("PEDRA", "perda"))

# CÓDIGO FUNCIONANDO, PORÉM É O(N²)
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
