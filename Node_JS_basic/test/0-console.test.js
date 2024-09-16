const assert = require('assert');
const displayMessage = require('../0-console');

describe('displayMessage', () => {
  it('should output the correct string', () => {
    const consoleSpy = jest.spyOn(console, 'log');
    displayMessage('Hello NodeJS!');
    assert(consoleSpy).toHaveBeenCalledWith('Hello NodeJS!');
  });
});
