# Вводится строка (число), которая представляет собой целое число в двоичном представлении.
# Необходимо сконвертировать его в десятичное представление.

#    876543210
# a='101001010'
#
# b = 0*1 + 1*2 + 0*4 + 1*8 + 0*16 + 0*32 + 1*64 + 0*128 + 1*256 = 2 + 8 + 64 + 256 = 10 + 320 = 330

a = input()
a_len = len(a)
num = 0

for x in a:
    delta = int(x) * (2 ** (a_len - 1))
    num = num + delta
    a_len = a_len - 1

print(num)