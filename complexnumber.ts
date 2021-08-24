const complexNumberMultiply = (num1: string, num2: string): string => {

  const complexToArray = (num: string): number[] => {
    const [ real, imaginary ] = num.split("+");
    return new Array<number>(+real, +imaginary.split("i")[0]);
  }

  const complexToString = (real: number, imaginary: number): string => {
    return `${real}+${imaginary}i`
  }

  const [a, b] = complexToArray(num1);
  const [c, d] = complexToArray(num2);
  const real = a*c - b*d;
  const imaginary = a*d + b*c;

  return complexToString(real, imaginary);
};
