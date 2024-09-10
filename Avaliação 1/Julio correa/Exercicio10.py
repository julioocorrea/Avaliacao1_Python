class Livro:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"'{self.title}' by {self.author}"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def add_book(self, title, author):
        livro = Livro(title, author)
        self.livros.append(livro)
        print(f"Livro '{title}' adicionado à biblioteca.")

    def list_books(self):
        if self.livros:
            for livro in self.livros:
                print(livro)
        else:
            print("Não há livros na biblioteca.")

    def find_book_by_title(self, title):
        for livro in self.livros:
            if livro.title == title:
                return livro
        return "Livro não encontrado."


# Exemplo de uso
biblioteca = Biblioteca()
biblioteca.add_book("O Senhor dos Anéis", "J.R.R. Tolkien")
biblioteca.add_book("1984", "George Orwell")

biblioteca.list_books()

livro_encontrado = biblioteca.find_book_by_title("1984")
print(livro_encontrado)
