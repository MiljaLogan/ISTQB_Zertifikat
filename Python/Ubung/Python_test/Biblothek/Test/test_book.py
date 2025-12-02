


from book import Book

def test_multiple_books_are_independent():
     # Erstellen von zwei unabhängigen Book-Objekten
    book1 = Book("Buch 1", "ISBN_1", "Author1")
    book2 = Book("Buch 2", "ISBN_2", "Author2")

    # Ändern eines Attributs von book1
    book1.title = "Neuer Titel für Buch 1"

    # Überprüfen, ob nur book1 geändert wurde
    assert book1.title == "Neuer Titel für Buch 1", "Der Titel von Buch 1 sollte geändert sein"
    assert book2.title == "Buch 2", "Der Titel von Buch 2 sollte unverändert sein"

    # Überprüfen, ob andere Attribute von book1 unverändert sind
    assert book1.isbn == "ISBN_1", "Die ISBN von Buch 1 sollte unverändert sein"
    assert book1.author == "Author1", "Der Autor von Buch 1 sollte unverändert sein"

    # Überprüfen, ob book2 unverändert ist
    assert book2.isbn == "ISBN_2", "Die ISBN von Buch 2 sollte unverändert sein"
    assert book2.author == "Author2", "Der Autor von Buch 2 sollte unverändert sein"

def test_book_creation():
    """Test: Ich kann ein Book Objekt erstellen"""
    title = "Python Testing"
    isbn = 978123456789
    author = "Max Mustermann"

    book = Book(title,isbn,author)

    assert book.title == title, f"Erwartet: {title} bekommen: {book.title}"
    assert book.isbn == isbn, f"Erwartet: {isbn} bekommen: {book.isbn}"
    assert book.author == author, f"Erwartet: {author} bekommen: {book.author}"
    print("Test bestanden")
