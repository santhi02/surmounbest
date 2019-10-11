with open('Book2.txt') as book:
	line = str(book.readlines())
#	line = line1.strip("['\\ufeffThe")
	words = line.split(' ')
	maxi = 0
	d1 = dict()
	d2 = dict()
#	for i in range(2000):
#		words.remove('')
	for i in words:
		if i not in d1:
			d1[i] = 1
		else:
			d1[i] += 1
	list_of_words = list(d1.keys())
	no_of_words = len(list_of_words)
	""" TASK 3.1 """
	print(list_of_words)
	"""	TASK 3.2 """
	print(no_of_words)
	"""	TASK 3.3 """
	for keys in d1.keys():
		d2[keys] = len(keys)
	for keys,values in d2.items():
		print (keys,values)
#		if values > maxi:
#			maxi = values
#	for keys,values in d1.items():
#		if values == maxi:
#			print (keys,values)


