const sinon = require("sinon");
const assert = require('assert');
const Utils = require("./utils");
const sendPaymentRequestToApi = require('./3-payment');
const { describe, it } = require('mocha');

describe("sendPaymentRequestToApi", function () {
  let spy;

  this.beforeEach(function () {
    spy = sinon.spy(Utils, 'calculateNumber');
  });

  this.afterEach(function () {
    spy.restore();
  });

  it("should call Utils.calculateNumber properly", function () {
    sendPaymentRequestToApi(100, 20);

    assert.strictEqual(spy.calledOnce, true);
    assert.deepStrictEqual(spy.firstCall.args, ['SUM', 100, 20]);
  });
});
