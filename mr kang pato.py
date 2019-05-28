arquivo = open('b.txt', 'w')


def inverter(frase):
    inver=' '
    tamanho = len(frase)
    for n in range(tamanho-1, -1, -1):
        inver +=frase[n]

    arquivo.write(inver)
    arquivo.close()
inverter(input('Frase:  '))
