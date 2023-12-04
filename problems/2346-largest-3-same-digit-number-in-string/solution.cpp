class Solution {
public:
    string largestGoodInteger(string num) {
        int p = 0, c = 0, len = num.length(), n = -1, t = 0;

        for (int i=0; i<len; i++) {
            if (num[p] == num[i]) c++;
            else {
                p = i;
                c = 1;
            }

            if (c == 3) {
                t = (num[p] - '0');
                t = t + 10 * t + 100 * t;
                if (t>n) n=t;
            }
        }

        if (n > 0) return std::to_string(n);
        if (n == 0) return "000";
        return "";
    }
};
