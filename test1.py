# Mawma this is garbage. I'm lying, it is not. It's just a silly program I'll be coding to practice all the new
# stuff I'll be learning about this fascinating script named Python. As you may already know (lmao I'm writing this
# to myself) I'm self-taught person. I'm self made bitches. An autodidact (that means that I love researching.
# Investigating. Scrutinizing the inter web if you will, in order to acquire new valuable knowledge). I'm a very
# knowledgeable person as you may or may not have noticed by the evident sapience exuded by the accoutrements
# embellishing this delicate paragraph prefacing what could possibly be the proof of and precursor to a new Valentin
# era. Enough dilly dallying. Ladies and gentlemen and everything in between... I present to you THE CODE.

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


