from itertools import combinations

x = input('\nEnter the the Set: ')

x = x.replace(',','')

s = list(x)
print('\nEntered Set is:',s,'\n')

print('All subsets of the given subset are:\n')
for n in range(len(x)+1):
	print(list(combinations(s,n)))


