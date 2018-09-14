import math

# Checks if an integer is prime or no
def isPrime(integer):
  i = 2
  while (i <= math.sqrt(abs(integer))):
    if integer % i == 0:
      return(False)

    i += 1

  return(True)

# Returns prime's array
def findPrimes(integers):
  primes = []
  for integer in integers:
    if isPrime(integer):
      primes.append(integer)

  return(primes)


print(findPrimes([1,2,3,4,5,6,7,8,9]))
