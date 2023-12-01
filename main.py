import re

input_string = input("Введите строку: ")

digits = re.findall(r'\d', input_string)

print("Найденные цифры:", ''.join(digits))