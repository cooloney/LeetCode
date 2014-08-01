class Solution {
public:
    int reverse(int x) {
        int ret = 0, digit = 0;

        while (x) {
            digit = x % 10;
            ret = ret * 10 + digit;
            x = x / 10;
        }

        return ret;
    }
};
