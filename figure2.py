import pickle
table = []

# M = size of subset
# Q = size of the target
# M, Q are the parameters for which you want to find the smearing prob P(M,Q)
# recall that this is the uniform distribution

# function
def main():
	global table 
	M, Q = map(int, raw_input().split())

	# try:
	# 	with open('recursion_table_2.pickle', 'rb') as handle:
	# 		table = pickle.load(handle)
	# 	# print 'opened pickle file'
	# 	# print table
	# except (OSError, IOError) as e:
	#     table = []
	#     with open('recursion_table_2.pickle', 'wb') as handle:
	#     	pickle.dump(table, handle, protocol=pickle.HIGHEST_PROTOCOL)
	table = []
	while (len(table) < M+1):
		# print "adding column"
		table.append([0])

	for i in range(M+1):
		while (len(table[i]) < Q+1):
			table[i].append(-1000)
			# print "adding element to column", i
	# print table 

	for q in range(Q+1):
		for m in range(q, M+1):
			f(m,q)
	# print table
	# return table[M,Q]
	with open('recursion_table_5.pickle', 'wb') as handle:
	    pickle.dump(table, handle, protocol=pickle.HIGHEST_PROTOCOL)

def factorial(n):
	if n < 0:
		print 'error, negative factorial'
	if n == 0:
		return 1
	else:
		f = 1
		while (n > 0):
			f = f*n
			n = n-1
		return f

# computes initial values for P on diagonal
def intial(m,q):
	if m == q:
		c = factorial(q)
		d = q**q
		ans = float(c)/d
		# table[m][q] = ans
		return ans
	else:
		print 'error, intial called on unequal m,q'

def f(m,q):
	if table[m][q] != -1000:
		return table[m][q] 
	else:
		if q == 0 or m == 0:
			ans = 0
		elif q == 1:
			ans = 1
		elif m == 1:
			ans = 1/float(q)
		elif m == q:
			ans = intial(m,q)
		else:
			a = f(m-1, q)
			k = (float(q-1)/q)**(m-1)
			b = f(m-1, q-1)
			ans = a + (k*b)
		table[m][q] = ans
		return ans

if __name__ == "__main__":
    main()
