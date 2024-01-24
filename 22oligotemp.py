# 22oligotemp.py by Jordan Shore
#
# This program contains a function that calculates oligo melting temperatures.

#Parameters are A,T,C,G counts.
#Returns oligo melt point.
def oligomp(a,t,c,g):
	length = (a+t+c+g)

	if (length<=13):
		mp = ((a+t)*2)+((g+c)*4)
	else:
		mp = (64.9+41*((g+c-16.4)/(length)))

	return mp

#Testing
(a1,t1,c1,g1) = (2,3,4,1)
test1 = oligomp(a1,t1,c1,g1)
print("Test 1: a="+str(a1),"t="+str(t1),"c="+str(c1),"g="+str(g1))
print("Melting Temp:", test1)
(a2,t2,c2,g2) = (3,3,12,12)
test2 = oligomp(a2,t2,c2,g2)
print("Test 2: a="+str(a2),"t="+str(t2),"c="+str(c2),"g="+str(g2))
print("Melting Temp:", test2)
(a3,t3,c3,g3) = (10,100,1000,1)
test3 = oligomp(a3,t3,c3,g3)
print("Test 3: a="+str(a3),"t="+str(t3),"c="+str(c3),"g="+str(g3))
print("Melting Temp:", test3)