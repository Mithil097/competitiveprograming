def couplehold(list1):
   n=len(list1)
   position=[None]*n
   for i, partner in enumerate(list1):
       position[partner]=i
   m=0
   for i in range(0,n,2):
       p, u=list1[i:i+2]
       v=p-1 if p%2 else p+1
       if v!=u:
           j=position[v]
           list1[j]= u
           position[u]=j
           m+=1
   return m 

print(couplehold([1,3,4,0,2,5]))
print(couplehold([3,2,0,1]))
print(couplehold([1,0]))
# print(couplehold([3,1,5,4,6,2]))
# print(couplehold([55,37,19,46,66,32,07,81,33,76,00,28,92,26,99,06,56,29,17,52,90,79,91,83,12,40,82,84,02,21,11,68,98,34,73,10,57,58,64,36]))