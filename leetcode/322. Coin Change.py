# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:


#         if amount == 0: 
#             return 0 

#         sol = [-1] * (amount+1) # amount = [0, 1, 2,... k]
        
#         # filling the base cases 
#         for coin in coins: 
#             if coin < amount: 
#                 sol[coin] = 1 

        

#         # for each amount, we see where we can get to with the coins that we have 
#         # if amount = 1 currently, then we have 3 coins of different value, we can go to 3 differnt amounts
        

#         for cur_amt, cur_ways in enumerate(sol): 
#             for coin in coins: 
                
#                 # the next amount we can go to
#                 next_amt = cur_amt + coin 

#                 if next_amt < amount: 
#                     num_ways = cur_ways + 1
#                     sol[next_amt] = min(num_ways, sol[next_amt])

#         return sol[amount]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        amount = k 

        start from 0 amount

        the minimum amount for k is the minimum amount for k-x + 1 
        """

        if amount == 0:
            return 0 

        sol = [float('inf')] * (amount + 1)
        sol[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                # build the number of ways with the smallest denominations first 
                # then slowly go for the higher ones, note that the higher amounts would get updated first, since sol[x-coin]
                # then would update the back ones 
                sol[x] = min(sol[x], sol[x - coin] + 1) 
                

        return sol[amount] if sol[amount] != float('inf') else -1