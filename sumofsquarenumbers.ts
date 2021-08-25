// Fermat's theorem

// A number can be a sum of two squares if and only if
// all of it's prime factors in the form 4k+3 occur an
// even number of times
function judgeSquareSum(c: number): boolean {
  let count;
  for (let i = 2; i * i <= c; i++) {
    count = 0;
    while (c % i === 0) {
      count++;
      c /= i;
    }
    if (i % 4 === 3 && count % 2 != 0) {
      return false;
    }
  }
  return c % 4 !== 3;
};
