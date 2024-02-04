#MergeSort algorithm:

#method to merge two lists together, so that the elements are in ascending order
#increase the number of inversions each time you swap two elements
def merge(a,b):
	inversions = 0
	sorted_list = [0]*(len(a) + len(b))
	len_a = len(a)
	len_b = len(b)
	mid_index = len_a
	i=0
	j=0
	k=0
	while i < len_a and j < len_b:
		if a[i] <= b[j]:
			sorted_list[k] = a[i]
			i += 1
			k+=1
		else:
			sorted_list[k] = b[j]
			inversions += (mid_index - i)
			j += 1
			k += 1
	while i < len(a):
		sorted_list[k] = a[i]
		i += 1
		k += 1
	while j < len(b):
		sorted_list[k] = b[j]
		j += 1 
		k += 1

	Inversions.increase(inversions)
	return sorted_list

#method to sort a list
def sort(a):

	if len(a) > 1:
		mid_index = len(a)//2
		left = a[:mid_index]
		right = a[mid_index:]
		
		left = sort(left)
		right = sort(right)

		return merge(left, right)

	else:
		return a

#class inversions 
#increments the number of inversions (static) when called during each merge 
class Inversions:
	number = 0

	def increase(new):
		Inversions.number += new
		return None

	#function reset to count only the relevant inversions
	def reset():
		Inversions.number = 0
		return None

#ask user for input 
#alternatively, can set lists manually
radian_measures_str = input("Enter the radian measures (separated by spaces): ")
identifiers_str = input("Enter the identifiers (separated by spaces): ")
#note that radian measures don't matter as they are sorted in the input
identifiers_split = identifiers_str.split()
n = len(identifiers_split)
identifiers = []
for i in range(n):
	identifiers.append(int(identifiers_split[i][1]))

#number the identifiers from 1 to n, based on which appear first
labels = {}
pos = 1
ids_labeled = []
for i in identifiers:
	if i not in labels:
		labels[i] = pos
	pos += 1
	ids_labeled.append(labels[i])

#count the number of inversions when sorting the endpoints such that s_1<e_1<...<s_n<e_n
#note that s_i and e_i can be in any order
Inversions.reset()
ids_sorted = sort(ids_labeled)
inv_total = Inversions.number

#separate the identifiers into starts and ends
starts = [0]*(n//2)
ends = [0]*(n//2)

ps = 0
pe = 0
for i in range (n):
	if ids_labeled[i] not in starts:
		starts[ps] = ids_labeled[i]
		ps += 1
	else:
		ends[pe] = ids_labeled[i]
		pe += 1

#count the number of inversions when sorting only ending endpoints to avoid counting intersections twice
Inversions.reset()
ends_sorted = sort(ends)
inv_ends = Inversions.number
print()
print("The total number of intersections is", inv_total - 2*inv_ends)



