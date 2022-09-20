import pandas

data = pandas.read_csv("alphabets - Copy.csv")

new_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(new_dict)



def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        list = [new_dict[letter] for letter in word]
        # print(list)
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(list)

generate_phonetic()