# Basic authentication

![basic authentication](https://i.imgur.com/ttcprl8.png)

- [Basic authentication](#basic-authentication)
  - [Overview](#overview)
  - [Project steps](#project-steps)
    - [0. Simple-basic-API](#0-simple-basic-api)
    - [1. Error handler: Unauthorized](#1-error-handler-unauthorized)
    - [2. Error handler: Forbidden](#2-error-handler-forbidden)
    - [3. Auth class](#3-auth-class)
    - [4. Define which routes don't need authentication](#4-define-which-routes-dont-need-authentication)
    - [5. Request validation!](#5-request-validation)
    - [6. Basic auth](#6-basic-auth)
    - [7. Basic - Base64 part](#7-basic---base64-part)
    - [8. Basic - Base64 decode](#8-basic---base64-decode)
    - [9. Basic - User credentials](#9-basic---user-credentials)
    - [10. Basic - User object](#10-basic---user-object)
    - [11. Basic - Overload current\_user - and BOOM!](#11-basic---overload-current_user---and-boom)


## Overview

Authentication is a critical part of any web application, ensuring that users can securely log in and access protected resources.
In this project, we will implement a basic authentication system from scratch on a simple API.
In real-world situation, it's highly recommended to use a module or framework to do it.

## Project steps

### 0. Simple-basic-API
Setup the server and access the API.

### 1. Error handler: Unauthorized
Add a new error handler for the Unauthorized status code (401) and test it.

### 2. Error handler: Forbidden
Add a new error handler for the Forbidden status code (403) and test it.

### 3. Auth class
Create a class to manage the API authentication.
This class is the template for all authentication system implemented.

### 4. Define which routes don't need authentication
Create a function to define if routes need authentication or not.

### 5. Request validation!
validate all requests to secure the API.

### 6. Basic auth
Create a class BasicAuth that inherits from Auth

### 7. Basic - Base64 part
BasicAuth now returns the Base64 part of the Authorization header for a Basic Authentication.

### 8. Basic - Base64 decode
BasicAuth now returns the decoded value of a Base64 string.

### 9. Basic - User credentials
BasicAuth now returns the user email and password from the Base64 decoded value.

### 10. Basic - User object
BasicAuth now returns a User instance based on his email and password.

### 11. Basic - Overload current_user - and BOOM!
BasicAuth now overloads Auth and retrieves the User instance for a request, the API is fully protected by a Basic Authentication.