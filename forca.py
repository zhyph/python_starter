def game_forca():
    secret_word = "banana"
    won = False
    tries = 0
    max_tries = 5
    line = ["_"] * len(secret_word)
    guessed_letters = []
    print("Bem vindo ao jogo da forca!")
    print(f"Voce tem {max_tries} tentativas para adivinhar a palavra!")
    print("Tente adivinhar a palavra secreta!")

    while not won and tries < max_tries:
        letter = input("Digite uma letra: ").lower().strip()

        if letter in secret_word and letter not in guessed_letters:
            for i in range(len(secret_word)):
                if letter == secret_word[i]:
                    line[i] = letter

        elif letter in guessed_letters:
            print("Você já tentou essa letra!")

        else:
            tries += 1
            missing_tries = max_tries - tries
            if missing_tries != 0:
                print(f"Você errou e tem mais {missing_tries}!")

        print(" ".join(line))

        if "_" not in line:
            won = True
            print("Parabéns, você ganhou!")

        guessed_letters.append(letter)

    if not won:
        print("Você perdeu!")
        print("A palavra secreta era {}".format(secret_word))


if __name__ == "__main__":
    game_forca()
