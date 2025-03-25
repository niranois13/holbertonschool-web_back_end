const assert = require('assert');
const calculateNumber = require('./0-calcul');
const { describe, it } = require('node:test');

describe('calculateNumber', () => {
  it('should return the sum of floats', () => {
    assert.strictEqual(calculateNumber(1.2, 2.7), 4);
    assert.strictEqual(calculateNumber(0.05, 0.05), 0);
    assert.strictEqual(calculateNumber(-1.3, -3.6), -5);
    assert.strictEqual(calculateNumber(-1.3, 2), 1);
    assert.strictEqual(calculateNumber(0, 2.2), 2);
  });

  it('should return the correct sum of whole numbers', () => {
    assert.strictEqual(calculateNumber(2, 3), 5);
    assert.strictEqual(calculateNumber(0, 0), 0);
    assert.strictEqual(calculateNumber(1, -1), 0);
  });

  it('should return the rounded number if only one is provided', () => {
    assert.strictEqual(calculateNumber(2), 2);
    assert.strictEqual(calculateNumber(2.7), 3);
    assert.strictEqual(calculateNumber(-1.2), -1);
    assert.strictEqual(calculateNumber(0), 0);
    assert.strictEqual(calculateNumber(-0), 0);
  });

  it('should cast non-numbers into numbers', () => {
    assert.strictEqual(calculateNumber(true, '3'), 4);
    assert.strictEqual(calculateNumber(1, '3.7'), 5);
    assert.strictEqual(calculateNumber('1.2', 3.7), 5);
  });

  it('should work with no parameters given and return 0', () => {
    assert.strictEqual(calculateNumber(), 0);
  });

  it('should ignore extra args if more than 2 are provided', () => {
    assert.strictEqual(calculateNumber(2.4, 9.2, 8.4), 11);
  })

  it('should throw typeerror if param is NaN', () => {
    assert.throws(() => calculateNumber('hello'), {
      name: 'TypeError'
    });
    assert.throws(() => calculateNumber(1.2, 'dog'), {
      name: 'TypeError',
    });
    assert.throws(() => calculateNumber('cat', 8.9), {
      name: 'TypeError'
    })
  });

  it('should throw TypeError with null parameters', () => {
    assert.throws(() => calculateNumber(2.4, null), {
      name: 'TypeError'
    });
    assert.throws(() => calculateNumber(null, 3.7), {
      name: 'TypeError'
    });
    assert.throws(() => calculateNumber(null, null), {
      name: 'TypeError'
    });
  });
});
