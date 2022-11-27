import ast
from LoLM import * 
L = ast.literal_eval(input())
a = int(input())

def monster(a,L):
  if is_empty_LoL(L):
    return L
  else:
    if is_list(first_list(L)):
      return konso_LoL(monster(a,first_list(L)),monster(a,tail_list(L)))
    else:
      if first_element(L) % a == 0: 
        return monster(a,tail_list(L))
      else: 
        return konso_LoL(first_element(L),monster(a,tail_list(L)))

print(monster(a,L))