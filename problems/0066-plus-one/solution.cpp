class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int ix = digits.size() - 1;

        while (true) {
            if (digits[ix] == 9) {
                if (ix == 0) {
                    digits[ix] = 1;
                    digits.push_back(0);
                    return digits;
                } else {
                    digits[ix] = 0;
                    ix--;
                }
            } else {
                digits[ix] += 1;
                return digits;
            }
        }
        
        return digits;
    }
};
