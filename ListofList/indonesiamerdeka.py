from LoLM import *
import ast

def sum_max(L):
  if is_empty_LoL(L):
    return 0
  else:
    return max(first_list(L)) + sum_max(tail_list(L))

def final(L):
  return sum_max(L) * 1000000

L = ast.literal_eval(input())
print(final(L))