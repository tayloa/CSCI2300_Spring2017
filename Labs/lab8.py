import numpy as np

def edit_distance(x,y):
	#insert cost = 1, E[i-1,j]
	#delete cost = 1, E[i,j-1]
	#replace cost = 0 or 1 depending on difference E[i-1,j-1]
	align1 = ""
	align2 = ""
	m,n = len(x)+1, len(y)+1
	E = np.zeros((m, n))
	path = []
	for i in range(0,m):
		E[i][0]=i
	for j in range(0,n):
		E[0][j]=j
	for i in range(1,m):
		for j in range(1,n):
			diff = 1
			if (x[i-1] == y[j-1]): diff = 0
			E[i][j] = min(1 + E[i-1, j], 1 + E[i, j-1], diff + E[i-1, j-1])

	i,j = m-1,n-1
	while i > 0 or j > 0:
			top = E[i-1, j]
			left = E[i, j-1]
			diagnol = E[i-1, j-1]
			min_cost = min(top,left,diagnol)
			if min_cost == diagnol: 
				align1+= x[i-1]
				align2+= y[j-1]
				i-=1
				j-=1
			elif min_cost == left: 
				align1+= "-"
				align2+=y[j-1]
				j-=1
			elif min_cost == top: 
				align1+= x[i-1]
				align2+="-"
				i-=1
	# ptint the reverse
	print(align1[::-1])
	print(align2[::-1])
	return int(E[m-1, n-1])

if __name__ == "__main__":
	
	result = edit_distance("EXPONENTIAL","POLYNOMIAL")
	result = edit_distance("CATAAGCTTCTGACTCTTACCTCCCTCTCTCCTACTCCTGCTCGCATCTGCTATAGTGGAGGCCGGAGCAGGAACAGGTTGAACAG",
	 "CGTAGCTTTTTGGTTAATTCCTCCTTCAGGTTTGATGTTGGTAGCAAGCTATTTTGTTGAGGGTGCTGCTCAGGCTGGATGGA")
	print("edit distance =",result)