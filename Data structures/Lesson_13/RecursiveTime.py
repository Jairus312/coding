def fac(n):
  if(n==1 or n==0):
    return 1

  return n*fac(n-1)

num = int(input("entert the number of which factorial is to be calculated:"))
print("factorial of given number is:",fac(num))