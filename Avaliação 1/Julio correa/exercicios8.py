def calcularMedia(notas, divisor):
    somaDasNotas = sum(notas)
    media = somaDasNotas / divisor
    return media;

def main():
    NOTA1 = input('Digite a nota 1: ')
    NOTA2 = input('Digite a nota 2: ')
    NOTA3 = input('Digite a nota 3: ')
    NOTA4 = input('Digite a nota 4: ')

    listaNotas = [int(NOTA1), int(NOTA2), int(NOTA3), int(NOTA4)]

    media = calcularMedia(listaNotas, 4)

    print('Media: ' + str(media))

    if media >= 7: 
        print('Aprovado')
    else :
        NOTAFINAL = input('Digite da prova final: ')
        listaNotas.append(int(NOTAFINAL))
        media = calcularMedia(listaNotas, 5)
        print('Media: ' + str(media))
        
        if media >= 5: 
            print('Aprovado')
        else:
            print('Reprovado')

main()