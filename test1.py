import pint, re, signal

while True:
    user_name = input("What's your name?: ")
    if not user_name.isalpha():
        print("Sorry, I didn't understand that! Please retry")
    else:
        print("Hi ", user_name.title())
        break


name = 'engel'
first_name, last_name, full_name = 'engelbert', 'humperdinck', 'engelbert humperdinck'
true_age = 30
false_height, true_height, ideal_height = 180, 167, 170

if true_age >= 30:
    print(name.capitalize() + ' sucks.')
    print('Yes, I said ' + full_name.title() + ' sucks!')
else:
    print(name.capitalize() + ' is the best!')
    print('Yup! you heard it first here...')
    print(full_name.title(), ' really is the best.')
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
    print(false_height.to(ureg.meter))
    print('When he clearly stands below ', end='')
    ureg = pint.UnitRegistry()
    ideal_height = ideal_height * ureg.centimeters
    print(ideal_height.to(ureg.meters))


print("Let's be honest, ", end='')
if true_age < 30:
    true_age = 'young'
    print(name.capitalize(), 'is young ', end='')
    print('and he has so much ahead of him!')
else:
    true_age = 'old'
    print(name.capitalize(), ' is an old hag... ', end='')
    print("and there's not much we can do about it!")


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print(color.RED + str('...') + color.END)

print('What is that?')

print(color.RED + str('...') + color.END)

print('Now hold on...', end='')
print(' Machine! Is ' + name.capitalize() + ' a digit?')
print(color.RED + str('...') + color.END)

if name.isdigit():
    print(color.RED + 'Yes... ', str(name.isdigit()) + color.END)
else:
    name.isdigit()
    print(color.RED + 'No... ', str(name.isdigit()) + color.END)

print('Ok... then I want you to change his name to a funny one and count the changes made')

print(color.RED + str('...') + color.END)
funny_name = re.subn('engel', 'ingle', first_name)
print(color.RED +str(funny_name) + color.END)
