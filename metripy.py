# metripy
#
# Brief: mathematical metrics and all other ways of measuring
# things with Python can go in here for now.
#
# Author: Ron Rihoo
#

__all__ = ['intlen', 'intlenb']

# get the length of a base-10 integer number (the amount of digits)
def intlen(number):
  # if it's a negative number, then make it positive and carry on
	if number < 0:
		number = number*(-1)
	
	if number != 0:
		digits = 1
		while number > 9:
			number = number / 10
			digits = digits + 1
	else:
		digits = 0

	return digits
	
# get the length of an n-base integer number (the amount of digits)
def intlenb(number, base):
  # if it's in base-10 and a negative number, then make it positive and carry on
	if base == 10 and number < 0:
		number = number*(-1)
  # otherwise, if it's not in base-10 and it's a negative number, return 0 for now
	elif base != 10 and number < 0:
		print('Error: non-base-10 negative numbers are not yet supported by intlenb().')
		return 0
	
	if number != 0:
		digits = 1
		while number > (base - 1):
			number = number / base
			digits = digits + 1
	else:
		digits = 0

	return digits
