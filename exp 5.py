# Python program to check
# if two lists have at-least
# one element common
# using traversal of list

def common_data(list1, list2):
	result = False

	# traverse in the 1st list
	for x in list1:

		# traverse in the 2nd list
		for y in list2:

			# if one common
			if x == y:
				result = True
				return result
				
	return result
	
# driver code
a = [1, 2, 3, 4]
b = [1, 2, 3,]
print(common_data(a, b))

