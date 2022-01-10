import pint
name = 'Engel'
first_name, last_name, full_name = 'Engelbert', 'Humperdinck', 'Engelbert Humperdinck'
true_age = 30
false_height, true_height, ideal_height = 180, 167, 170

if true_age >= 30:
    print(name + ' sucks.')
    print('Yes, I said '+full_name+' sucks!')
else:
    print(name + ' is the best!')
    print('Yup! you heard it first here...')
print("You know, he is ", end='')
ureg = pint.UnitRegistry()
true_height = int(true_height) * ureg.centimeters
print(true_height.to(ureg.meters), end='')
print(" tall...")

if true_age < 30:
    print("But everytime he enters a room, he carries himself as the most utterly confident person ever")
else:
    print("But he always says he stands more than ", end='')
    ureg = pint.UnitRegistry()
    false_height = false_height * ureg.centimeters
    print(false_height.to(ureg.meters))
    print('When he clearly stands below ', end='')
    ureg = pint.UnitRegistry()
    ideal_height = ideal_height * ureg.centimeters
    print(ideal_height.to(ureg.meters))

print("Let's be honest, ", end='')
if true_age < 30:
    true_age = 'young'
    print('Engel is young ', end='')
    print('and he has so much ahead of him!')
else:
    true_age = 'old'
    print('Engel is an old hag... ', end='')
    print("and there's not much we can do about it!")
print('-' * 80)


