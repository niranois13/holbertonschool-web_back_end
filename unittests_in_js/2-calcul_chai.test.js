const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');
const { describe, it } = require('mocha');

describe('2-calcul_chai - calculateNumber - SUM ', () => {
  it('should return the sum of floats', () => {
    expect(calculateNumber('SUM', 1.2, 2.7)).to.equal(4);
    expect(calculateNumber('SUM', 0.05, 0.05)).to.equal(0);
    expect(calculateNumber('SUM', -1.3, -3.6)).to.equal(-5);
    expect(calculateNumber('SUM', -1.3, 2)).to.equal(1);
    expect(calculateNumber('SUM', 0, 2.2)).to.equal(2);
  });

  it('should return the correct sum of whole numbers', () => {
    expect(calculateNumber('SUM', 2, 3)).to.equal(5);
    expect(calculateNumber('SUM', 0, 0)).to.equal(0);
    expect(calculateNumber('SUM', 1, -1)).to.equal(0);
  });

  it('should return the rounded number if only one is provided', () => {
    expect(calculateNumber('SUM', 2)).to.equal(2);
    expect(calculateNumber('SUM', 2.7)).to.equal(3);
    expect(calculateNumber('SUM', -1.2)).to.equal(-1);
    expect(calculateNumber('SUM', 0)).to.equal(0);
    expect(calculateNumber('SUM', -0)).to.equal(0);
  });

  it('should cast non-numbers into numbers', () => {
    expect(calculateNumber('SUM', true, '3')).to.equal(4);
    expect(calculateNumber('SUM', 1, '3.7')).to.equal(5);
    expect(calculateNumber('SUM', '1.2', 3.7)).to.equal(5);
  });
});

describe('2-calcul_chai - calculateNumber - SUBTRACT', () => {
  it('should return the subtract of floats', () => {
    expect(calculateNumber('SUBTRACT', 2.7, 1.2)).to.equal(2);
    expect(calculateNumber('SUBTRACT', 0.05, 0.05)).to.equal(0);
    expect(calculateNumber('SUBTRACT', -1.3, -3.6)).to.equal(3);
    expect(calculateNumber('SUBTRACT', -1.3, 2)).to.equal(-3);
    expect(calculateNumber('SUBTRACT', 2.2, 0)).to.equal(2);
  });

  it('should return the correct subtract of whole numbers', () => {
    expect(calculateNumber('SUBTRACT', 3, 2)).to.equal(1);
    expect(calculateNumber('SUBTRACT', 2, 3)).to.equal(-1);
    expect(calculateNumber('SUBTRACT', 0, 0)).to.equal(0);
    expect(calculateNumber('SUBTRACT', 1, -1)).to.equal(2);
  });

  it('should return the rounded number if only one is provided', () => {
    expect(calculateNumber('SUBTRACT', 2)).to.equal(2);
    expect(calculateNumber('SUBTRACT', 2.7)).to.equal(3);
    expect(calculateNumber('SUBTRACT', -1.2)).to.equal(-1);
    expect(calculateNumber('SUBTRACT', 0)).to.equal(0);
    expect(calculateNumber('SUBTRACT', -0)).to.equal(-0);
  });

  it('should cast non-numbers into numbers', () => {
    expect(calculateNumber('SUBTRACT', true, '3')).to.equal(-2);
    expect(calculateNumber('SUBTRACT', '3.7', 1)).to.equal(3);
    expect(calculateNumber('SUBTRACT', '1.2', 3.7)).to.equal(-3);
  });
});

describe('2-calcul_chai - calculateNumber - DIVIDE', () => {
  it('should return the remainder of float division', () => {
    expect(calculateNumber('DIVIDE', 2.7, 1.2)).to.equal(3);
    expect(calculateNumber('DIVIDE', 0.05, 0.05)).to.equal('Error');
    expect(calculateNumber('DIVIDE', -1.3, -3.6)).to.equal(0.25);
    expect(calculateNumber('DIVIDE', -1.3, 2)).to.equal(-0.5);
    expect(calculateNumber('DIVIDE', 2.2, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 8.2, 3.9)).to.equal(2);
  });

  it('should return the rounded remainder of whole numbers divided', () => {
    expect(calculateNumber('DIVIDE', 8, 4)).to.equal(2);
    expect(calculateNumber('DIVIDE', 3, 2)).to.equal(1.5);
    expect(calculateNumber('DIVIDE', 2, 3)).to.equal(0.6666666666666666);
    expect(calculateNumber('DIVIDE', 0, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 1, -1)).to.equal(-1);
  });

  it('should return Error if only one is provided as args initialized at 0', () => {
    expect(calculateNumber('DIVIDE', 2)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 2.7)).to.equal('Error');
    expect(calculateNumber('DIVIDE', -1.2)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', -0)).to.equal('Error');
  });

  it('should cast non-numbers into numbers', () => {
    expect(calculateNumber('DIVIDE', true, '3')).to.equal(0.3333333333333333);
    expect(calculateNumber('DIVIDE', '3.7', 1)).to.equal(4);
    expect(calculateNumber('DIVIDE', '8.2', 3.7)).to.equal(2);
  });
});

describe('2-calcul_chai.js - calculateNumber - General assumptions', () => {
  it('should throw TypeError if param is NaN', () => {
    expect(() => calculateNumber('SUBTRACT', 'hello')).to.throw(TypeError);
    expect(() => calculateNumber('SUM', 1.2, 'dog')).to.throw(TypeError);
    expect(() => calculateNumber('DIVIDE', 'cat', 8.9)).to.throw(TypeError);
  });

  it('should throw an error on invalid operation type', () => {
    expect(() => calculateNumber('INVALID', 2, 3)).to.throw();
  });
});
