my_dict = {"Иван": 1912, "Петя": 1290, "Jimmy": 2023}
print('Dict', my_dict)
print('Existing value:', my_dict['Иван'], my_dict.get('Kaneki', 'Not existing value:'))
my_dict.update({'kaleion@gmail.com': '49293faWj34',
                'Дерево': 'Пихта'})
print(f'Deleted value: {my_dict["Петя"]}\nModified dictionary: {my_dict}')
del my_dict['Петя']
