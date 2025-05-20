# Solicita ao usuário um número inteiro positivo n
n = int(input("Digite um número inteiro positivo: "))

# Inicializa uma lista vazia
numeros = []

# Lê n números inteiros e os adiciona à lista
for _ in range(n):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)

# Solicita ao usuário um número inteiro x
x = int(input("Digite um número para verificar se está na lista: "))

# Verifica se x pertence à lista
if x in numeros:
    print(f"O número {x} está na lista.")
else:
    print(f"O número {x} não está na lista.")
