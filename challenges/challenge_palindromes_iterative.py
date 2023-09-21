def is_palindrome_iterative(word: str):
    count = 0
    regresso = len(word) - 1
    isValid = False
    while regresso >= 0:
        if word[regresso] != word[count]:
            return False
        regresso -= 1
        count += 1
        isValid = True
    return isValid


print(is_palindrome_iterative("I"))
print(is_palindrome_iterative("GG"))
print(is_palindrome_iterative("ANA"))
print(is_palindrome_iterative("ESSE"))
print(is_palindrome_iterative("SOCOS"))
print(is_palindrome_iterative("REVIVER"))
print(is_palindrome_iterative("AGUA"))
print(is_palindrome_iterative(""))
