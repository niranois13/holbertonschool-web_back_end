# Unttest in JS

![unittests](https://i.imgur.com/5T79Gca.png)

## Project Overview
This project aims to provide a comprehensive understanding of testing in Node.js using Mocha. By the end of this project, you should be able to explain and apply essential testing concepts without external help.

## Learning Objectives
By completing this project, you will learn:
- How to use Mocha to write a test suite
- How to use different assertion libraries (Node or Chai)
- How to present long test suites effectively
- When and how to use spies
- When and how to use stubs
- What hooks are and when to use them
- Unit testing with asynchronous functions
- How to write integration tests with a small Node.js server

## Prerequisites
To get started, ensure you have the following installed:
- [Node.js](https://nodejs.org/)
- [npm](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/)

## Installation
1. Clone this repository:
   ```
   git clone <repository-url>
   cd <project-folder>
   ```
2. Install dependencies:
   ```
   npm install
   ```

## Usage
### Running Tests
To execute the test suite, run:
```
npm test
```
This will invoke Mocha and run all test files in the project.

### Using Mocha with Chai
This project leverages [Chai](https://www.chaijs.com/) for assertions. Ensure you require Chai in your test files:
```
const { expect } = require('chai');
```

### Working with Spies and Stubs
For mocking functions, we use [Sinon.js](https://sinonjs.org/):
```
const sinon = require('sinon');
```

### Hooks in Mocha
Mocha provides hooks to manage test setup and teardown:
- `before()`, `beforeEach()`, `after()`, `afterEach()`

Example:
```
beforeEach(() => {
  console.log('Runs before each test');
});
```

### Writing Integration Tests
To test a small Node.js server, we use [Supertest](https://github.com/visionmedia/supertest):
```
const request = require('supertest');
const app = require('../app');

request(app)
  .get('/api/example')
  .expect(200)
  .end((err, res) => {
    if (err) throw err;
  });
```
