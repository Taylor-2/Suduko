import os
def setup(show):							#Works			Pulls and formats data from text file
	global filein
	global listin
	file=open("Test Cases/"+intensity+"/"+intensity+".txt","r")
	filein=file.readlines()
	file.close()
	listin=[]
	for x in filein:
		listin.append(x[0:len(x)-1])
	if show[0] == True:
		print("Original List: " + str(listin) + "\n")

def block_setup(show):						#Works			Calculates the block formating
	global blocklist
	blocklist=[[],[],[],[],[],[],[],[],[]]
	ctr=0
	while(ctr<3):
		temprow=listin[ctr]
		ctr2=0
		while(ctr2<3):
			blocklist[0].append(temprow[ctr2])
			ctr2+=1
		while(ctr2>=3 and ctr2<6):
			blocklist[1].append(temprow[ctr2])
			ctr2+=1
		while(ctr2<9):
			blocklist[2].append(temprow[ctr2])
			ctr2+=1
		ctr+=1
	while(ctr<6):
		temprow=filein[ctr]
		ctr2=0
		while(ctr2<3):
			blocklist[3].append(temprow[ctr2])
			ctr2+=1
		while(ctr2>=3 and ctr2<6):
			blocklist[4].append(temprow[ctr2])
			ctr2+=1
		while(ctr2<9):
			blocklist[5].append(temprow[ctr2])
			ctr2+=1
		ctr+=1
	while(ctr<9):
		temprow=filein[ctr]
		ctr2=0
		while(ctr2<3):
			blocklist[6].append(temprow[ctr2])
			ctr2+=1
		while(ctr2>=3 and ctr2<6):
			blocklist[7].append(temprow[ctr2])
			ctr2+=1
		while(ctr2<9):
			blocklist[8].append(temprow[ctr2])
			ctr2+=1
		ctr+=1
	if show[5] == True:
		print("Blocks: " + str(blocklist))

def blockfinder(rownum,column,show):		#Works			Returns the block information for a given row and column
	global blocklist
	if rownum<=2:
		if column<=2:
			block=blocklist[0]
		if column>=3 and column <=5:
			block=blocklist[1]
		if column>=6:
			block=blocklist[2]
	if rownum>=3 and rownum<=5:
		if column<=2:
			block=blocklist[3]
		if column>=3 and column <=5:
			block=blocklist[4]
		if column>=6:
			block=blocklist[5]
	if rownum>=6:
		if column<=2:
			block=blocklist[6]
		if column>=3 and column <=5:
			block=blocklist[7]
		if column>=6:
			block=blocklist[8]
	if show[6] == True:
		print("Block Data: " + str(block))
	return block

def possibilities_of(rownum,column,show):	#Needs work... Probably isolate this... want it to return all possible numbers a given unknown could be
	posrow=[1,2,3,4,5,6,7,8,9]
	rowdata=listin[rownum]
	for x in rowdata:
		ctr=1
		while (ctr<10):
			if(x==str(ctr)):
				posrow.remove(ctr)
			ctr +=1

	poscol=[1,2,3,4,5,6,7,8,9]
	ctr=0
	while(ctr<9):
		temprowdata=listin[ctr]
		colval=temprowdata[column]
		for x in poscol:
			if str(x)==colval:
				poscol.remove(x)
		ctr+=1

	block_setup(show)
	block=blockfinder(rownum,column,show)
	posblock=[1,2,3,4,5,6,7,8,9]
	for x in block:
		ctr=1
		while(ctr<10):
			if(x==str(ctr)):
				posblock.remove(ctr)
			ctr+=1

	allpos=[]
	ctr=1
	while(ctr<10):
		if (ctr in posrow) and (ctr in poscol) and (ctr in posblock):
			allpos.append(ctr)
		ctr +=1

	if show[1] == True:
		print("\nCoord: 	" + str([rownum,column]))
		print("Row: 	" + str(posrow))
		print("Col: 	" + str(poscol))
		print("Block: 	" + str(posblock))
		print("All:	" + str(allpos))

	return allpos
		
def unknownctr(show):						#Works			Returns the number of unknowns left in the puzzle
	unknownctr=0
	for x in listin:
		for xx in x:
			if xx == "*":
				unknownctr+=1
	if show[2]==True:
		print ("Unknowns Left: " + str(unknownctr))
	return unknownctr

def evaluate_unknowns(show):				#Works			Returns the coordinates of every unknown in the puzzle
	global unknowns
	unknowns=[]
	ctr=0
	while(ctr<9):
		rowinfo=listin[ctr]
		ctr2=0
		while(ctr2<9):
			if rowinfo[ctr2] == "*":
				unknowns.append([ctr,ctr2])
			ctr2+=1
		ctr +=1
	if show[3]==True:
		print("Unknowns: " + str(unknowns))
	return unknowns

def replace(rownum,column,solved_num,show):	#Works			Replaces a coordinate with the given value
	global listin
	rowdata=listin[rownum]
	newrow=""
	ctr=0
	while(ctr<9):
		if ctr==column:
			newrow+=str(solved_num)
		else:
			newrow+=rowdata[ctr]
		ctr+=1
	ctr=0
	listout=[]
	while(ctr<9):
		if ctr==rownum:
			listout.append(newrow)
		else:
			listout.append(listin[ctr])
		ctr+=1
	listin=listout
	if show[4] == True:
		print("Replacing unknown at [" + str(rownum) + "," + str(column) + "] with " + str(solved_num))

def small_number_method(show):				#Works			Finds the possible numbers for the unknowns and if there is only one, it replaces the * with the value
	block_setup(show)
	for x in evaluate_unknowns(show):
		rownum=x[0]
		column=x[1]
		allpossibilities=possibilities_of(rownum,column,show)
		if len(allpossibilities) == 1:
			new=allpossibilities[0]
			replace(rownum,column,new,show)

def advanced_method(show):					#NOPE			Still Needs Lots of work
	ctr=0
	while(ctr<9):							#Everything from here on is evaluating every row individualy

		inrow=0
		rowdata=listin[ctr]
		for x in rowdata:
			if x == "*":					#Finds the number of unknowns in the given row
				inrow+=1

		if inrow>3:
			unknowns=evaluate_unknowns(show)
			unknown_coords=[]
			for x in unknowns:
				if x[0] == ctr:
					unknown_coords.append(x)	#Now we have the coords of the unknowns in the row

		if ctr==0:
			print (str(unknown_coords)+"\n")

		ctr2=0									#Runs through each coordinate of the unknowns in a row
		while(ctr2<len(unknown_coords)-1):

			coord1=unknown_coords[ctr2]
			coord2=unknown_coords[ctr2+1]

			possibilities1=possibilities_of(coord1[0],coord1[1],show)
			possibilities2=possibilities_of(coord2[0],coord2[1],show)

			if ctr == 0:
				print(str(coord1) + " : " + str(possibilities1))
				print(str(coord2) + " :: " + str(possibilities2))

			matches=[]
			for x in possibilities1:
				for xx in possibilities2:					#Ok, so now we have the matching possibilities of the first and second coordinates
					if x == xx:
						matches.append(x)
			if ctr == 0:
				print("Matches: " + str(matches))


			for x in unknown_coords:
				if (x!=coord1) and (x!=coord2):			#This is our test coordinate	
					coord3=x
					possibilities3=possibilities_of(coord3[0],coord3[1],show)

					if ctr == 0:
						print(str(coord3) + " ::: " + str(possibilities3))

					matched_possibilities=[]
					for ppp in possibilities3:
						for pp in matches:
							if ppp == pp:
								matched_possibilities.append(pp)


					for xx in matched_possibilities:
						possibilities1a=[]
						for xxx in possibilities1:
							if xx != xxx:
								possibilities1a.append(xxx)
						possibilities2a=[]
						for xxx in possibilities2:
							if xx != xxx:
								possibilities2a.append(xxx)
						possibilities3a=[]
						for xxx in possibilities3:
							if xx != xxx:
								possibilities3a.append(xxx)

					if len(possibilities1a) == 1:
						replace(coord1[0],coord1[1],possibilities1a[0],show)
					if len(possibilities2a) == 1:
						replace(coord2[0],coord2[1],possibilities2a[0],show)
					if len(possibilities3a) == 1:
						replace(coord3[0],coord3[1],possibilities3a[0],show)

					if ctr == 0:									#Now I have matching possibilities
						print ("At least one match")
						print ("matched_possibilities: " + str(matched_possibilities))
						print ("1a: " + str(possibilities1a))
						print ("2a: " + str(possibilities2a))
						print ("3a: " + str(possibilities3a))
			if ctr == 0:
				print("")
			advanced_method(show)
			ctr2+=1
		ctr+=1

def output():								#Works			Writes the final solution to a text file
	print("\nWriting to text file...")
	file=open("Output.txt","w")
	for x in listin:
		file.write(str(x)+"\n")
	file.close()

def tester():								#Works			Tests the output against a known solution
	file=open("Test Cases/" + intensity + "/" + intensity +" Solution.txt","r")
	solution=file.readlines()
	file.close()

	file=open("Output.txt","r")
	output=file.readlines()
	file.close()

	print("\nChecking Against Answer...")

	if (output==solution):
		print ("\nAll Lines Correct")
	else:
		print("\nThere is a mistake somewhere")

def main(show):								#Works			Main function
	ctr=0
	while(unknownctr(show)>0) and (ctr<21):
		if (ctr%4==0) and (ctr != 0):
			print("Attempting advanced_method		Iteration: " + str(ctr) + " 		Unknowns Remaining: " + str(unknownctr(show)) + "\n")
			ctr2=0
			while(ctr2<9):
				advanced_method(ctr2,show)
				ctr2+=1
		else:
			print ("Attempting small_number_method		Iteration: " + str(ctr)+ " 		Unknowns Remaining: " + str(unknownctr(show)) + "\n")
			small_number_method(show)
		unknownctr(show)
		ctr+=1
	
	if(unknownctr(show)!=0):
		print("\nStopped by Failsafe 		Unknowns left: " + str(unknownctr(show)))
		output()
	else:
		output()
		tester()

def testing_main(show):
	shownone=[False,False,False,False,False,False,False]
	ctr=0
	while(ctr<5):
		print ("Attempting small_number_method		Iteration: " + str(ctr)+ " 		Unknowns Remaining: " + str(unknownctr(shownone)) + "\n")
		if ctr == 4:
			small_number_method(show)
			ctr +=1
			print("Attempting advanced_method		Iteration: " + str(ctr) + " 		Unknowns Remaining: " + str(unknownctr(show)) + "\n")
			advanced_method(show)
		else:
			small_number_method(shownone)
		ctr +=1		

#####################################################################################
# intensity="Very Easy"					#Good
# intensity="Easy"						#Good
intensity="Medium"					#No
# intensity="Hard"						#Not set up
# intensity="Expert"					#Not set up

# show = [0)Setup, 1)Possibilities_of, 2)Unknownctr, 3)evaluate_unknowns, 4)replace, 5)Blocklist, 6)Block]
# show=[False,False,False,False,False,False,False]
show=[False,False,False,False,True,False,False]

os.system("cls")
print("")

setup(show)
block_setup(show)

testing_main(show)
