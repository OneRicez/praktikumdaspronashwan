from treem import *

def is_member(P,x):
  if is_tree_empty(P):
    return False
  else:
    if akar(P) == x: 
      return True
    else:
      if is_one_element(P):
        return akar(P) == x
      elif is_biner(P):
        return is_member(left(P),x) or is_member(right(P),x)
      elif is_uner_left(P):
        return is_member(left(P),x)
      elif is_uner_right(P):
        return is_member(right(P),x)

T = makePb(1,makePb(2,makePb(4,None,None),makePb(5,None,None)),makePb(3,None,None))
print(is_member(T,2))