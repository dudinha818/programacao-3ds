# a) Lista com pelo menos 8 nomes
nomes = ["Carlos", "Fernanda", "Lucas", "Amanda", "Roberta", "Bruno", "Sérgio", "Larissa"]

# b) Solicita ao usuário uma letra ou sequência
sequencia = input("Digite uma letra ou sequência para buscar nos nomes: ").lower()

# c) Filtra nomes que contêm a sequência (sem diferenciar maiúsculas/minúsculas)
resultados = [nome for nome in nomes if sequencia in nome.lower()]

# d) Exibe os resultados ou mensagem de nenhum nome encontrado
if resultados:
    print("Nomes encontrados:")
    for nome in resultados:
        print("-", nome)
else:
    print("Nenhum nome contém a sequência digitada.")
