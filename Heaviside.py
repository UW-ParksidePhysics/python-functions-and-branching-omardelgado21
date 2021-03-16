
def H(x):
  if(x<0): 
    return 0
  if(x>=0):
    return 1


def test_H():
  x=int(input("Enter value of x : "))
  result=H(x)
  print(result)
  x=int(input("Enter value of x : "))
  result=H(x)
  print(result)

test_H()