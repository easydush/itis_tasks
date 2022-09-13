# Вводится текст (строка). Составить статистику, сколько раз упоминается каждая буква алфавита (регистр не учитывать).
a = {}

text = input('Введите текст...\n')

for elem in text:
    lowered_elem = elem.lower()
    a[lowered_elem] = a.get(lowered_elem, 0) + 1

print(a)