# try:
#     file = open('a_file.txt')
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['key'])
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} was not found")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")

height = float(input("Enter height:"))
weight = int(input("Enter weight:"))

if height > 3:
    raise ValueError("HAbibi")


bmi = weight/height**2
print(bmi)