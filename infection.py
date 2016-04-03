import re

# Input
# G is the graph representation of user base
# u is the user that starts infected

# Output 
# The set of users that would be infected

def total_infection(G, u):
	# R - the set of users that were newly infected after a time step
	# I - the set of infected users
	# B - after time step I, B is the set of all users adjacent to users in R from the previous time step
	R = set()
	I = set()
	B = set()

	# At time step 0
	I.add(u)
	R.add(u)

	while len(R) != 0:
		# Empty B after each time step
		B = set()
		for user in R:
			for adjacent_user in G[user]:
				B.add(adjacent_user)

		# R is the set of newly infected users. That is, the set of users in buffer set B but not in I.
		# I is the set of all infected users. So we add the newly infected users to I.
		R = B - I
		I = I | R

	return I

# Input
# G is the graph representation of user base
# amount is the amount of users we want to infect

# Output
# A subgraph of G, so that if any user in said subgraph is infected,
# then only the amount of users specified will be infected

def limited_infection(G, amount):
	# A set of users checked so far
	T = set()

	# The list of self-contained subgraphs of G
	C = []

	# The set of users in G
	U = set(G.keys())

	# While the set of checked users does not equal the set of users
	while T != U:
		# Choose a user from U that does not belong in T
		K = list(U - T)
		user = K[0]

		# Get the self-contained subgraph containing user
		I = total_infection(G, user)

		# Add our self contained subgraph to C
		C.append(I)

		T = T | I

	# Check each subgraph
	for clique in C:
		if len(clique) == amount:
			return clique

	# Since there was no match, we return the null set
	return set()

# Input
# users_file_name - The name of a file containing a list of users (Vertices)
# relations_file_name - The name of a file containing the relations between users (Edges)

# Output
# A graph G modeling the user base

def read_graph(users_file_name, relations_file_name):
	G = {}

	users_file = open(users_file_name, 'r')
	relations_file = open(relations_file_name, 'r')

	# First read in the users
	while True:
		U = users_file.readline().strip()

		if U == '':
			break

		G[U] = []
	users_file.close()

	regex = r'(.+)(coaches|is coached by)(.+)'
	# Now read in the relationships
	while True:
		R = relations_file.readline().strip()

		if R == '':
			break

		match = re.match(regex, R)

		if match:
			user_1 = match.group(1).strip()
			user_2 = match.group(3).strip()

			G[user_1].append(user_2)
	relations_file.close()

	return G