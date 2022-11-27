import ast
from LoLM import *

def isPrima(n, i = 2):
  if n < 2: return False
  elif n == 2: return True
  elif n % i == 0: return False
  elif (i * i) > n: return True
  else: 
    return isPrima(n, i + 1)

def jml_prima(L):
  if is_empty_LoL(L):
    return 0
  else:
    if not(is_list(first_element(L))): #bukan list
      if isPrima(first_element(L)):
        return first_element(L) + jml_prima(tail_list(L))
      else: 
        return jml_prima(tail_list(L))
    else: #list
      if is_atom(L): 
        return jml_prima(first_element(L)) 
      else:
        return jml_prima(first_list(L)) + jml_prima(tail_list(L)) 

L = ast.literal_eval(input())
print(jml_prima(L))  