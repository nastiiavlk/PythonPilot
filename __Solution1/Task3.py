input_string = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

lowercase_string = input_string.lower()
result = ""

# Handle Capitalization
capitalize_flag = True  # firs symbol should be capital
for char in lowercase_string:
    if char.isalpha() and capitalize_flag:
        char = char.capitalize()
        capitalize_flag = False
    if char in ":\t.\n":
        capitalize_flag = True
    result += char

# Extra sentence from last words of each sentences
splitted = result.split()
extra_sentence = ""
for word in splitted:
    if word.endswith('.'):
        extra_sentence += word.replace(".", "") + " "
extra_sentence = extra_sentence[:-1].capitalize() + "."  # First letter is capital and end symbol is dot

# Insert extra sentence after the "paragraph." (len("paragraph.") = 10)
result = result[:result.find("paragraph.") + 10] + " " + extra_sentence + result[result.find("paragraph.") + 10:]

# fixing iz to is when it's a single word
result = result.replace(" iz ", " is ")

print(result)

# number of whitespaces
import re

whitespace_count = len(re.findall(r'\s', input_string))
print("Number of whitespaces in initial string: ", whitespace_count)
