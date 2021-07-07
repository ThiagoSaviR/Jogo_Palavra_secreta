"""""
jogo: Palavra secreta
"""""

secreta = 'lasanha'
dig = []

while True:
    letra_dig = input('digite uma letra: ')

    if len(letra_dig) > 1:
        print('Ahh, não pode roubar... Digite uma letra por vez.')
        continue
    dig.append(letra_dig)

    if letra_dig in secreta:
        print('Aeee, acertou!!!')
    else:
        print('Ahh, errou...')
        dig.pop()

    letra_em_secreta = ''

    for i in secreta:
        if i in dig:
            letra_em_secreta += i
        else:
            letra_em_secreta += '_'

    print(f'A palavra secreta está assim: {letra_em_secreta}')
    print()

    if letra_em_secreta == secreta:
        print('Uhuul, você ganhou!!!')
        print()
        print(f'A palavra secreta é: {secreta}')
        print()
        break

sair = input('precione ENTER para sair.')
