# Library Management System

## Description
The Library Management System is a Python-based console application designed for efficient management of books and customer interactions in a library. Users can:

- View available books and their quantities.
- Borrow up to three books, ensuring inventory accuracy.
- Return borrowed books and update their records.
- View customer details such as name, phone number, address, and borrowed books.

This system simplifies library operations while providing a user-friendly interface for customers.

---

## Features

1. **Display All Book Details**
   - Lists all available books and their current quantities.

2. **Borrow Books**
   - Allows customers to borrow up to three books from the library.
   - Updates the inventory dynamically.

3. **Return Books**
   - Customers can return books they have borrowed.
   - Ensures only valid returns from the customer's borrowed list are accepted.

4. **Customer Details**
   - Displays the customer's name, phone number, address, and list of currently borrowed books.

5. **Exit**
   - Allows users to exit the application gracefully.

---

## How to Use

1. Run the program using Python.
2. Enter your name, phone number, and address as prompted.
3. Choose from the menu options:
   - `1`: View all available books.
   - `2`: Borrow books by selecting from the list of available titles.
   - `3`: Return previously borrowed books.
   - `4`: View your personal and borrowed book details.
   - `5`: Exit the application.

---

## Code Structure

The program is built around a `Library` class with the following key components:

- **Class Variables**: Maintains the library's name, location, and inventory of books.
- **Instance Variables**: Stores customer details such as name, phone number, address, and borrowed books.
- **Methods**:
  - `all_books`: Displays the list of books and quantities.
  - `borrow_book`: Handles borrowing logic with validation.
  - `borrow_return`: Manages book returns with checks.
  - `data`: Displays customer details.

---

## Prerequisites

- Python 3.x installed on your system.
- Basic understanding of Python to modify or enhance the program if needed.

---

## Future Enhancements

- Add a graphical user interface (GUI) for better usability.
- Implement a database for persistent storage of book and customer records.
- Enable customer registration and login features.

---

## License
This project is open-source and available for modification and distribution under the [AVH](https://avhinfotechs.netlify.app).
