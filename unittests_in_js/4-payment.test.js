const sinon = require("sinon");
const Utils = require("./utils");
const sendPaymentRequestToApi = require('./4-payment');
const { describe, it } = require('mocha');
const { expect } = require("chai");


describe("sendPaymentRequestToApi", () => {
  it('should call calculateNumber and return 10', () => {
    const stub = sinon.stub(Utils, 'calculateNumber');
    stub.returns(10);

    const spy = sinon.spy(console, 'log');

    const apiRequests = sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
    expect(spy.calledOnceWithExactly('The total is: 10'));
    expect(Utils.calculateNumber('SUM', 100, 20)).to.equal(apiRequests);

    stub.restore();
    spy.restore();
  });
});
