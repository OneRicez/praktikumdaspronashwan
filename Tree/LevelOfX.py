from treem import *

def level_of_x(P,x):
  if not is_member(P,x):
    return 0
  else:
    if akar(P) == x:
      return 0
    else:
      if is_biner(P): 
        return 1 + level_of_x(left(P),x) + level_of_x(right(P),x)
      if is_uner_left(P):
        return 1 + level_of_x(left(P),x)
      if is_uner_right(P):
        return 1 + level_of_x(right(P),x)

T = makePb(1,makePb(2,makePb(4,None,None),makePb(5,None,None)),makePb(3,None,None))
print(level_of_x(T,2))