import numpy as np
import time 
def read_input():
	r1, c1, r2, c2 = [int(x) for x in input().split(" ")]
	m1 = []
	m2 = []
	for _ in range(0, r1):
		m1.append([int(x) for x in input().split(" ")])
	for _ in range(0, r2):
		m2.append([int(x) for x in input().split(" ")])
	return m1, m2

def my_imp_matrix_mult(m1 , m2):
	transpose_m2 = list(map(list, zip(*m2)))
	res = []
	for row in m1:
		this_row = []
		for col in transpose_m2:
			this_row.append(sum([a*b for a,b in zip(row,col)]))
		res.append(this_row)
	return res

def numy_matrix_mul(m1, m2):
	res = np.matmul(m1, m2)
	return res

def compare_outputs(res1, res2):
	for rowInd in range(0, len(res1)):
		for colInd in range(0, len(res1)):
			if not res1[rowInd][colInd] == res2[rowInd][colInd]:
				print('WRONG OUTPUT')
				exit()

def print_output(res):
	for r in res:
		print(' '.join(map(str, r)))

if __name__ == '__main__':
	m1, m2 = read_input()
	my_imp_start = time.time()
	res1 = my_imp_matrix_mult(m1 , m2)
	my_imp_end = time.time()
	numpy_start = time.time()
	res2 = numy_matrix_mul(m1, m2)
	numpy_end = time.time()
	print_output(res1)
	diff = (my_imp_end - my_imp_start) - (numpy_end - numpy_start)
	print('Time difference: %.2f' %diff)
	compare_outputs(res1, res2)