#Searches for the Kozac sequence 2 lines at a time,
#Lines are longer than sequence so a sequence can only be
#within a line or across two lines
	current_line1 = ""
	current_line2 = ""

#Sequence starts at "ORIGIN"
#IF/ELIF Fills line 1 and 2  
#ELSE makes line 1 = 2 and then fill line 2
		'''
Imagine looking at the last 2 rows of a Jenga Tower
and each turn you slide out the bottom layer
		'''
		if "ORIGIN" in line:
			atseq = True
		elif atseq == False:
			continue
		elif (current_line1 == "") and (current_line2 == ""):
			current_line1 = mcb185.clean_line(line)
		elif (current_line2 == ""):
			current_line2 = mcb185.clean_line(line)
		else: 
			current_line1 = current_line2
			current_line2 = mcb185.clean_line(line)

#Search for Kozac sequence across the combo of both lines
		mkozac = re.search(kozacpat,current_line1+current_line2)
		if mkozac:
			kozac_list.append(mkozac.group(1))

#If it is found in line 2, we know it is not in line 1
#We can reempty line 2 shunt it to the duplicate checking 
		if (mkozac != None) and (mkozac.group(1) in current_line2):
			current_line1 = current_line2
			current_line2 = ""
		'''
Duplicate Checking WHILE Loop:
If sequence is found;
	#We want to find all of them if they are within line 1
	#We also get rid of all of line 1 searched through
		'''
		while (mkozac != None) and (mkozac.group(1) in current_line1):
			kozacend = current_line1.find(mkozac.group(1))+len(mkozac.group(1))
			current_line1 = current_line1[kozacend:]
			mkozac = re.search(kozacpat,current_line1+current_line2)
			if mkozac:
				kozac_list.append(mkozac.group(1))