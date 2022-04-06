class Solution:
    def coinChange(self, coins, amount) :
        dp = [amount+1] * (amount+1)

        dp[0] = 0


        for i in range(1,amount+1):

            for c in coins:

                if c > i:
                    continue

                remain = i-c

                dp[i] = min(dp[i], 1+ dp[remain])

        return dp[amount] if dp[amount] != amount+1 else -1


s = Solution()

print(s.coinChange([1,2,5], 11))