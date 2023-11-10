from random import randrange

KEY_STRING = 'abcdefghijklmnopqrstuvwxxyz'


def generate_dict():
    result_dict = {}
    key_string = KEY_STRING
    string_len = len(key_string)
    dict_len = randrange(string_len) + 1
    for _ in range(dict_len):
        key = key_string[randrange(string_len)]
        value = randrange(100)
        result_dict[key] = value
        key_string.replace(key, "")
        string_len = len(key_string)
    return result_dict


# 1. create a list of random number of dicts (from 2 to 10)
dicts_number = randrange(start=2, stop=11, step=1)
print(dicts_number)
dicts_list = [generate_dict() for i in range(dicts_number)]
print(dicts_list)

# 2. create commond dictionary with _i postfix for number of dictionary with key containig max value from the dict list and max value
merged_dict = {}
for letter in KEY_STRING:
    postfix = ""
    counter = 0
    max_value = -1
    for i in range(dicts_number):
        try:
            curr_value = dicts_list[i][letter]
        except:
            curr_value = None
        if curr_value:
            counter += 1
            if counter == 1:
                max_value = curr_value
                postfix = '_' + str(i + 1)
            elif max_value < curr_value:
                max_value = curr_value
                postfix = '_' + str(i + 1)
    if max_value != -1:
        if counter == 1:
            merged_dict[letter] = max_value
        elif counter > 1:
            merged_dict[letter + postfix] = max_value

print(merged_dict)
