class Solution {
public:
    int numberOfMatches(int n) {
        if (n == 1){
            return 0;
        }
        if (n % 2 == 0){
            return (int)(n / 2) + numberOfMatches((int)(n / 2));
        }
        else {
            return (int)((n - 1) / 2) + numberOfMatches((int)((n - 1) / 2) + 1);
        }
    }
};