# Nama: Nashwan Adenaya
# NIM: 24060122130084

def is_member(L,x):
  if is_empty_LoL(L):
    return False
  else:
    if first_element(L)==x:
      return True
    else:
      return is_member(tail_list(L),x)

def is_list(L):
  return type(L) == list

def first_element(L):
  return L[0]

def jml_elemen_list(L):
  if is_empty_LoL(L):
    return 0
  else: 
    return 1 + jml_elemen_list(tail_list(L))

def is_empty_LoL(S):
  return S==[]

def is_atom(S):
  return not(is_empty_LoL(S)) and jml_elemen_list(S)==1

def isList(S):
  return not(is_atom(S)) or type(S) == list

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

def first_list(S):
  if not(is_empty_LoL(S)):
    return S[0]

def tail_list(S):
  if not(is_empty_LoL(S)):
    return S[1:]

def last_list(S):
  if not(is_empty_LoL(S)):
    return S[-1:]

def head_list(S):
  if not(is_empty_LoL(S)):
    return S[:-1]

def make_set(L):
  if is_empty_LoL(L):
    print(L)
    return L
    
  else:
    if is_member(tail_list(L),first_element(L)):
      return make_set(tail_list(L))
    else:
      return konso(first_element(L), make_set(tail_list(L)))

def isEqs(S1,S2):
  if is_empty_LoL(S1) and is_empty_LoL(S2): True
  elif not(is_empty_LoL(S1)) and is_empty_LoL(S2): False
  elif is_empty_LoL(S1) and not(is_empty_LoL(S2)): False
  elif not(is_empty_LoL(S1)) and not(is_empty_LoL(S2)): 
    if is_atom(first_list(S1)) and is_atom(last_list(S2)):
      return first_list(S1) == first_list(S2) and isEqs(tail_list(S1),tail_list(S2))
    if isList(first_list(S1)) and isList(first_list(S2)):
      return isEqs(first_list(S1),first_list(S2)) and isEqs(tail_list(S1),tail_list(S2))
  else:
    return False 

def IsOneELmt(L):
  return len(L) == 1

# print(max(L))
def max2(a, b):
  if a >= b:
    return a
  else: 
    return b

# def maxL(L):
#   if IsOneELmt(L): 
#     if is_atom(first_list(L)):
#       return first_list(L)
#     else: #List
#       return maxL(first_list(L))
#   else:
#     if is_atom(first_list(L)): #Fl adalah atom
#       return max2(first_list(L),maxL(tail_list(L)))
#     else: #FL adalah list
#       return max2(maxL(first_list(L)),maxL(tail_list(L)))



def rember(a,L):
  if is_empty_LoL(L):
    return L
  else:
    if is_list(first_list(L)):
      print(L, "1")
      return konso_LoL(rember(a,first_list(L)),rember(a,tail_list(L)))
    else:
      if first_element(L) == a:
        print(L, "2") 
        return rember(a,tail_list(L))
      else: 
        print(L, "3")
        return konso_LoL(first_element(L),rember(a,tail_list(L)))


