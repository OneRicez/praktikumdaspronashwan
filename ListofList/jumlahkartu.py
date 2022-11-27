import ast
from LoLM import *

def is_list(L):
  return type(L) == list

def jml_elemen_lol(L):
  if is_empty_LoL(L):
    return 0
  else:
    if not(is_list(first_element(L))): #bukan list
      print(L, "1")
      return jml_elemen_lol(tail_list(L)) + 1
    else: #list
      if is_atom(L): 
        print(L, "2")
        return jml_elemen_list(first_list(L)) and jml_elemen_lol(first_element(L)) 
      else:
        print(L, "3")
        return jml_elemen_lol(first_list(L)) + jml_elemen_lol(tail_list(L)) 


list_of_list = ast.literal_eval(input())
jml_elemen_lol(list_of_list)
