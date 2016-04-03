import unittest
from infection import total_infection, limited_infection, read_graph

# G looks like this
#				A     I    H	   J         
#              / \     \  /       / \
#			  B   C     G        K   L
#            /  \  \   /
#           D    E   F

G = {"A": ["B", "C"],
	 "B": ["A", "D", "E"],
	 "C": ["A", "F"],
			 "D": ["B"],
			 "E": ["B"],
			 "F": ["C", "G"],
			 "G": ["F", "I", "H"],
			 "H": ["G"],
			 "I": ["G"],
			 "J": ["K", "L"],
			 "K": ["J"],
			 "L": ["J"]}

class InfectionTest(unittest.TestCase):
	def test_read_graph(self):
		read_in_G = read_graph('users.txt', 'relations.txt')

		# First check that the vertices of the graph are same
		self.assertEqual(set(G.keys()), set(read_in_G.keys()))
		
		# Now check that the edges are the same
		keys = list(G.keys())
		keys.sort()

		for key in G.keys():
			g_edges = set(list(G[key]))

			rg_edges = set(list(read_in_G[key]))
			
			self.assertEqual(g_edges, rg_edges)


	def test_total_infection_case_1(self):
		I = total_infection(G, "C")

		self.assertEqual(set(["A", "B", "C", "D", "E", "F", "G", "H", "I"]), I)

	def test_total_infection_case_2(self):
		I = total_infection(G, "J")

		self.assertEqual(set(["J", "K", "L"]), I)

	def test_limited_infection_case_1(self):
		I = limited_infection(G, 3)

		self.assertEqual(set(["J", "K", "L"]), I)

	def test_limited_infection_case_2(self):
		I = limited_infection(G, 9)

		self.assertEqual(set(["A", "B", "C", "D", "E", "F", "G", "H", "I"]), I)

	def test_limited_infection_case_3(self):
		I = limited_infection(G, 5)

		self.assertEqual(set(), I)

if __name__ == '__main__':
	unittest.main()