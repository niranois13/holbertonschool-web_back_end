# Session authentication

![session authentication](https://i.imgur.com/a6Zto2c.png)

- [Session authentication](#session-authentication)
  - [Overview](#overview)
  - [Project steps](#project-steps)
    - [0. Et moi et moi et moi!](#0-et-moi-et-moi-et-moi)
    - [1. Empty session](#1-empty-session)
    - [2. Create a session](#2-create-a-session)
    - [3. User ID for Session ID](#3-user-id-for-session-id)
    - [4. Session cookie](#4-session-cookie)
    - [5. Before request](#5-before-request)
    - [6. Use Session ID for identifying a User](#6-use-session-id-for-identifying-a-user)
    - [7. New view for Session Authentication](#7-new-view-for-session-authentication)
    - [8. Logout](#8-logout)


## Overview

Authentication is a critical part of any web application, ensuring that users can securely log in and access protected resources.
In this project, we will implement a basic session authentication system from scratch on a simple API.
In real-world situation, it's highly recommended to use a module or framework to do it.

## Project steps

### 0. Et moi et moi et moi!
Starting from the work done for the `Basic_authentication/` project, we add a specifc endpoint to retreive the **Authenticated User** object.

### 1. Empty session
Add a -for now- empty `SessionAuth` environment variable, it will allow us to switch to, and enable, our future **Session Authenticaton** system.

### 2. Create a session
Create a class and instance method to store key-value pairs in a dictionnary. The key will be a `SessionID` (uuid4), the value will be `user_id`.

### 3. User ID for Session ID
Update SessionAuth class to add an instance method that returns a `user_id` based on a `SessionID`.

### 4. Session cookie
Update auth.py to add a method that returns a **cookie** value from a request. The cookie's name is define by the environment variable `SESSION_NAME` .

### 5. Before request
Update the before_request method to add the `login/` endpoint to the `excluded_paths` list.

### 6. Use Session ID for identifying a User
Update SessionAuth to add an instance method that returns a `User` instance based on a **cookie** value.

### 7. New view for Session Authentication
Create a new Flask view that handles all routes for the Session authentication.

### 8. Logout
Update SessionAuth to add a new instance method that deletes the user session.
