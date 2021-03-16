def poly(roots, x):
  product = 1
  x = int(x)
  for i in range(0,len(roots)):
    h = x-int(roots[i])
    product = product*h
  return product  

root=[int(x) for x in input("roots1 :[").split()]
X = 10
print("poly(roots1,x) = " + str(poly(root,X)))