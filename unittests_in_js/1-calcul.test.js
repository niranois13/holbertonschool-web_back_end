const assert = require('assert');
const calculateNumber = require('./1-calcul');
const { describe, it } = require('mocha');

describe('1-calcul - calculateNumber - SUM ', () => {
  it('should return the sum of floats', () => {
    assert.strictEqual(calculateNumber('SUM', 1.2, 2.7), 4);
    assert.strictEqual(calculateNumber('SUM', 0.05, 0.05), 0);
    assert.strictEqual(calculateNumber('SUM', -1.3, -3.6), -5);
    assert.strictEqual(calculateNumber('SUM', -1.3, 2), 1);
    assert.strictEqual(calculateNumber('SUM', 0, 2.2), 2);
  });

  it('should return the correct sum of whole numbers', () => {
    assert.strictEqual(calculateNumber('SUM', 2, 3), 5);
    assert.strictEqual(calculateNumber('SUM', 0, 0), 0);
    assert.strictEqual(calculateNumber('SUM', 1, -1), 0);
  });

  it('should return the rounded number if only one is provided', () => {
    assert.strictEqual(calculateNumber('SUM', 2), 2);
    assert.strictEqual(calculateNumber('SUM', 2.7), 3);
    assert.strictEqual(calculateNumber('SUM', -1.2), -1);
    assert.strictEqual(calculateNumber('SUM', 0), 0);
    assert.strictEqual(calculateNumber('SUM', -0), 0);
  });

  it('should cast non-numbers into numbers', () => {
    assert.strictEqual(calculateNumber('SUM', true, '3'), 4);
    assert.strictEqual(calculateNumber('SUM', 1, '3.7'), 5);
    assert.strictEqual(calculateNumber('SUM', '1.2', 3.7), 5);
  });
});

describe('1-calcul - calculateNumber - SUBTRACT', () => {
  it('should return the subtract of floats', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 2.7, 1.2), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 0.05, 0.05), 0);
    assert.strictEqual(calculateNumber('SUBTRACT', -1.3, -3.6), 3);
    assert.strictEqual(calculateNumber('SUBTRACT', -1.3, 2), -3);
    assert.strictEqual(calculateNumber('SUBTRACT', 2.2, 0), 2);
  });

  it('should return the correct subtract of whole numbers', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 3, 2), 1);
    assert.strictEqual(calculateNumber('SUBTRACT', 2, 3), -1);
    assert.strictEqual(calculateNumber('SUBTRACT', 0, 0), 0);
    assert.strictEqual(calculateNumber('SUBTRACT', 1, -1), 2);
  });

  it('should return the rounded number if only one is provided', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 2), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 2.7), 3);
    assert.strictEqual(calculateNumber('SUBTRACT', -1.2), -1);
    assert.strictEqual(calculateNumber('SUBTRACT', 0), 0);
    assert.strictEqual(calculateNumber('SUBTRACT', -0), -0);
  });

  it('should cast non-numbers into numbers', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', true, '3'), -2);
    assert.strictEqual(calculateNumber('SUBTRACT', '3.7', 1), 3);
    assert.strictEqual(calculateNumber('SUBTRACT', '1.2', 3.7), -3);
  });
});

describe('1-calcul - calculateNumber - DIVIDE', () => {
  it('should return the remainder of float division', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 2.7, 1.2), 3);
    assert.strictEqual(calculateNumber('DIVIDE', 0.05, 0.05), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', -1.3, -3.6), 0.25);
    assert.strictEqual(calculateNumber('DIVIDE', -1.3, 2), -0.5);
    assert.strictEqual(calculateNumber('DIVIDE', 2.2, 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 8.2, 3.9), 2);
  });

  it('should return the rounded remainder of whole numbers deivided', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 8, 4), 2);
    assert.strictEqual(calculateNumber('DIVIDE', 3, 2), 1.5);
    assert.strictEqual(calculateNumber('DIVIDE', 2, 3), 0.6666666666666666);
    assert.strictEqual(calculateNumber('DIVIDE', 0, 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 1, -1), -1);
  });

  it('should return Error if only one is provided as args initialized at 0', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 2), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 2.7), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', -1.2), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', -0), 'Error');
  });

  it('should cast non-numbers into numbers', () => {
    assert.strictEqual(calculateNumber('DIVIDE', true, '3'), 0.3333333333333333);
    assert.strictEqual(calculateNumber('DIVIDE', '3.7', 1), 4);
    assert.strictEqual(calculateNumber('DIVIDE', '8.2', 3.7), 2);
  });
});

describe ('1-calcul.js - calculateNumber - General assumptions', () => {
  it('should throw typeerror if param is NaN', () => {
    assert.throws(() => calculateNumber('SUBTRACT', 'hello'), {
      name: 'TypeError'
    });
    assert.throws(() => calculateNumber('SUM', 1.2, 'dog'), {
      name: 'TypeError'
    });
    assert.throws(() => calculateNumber('DIVIDE', 'cat', 8.9), {
      name: 'TypeError'
    })
  });

  it('should throw an error on invalid operation type', () => {
    assert.throws(() => calculateNumber('INVALIDE', 2, 3))
  });
});
