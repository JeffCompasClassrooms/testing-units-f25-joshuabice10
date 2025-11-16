

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False
        self.hold = False

    def check_out(self):
        if self.checked_out:
            print("Book already checked out")
            return False
        self.checked_out = True

    def return_book(self):
        if not self.checked_out:
            print("Book is not checked out")
            return False
        self.checked_out = False

    def put_hold(self, name):
        if not self.hold:
            self.hold = name
            return True
        print("Book is already on hold")
        return False


    