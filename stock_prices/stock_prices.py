#!/usr/bin/python

import argparse

def find_max_profit(prices):        #Overall - O(n)
  buy = max(prices[1:])                       #O(n)
  sell = min(prices[:prices.index(buy)])      #O(n)
  profit = buy - sell                         #O(1)
  if profit > 0:                              
    return profit                             #O(1)
  else:
    for i in range(len(prices)-1):            #O(n)
      current_profit = prices[i+1]-prices[i]  #O(1)
      if current_profit > profit:             
        profit = current_profit               #O(1)
    return profit                             #O(1)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))