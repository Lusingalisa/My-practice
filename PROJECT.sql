CREATE DATABASE LIBRARY;
USE LIBRARY;
CREATE TABLE Book(
    Book_ID INT PRIMARY KEY,
    Title VARCHAR(60),
    Publisher_ID INT,
    ISBN VARCHAR(40),
    Category_ID INT,
    Total_Copies INT,
    FOREIGN KEY (Publisher_ID) REFERENCES Publisher(Publisher_ID),
    FOREIGN KEY (Category_ID) REFERENCES Category(Category_ID) 
);
INSERT INTO Book (Book_ID, Title, Publisher_ID, ISBN, Category_ID, Total_Copies) VALUES
(1, 'To Kill a Mockingbird', 1, '978-0446310789', 1, 5),
(2, 'A Brief History of Time', 2, '978-0553380163', 3, 3),
(3, 'The Hobbit', 3, '978-0547928227', 5, 7),
(4, 'Sapiens', 4, '978-0062316097', 4, 4),
(5, '1984', 5, '978-0451524935', 1, 6);
ALTER TABLE Book CHANGE Books_ID Book_ID INT;
DESC Book;
CREATE TABLE Author(
    Author_ID INT(100) PRIMARY KEY,
    First_Name VARCHAR(20) NOT NULL,
    Last_Name VARCHAR(30) NOT NULL
);
DESC Author;
INSERT INTO Author (Author_ID, First_Name, Last_Name) VALUES
(1, 'Harper', 'Lee'),
(2, 'Stephen', 'Hawking'),
(3, 'J.R.R.', 'Tolkien'),
(4, 'Yuval Noah', 'Harari'),
(5, 'George', 'Orwell');

CREATE TABLE BookAuthor(
    Book_ID INT,
    Author_ID INT(100),
    FOREIGN KEY (Book_ID) REFERENCES Book(Book_ID),
    FOREIGN KEY (Author_ID) REFERENCES Author(Author_ID)
);
DESC BookAuthor;
INSERT INTO BookAuthor (Book_ID, Author_ID) VALUES
(1, 1),  -- Harper Lee wrote To Kill a Mockingbird
(2, 2),  -- Stephen Hawking wrote A Brief History of Time
(3, 3),  -- J.R.R. Tolkien wrote The Hobbit
(4, 4),  -- Yuval Noah Harari wrote Sapiens
(5, 5);  -- George Orwell wrote 1984


CREATE TABLE Publisher(
    Publisher_ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Contact_Info INT(10)
);
INSERT INTO Publisher (Publisher_ID, Name, Contact_Info) VALUES
(1, 'Penguin Books', 0773459021),
(2, 'HarperCollins', 0783459021),
(3, 'Oxford University Press', 0773456421),
(4, 'Scholastic', 0752459021),
(5, 'Random House', 0773459039);

CREATE TABLE Category(
    Category_ID INT PRIMARY KEY,
    Category_Name VARCHAR(20),
    Copies_available INT
);

INSERT INTO Category (Category_ID, Category_Name, Copies_available) VALUES
(1, 'Fiction', 20),
(2, 'Non-Fiction', 15),
(3, 'Science', 10),
(4, 'History', 12),
(5, 'Fantasy', 18);

CREATE TABLE Student(
    Student_ID VARCHAR(20) PRIMARY KEY,
    First_Name VARCHAR(20),
    Last_Name VARCHAR(30),
    Year INT,
    Contact_Info INT(10),
    Email VARCHAR(40)
);
DESC Student;
INSERT INTO Student (Student_ID, First_Name, Last_Name, Year, Contact_Info, Email) VALUES
('S001', 'John', 'Doe', 2, 0772223333, 'john.doe@example.com'),
('S002', 'Jane', 'Smith', 3, 0753334444, 'jane.smith@example.com'),
('S003', 'Alice', 'Johnson', 1, 0704445555, 'alice.j@example.com'),
('S004', 'Bob', 'Wilson', 4, 0785556666, 'bob.wilson@example.com'),
('S005', 'Emma', 'Brown', 2, 0726667777, 'emma.brown@example.com');
ALTER TABLE Student ADD PRIMARY KEY(Student_ID);

CREATE TABLE Staff(
    Staff_ID INT PRIMARY KEY,
    First_Name VARCHAR(20) NOT NULL,
    Last_Name VARCHAR(30),
    Role VARCHAR(20) NOT NULL,
    Contact_Info INT(10) NOT NULL,
    Email VARCHAR(50) NOT NULL
);
DESC Staff;
INSERT INTO Staff (Staff_ID, First_Name, Last_Name, Role, Contact_Info, Email) VALUES
(1, 'Michael', 'Scott', 'Librarian', 0717778888, 'michael.scott@library.org'),
(2, 'Pam', 'Beesly', 'Assistant', 0738889999, 'pam.beesly@library.org'),
(3, 'Jim', 'Halpert', 'Clerk', 0769990000, 'jim.halpert@library.org'),
(4, 'Dwight', 'Schrute', 'Security', 0770001111, 'dwight.schrute@library.org'),
(5, 'Angela', 'Martin', 'Accountant', 0782223333, 'angela.martin@library.org');
CREATE TABLE BorrowingRecord(
    Record_ID INT PRIMARY KEY,
    Book_ID INT,
    Student_ID VARCHAR(20),
    Borrow_Date DATE NOT NULL,
    Due_Date DATE NOT NULL,
    Return_Date DATE NOT NULL,
    STATUS ENUM('borrowed','returned','overdue') NOT NULL DEFAULT 'borrowed',
    FOREIGN KEY (Book_ID) REFERENCES Book(Book_ID),
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID)
);
DESC BorrowingRecord;
INSERT INTO BorrowingRecord (Record_ID, Book_ID, Student_ID, Borrow_Date, Due_Date, Return_Date, STATUS) VALUES
(1, 1, 'S001', '2025-03-01', '2025-03-15', '2025-03-10', 'returned'),
(2, 2, 'S002', '2025-03-05', '2025-03-19', '2025-03-20', 'overdue'),
(3, 3, 'S003', '2025-03-10', '2025-03-24', '2025-03-15', 'returned'),
(4, 4, 'S004', '2025-03-12', '2025-03-26', '2025-03-25', 'borrowed'),
(5, 5, 'S005', '2025-03-15', '2025-03-29', '2025-03-18', 'returned');
CREATE TABLE Fine(
    Fine_ID INT PRIMARY KEY,
    Student_ID VARCHAR(20),
    Book_ID INT,
    Payment_Status ENUM('paid','unpaid') DEFAULT 'unpaid',
    FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID),
    FOREIGN KEY (Book_ID) REFERENCES Book(Book_ID)
);
DESC Fine;
INSERT INTO Fine (Fine_ID, Student_ID, Book_ID, Payment_Status) VALUES
(1, 'S002', 2, 'unpaid'),  -- Overdue fine for A Brief History of Time
(2, 'S004', 4, 'unpaid'),  -- Potential fine for Sapiens (still borrowed)
(3, 'S001', 1, 'paid'),    -- Fine paid for To Kill a Mockingbird
(4, 'S003', 3, 'paid'),    -- Fine paid for The Hobbit
(5, 'S005', 5, 'paid');    -- Fine paid for 1984
CREATE TABLE FineRule(
    Days_Overdue INT PRIMARY KEY,
    Fine_Amount VARCHAR(30)
);
DESC FineRule;
INSERT INTO FineRule (Days_Overdue, Fine_Amount) VALUES
(1, '$0.50'),
(5, '$2.00'),
(10, '$5.00'),
(15, '$10.00'),
(30, '$20.00');
SHOW TABLES;
SELECT * FROM BOOK;