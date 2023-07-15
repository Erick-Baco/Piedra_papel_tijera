import random

options = ('piedra','papel','tijera')
user = 0
computer = 0

print('\n\t PIEDRA PAPEL O TIJERA ')


round = 0
while not user < 2 or computer < 2:
    round += 1
    print('\t *********************')
    print(f'\t ROUND {round}')
    print('\t *********************')

    print('\t MARCADOR')
    print(f' User: {user}')
    print(f' Computer: {computer}')
    print('\t *********************')

    user_option = input('piedra, papel o tijera: ').lower()
    computer_option = random.choice(options)

    if not user_option in options:
        print('opcion no valida')
    else:
        print(f'Computer option {computer_option}')

        if user_option == computer_option:
            print('empate')
        elif user_option == 'piedra':
            if computer_option == 'tijera':
                print('gana piedra')
                print('gana user')
                user += 1
            else:
                print('papel gana a piedra')
                print('computer gana')
                computer += 1

        elif user_option == 'papel':
            if computer_option == 'tijera':
                print('gana tijera')
                print('gana computer')
                computer += 1
            else:
                print('papel gana a piedra')
                print('user gana')
                user += 1
        elif user_option == 'tijera':
            if computer_option == 'piedra':
                print('gana piedra')
                print('gana computer')
                computer += 1
            else:
                print('tijera gana a papel')
                print('user gana')
                user += 1


print('\t *********************')
print('\t MARCADOR')
print(f' User: {user}')
print(f' Computer: {computer}')
print('\t *********************')

if user > computer:
    print('user gana')
else:
    print('computer gana')