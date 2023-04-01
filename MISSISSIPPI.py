frequent = {"I":0,"S":0,"P":0,"M":0}
word = "MISSISSIPPI"
for i in word:
	if i == "M":
		frequent['M'] = frequent['M']+1
	elif i == "I":
		frequent['I'] = frequent['I']+1
	elif i == "S":
		frequent['S'] = frequent['S']+1
	elif i == "P":
		frequent['P'] = frequent['P']+1
print (frequent)