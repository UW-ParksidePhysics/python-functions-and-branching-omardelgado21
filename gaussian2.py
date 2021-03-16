import numpy as np

def gaussian(x, mu=0, s=1):
  
  numerator=-(np.power(x - mu, 2)) #numerator
  
  denominator=(2 * np.power(s, 2))#denoiminator
  
  exponent_value=np.exp(numerator/denominator)#exponential expression value
  
  y =(exponent_value)/(s*(np.sqrt(2*3.14)))#total f(x)
  
  return y

for i in range(-5, 6):
  print(i, gaussian(i)) 
