vals = list(range(0,1000))

for n in vals:
   if n > len(vals)**0.5:
       break
   if n == -1 or n == 0 or n==1:
       continue
   for x in range(2*n, len(vals), n):
       vals[x] = -1

print (vals)
