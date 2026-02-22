
#=====================================================Filo I/O==============================================

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[1: Read file]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
myFile = open("Sample.txt","r")
#print(myFile)

myFileRead = myFile.read()
print(myFileRead) 		# read() function used to your file only for read.
'''


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[2: Write file]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
myFile = open("Sample2.txt","w")
myFile.write("Hello my Family")
myFile.close()			# wirte() function used to your file in put any data using...
'''


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[3: Append mode]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
myFile = open("Sample2.txt","a")
myFile.write("\n Hello my best Family")
myFile.close()				# append / (a) functoin used to put data automatic
'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[4: Shortcut property with any opration(r,w,a)]~~~~~~~~~~~~~~

with open('Sample2.txt', 'w') as sagar:
	sagar.write("Hey guys I hope, are you fine!")