
class Library:
    library_name = "AH Library"
    Location = "Chennai"
    books = {"a": 0, "b": 2, "c": 6, "d": 3, "e": 1}

    def __init__(self, name, ph_no, address, book_list=[]):
        self.name = name
        self.ph_no = ph_no
        self.address = address
        self.book_list = book_list

    def data(self):
        print("\nCustomer Details:")
        print("Name:", self.name)
        print("Phone Number:", self.ph_no)
        print("Address:", self.address)
        print("Borrowed Books:", self.book_list)

    @classmethod
    def all_books(cls):
        print("\nAvailable Books in the Library:")
        print("    Books         Quantity")
        print("_____________________________")
        for book ,values in cls.books.items():
            print(f"     {book}      :       {values}")

    @classmethod
    def borrow_book(cls, book_list):
        print("\nBorrowing Books Section")
        while True:
            borrow = input("\n Do you want to borrow any books? (yes/no): ").lower()
            if borrow == "yes":
                print("\nAvailable Books:")
                cls.all_books()

                book_name = input("Enter the book name you want to borrow: ").lower()
               
                if book_name in cls.books and cls.books[book_name] > 0 and book_name not in book_list:
                    cls.books[book_name] -= 1  
                    book_list.append(book_name)  
                    print(f"\nYou successfully borrowed '{book_name}'.")
                    
                    if len(book_list) >= 3:
                        print("\nYou have reached the borrowing limit of 3 books.")
                        break
                elif book_name in book_list:
                    print(f"\n u didn't take  '{book_name}'book, beacuse u already having in ur book_list")
                else:
                    print(f"\nSorry, '{book_name}' is not available or out of Library.")
            elif borrow == "no":
                print("\nYou chose not to borrow any more books.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    @classmethod
    def borrow_return(cls,book_list):
        print("\nReturning Books Section")
        if  book_list==[]:
            print("You have no books borrow  so u cant't return.")
            return

        while True:
            user_re = input("\nDo you want to return a book? (yes/no): ").lower()
            if user_re == "yes":
                print(f"\nYour Borrowed Books: {book_list}")
                if book_list==[]:
                    print("You Didn't Return Any books ,Because u r Book list Empty")
                    break
                book_name = input("Enter the name of the book you want to return: ").lower()
                if book_name in book_list:
                    book_list.remove(book_name)  
                    cls.books[book_name] += 1 
                    print(f"\nYou successfully returned '{book_name}'.")
                else:
                    print(f"\nYou cannot return {book_name} because it is not in your borrowed list.")
            elif user_re == "no":
                print("\nThank you! Have a great day.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

print("Welcome to AH Library!")
name = input("Enter your name: ")
ph_no = input("Enter your phone number: ")
address = input("Enter your address: ")
customer = Library(name, ph_no, address)


while True:
    print("\n1. Display All Book Details")
    print("2. Borrow Books")
    print("3. Return Books")
    print("4. View Customer Details")
    print("5. Exit") 
    
    user_input = input("Enter your choice (1-5): ")
    
    if user_input == "1":
        Library.all_books()
    elif user_input == "2":
        Library.borrow_book(customer.book_list)
    elif user_input == "3":
        Library.borrow_return(customer.book_list)
    elif user_input == "4":
        customer.data()
    elif user_input == "5":
        print("\nThank you for visiting AH Library!")
        exit()
    else:
        print("Invalid choice. Please select a valid option.")




