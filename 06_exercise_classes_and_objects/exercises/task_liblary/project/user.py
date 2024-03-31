class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        books = ", ".join(b for b in sorted(self.books))
        return books

    def __str__(self):
        books = ", ".join(b for b in self.books)
        return f"{self.user_id}, {self.username}, {books}"
