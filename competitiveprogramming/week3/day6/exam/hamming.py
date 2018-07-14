
def hamming(x,y):
	# x=bin(x)
	# y=bin(y)
	return bin(x^y).count('1')

print(hamming(1,4))
print(hamming(25,30))
print(hamming(100,250))
print(hamming(1,30))
print(hamming(0,255))