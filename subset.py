from itertools import combinations      #import the itertools module to use the combinations function

x = input('\nEnter the the Set: ') 	#enter a string of numbers. They can be separated by commas or can be input as a single string

x = x.replace(',','') 			#This basically removes commas if they are there and replaces them with whitespace

s = list(x) 				#Make a list so that the elements of the set of numbers become iterable
print('\nEntered Set is:',s,'\n')	#This is pretty self explanatory

print('All subsets of the given subset are:\n')
for n in range(len(x)+1):		#Here i am iterating n from 0 to the length of the string to get all possible variations of the 
	print(list(combinations(s,n)))	#set. 


