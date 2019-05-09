#!/usr/bin/python

import sys
# amount = [0+, 5+, 10+, 15+, 20+, 25+, 30+, 35+, 40+, 45+, 50+, 55+, ]
# cache =  [1,  2,  4,   6,   9,   13,  18,  24,  31,  39,  50,  62]

def making_change(amount, denominations): # Overall - O(n)
  cache = [1 for i in range(amount + 1)]            # O(1)                
  if amount < 0:
    return 0                                        # O(1)
  elif amount < 5:
    return 1                                        # O(1)
  else:
    for coin in denominations[1:]:                  # O(4)
      for higher_amount in range(coin, amount + 1): # O(n)
        difference = higher_amount - coin           # O(1)
        cache[higher_amount] += cache[difference]   # O(1)
    return cache[amount]                            # O(1)


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")