#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None): # Overall - O(n)
  if n < 0:
    return 0                                 # O(1)
  elif n == 0:
    return 1                                 # O(1)
  elif cache and cache[n] > 0:
    return cache[n]                          # O(1)
  else:
    if not cache:
      cache = {i: 0 for i in range(n+1)}     # O(n)
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]                          # O(1)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')