# User Authenticaton Service

## Overview
In this project, we will implement a **User Authentication Service** as a _Flask-based authentication system_ built for _learning purposes_. While in real-world applications, authentication should be handled by established modules like Flask-User, this project walks through implementing authentication from scratch to understand the mechanisms behind it.

## Project steps

### 0. User model
We will create a SQLAlchemy model named User for a database table named users (by using the mapping declaration of SQLAlchemy).

### 1. create user
We will complete a `DB class` provided to implement the add_user method, that allows the creation of users.

### 2. Find user
We will implement the `DB.find_user_by` method. This method takes in arbitrary keyword arguments and returns the first row found in the users table as filtered by the method’s input arguments. No validation of input arguments required at this point.

### 3. update user
We will implement the `DB.update_user` method that takes as argument a required `user_id` integer and arbitrary keyword arguments, and returns `None`.

The method will use `find_user_by` to locate the user to update, then will update the user’s attributes as passed in the method’s arguments then commit changes to the database.

### 4. Hash password
We will define a `_hash_password` method that takes in a `password` string arguments and returns bytes.

The returned bytes is a salted hash of the input password, hashed with `bcrypt.hashpw`.

### 5. Register user
We will implement the `Auth.register_user` in the provided `Auth` class.

### 6. Basic Flask app
We will set up a basic `Flask` app.

### 7. Register user
We will implement the end-point to register a user.

### 8. Credentials validation
We  will implement the `Auth.valid_login` method. It is used to check if given credentials match registered ones.

### 9. Generate UUIDs
We will implement a `_generate_uuid` function in the auth module. The function should return a string representation of a new UUID.

### 10. Get session ID
We will implement the `Auth.create_session` method. It takes an `email` string argument and returns the `session ID` as a string.

### 11. Log in
We will implement a `login` function to respond to the `POST /sessions` route.

### 12. Find user by session ID
We will implement the `Auth.get_user_from_session_id` method. It takes a single `session_id` string argument and returns the corresponding `User` or `None`.

### 13. Destroy session
We will implement `Auth.destroy_session`. The method takes a single `user_id` integer argument and returns `None`.

### 14. Log out
We will implement a `logout` function to respond to the `DELETE /sessions` route.

### 15. User profile
We will implement a `profile` function to respond to the `GET /profile` route.

### 16. Generate reset password token
We will implement the `Auth.get_reset_password_token` method. It take an `email` string argument and returns a string.

### 17. Get reset password token
We will implement a `get_reset_password_token` function to respond to the `POST /reset_password` route.

### 18. Update password
We will implement the `Auth.update_password` method. It takes `reset_token` string argument and a password string argument and returns `None`.

### 19. Update password end-point
We will implement the `update_password` function in the `app` module to respond to the `PUT /reset_password` route.