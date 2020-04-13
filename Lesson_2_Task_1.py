name = 'Alex'
day = 'monday'

print('Good day', name + '!', day, 'is a perfect day to learn some python.')

print()

print('Good day'.upper(), name.center(12, '-'),'!'.upper(), day.center(12, '*'), 'is a perfect day to learn some python.'.upper())

print()

print(('Good day ' + name) + '! ' + (day + ' is a perfect day to learn some python.'))

print()

print(f'Good day {name}! {day} is a perfect day to learn some python.')

print()

print(f'Good day {name}! {day} is a perfect day to learn some python.'.swapcase())

print()

print(f'Good day {name}! {day} is a perfect day to learn some python.'.title())