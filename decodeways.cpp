class Solution {
public:
    int numDecodings(string s) {
        
        int n = s.length();
        int output[n + 1];
        
        for (int i = 0; i < n; i++) {
            output[i] = 0;
        }
        output[n] = 1;
        
        if (s[n - 1] != '0') {
            output[n - 1] = 1;
        }
        
        for (int i = n - 2; i > -1; i--) {
            if (s[i] != '0') {
                output[i] += output[i + 1];
            }
            if (s[i] == '1' || (s[i] == '2' && s[i + 1] < '7')) {
                output[i] += output[i + 2];
            }
        }
        
        return output[0];
        
    }
};
