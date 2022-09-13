# Дан отсортированный список. Вводится число x, необходимо найти номер элемента x в списке.
a = []
a_input = input()
for elem in a_input.split(' '):
    a.append(int(elem))

x = int(input())

result = -1

for index in range(len(a)):
    if a[index] == x:
        result = index

print(result)