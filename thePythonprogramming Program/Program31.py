
#=======================================OS Moduls in Python=======================================

import os

'''
if(not os.path.exists("data")):
	os.mkdir(data)

for i in range(0,5):
	os.mkdir(f"data/Sagar{i+1}")		#To create new FOLDER in your OS using python "mkdir" method
'''

'''
for i in range(0,5):
	os.rename(f"data/Family{i+1}",f"data/Ro-heat Man sharma{i+1}")	#To rename of FOLDER in your OS using python "rename" method
'''

'''
folders = os.listdir("data")
for folder in folders:
	print(folder)			#Data folder in under how many folder available using "listdir" methos
'''

'''
folders = os.listdir("data")
for folder in folders:
	print(os.listdir(f"data/{folder}"))		#Using this mathod used to check folder in under how many file available
'''