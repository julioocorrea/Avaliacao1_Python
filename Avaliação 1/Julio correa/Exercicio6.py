CPF = input('Digite seu CPF:')

CPF = CPF.replace('.', '')
CPF = CPF.replace('-', '')

digitos = [int(d) for d in CPF]

soma = sum(digitos)

if soma % 2 == 0:
    print('Soma:' + str(soma) +  ' E o numero é par')
else:
    print('Soma:' + str(soma) +  ' E o numero é impar')

print(soma)