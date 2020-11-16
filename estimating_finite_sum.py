from math import *

class func_struct:
	def __init__(self, f):
		self.f = f

	def return_val(self, val):
		x = val # i can't find a way quickly enough to work around the different variable so you now have to work with `x` only
		return eval(self.f)

def lower_sum(f: func_struct, MIN, MAX, INTERVAL_NUM):
	interval_val = (MAX - MIN) / INTERVAL_NUM

	total_sum = 0
	for i in range(INTERVAL_NUM):
		x = MIN + interval_val * (i+1) # modifiers only work for decreasing functions or decreasing sections of a function, at the increasing parts, modifiers for lower and upper here have to switch
		total_sum += abs(f.return_val(x) * interval_val)

	return total_sum, (total_sum / INTERVAL_NUM)

def upper_sum(f: func_struct, MIN, MAX, INTERVAL_NUM):
	interval_val = (MAX - MIN) / INTERVAL_NUM

	total_sum = 0
	for i in range(INTERVAL_NUM):
		x = MIN + interval_val * (i)
		total_sum += abs(f.return_val(x) * interval_val)

	return total_sum, (total_sum / INTERVAL_NUM)

def midpoint_sum(f: func_struct, MIN, MAX, INTERVAL_NUM):
	interval_val = (MAX - MIN) / INTERVAL_NUM

	total_sum = 0
	for i in range(INTERVAL_NUM):
		x = MIN + interval_val * (i+0.5)
		total_sum += abs(f.return_val(x) * interval_val)

	return total_sum, (total_sum / INTERVAL_NUM)

def find_interval_num(MAX, MIN, interval_val):
	return (MAX - MIN) / interval_val

def main(_F, MIN, MAX, INTERVAL_NUM):
	obj = func_struct(_F)

	lower_sum_total, lower_sum_avg = lower_sum(obj, MIN, MAX, INTERVAL_NUM)
	upper_sum_total, upper_sum_avg = upper_sum(obj, MIN, MAX, INTERVAL_NUM)
	midpoint_sum_total, midpoint_sum_avg = midpoint_sum(obj, MIN, MAX, INTERVAL_NUM)

	print(f'From `{MIN}` to `{MAX}`')
	print(f'INTERVAL VALUE: `{(MAX - MIN) / INTERVAL_NUM}`; INTERVAL NUMBER: `{INTERVAL_NUM}`')
	print(f'LOWER SUM: `{lower_sum_total}`')
	print(f'UPPER SUM: `{upper_sum_total}`')
	print(f'MIDPOINT SUM: `{midpoint_sum_total}`')

# edit your values here
# `**` means `to the power of` like `x**2` is `x square`
# be descriptive, instead of `6x` try `6*x`
if __name__ == '__main__':
	_F = "sin(x)"
	INTERVAL_NUM = 10000 # in case you know interval value but not number, use find_interval_num()
	MIN = 0
	MAX = 2*pi

	main(_F, MIN, MAX, INTERVAL_NUM)