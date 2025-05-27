class Biblioteca:
    def __init__(self):
        self.livros = []
        self.lista_livros = []

    def adicionar_livro(self, titulo, autor, ano):
        livro = (titulo, autor, ano)  # Tupla com dados do livro
        self.livros.append(livro)  # Armazenando na coleção de tuplas
        self.lista_livros.append(livro)  # Atualizando a lista automaticamente

    def consultar_colecao(self):
        return self.livros

    def consultar_lista(self):
        return self.lista_livros


# Criando instância da biblioteca
biblioteca = Biblioteca()

# Adicionando livros
biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)
biblioteca.adicionar_livro("1984", "George Orwell", 1949)
biblioteca.adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

# Exibindo os dados armazenados
print("Coleção de livros (tupla):", biblioteca.consultar_colecao())
print("Lista de livros:", biblioteca.consultar_lista())
