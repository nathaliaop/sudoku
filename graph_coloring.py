from random import shuffle, randint

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

grid2 = [
        [8, 0, 0, 1, 5, 0, 6, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 4, 1],
        [5, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 6, 2],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [1, 4, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 9],
        [2, 9, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 5, 0, 9, 7, 0, 0, 6],
    ]

grid3 = [
	[0, 0, 0, 1, 5, 0, 6, 0, 0],
	[0, 0, 0, 3, 0, 0, 0, 4, 1],
	[0, 0, 0, 0, 0, 0, 7, 0, 0],
	[0, 0, 0, 0, 0, 9, 0, 6, 2],
	[0, 0, 0, 0, 3, 0, 0, 0, 0],
	[0, 0, 0, 8, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 9],
	[2, 9, 0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 7, 0, 0, 6],
]

class Sudoku():
	def __init__(self, grid):
		self.grid = grid
		self.vertices_colors = []
		self.adj = []
		self.valid = True
		self.found = False

	def add_vertices(self):
		for i in range(9):
			for j in range(9):
				self.vertices_colors.append(self.grid[i][j])

		return self.vertices_colors

	def build_adjacency(self):
		for i in range(81):
			self.adj.append([])

		counter = 0;

		for i in range(9):
			for j in range(9):

				# row
				for k in range(9):
					if (k != j):
						self.adj[counter].append(9*i + k)

				# columns
				for k in range(9):
					if (k != i):
						self.adj[counter].append(9*k + j)

				# square
				square_i = i - i%3
				square_j = j - j%3

				for a in range(square_i, square_i + 3):
					for b in range(square_j, square_j + 3):
						if (i != a) and (j != b):
							self.adj[counter].append(9*a + b)

				counter += 1

		return self.adj

	def is_valid(self):
		# confere se os valor dos vértices são menores ou iguais a 9
		for vertex in self.vertices_colors:
			if (vertex < 0) or (vertex > 9):
				self.valid = False

		# confere os números 
		for i in range(81):
			for k in range(1,9):
				if (self.adj[i].count(self.vertices_colors[i]) > 1 and self.vertices_colors[i] != 0):
					self.valid = False

		return self.valid

	def color(self, x):
			if x >= 81:
				self.found = True
				return

			if self.vertices_colors[x] != 0:
				self.color(x + 1)
				return

			neighbours_colors = list(set([self.vertices_colors[k] for k in self.adj[x]]))
			total_colors = [i for i in range(1, 10)]
			shuffle(total_colors)
			available_colors = [item for item in total_colors if item not in neighbours_colors]

			for c in available_colors:
				self.vertices_colors[x] = c
				self.color(x + 1)

				if self.found:
					return

				self.vertices_colors[x] = 0

	def build_grid(self):
		for i in range(81):
			self.grid[i//9][i%9] = self.vertices_colors[i]

		return self.grid

	def random_sudoku(self):
		# empty_grid = [[0] * 9 for _ in range(9)]
		# reseta parâmetros
		self.vertices_colors = [0]*81
		self.valid = True
		self.found = False

		self.color(0)

		for i in range(81):
			number = randint(1, 10)
			if number <= 7:
				self.vertices_colors[i] = 0

		return self.build_grid()

sudoku = Sudoku(grid)
sudoku.add_vertices()
adj = sudoku.build_adjacency()
valid = sudoku.is_valid()
sudoku.color(0)
print(sudoku.is_valid())
print(sudoku.build_grid())
print(sudoku.random_sudoku())