def getBrackets(n):
  if(n == 0):
    return [""]

  ret = []
  c=0

  for i in range(n):

    brackets1 = getBrackets(i)
    brackets2 = getBrackets(n-i-1)

    for b1 in brackets1:
      for b2 in brackets2:
        ret.append( "(" + b1 + ")" + b2)  
  return ret
x=getBrackets(2)
y=getBrackets(3)
z=getBrackets(5)
a=getBrackets(4)
b=getBrackets(6)
print(x)
print(len(x))
# print(y)
print(len(y))
# print(z)
print(len(z))
# print(a)
print(len(a))
# print(b)
print(len(b))