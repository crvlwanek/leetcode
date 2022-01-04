class Solution {
public:
    int bitwiseComplement(int n) {
        return n > 1 ? pow(2, floor(log2(n)) + 1) - 1 - n : n == 0 ? 1 : 0;
    }
};