class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 1

        '''def recursive_steps(val):
            
            if val <= 1:
                return 1
            
            if dp[val] != 0:
                return dp[val]
            
            dp[val] = recursive_steps(val-1) + recursive_steps(val-2)
            
            return dp[val]
        
        return recursive_steps(n)'''
        if n <= 1:
            return 1

        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]




