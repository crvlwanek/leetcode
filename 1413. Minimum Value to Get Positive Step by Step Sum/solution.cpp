class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int _min = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            nums[i] += nums[i-1];
            _min = min(_min, nums[i]);
        }
        if (_min < 1) return 1 - _min;
        return 1;
    }
};