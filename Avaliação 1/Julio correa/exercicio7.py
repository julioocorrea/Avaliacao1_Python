def calcular_soma_quadrados(vetor):
    soma = sum(x**2 for x in vetor)
    print(soma)


def main():
    vetor_A = [1,2,3,4,5,6,7,8,9,10]
    calcular_soma_quadrados(vetor_A)

main()