class pohonbiner:
  def __init__(self, A, L, R):
    self.A = A
    self.L = L
    self.R = R
  def __repr__(self):  # Untuk merepresentasikan BinaryTree dalam bentuk string
        return "(%s, %s, %s)" % (repr(self.A), repr(self.L), repr(self.R))
        
def akar(P):
  return P.A

def left(P):
  return P.L

def right(P):
  return P.R

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

def makePb(A,L,R):
  return pohonbiner(A,L,R)
  
def is_tree_empty(P):
  if P == None:
    return True
  else:
    return False

def is_one_element(P):
  if not(is_tree_empty(P)) and is_tree_empty(left(P)) and is_tree_empty(right(P)):
    return True
  else :
    return False

def is_uner_left(P):
  if (not(is_tree_empty(P)) and not(is_tree_empty(left(P))) and is_tree_empty(right(P))):
    return True
  else:
    return False

def is_uner_right(P):
  if (not(is_tree_empty(P)) and is_tree_empty(left(P)) and not(is_tree_empty(right(P)))):
    return True
  else:
    return False

def is_biner(P):
  if (not(is_tree_empty(P)) and not(is_tree_empty(left(P))) and not(is_tree_empty(right(P)))):
    return True
  else:
    return False

def repPrefixPB(P):
  if is_one_element(P):
    return [akar(P)]
  else:
    if is_biner(P):
      return [akar(P)] + repPrefixPB(left(P)) + repPrefixPB(right(P))
    elif is_uner_left(P):
      return [akar(P)] + repPrefixPB(left(P))
    elif is_uner_right(P):
      return [akar(P)] + repPrefixPB(right(P))

def nbDaunPB(P):
    print("A")
    if is_one_element(P):
        return 1
    elif is_biner(P):
        return nbDaunPB(left(P)) + nbDaunPB(right(P))
    elif is_uner_left(P):
        return nbDaunPB(left(P))
    elif is_uner_right(P):
        return nbDaunPB(right(P))