import re


def get_words(text):
    return re.findall(r"[А-Яа-яЇїІіЄєҐґA-Za-z]+", text.lower())


def frequency_dictionary(text):
    words = get_words(text)
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    total_words = len(words)

    if total_words == 0:
        return {}

    frequency = {}

    for word in word_counts:
        frequency[word] = round(
            word_counts[word] / total_words * 100, 2
        )

    return frequency


def shortest_words(text):
    words = get_words(text)

    if len(words) == 0:
        return []

    shortest_length = len(words[0])

    for word in words:
        if len(word) < shortest_length:
            shortest_length = len(word)

    result = []

    for word in words:
        if len(word) == shortest_length and word not in result:
            result.append(word)

    return result


def longest_words(text):
    words = get_words(text)

    if len(words) == 0:
        return []

    longest_length = len(words[0])

    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)

    result = []

    for word in words:
        if len(word) == longest_length and word not in result:
            result.append(word)

    return result


def unique_words_count(text):
    words = get_words(text)
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return len(word_counts)


def words_count(text):
    words = get_words(text)
    return len(words)


def used_letters(text):
    letter_counts = {}

    for char in text.lower():
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    return sorted(letter_counts.keys())


def most_frequent_letter(text):
    letter_counts = {}

    for char in text.lower():
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    if len(letter_counts) == 0:
        return []

    max_count = 0

    for letter in letter_counts:
        if letter_counts[letter] > max_count:
            max_count = letter_counts[letter]

    result = []

    for letter in letter_counts:
        if letter_counts[letter] == max_count:
            result.append(letter)

    return result


with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

      

print("\n Частотний словник у %:")
frequency = frequency_dictionary(text)

for word in frequency:
    print(f"{word}: {frequency[word]}%")


print("\n Найкоротше слово:")
print(shortest_words(text))


print("\n Найдовше слово:")
print(longest_words(text))


print("\n Кількість унікальних слів:")
print(unique_words_count(text))


print("\n Кількість слів:")
print(words_count(text))


print("\n Літери, що використовувалися у тексті:")
print(used_letters(text))


print("\n Літера, що зустрічалася найчастіше:")
print(most_frequent_letter(text))


   

