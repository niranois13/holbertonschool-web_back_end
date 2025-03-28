const sinon = require("sinon");
const getPaymentTokenFromAPI = require('./6-payment_token');
const { describe, it } = require('mocha');
const { assert } = require("chai");

describe('getPaymentTokenFromAPI', function () {
  it('getPaymentTokenFromAPI(true) should return a resolved promise', (done) => {
    getPaymentTokenFromAPI(true).then((response) => {
      assert.deepStrictEqual(getPaymentTokenFromAPI(true), {data: 'Successful response from the API' });
      done();
    }).catch(done);
  });
});
