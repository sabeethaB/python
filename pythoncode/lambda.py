def mymul(n):
  return lambda a : a * n

mydouble = mymul(2)
mytriple = mymul(3)

print(mydouble(11)) 
print(mytriple(11))
