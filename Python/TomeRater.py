class User():
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        #empty dict map a Book object to this users rating of the book
        self.books = {}
        #how to do the annotation for dictionaries?

    def get_email(self, email):
        self.email = email

    def change_email(self, address):
        self.email = address
        print("User e-mail updated.")

    def __repr__(self):
        return "User " + self.name + ", E-Mail: " + self.email + " - Books read: " + str(len(self.books))

    def __eq__(self, other_user):
        return self.email == other_user.email and self.name == other_user.name

    def read_book(self, book, rating=None):
#    def read_book(self, book):
        self.books[book] = rating
        
    def get_average_rating(self):
        rated_books = 0
        book_sum = 0
        for book in self.books:
            rated_books += 1
            book_sum += self.books[book]
        return book_sum/rated_books    
   
class Book():
    
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        #how to do the annotation for ratings?
        self.ratings = []
        
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The ISBN of " + self.title + " has been updated to " + str(self.isbn))
        
    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
            
    def get_average_rating(self):
        if len(self.ratings) == 0:
            return None
        sum = 0
        for rating in self.ratings:
            sum += rating
        else:
            pass
        return (sum / len(self.ratings))
    
    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):

    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return self.title + ", by " + self.author
     
class Non_Fiction(Book):
    
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject
    
class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
        
    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
    
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)
    
    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            print("No user with email {email}!")
        else:
            #call read_book on this user, with book and rating AND self.users is dict
            self.users[email].read_book(book, rating)
            if rating != None:
            #call add_rating on book , with rating; self.ratings is [] to have rating added
                book.add_rating(rating)
            # Check if the book is in TomeRaters self.books already
            else:
                pass
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1

    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[email] = user
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)
        else:
            print("User already registered")
        
    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)
                       
    def most_read_book(self):
        key_max = max(self.books.keys(), key=(lambda k: self.books[k]))
        return key_max
    
    def highest_rated_book(self):
        highest_rated = None
        highest_rating = 0
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > highest_rating:
                highest_rated = book                
                highest_rating = rating
            else: pass    
        return highest_rated
       
    def most_positive_user(self):
        most_positive_user = None
        highest_rating = 0
        for user in self.users.values():
            user_avg_rating = user.get_average_rating()
            if user_avg_rating > highest_rating:
                most_positive_user = user
                highest_rating = user_avg_rating
            else:
                pass
            return most_positive_user
    
from TomeRater import *
Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
print("Most positive user:")
print(Tome_Rater.most_positive_user())