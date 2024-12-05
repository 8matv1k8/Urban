def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [1, 'no', False]
values_list_2 = ['no', False]
values_dict = {'a': False, 'b': 'cesium', 'c': 0}
print_params(*values_list_2, 42)
