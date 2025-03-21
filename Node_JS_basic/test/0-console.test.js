const chai = require('chai');
const sinon = require('sinon');
const displayMessage = require('../0-console');
const assert = chai.assert;

describe('displayMessage', () => {
  let consoleSpy;

  beforeEach(() => {
    // Create a spy on console.log before each test
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // Restore the original console.log after each test
    consoleSpy.restore();
  });

  it('should output the correct string', () => {
    // Call the function
    displayMessage('Hello NodeJS!');

    // Assert that console.log was called with the correct argument
    assert(consoleSpy.calledWith('Hello NodeJS!'), 'console.log was not called with "Hello NodeJS!"');
  });
});
