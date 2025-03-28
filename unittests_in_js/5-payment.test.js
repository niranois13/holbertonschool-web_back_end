const sinon = require("sinon");
const sendPaymentRequestToApi = require('./4-payment');
const { describe, it } = require('mocha');
const { assert } = require("chai");

describe("sendPaymentRequestToApi", function () {
  let spy;

  this.beforeEach(function() {
    spy = sinon.spy(console, 'log');
  });

  this.afterEach(function () {
    spy.restore();
  });

  it("should log the right total for 100, 20", () => {
    sendPaymentRequestToApi(100, 20)
    assert.strictEqual(spy.calledOnceWith('The total is: 120'), true);
  })

  it('shoudl log the right amount for 10, 10', () => {
    sendPaymentRequestToApi(10, 10)
    assert.strictEqual(spy.calledOnceWith('The total is: 20'), true);
  })
})
