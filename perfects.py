vals = list(range(1,10000))
perfects = []

for n in vals:
  divisorsSum = 1

  # Add square root for square numbers
  if int(n**0.5) == n**0.5:
      divisorsSum += n**0.5

  # Loop through all the divisors until the square root
  # max is added as in some cases int just gives 2
  for x in range(2, max(int(n**0.5), 3)):
    if n % x == 0:
      divisorsSum += (x + n/x)
      
      if divisorsSum > n:
        break

      if divisorsSum == n:
        perfects.append(n)
        break


print(perfects)
