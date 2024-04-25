def combine_anagrams(words_array):
    # метод принимает массив слов и разбивает их в группы по анаграммам
    anagrams = {}
    for word in words_array:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"]))  # => [ ["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"]]