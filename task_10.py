def count_words(text):
    # метод возращает словарь со статистикой частоты употребления входящих в неё слов
    for char in text:
        if char in ",.?*!`@#$%^&*()-~'":
            text = text.replace(char, '')
    text = [item.strip() for item in text.lower().split()]
    words = {}
    for item in text:
        if item in words:
            words[item] += 1
        else:
            words[item] = 1
    return words


print(count_words("A man, a plan, a canal -- Panama")) # => {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}
print(count_words("Doo bee doo bee doo")) # => {"doo": 3, "bee": 2}