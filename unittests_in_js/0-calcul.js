module.exports = function calculateNumber(a = 0, b = 0) {
  if (isNaN(a) || isNaN(b)) {
    throw new TypeError()
  }

  return (Math.round(a) + Math.round(b));
}
