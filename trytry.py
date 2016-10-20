def speed(km, hour):
	a = km * hour
	b = a <= 4
	c = a > 4
	if b:
		print (a, 'kilometra')
	elif c:
		print (a, 'kilometra')

speed(int(input('skorost ')),int(input('vremya ')))