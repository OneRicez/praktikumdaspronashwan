# Nama: Nashwan Adenaya
# NIM: 24060122130084

def is_member(L,x):
  if is_empty_LoL(L):
    return False
  else:
    if first_element(L)==x:
      return True
    else:
      return is_member(tail(L),x)

def first_element(L):
  return L[0]
def tail(L):
  return L[1:]

def jml_elemen_list(L):
  if is_empty_LoL(L):
    return 0
  else: 
    return 1 + jml_elemen_list(tail(L))

def is_empty_LoL(S):
  return S==[]

def is_atom(S):
  return not(is_empty_LoL(S)) and jml_elemen_list(S)==1

def isList(S):
  return not(is_atom(S)) 

def konso_LoL(L,S):
  if is_empty_LoL(S):
    return [L]
  else:
    return [L]+S

def konsi_LoL(L,S):
  if is_empty_LoL(S):
    return [L]
  else:
    return S+[L]
def konso(S,L):
  if L==[]:
    return [S]
  else:
    return [S]+L

def first_List(S):
  if not(is_empty_LoL(S)):
    return S[0]

def tail_List(S):
  if not(is_empty_LoL(S)):
    return S[1:]

def last_List(S):
  if not(is_empty_LoL(S)):
    return S[-1:]

def head_List(S):
  if not(is_empty_LoL(S)):
    return S[:-1]

def make_set(L):
  if is_empty_LoL(L):
    print(L)
    return L
    
  else:
    if is_member(tail(L),first_element(L)):
      return make_set(tail(L))
    else:
      return konso(first_element(L), make_set(tail(L)))

# def isEqs(S1,S2):
#   if is_empty_LoL(S1) and is_empty_LoL(S2): True
#   elif not(is_empty_LoL(S1)) and is_empty_LoL(S2): False
#   elif is_empty_LoL(S1) and not(is_empty_LoL(S2)): False
#   elif not(is_empty_LoL(S1)) and not(is_empty_LoL(S2)): 
#     if is_atom(first_List(S1)) and is_atom(last_List(S2)):
#       first_List(S1) = first_List(S2) and isEqs(tail_List(S1),tail_List(S2))
    
def IsOneELmt(L):
  return len(L) == 1

# print(max(L))
def max2(a, b):
  if a >= b:
    return a
  else: 
    return b

def maxL(L):
  if IsOneELmt(L): 
    return [L]
  else:
    max2(last_List(L),max(head_List(L)))

