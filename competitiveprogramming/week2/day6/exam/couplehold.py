def couplehold(row):
   n=len(row)
   person2position=[None]*n
   for i, person in enumerate(row):
       person2position[person]=i
   cpt=0
   for i in range(0,n,2):
       p, z=row[i:i+2]
       q=p-1 if p%2 else p+1
       if q!=z:
           j=person2position[q]
           row[j]= z
           person2position[z]=j
           cpt+=1
   return cpt 

print(couplehold([1,3,4,0,2,5]))
print(couplehold([3,2,0,1]))
print(couplehold([1,0]))
# print(couplehold([3,1,5,4,6,2]))
# print(couplehold([55,37,19,46,66,32,07,81,33,76,00,28,92,26,99,06,56,29,17,52,90,79,91,83,12,40,82,84,02,21,11,68,98,34,73,10,57,58,64,36]))