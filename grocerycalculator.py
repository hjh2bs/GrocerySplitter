#Hans He
#8/25/2015


import csv
import math


#Global Variables

reference1 = {'hjh': 'Hans', 'mhl': 'Megan', 'wl5': 'Wei', 'msq':'Michael', 'ss9':'Sarah'}
reference2 = {'Hans': 'hjh', 'Megan': 'mhl', 'Wei': 'wl5', 'Michael': 'msq', 'Sarah': 'ss9' }
reference3 = {'hjh': 0, 'mhl': 1, 'wl5': 2, 'msq':3, 'ss9':4}
reference4 = {0: 'Hans', 1: 'Megan', 2: 'Wei', 3: 'Michael', 4: 'Sarah'}

moneyChart = [[0 for x in range(5)] for x in range(5)]

def findCommas(str):
	tempIndex = []
	commaCount = 0
	for c in str:
		if c == ',':
			tempIndex.append(commaCount)
		commaCount += 1
	return tempIndex

def putNamesInList(str, index):
	nameList = []
	temp = 0
	for a in index:
		nameList.append(str[temp:a])
		temp = a + 2
	nameList.append(str[index[len(index)-1]+2:])
	return nameList	


def findMax(c, d):
	if moneyChart[c][d] > moneyChart[d][c]:
		return [c, d]
	else:
		return [d, c]


def moneyAggregate():

	for a in range(0, 5):
		for b in range(a, 5):
			maximum = findMax(a, b)
			moneyChart[maximum[0]][maximum[1]] = moneyChart[maximum[0]][maximum[1]] - moneyChart[maximum[1]][maximum[0]]
			moneyChart[maximum[1]][maximum[0]] = 0


with open('../Downloads/$$$ 116 A HYPESQUAD MONEY $$$ (Responses) - Form Responses 1.csv') as csvfile:
	moneyreader = csv.DictReader(csvfile)
	for row in moneyreader:
		totalCost = float(row['Cost'])*100			#Converts to cents
		

		if row['Does this include tax?'] == 'No': 		#Calculates tax
			totalCost += totalCost*.05
			#totalCost = round(totalCost)
			
		
		
		sharedBetween = row['This item is shared between:']
		indexOfComma = findCommas(sharedBetween)
		numberOfPeople = len(indexOfComma) + 1
		costPerPerson = totalCost / numberOfPeople
		costPerPerson = round(costPerPerson)


		totalCost /= 100					#Total costs in dollars
		costPerPerson /= 100				#Cost for each person


		people = putNamesInList(sharedBetween, indexOfComma)	#list of people that owe money


		collector = row['Username'][:3]
		
		for person in people:
			if reference2[person] != collector:
				moneyChart[reference3[collector]][reference3[reference2[person]]] += costPerPerson 


		moneyAggregate()


		print(people)				#Prints people item is shared between
		print 'Total Cost: ', totalCost	#Prints Total cost of item
		print 'Cost per person ', costPerPerson		#Prints cost per person
		print row['Username'][:3]
		
	for e in range (0, 5):
		for f in range(0, 5):
			if moneyChart[e][f] != 0:
				print reference4[f], 'pays $', moneyChart[e][f], 'to ', reference4[e]



		







