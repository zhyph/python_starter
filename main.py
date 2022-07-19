def choose():
    print('Escolha seu jogo!')
    print('(1) Advinhação (2) Forca')

    jogo = int(input('Digite o número do jogo que deseja jogar: '))

    if jogo == 1:
        from advinhacao import game_advinhacao

        game_advinhacao()
    elif jogo == 2:
        from forca import game_forca

        game_forca()


if __name__ == '__main__':
    choose()
    print('Obrigado por jogar!')
    input('Pressione Enter para sair...')
    exit()
