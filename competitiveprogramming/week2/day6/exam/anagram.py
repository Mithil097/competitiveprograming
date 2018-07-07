def anagram(s,t):
	s=s.lower()
	t=t.lower()
	alist=list(t)
	blist=list(s)
	i=0
	while i<len(alist):
		if alist[i]==" ":
			i=i+1
		if alist[i] in s:
			i=i+1
		
		else:
			return False
	return True	

s=input()
t=input() 
k=anagram(s,t)
print(k)