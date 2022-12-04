

"""
    4) Пользователь вводит строку из нескольких слов, разделённых пробелами. 
    Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
    Если в слово длинное, выводить только первые 10 букв в слове
"""

custom_string = input("введите строку из нескольких слов: ")
list_words = []
start_number = 1
for element in range(custom_string.count(' ') + 1):
    list_words = custom_string.split()
    if len(str(list_words)) <= 10:
        print(f" {start_number} {list_words [element]}")
        start_number += 1
    else:
        print(f" {start_number} {list_words [element] [0:10]}")
        start_number += 1