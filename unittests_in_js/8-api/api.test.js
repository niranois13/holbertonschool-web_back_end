const request = require('request');
const { expect } = require('chai');
const app = require('./api');

describe('Integration Testing', function () {
  let server;

  before((done) => {
    server = app.listen(7865, () => done);
  });

  after(() => {
    server.close();
  })

  describe('GET /', () => {
    it('Code: 200 | Body: Welcome to the payment system', (done) => {
      request('http://localhost:7865', function (error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });
});
