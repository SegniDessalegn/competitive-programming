#include <cmath>

class Solution {
public:
    int numberOfWays(string corridor) {
        int N = corridor.length();
        int p_count = 0;
        int MOD = pow(10, 9) + 7;
        for (int i = 0; i <= N; i++){
            if (corridor[i] == 'S'){
                p_count++;
            }
        }
        
        if (p_count % 2 != 0 || p_count < 2){
            return 0;
        }
        
        long long ans = 1;
        int streak = 0;
        int curr_count = 0;
        for (int i = 0; i <= N; i++){
            if (corridor[i] == 'S'){
                curr_count++;
            }
            
            if (curr_count == 2){
                streak++;
            }
            if (curr_count > 2){
                ans *= streak;
                ans %= MOD;
                curr_count = 1;
                streak = 0;
            }
        }
        
        return ans;
    }
};