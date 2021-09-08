const shiftingLetters = (s: string, shifts: number[]): string => {
  for (let i = shifts.length - 2; i > -1; i--){
    shifts[i] += shifts[i + 1];
  }
  return String.fromCharCode(...shifts.map((amount, i) => {
    return (s.charCodeAt(i) - 97 + amount) % 26 + 97
  }));
};
