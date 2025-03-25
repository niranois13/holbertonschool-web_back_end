module.exports = function calculateNumber(a = 0, b = 0) {
  const NumA = Number(a)
  const NumB = Number(b)

  if (a === null || b === null) {
    throw new TypeError()
  }

  if (isNaN(NumA) || isNaN(NumB)) {
    throw new TypeError()
  }

  return (Math.round(NumA) + Math.round(NumB));
}
