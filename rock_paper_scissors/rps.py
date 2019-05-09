#!/usr/bin/python

import sys


def rock_paper_scissors(n):     # Overall - O(n)
  rps = ['rock', 'paper', 'scissors']     # O(1)
  plays = []                              # O(1)
  
  def rps_results_adder(n, play):
    if n == 0:
      return plays.append(play)           # O(1)
    for i in rps:                         # O(3)
      rps_results_adder(n-1, play + [i])  # O(n)

  rps_results_adder(n, [])                # O(1)
  return plays                            # O(1)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')