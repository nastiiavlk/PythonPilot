def capitalize_string(string: str) -> str:
    lowercase_string = string.lower()
    result_string = ""
    capitalize_flag = True  # firs symbol should be capital
    for char in lowercase_string:
        if char.isalpha() and capitalize_flag:
            char = char.capitalize()
            capitalize_flag = False
        if char in ":\t.\n!?":
            capitalize_flag = True
        result_string += char
    return result_string
