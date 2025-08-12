class CatalogoFilmes:
    def __init__(self):
        self.filmes = []

    def adicionar_filme(self, titulo, genero, ano):
        self.filmes.append({"titulo": titulo, "genero": genero, "ano": ano})

    def pesquisar_filme(self, genero):
        resultados = [filme for filme in self.filmes if filme["genero"] == genero]
        return resultados


catalogo = CatalogoFilmes()

catalogo.adicionar_filme("Filme 1", "Ação", 2020)
catalogo.adicionar_filme("Filme 2", "Comédia", 2018)
catalogo.adicionar_filme("Filme 3", "Drama", 2021)
catalogo.adicionar_filme("Filme 4", "Ação", 2019)

genero_pesquisado = "Drama"
resultados = catalogo.pesquisar_filme(genero_pesquisado)

print(f"Filmes do gênero '{genero_pesquisado}':")
for filme in resultados:
    print(f"Título: {filme['titulo']}, Ano: {filme['ano']}")