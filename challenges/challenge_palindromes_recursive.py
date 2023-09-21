def is_palindrome_recursive(word, low_index, high_index):
    if high_index == -1:
        return False
    if low_index == high_index or low_index > high_index:
        return True
    else:
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return False


if __name__ == "__main__":
    word = "amor"
    print(is_palindrome_recursive(word, 0, len(word) - 1))
