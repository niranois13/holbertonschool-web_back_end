const Utils = {
  calculateNumber(type, a = 0, b = 0) {
    if (isNaN(a) || isNaN(b)) {
      throw new TypeError();
    };

    switch(type) {
      case ('SUM'):
        return (Math.round(a) + Math.round(b));
      case ('SUBTRACT'):
        return (Math.round(a) - Math.round(b));
      case ('DIVIDE'):
        if (Math.round(b) == 0) {
          return ('Error');
        }
        return (Math.round(a) / Math.round(b));
      default:
        throw new Error;
    };
  }
};

module.exports = Utils;
