def is_palindrome(text):
    # метод для определения является ли параметр палиндромом
    text = str(text).lower()
    for char in text:
        if char in " ,.?*!`@#$%^&*()-~'":
            text = text.replace(char, '')
    if text == text[::-1]:
        return True
    return False


print(is_palindrome("A man, a plan, a canal -- Panama")) # => True
print(is_palindrome("Madam, I'm Adam!")) # => True
print(is_palindrome(333)) # => True
print(is_palindrome(None)) # => False
print(is_palindrome("Abracadabra")) # => False