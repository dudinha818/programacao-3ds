# Lista de dicionários representando de informatica
produtos = [
    {"nome": "Teclado", "preco": 45.50, "quantidade": 12},
    {"nome": "fone", "preco": 99.90, "quantidade": 1},
    {"nome": "webcam", "preco": 197.91, "quantidade": 1},
    {"nome": "teclado", "preco": 179.50, "quantidade": 1},
    {"nome": "mouse", "preco": 199.50, "quantidade": 1}
] 


# Ordenar os produtos com filtro pelo "preco" de forma crescente
produtos_ordenados_preco = sorted(produtos, key=lambda x: x['preco'])
# Mostra lista crescente com nome e preço do produto
print("Produtos ordenados pelo preço (crescente):")
for produto in produtos_ordenados_preco:
    print(f"{produto['nome']}: ${produto['preco']}")

# Ordenar os produtos com filtro pelo "nome" em ordem alfabética
produtos_ordenados_nome = sorted(produtos, key=lambda x: x['nome'])
# Mostra lista alfabética com nome e preco dos produtos
print("\nProdutos ordenados pelo nome (alfabética):")
for produto in produtos_ordenados_nome:
    print(f"{produto['nome']}: ${produto['preco']}")



# Ordenar os produtos com filtro por "quantidade" de forma decrescente
produtos_ordenados_quantidade = sorted(produtos, key=lambda x: x['quantidade'], reverse=True)
# Mostra lista decrescente com nome e quantidade dos produtos
print("\nProdutos ordenados pela quantidade (decrescente):")
for produto in produtos_ordenados_quantidade:
    print(f"{produto['nome']}: {produto['quantidade']} unidades")
