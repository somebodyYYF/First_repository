def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1,arg2)

def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_one(arg1):
	print "i got nothink'."

print_two('Zed','shaw')
print_two_again('Zed','shaw')
print_one('first')
