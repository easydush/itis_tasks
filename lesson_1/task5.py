
a = []
a_input = input()
for elem in a_input.split(' '):
    a.append(int(elem))


total_count = 0
for x in a:
    b = x

    counter = 0

    while b > 0:

        if b % 2 == 0:
            counter = counter + 1

        b = b // 10
    if counter == 2:
        total_count = total_count + 1
if total_count <= 3:
    print('yes!')
else:
    print('no :(')