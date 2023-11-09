import csv
from collections import Counter
from common import FILENAME


def recalculate_words_statistic():
    with open(FILENAME, 'r') as feed_file:
        feed_file_content = feed_file.read()

    if not feed_file_content:
        print("Feed file is empty")
        return

    words = []
    chars = {}
    chars_cnt = 0

    is_word = False
    word = ""
    for char in feed_file_content:
        if char.isalpha():
            chars_cnt += 1
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
            word += char
            if not is_word:
                is_word = True
        else:
            is_word = False
            if word:
                words.append(word.lower())
            word = ""

    words_count = Counter(words)
    with open('Task7_words_count.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='-')
        for key, value in sorted(words_count.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([key, str(value)])

    headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
    data = []

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        data_row = {}
        if letter in chars.keys() or letter.upper() in chars.keys():
            data_row['letter'] = letter
            data_row['count_all'] = chars.get(letter, 0) + chars.get(letter.upper(), 0)
            data_row['count_uppercase'] = chars.get(letter.upper(), 0)
            data_row['percentage'] = 100 * data_row['count_all'] / chars_cnt
            data.append(data_row)

    with open('Task7_letters_count.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
