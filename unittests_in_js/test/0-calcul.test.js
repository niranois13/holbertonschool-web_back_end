const assert = require('node:assert');
const calculateNumber = require('../0-calcul');
const { it } = require('node:test');

describe('calculateNumber', () => {
  it('should return the sum of rounded numbers', () => {
    assert.strictEqual(calculateNumber(1.2, 2.7), 4);
  });
  it('should return the correct sum of whole numbers', () => {
    assert.strictEqual(calculateNumber(2, 3), 5);
  });
  it('should work with negative numbers', () => {
    assert.strictEqual(calculateNumber(-1.3, -3.6), -5);
  });
  it('should work with one zero', () => {
    assert.strictEqual(calculateNumber(0, 2,2), 2);
  });
  it('should work with two zeros', () => {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });
  it('shoukd work with small numbers', () => {
    assert.strictEqual(calculateNumber(0.05, 0.05), 0);
  });
});
