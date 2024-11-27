first, second, third = map(int, input('Введите три целых числа: ').split())
if first == second == third:
    print('3')
elif len(set([first, second, third])) == 2:
    print('2')
else:
    print('0')
