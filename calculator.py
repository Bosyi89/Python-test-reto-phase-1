name = input('Please, write your name:')
while True:
    operator = input(f'{name.capitalize()} Виберіть операцію з +; -; *; /; //; %; **; round; square of number or/'
                     f'if your want exit please push 0:')
    if operator == '+':
        number1 = (input('Please, write first digit:'))
        number2 = (input('Please, write second digit:'))
        if number1.isdigit and number2.isdigit:
            print(f'{number1} + {number2} = {int(number1) + int(number2)}')
        else:
            print(f'{number1} or {number2} is not digits.')
    elif operator == '-':
        number1 = input('Please, write first digit:')
        number2 = input('Please, write second digit:')
        if number1.isdigit() and number2.isdigit():
            print(f'{number1} - {number2} = {int(number1) - int(number2)}')
        else:
            print(f'{number1} or {number2} is not digits.')
    elif operator == '*':
        number1 = input('Please, write first digit:')
        number2 = input('Please, write second digit:')
        if number1.isdigit() and number2.isdigit():
            print(f'{number1} * {number2} = {int(number1) * int(number2)}')
        else:
            print(f'{number1} or {number2} is not digits.')
    elif operator == '/':
        number1 = input('Please, write first digit:')
        number2 = input('Please, write second digit:')
        if number1.isdigit() and number2.isdigit():
            print(f'{number1} / {number2} = {int(number1) / int(number2)}')
        else:
            print(f'{number1} or {number2} is not digits.')
    elif operator == '//':
        number1 = input('Please, write first digit:')
        number2 = input('Please, write second digit:')
        if number1.isdigit() and number2.isdigit():
            print(f'{number1} // {number2} = {int(number1) // int(number2)}')
        else:
            print(f'{number1} or {number2} is not digits.')
    elif operator == '%':
        number1 = input('Please, write first digit:')
        number2 = input('Please, write second digit:')
        if number1.isdigit() and number2.isdigit():
            print(f'{number1} % {number2} = {int(number1) % int(number2)}')
        else:
            print(f'{number1} or {number2} is not digits.')
    elif operator == '**':
        number1 = input('Please, write your digit:')
        number2 = input('Please, write degree of number:')
        if number1.isdigit() and number2.isdigit():
            print(f'{number1} ** {number2} = {int(number1) ** int(number2)}')
        else:
            print(f'{number1} or {number2} is not digits.')
    elif operator == 'square of number':
        number1 = input('Please, write your digit:')
        if number1.isdigit():
            print(f'{number1} * {number1} = {int(number1) * int(number1)}')
        else:
            print(f'{number1} or {number1} is not digits.')
    elif operator == 'round':
        number1 = float(input('Please, write your digit:'))
        if number1 == number1:
            print(round(number1))
        else:
            print(f'{number1} is not digits.')
    elif operator == '0':
        break
print('Thank you for a spend your time!')
