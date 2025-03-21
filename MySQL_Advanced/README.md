# MySQL Overview

![mysql](https://upload.wikimedia.org/wikipedia/fr/thumb/6/62/MySQL.svg/1200px-MySQL.svg.png)

## What is MySQL?
MySQL is an **open-source relational database management system (RDBMS)** that is widely used for managing and organizing data. It is known for its **speed, reliability, and ease of use**.

## Features
- **Relational Database**: Uses tables to store and organize data.
- **SQL Support**: Uses Structured Query Language (SQL) for database operations.
- **High Performance**: Optimized for fast query execution.
- **Scalability**: Supports small to large-scale applications.
- **Security**: Provides user authentication and data encryption.

## Installation
### Linux (Ubuntu/Debian)
```
sudo apt update
sudo apt install mysql-server
```

## Basic Commands
### Start & Stop MySQL Server
```
sudo systemctl start mysql  # Start MySQL
sudo systemctl stop mysql   # Stop MySQL
sudo systemctl restart mysql # Restart MySQL
```
### Access MySQL Shell
```
mysql -u root -p
```
### Creating a Database
```
CREATE DATABASE my_database;
```
### Using a Database
```
USE my_database;
```
### Creating a Table
```
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
```
### Inserting Data
```
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
```
### Fetching Data
```
SELECT * FROM users;
```
### Updating Data
```
UPDATE users SET name = 'Alice Smith' WHERE id = 1;
```
### Deleting Data
```
DELETE FROM users WHERE id = 1;
```

## Backup & Restore
### Backup a Database
```
mysqldump -u root -p my_database > backup.sql
```
### Restore a Database
```
mysql -u root -p my_database < backup.sql
```

## Additional Resources
- [Official MySQL Documentation](https://dev.mysql.com/doc/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)
