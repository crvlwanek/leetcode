class Solution {
public:
  bool judgeSquareSum(int c) {
    int count;
    for (int i = 2; i * i <= c; i++) {
      count = 0;
      while (c % i == 0) {
        c /= i;
        count++;
      }
      if (i % 4 == 3 && count % 2 != 0) {
        return false;
      }
    }
    return c % 4 != 3;
  }
};
