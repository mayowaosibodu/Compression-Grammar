'''
An attempt to achive useful compression by employing exponentiation as 
a grammar, to specify what subset of integers are valid compression indexes.

'''

#Degrees of exponentiation.

grammar_kernels = [2.,3.,4.,5.,6.,7.,8.,9.,10.]


def express(number, kernel_index):
	#Express the given number in the language defined by the given degree of exponentiation.

	kernel = grammar_kernels[kernel_index]

	expressed = ''

	while number > 0:

		root = (number)**(1/kernel)
		root_whole = int(root)
		expressed += str(root_whole)
		number -= root_whole**kernel

	return expressed


def get_trend(kernel_index):
	#Derive the trend lines describing 'Length of compression Index' vs 'Length of uncompressed target'.

	trend = []

	for step in range(0, 100000000, 5000):

		trend.append(len(express(step, kernel_index)))

	return trend


from matplotlib import pyplot as plt


def run():

	base_trend = [len(str(step)) for step in range(0, 100000000, 5000)]
	for index in range(len(grammar_kernels)):

		print 'Running for index:', index

		plt.plot(base_trend, get_trend(index))


	plt.legend(['Trend line for kernel:'+ str(grammar_kernels[index]) for index in range(len(grammar_kernels))])
	plt.show()

run()