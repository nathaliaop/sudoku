grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

n, m = 9, 9

compact = []
for i in range(n):
	for j in range(m):
		compact.append(grid[i][j])

# print(compact)

def to_adjacency(grid):
	adj = []
	for i in range(81):
		adj.append([])

	counter = 0;

	for i in range(n):
		for j in range(m):

			# row
			for k in range(9):
				if (k != j):
					adj[counter].append(grid[i][k])

			# columns
			for k in range(9):
				if (k != i):
					adj[counter].append(grid[k][j])

			# square
			# print(counter)
			# primeiro multiplo de 3 menor do que o número
			m3 = counter - (counter % 3)

			# linha e coluna do quadrado
			square_i = (m3 // 27) * 3
			square_j = m3 % 9

			# print(square_i, square_j)

			for a in range(square_i, square_i + 3):
				for b in range(square_j, square_j + 3):
					if (i != a) and (j != b):
						adj[counter].append(grid[a][b])



			counter += 1

	return adj

#adj = [
#		[1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 27, 36, 45, 54, 63, 72, 10, 11, 19, 20]
#	  ]

def valid_graph(grid, adj):

	# conferir se os numeros sao menores que 9
	ans = True
	for i in range(81):
		for k in range(1,9):
			if (adj[i].count(compact[i]) > 1 and compact[i] != 0):
				# print(compact[i], adj[i])
				# print(k, i, adj[i])
				ans = False

	return ans




#print(valid_matrix(grid))
adj = to_adjacency(grid)
# print(adj)
print(valid_graph(grid, adj))