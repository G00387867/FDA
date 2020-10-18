
# Adam Shaat
# a Python function calledcountsthat takes a list as input 
# and returns a dictionary of unique items in the list as keys and the number of times each item appears as values

# reference: https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/
# Python program to count the frequency of 
# elements in a list using a dictionary 

def CountFrequency(my_list): 

	# Creating an empty dictionary 
	freq = {} 
	for item in my_list: 
		if (item in freq): 
			freq[item] += 1
		else: 
			freq[item] = 1

	for key, value in freq.items(): 
		print ("%d  : %d "%(key, value))


# Driver function 
if __name__ == "__main__": 
	my_list =  [1, 1, 5, 5, 3, 1, 3, 3, 4, 4, 2, 2, 2]

	CountFrequency(my_list) 

#--------------------------------------------------------------------------

# reference : https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list

items = [1, 1, 5, 5, 3, 1, 3, 3, 4, 4, 2, 2, 2, "A", "A", "B", "a", "red"] 

counts = dict()
for i in items:
  counts[i] = counts.get(i, 0) + 1

print(counts)

# -----------------------------------------------------------------------------

# Reference: https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list

Items = [1, 1, 5, 5, 3, 1, 3, 3, 4, 4, 2, 2, 2, "A", "A", "B", "a"]

stats = {}
for i in Items:
    if i in stats:
        stats[i] += 1
    else:
        stats[i] = 1

# bonus
for i in sorted(stats, key=stats.get):
    print("%d×'%s'" % (stats[i], i))