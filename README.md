<p align="center">
  A simple and modular <b>Bank Management System</b> built using <b>Python</b> and <b>MySQL</b>, featuring account creation, balance management, deposits, withdrawals, and database integration through a clean CLI-based architecture.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Programming-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql">
  <img src="https://img.shields.io/badge/CLI-Application-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/CRUD-Operations-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

---

# 🏦 Bank Management System

A Command Line Interface (CLI) based banking application developed using Python and MySQL. The project allows users to create bank accounts, view account information, deposit funds, withdraw money, and check account balances while storing all data in a MySQL database.

This project was built to strengthen understanding of:

- Python Programming
- Modular Project Structure
- Database Connectivity
- SQL Operations
- CRUD Functionality
- Real-World Application Development

---

# 🚀 Features

## 👤 Account Management

### Create Account

Users can create a new bank account by providing:

- Name
- Email Address
- Opening Balance

Example:

```text
Enter your name: Sachin
Enter your Email: sachin@gmail.com
Enter your opening balance: 5000

Account Created Successfully!
```

---

## 📋 View Accounts

Displays all registered bank accounts stored in the database.

Information displayed:

- Account ID
- Name
- Email
- Current Balance

Example:

```text
ID: 1
Name: Sachin
Email: sachin@gmail.com
Balance: 5000
```

---

## 💰 Deposit Money

Allows users to deposit money into an existing account.

Features:

✅ Instant balance update

✅ Database synchronization

✅ Secure SQL execution using parameters

Example:

```text
Enter Account ID: 1
Enter deposit amount: 1000

Money Deposited Successfully!
```

---

## 💸 Withdraw Money

Allows users to withdraw money from an account.

Validation Included:

✅ Balance verification

✅ Insufficient balance protection

✅ Automatic balance update

Example:

```text
Enter Account ID: 1
Enter amount to withdraw: 500

Withdraw Successfully!
```

If balance is insufficient:

```text
Insufficient Balance
```

---

## 📊 Check Balance

Users can check account balance using Account ID.

Example:

```text
Enter Account ID: 1

Account Holder: Sachin
Balance: 5500
```

---

# 🗄️ Database Integration

This project uses:

```text
MySQL Database
```

Database Operations:

✅ Insert Records

✅ Read Records

✅ Update Records

✅ Fetch Account Details

Database Table:

```sql
accounts
```

Stored Information:

- Account ID
- Name
- Email
- Balance

---

# 🧠 Concepts Used

## Python Concepts

- Functions
- Conditional Statements
- Loops
- User Input Handling
- Modular Programming
- Database Connectivity

---

## SQL Concepts

- INSERT Query
- SELECT Query
- UPDATE Query
- Database Transactions

---

## Software Development Concepts

- CRUD Operations
- Database Management
- Separation of Concerns
- Modular Architecture
- Command Line Applications

---

# 📂 Project Structure

```bash
Bank-Management-System/
│
├── main.py
├── menu.py
├── account_operations.py
├── db_config.py
├── README.md
│
└── Database
```

---

# 📄 File Description

| File | Purpose |
|--------|---------|
| `main.py` | Application entry point |
| `menu.py` | Displays menu and handles user navigation |
| `account_operations.py` | Contains all banking functionalities |
| `db_config.py` | Establishes MySQL database connection |
| `README.md` | Project documentation |

---

# ⚙️ Database Setup

## Step 1: Create Database

```sql
CREATE DATABASE bank_db;
```

---

## Step 2: Select Database

```sql
USE bank_db;
```

---

## Step 3: Create Accounts Table

```sql
CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    balance DECIMAL(10,2) DEFAULT 0
);
```

---

# 🔧 Configuration

Open:

```python
db_config.py
```

Update your database credentials:

```python
import mysql.connector as myconn

def connect():
    return myconn.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="bank_db"
    )
```

---

# 🚀 Installation



## 2️⃣ Navigate to Project Directory

```bash
cd bank-management-system
```

---

## 3️⃣ Install Required Package

```bash
pip install mysql-connector-python
```

---

## 4️⃣ Run Application

```bash
python main.py
```

---

# 📋 Menu Interface

```text
---- Bank Management System ----

1. Create Account
2. View Account
3. Deposit Money
4. Withdraw Money
5. Check Balance
6. Exit
```

---

# 🔄 Application Workflow

```text
Start Program
      │
      ▼
Display Menu
      │
      ▼
Select Operation
      │
      ├── Create Account
      ├── View Accounts
      ├── Deposit Money
      ├── Withdraw Money
      ├── Check Balance
      └── Exit
      │
      ▼
Update MySQL Database
      │
      ▼
Display Result
```

---

# 💡 Learning Outcomes

Through this project, the following concepts were practiced:

### Python

- Functions
- Modules
- File Organization
- User Interaction

### Database

- MySQL Integration
- SQL Queries
- Data Persistence
- CRUD Operations

### Software Engineering

- Modular Design
- Code Separation
- Maintainability
- Real-World Project Structure

---

# ⚠ Challenges Faced

### Database Connectivity

Challenges:

- Connecting Python with MySQL
- Managing database sessions
- Executing parameterized queries

---

### Data Validation

Challenges:

- Preventing invalid withdrawals
- Handling missing account IDs
- Managing user input

---

### Project Organization

Challenges:

- Separating business logic
- Maintaining reusable code
- Structuring files properly

---

# ✅ Solutions Implemented

✅ Modular architecture

✅ MySQL database integration

✅ CRUD operations

✅ Secure parameterized SQL queries

✅ Balance validation before withdrawal

✅ Reusable database connection function

---

# 🔮 Future Improvements

Planned enhancements:

- Account Update Feature
- Delete Account Feature
- Login Authentication System
- Transaction History
- Money Transfer Feature
- Exception Handling
- Object-Oriented Programming (OOP)
- SQLite Support
- GUI Version using Tkinter
- Django Web Application
- REST API Integration

---

# ✨ Key Highlights

🏦 Banking Management System

💾 MySQL Database Integration

📋 Account Management

💰 Deposit Functionality

💸 Withdrawal Functionality

📊 Balance Checking

🧠 CRUD Operations

📂 Modular Project Structure

🚀 Beginner-Friendly Database Project

---

# 🤝 Contributing

Contributions are welcome.

Feel free to:

⭐ Star the repository

🍴 Fork the project

📢 Share suggestions

🚀 Submit pull requests

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork it

📢 Share it with others

---

# 👨‍💻 Author

**Saachin Kunwar**

Python Developer | Web Developer



<p align="center">
Built with ❤️ while learning Python, MySQL, CRUD Operations, and Software Development.
</p>
