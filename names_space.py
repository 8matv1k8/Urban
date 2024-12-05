def count_calls():
    global calls
    calls += 1


def string_info(s):
    count_calls()
    return tuple([len(s), s.upper(), s.lower()])


def is_contains(word, string):
    count_calls()
    if word.lower() in [i.lower() for i in string]:
        return True
    else:
        return False


calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
