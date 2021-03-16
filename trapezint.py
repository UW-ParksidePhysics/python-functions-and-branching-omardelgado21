import math

def trapezint1(f, a, b):
  return (b-a)*(f(a)+f(b))/2

trapezint1(math.cos, 0 , math.pi)

trapezint1(math.sin, 0 , math.pi/2)


def trapezint2(f, a, b):
    val = 0
    val += (b - a) * 0.25 * (f(a) + f((b - a) * 0.5))
    val += (b - a) * 0.25 * (f(b) + f((b - a) * 0.5))
    return val

trapezint2(math.cos, 0 , math.pi)

trapezint2(math.sin, 0 , math.pi/2)

def trapezint(f, a, b, n):
    step = ((b - a) * 1.0) / n 
    val = 0
    while (a < b):
        val += 0.5 * step * (f(a) + f(a + step))
        a += step
    return val

print(trapezint(math.cos, 0 , math.pi, 10))
print(trapezint(math.sin, 0 , math.pi/2, 10))


#def test_trapezint():
  print(trapezint(math.cos, 0 , math.pi, 10))
  print(trapezint(math.sin, 0 , math.pi/2, 10))
  