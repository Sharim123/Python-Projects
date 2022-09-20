# new_list = [new_item for (#every#) item in list]

numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)



name = 'Sharim'
letters_list = []
new_list = [letter for letter in name]
print(new_list)


range_list = [n*2 for n in range(1,5)]
print(range_list)


#new_list = [new_item for item in list if test]

names = ['alex', 'beth', 'dave', 'caroline', 'freddie', 'eleanor']

short_names = [name for name in names if len(name) < 5]
print(short_names)

big_names = [name.upper() for name in names if len(name) > 5]
print(big_names)