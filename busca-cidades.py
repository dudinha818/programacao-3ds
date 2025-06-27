# Lista pré-definida com nomes de cidades
cidades = [
    "Curitiba", "São Paulo", "Rio de Janeiro", "Belo Horizonte",
    "Salvador", "Fortaleza", "Recife", "Porto Alegre"
]

# Solicita ao usuário a letra ou sequência de caracteres
busca = input("Digite uma letra ou sequência de caracteres para buscar nas cidades: ")

# Converte o critério de busca para minúsculas
busca = busca.lower()

# Filtra as cidades que contêm a sequência (sem diferenciar maiúsculas e minúsculas)
resultado = [cidade for cidade in cidades if busca in cidade.lower()]

# Exibe o resultado
if resultado:
    print("\nCidades encontradas:")
    for cidade in resultado:
        print(f"- {cidade}")
else:
    print("\nNenhuma cidade encontrada com esse critério.")
