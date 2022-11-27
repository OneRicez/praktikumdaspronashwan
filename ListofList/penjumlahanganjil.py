import ast
from LoLM import *

def is_odd(e):
  return e % 2 != 0

def jml_ganjil(L):
  if is_empty_LoL(L):
    return 0
  else:
    if not(is_list(first_element(L))): #bukan list
      if is_odd(first_element(L)):
        return first_element(L) + jml_ganjil(tail_list(L))
      else: 
        return jml_ganjil(tail_list(L))
    else: #list
      if is_atom(L): 
        return jml_ganjil(first_element(L)) 
      else:
        return jml_ganjil(first_list(L)) + jml_ganjil(tail_list(L)) 

L = ast.literal_eval(input())
print(jml_ganjil(L))
