palavra = 'paralelepipedo'
letraCerta = ['_'] * len(palavra)
chances = 6

print("Jogo da Forca")
print("Palavra:", " ".join(letraCerta))

while True:
    letra = input(f'Digite uma letra: ').lower()

    if len(letra) != 1:
        print(f'Digite apenas uma letra: ')
        continue


    if letra in palavra:
        for a in range(len(palavra)):
            if palavra[a] == letra:
               letraCerta[a] = letra
        print(f'Acertou!')
        print("Palavra:", " ".join(letraCerta))
    else:
        chances = chances - 1
        print(f'Errou!\n Tentativas restantes: {chances}')
        print("Palavra:", " ".join(letraCerta))


    if chances == 0:
        print(f'Você perdeu!')
        print("Palavra:", " ".join(letraCerta))
        break

    if '_' not in letraCerta:
        break

if '_' not in letraCerta:
    print('Parabéns! Você ganhou o jogo!')
else:
    print(f'A palavra era: {palavra}')