grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

class Sudoku():
	def __init__(self, grid):
		self.adj = []
		self.valid = True
		self.all_vertices = []
		self.grid = grid

	def add_vertices(self):
		for i in range(9):
			for j in range(9):
				self.all_vertices.append(self.grid[i][j])

		return self.all_vertices

	def build_adjacency(self):
		for i in range(81):
			self.adj.append([])

		counter = 0;

		for i in range(9):
			for j in range(9):

				# row
				for k in range(9):
					if (k != j):
						self.adj[counter].append(self.grid[i][k])

				# columns
				for k in range(9):
					if (k != i):
						self.adj[counter].append(self.grid[k][j])

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
							self.adj[counter].append(self.grid[a][b])

				counter += 1

		return self.adj

	def is_valid(self):
		# confere se os valor dos vértices são menores ou iguais a 9
		for vertex in self.all_vertices:
			if (vertex < 0) or (vertex > 9):
				self.valid = False

		for i in range(81):
			for k in range(1,9):
				if (self.adj[i].count(self.all_vertices[i]) > 1 and self.all_vertices[i] != 0):
					self.valid = False

		return self.valid

	def solve():
		pass

sudoku = Sudoku(grid)
sudoku.add_vertices()
adj = sudoku.build_adjacency()
valid = sudoku.is_valid()

print(valid)