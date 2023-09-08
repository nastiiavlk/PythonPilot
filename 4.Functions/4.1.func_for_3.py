# Taken from 3.2 submission

STRING = """  tHis iz your homeWork, copy these Text to variable.




  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.




  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.




  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""
# Constants go in uppercase

# Typing can be used to guide on input/output types. Although, they are not checked in compilation nor execution
def count_whitespaces(initial_string: str) -> int: 
    """
    Function description. Multi-line

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
    """
    return initial_string.count(' ') + initial_string.count('\n')

def normalize_string(initial_string: str) -> str:
    """
    Run homework string normalization

    Parameters:
    argument1 (str): String we want to normalize

    Returns:
    str: String normalized under homework conditions
    """
    lower_string = initial_string.lower().replace('\n', ' ')
    split_string = lower_string.split()
    last_words = []
    
    for i in range(len(split_string)):
        if '.' in split_string[i - 1]:
            split_string[i] = split_string[i].capitalize()
        if split_string[i] == 'iz':
            split_string[i] = 'is'
        if '.' in split_string[i]:
            last_words.append(split_string[i].replace('.', ''))

    last_words[0] = last_words[0].capitalize()
    res = ' '.join(split_string) + ' ' + ' '.join(last_words) + '.'

    return res


# Main code can be executed in file level on Python 3+
final_string = normalize_string(STRING)
print(final_string)

count_of_whitespaces = count_whitespaces(STRING)
print(f'Number of whitespace characters: {count_of_whitespaces}')

# Bonus: Print function __doc__
print(normalize_string.__doc__)

