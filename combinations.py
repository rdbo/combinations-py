'''
[Visualization]
combination 0:
[ 'A', 'B', 'C', 'D' ]
   i    j    k
   0    1    2    3

c = [ 'A', 'B', 'C' ]

combination 1:
[ 'A', 'B', 'C', 'D' ]
   i    j         k
   0    1    2    3

c = [ 'A', 'B', 'D' ]

combination 2:
[ 'A', 'B', 'C', 'D' ]
   i         j    k
   0    1    2    3

c = [ 'A', 'C', 'D' ]

combination 3:
[ 'A', 'B', 'C', 'D' ]
        i    j    k
   0    1    2    3

c = [ 'B', 'C', 'D' ]

'''

def combinations(items : list, amount : int):
	combs = []
	nitems = len(items)

	if amount > nitems or amount == 0:
		return combs

	indices = [i for i in range(amount)]
	combs.append([items[i] for i in indices])

	while True:
		for i in reversed(range(amount)):
			if indices[i] != i + nitems - amount: # indices[i] is not at its max value, so break
				break
		else:
			break

		indices[i] += 1 # increment 1 to indices, as its not maxed out

		for j in range(i + 1, amount): # update all indices after i
			indices[j] = indices[j - 1] + 1
		
		combs.append([items[i] for i in indices]) # append current index list
	
	return combs
