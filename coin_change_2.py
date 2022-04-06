class Solution:
    def change(self, amount, coins):

        if amount == 0:
            return 1

        mem = [[0]*len(coins) for i in range (len(amount)+1)]
        mem[0] = [1] * len(coins)

        


s = Solution()

amount = 5
coins = [1,2,5]

print(s.change(amount, coins))
