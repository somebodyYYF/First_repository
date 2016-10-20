summa = 0
cena_1 = 100
cena_2 = 200
cena_3 = 300

deneg = int(raw_input('skoka u vas deneg?>'))

kolichestvo_1 = raw_input('skoka tovara 1?>')
summa = summa + int(kolichestvo_1) * cena_1

kolichestvo_2 = raw_input('skoka tovara 2?>')
summa = summa + int(kolichestvo_2) * cena_2

kolichestvo_3 = raw_input('skoka tovara 3?>')
summa = summa + int(kolichestvo_3) * cena_3

if summa < 500:
	total = summa
else:
	total = summa * 0.9

if deneg < total:
	print 'nedostatochno sredstv'
elif deneg == total:
	print 'spasibo za pokupku'
else:
	sdacha = deneg - total
	print 'vasha sdacha ' + str(sdacha)

