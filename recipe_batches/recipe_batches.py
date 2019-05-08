#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):        #Overall - O(n)
  batches = None                                          #O(1)
  for k, v in recipe.items():                             #O(n)
    has_item_amount = ingredients.get(k)                  #O(1)
    if not has_item_amount or has_item_amount < v:
      return 0                                            #O(1)
    else:
      current_item_batches = has_item_amount // v         #O(1)
      if not batches or current_item_batches < batches:   
        batches = current_item_batches                    #O(1)
  return batches                                          #O(1)
      

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))