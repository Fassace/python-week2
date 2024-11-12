# Program 2: Create a tuple of favorite books and print each book name
def favorite_books():
    books = ("The Alchemist", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "Moby-Dick")
    return books
# Program 2
books = favorite_books()
print("Favorite Books:")
for book in books:
    print(book)