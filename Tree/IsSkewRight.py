from treem import *

def is_skew_right(P):
  if is_tree_empty(P) or is_biner(P) or is_uner_left(P):
    return False
  elif is_uner_right(P):
    return True

T = makePb(1,makePb(2,makePb(4,None,None),makePb(5,None,None)),makePb(3,None,None))
print(T)