my_string = "Hello, World!"
print(len(my_string))  # Output: 13

my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5

dictionary = {"name": "John", "age": 30}
print(dictionary["name"])  # Output: John
print(dictionary["age"])

class Book:
    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages

book1 = Book("John Doe", "Python Programming", 300)
print(book1.author)  # Output: John Doe
print(book1.title)  # Output: Python Programming
print(book1.pages)  # Output: 300

