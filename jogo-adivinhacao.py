import random  # Importa o módulo 'random', que permite gerar números aleatórios.

# Gera um número aleatório entre 1 e 10, que será o número secreto a ser adivinhado pelo jogador.
numero_secreto = random.randint(1, 10)

# Variável que armazena o número de tentativas já realizadas pelo jogador.
tentativas = 0

# Define o número máximo de tentativas permitidas antes de encerrar o jogo.
max_tentativas = 5

# Exibe uma mensagem inicial para dar boas-vindas ao jogador e explicar o objetivo do jogo.
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")

# Estrutura de repetição que mantém o jogo ativo enquanto o jogador ainda tem tentativas restantes.
while tentativas < max_tentativas:
    # Solicita ao jogador que digite um número como seu palpite e converte a entrada para inteiro.
    palpite = int(input("Digite seu palpite: "))

    # Incrementa o número de tentativas a cada palpite realizado.
    tentativas += 1

    # Verifica se o palpite do jogador está correto.
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break  # Encerra o jogo caso o jogador acerte o número.

    # Caso o palpite seja menor que o número secreto, orienta o jogador a tentar um número maior.
    elif palpite < numero_secreto:
        print("Quase lá! Tente um número maior.")

    # Caso contrário, se o palpite for maior que o número secreto, orienta o jogador a tentar um número menor.
    else:
        print("Quase lá! Tente um número menor.")

    # Se ainda houver tentativas restantes, informa ao jogador quantas ainda pode fazer.
    if tentativas < max_tentativas:
        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")

# Caso o jogador não tenha acertado dentro do número máximo de tentativas, exibe uma mensagem de encerramento.
else:
    print(f"Infelizmente, você não acertou. O número era {numero_secreto}.")
    print("Fim do jogo!")
