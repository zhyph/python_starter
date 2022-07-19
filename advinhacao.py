def get_input_number(message):
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print("Tem que ser um numero!")


def game_advinhacao():
    import random

    numero_secreto = random.randint(1, 10)
    print("Bem vindo ao jogo de adivinhação.")
    num = get_input_number("Digite: ")
    tries = 0

    while num != numero_secreto and tries < 4:
        if num > numero_secreto:
            message = "O número é menor!"
        else:
            message = "O número é maior!"

        print(message)
        num = get_input_number("Voce tem mais {} tentativas, tente novamente: ".format(5 - (tries + 1)))

        tries += 1

    if num == numero_secreto:
        print("Parabéns, você acertou!")

    if tries == 4:
        print("Você errou, o número secreto era {}".format(numero_secreto))

    user_response = input("Deseja jogar novamente? (S/N) ")
    if user_response == "S":
        game_advinhacao()


if __name__ == "__main__":
    game_advinhacao()
