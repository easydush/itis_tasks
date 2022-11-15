# Вводится массив размера n целых положительных чисел.
# Проверить, что в массиве существуют 3 числа подряд,
# в которых количество нечетных цифр больше четных.
# При каждом результате выводить соответствующее сообщение.

n = int(input())

a = []

for i in range(n):
    item = int(input())
    a.append(item)

def check(num):
    odd = 0 # нечетное
    even = 0 # четное

    current_num = num

    if current_num % 2 == 0:
        even += 1
    else:
        odd += 1

    current_num = current_num // 10

    while current_num > 0:
        if current_num % 2 == 0:
            even += 1
        else:
            odd += 1

        current_num = current_num // 10

    return odd > even

current_result = 0

for elem in a:
    if check(elem):
        current_result += 1
        if current_result == 3:
            print('Условие соблюдено')
            exit(1)
    else:
        current_result = 0
print('Условие не соблюдено')
