def is_num_multiple(first, second, num):
    if num % (first + second) == 0:
        return True
    else:
        return False


# num = int(input('Введите число первой вставки (от 3 до 20): '))

for num in range(3, 21):
    result = []
    for i in range(1, 20):
        for j in range(1, 20):
            if is_num_multiple(i, j, num) and [j, i] not in result and i != j:
                result.append([i, j])

    print(num, end=' - ')
    for i in result:
        print(''.join(list(map(str, i))), end='')
    print()
