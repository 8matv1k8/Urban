first, second, third = map(int, input('Введите три целых числа: ').split())
if first == second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')
