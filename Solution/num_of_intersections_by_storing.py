#binary search algorithm 
def search(array, x):
	start = 0
	end = len(array) - 1
	while start <= end:
		mid = (start + end) // 2 
		if x == array[mid]:
			return mid
		elif x < array[mid]:
			end = mid-1
		else:
			start = mid + 1
	return -1

#ask user for input 
#alternatively, can set lists manually
radian_measures_str = input("Enter the radian measures (separated by spaces): ")
identifiers_str = input("Enter the identifiers (separated by spaces): ")
identifiers_split = identifiers_str.split()
identifiers = [int(i[1]) for i in identifiers_split]

n = len(identifiers)

id_values = {}
label = 1
for i in identifiers:
	if i not in id_values:
		id_values[i] = label
		label += 1

endpoints = []
nint = 0 
for i in range(n):
	if id_values[identifiers[i]] not in endpoints:
		endpoints.append(id_values[identifiers[i]])

	else:
		pos = search(endpoints, id_values[identifiers[i]])
		nint += len(endpoints)-pos-1
		endpoints.pop(pos)

print("Number of intersections =",nint)




