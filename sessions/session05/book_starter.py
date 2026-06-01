# Introduction to Object-Oriented Programming: The Book Class
# ====================================================
#
# In this exercise, you'll create a Book class that represents a book in a library.
# Follow the instructions in the TODO comments to complete the implementation.
#
# Learning Objectives:
# 1. Understand how to create a class
# 2. Learn about class attributes and methods
# 3. Practice using the __init__ constructor
# 4. Implement instance methods
# 5. Create string representation of objects

class Book:
    """
    A class representing a book in a library.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        pages (int): The number of pages in the book
        is_available (bool): Whether the book is available for checkout
    """
    
    def __init__(self, title, author, pages):
        """
        Initialize a new Book object.
        
        TODO 1: Initialize the book's attributes:
        - Set the title attribute to the title parameter
        - Set the author attribute to the author parameter
        - Set the pages attribute to the pages parameter
        - Set is_available to True by default (all new books start as available)
        """
        pass  # Remove this line when you start implementing
    
    def checkout(self):
        """
        Mark the book as checked out (not available).
        
        TODO 2: Implement the checkout method:
        - If the book is available, set is_available to False and return True
        - If the book is not available, return False
        """
        pass  # Remove this line when you start implementing
    
    def return_book(self):
        """
        Mark the book as returned (available).
        
        TODO 3: Implement the return_book method:
        - Set is_available to True (the book is now available)
        - Return True to indicate successful return
        """
        pass  # Remove this line when you start implementing
    
    def get_info(self):
        """
        Return a string with the book's information.
        
        TODO 4: Return a string that includes:
        - The book's title
        - The author's name
        - The number of pages
        - Whether it's available or not
        
        Example format: "Harry Potter by J.K. Rowling (300 pages) - Available"
        """
        pass  # Remove this line when you start implementing


# Test your implementation
def test_book_class():
    """
    Test the Book class implementation.
    """
    # Create a new book
    book = Book("The Hobbit", "J.R.R. Tolkien", 295)
    
    # Test initial state
    print("Initial book info:", book.get_info())
    
    # Test checkout
    success = book.checkout()
    print("Checkout successful?", success)
    print("After checkout:", book.get_info())
    
    # Try to checkout again (should fail)
    success = book.checkout()
    print("Second checkout successful?", success)
    
    # Return the book
    success = book.return_book()
    print("Return successful?", success)
    print("After return:", book.get_info())


if __name__ == "__main__":
    test_book_class()


# Expected Output:
# Initial book info: The Hobbit by J.R.R. Tolkien (295 pages) - Available
# Checkout successful? True
# After checkout: The Hobbit by J.R.R. Tolkien (295 pages) - Not Available
# Second checkout successful? False
# Return successful? True
# After return: The Hobbit by J.R.R. Tolkien (295 pages) - Available
