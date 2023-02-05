def mn(l):
  l.sort()
  n=l[-1]
  for i in range (n+1):
    if i not in l:
      return i
