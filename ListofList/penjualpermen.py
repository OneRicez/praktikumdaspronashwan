import ast
from LoLM import *

def is_odd(e):
  return e % 2 != 0

def total_list(L):
  if is_empty_LoL(L):
    return 0
  else:
    return first_element(L) + total_list(tail_list(L))

def promo(L):
  if is_empty_LoL(L):
    return 0
  else:
    if not(is_list(first_element(L))): #bukan list
      if is_odd(first_element(L)):
        return first_element(L) * 3000 + promo(tail_list(L))
      else: 
        return first_element(L) * 4000 + promo(tail_list(L))
    else: #list
      if is_odd(total_list(first_element(L))): 
        return total_list(first_element(L)) * 1000 + promo(tail_list(L)) 
      else:
        return total_list(first_element(L)) * 2000 + promo(tail_list(L)) 

L = ast.literal_eval(input())
print(promo(L))
