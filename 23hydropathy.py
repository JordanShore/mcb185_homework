# 23hydropathy.py by Jordan Shore
#
# This program contains a function that returns the Kyte-Doolittle hydrophobicity value for an Amino Acid.

#Parameters is amino acid name symbol. 
#Returns hydrophobicity value as hpb. 
def kd_hydrophobicity(aa):
	if (aa == "A"):
		hpb = 1.8
	elif (aa == "C"):
		hpb = 2.5
	elif (aa == "D"):
		hpb = -3.5
	elif (aa == "E"):
		hpb = -3.5
	elif (aa == "F"):
		hpb = 2.8
	elif (aa == "G"):
		hpb = -0.4
	elif (aa == "H"):
		hpb = -3.2
	elif (aa == "I"):
		hpb = 4.5
	elif (aa == "K"):
		hpb = -3.9
	elif (aa == "L"):
		hpb = 3.8
	elif (aa == "M"):
		hpb = 1.9
	elif (aa == "N"):
		hpb = -3.5
	elif (aa == "P"):
		hpb = -1.6
	elif (aa == "Q"):
		hpb = -3.5
	elif (aa == "R"):
		hpb = -4.5
	elif (aa == "S"):
		hpb = -0.8
	elif (aa == "T"):
		hpb = -0.7
	elif (aa == "V"):
		hpb = 4.2
	elif (aa == "V"):
		hpb = 4.2
	elif (aa == "W"):
		hpb = -0.9
	elif (aa == "Y"):
		hpb = -1.3
	else:
		hpb = ("na")
		print("Error Invalid Amino Acid. Use Single String Capitals.")

	return hpb

test1 = kd_hydrophobicity("A")
print("Test 1: Amino Acid = 'A'")
print("Kyte-Doolittle Hydrophobicity Value:", test1)
test2 = kd_hydrophobicity("W")
print("Test 2: Amino Acid = 'W'")
print("Kyte-Doolittle Hydrophobicity Value:", test2)
test3 = kd_hydrophobicity("J")
print("Test 3: Amino Acid = 'J'")
print("Kyte-Doolittle Hydrophobicity Value:", test3)