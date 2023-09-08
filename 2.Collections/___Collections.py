import random
import string

#Create a list containing from 2 to 10 dictionaries.
list_of_dicts = []
num_of_dicts = random.randint(2, 10)

for i in range(num_of_dicts):
    num_of_keys = random.randint(1, 5)  #range number of elements in the dictionary
    new_dict = {}

    # Dictionary elements - random numbers from 0 to 30 and rundom letters
    for j in range(num_of_keys):
        key =random.choice(string.ascii_letters)  #get random letters both upper lower case,can be replaced by ascii_uppercase or ascii_lowercase
        value = random.randint(0, 30)
        new_dict[key] = value

    list_of_dicts.append(new_dict)

print("List of dictionaries:")
for index, dicts  in enumerate(list_of_dicts, start=1): # use enumerate object to list all disctionaries and elements,returns a tuple with the counter and value
    print(f"Dict {index}: {dicts}")

# Create a combined dictionary from 2 generated dictionaries
combined_dict = {}

for index, dicts in enumerate(list_of_dicts, start=1): 
    for key, value in dicts.items():
        if key in combined_dict:
            if value > combined_dict[key]:  # Compare key, take bigger/max value and rename key
                combined_dict[f"{key}_{index}"] = value
                del combined_dict[key]
        else:
            combined_dict[key] = value  # If key peresent in only one dict, take it as is.

print("\nCombined dict:")
print(combined_dict)
