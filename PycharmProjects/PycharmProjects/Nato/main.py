student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

data = pandas.read_csv("alphabets.csv")
#print(data.to_dict())

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
new_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(new_dict)




# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()



list = [new_dict[letter] for letter in word]
print(list)
