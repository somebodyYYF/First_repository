

def charCounter(text):
	array = {}
	array['upperCount'] = 0
	array['lowerCount'] = 0
	for char in text:
		if char.isupper():
			array['upperCount'] += 1
		elif char.islower():
			array['lowerCount'] += 1
	return array


print 'Input string'
message = raw_input()

result = charCounter(message);

print 'Uppercase chars count is: ' + str(result['upperCount'])
print 'Lowercase chars count is: ' + str(result['lowerCount'])