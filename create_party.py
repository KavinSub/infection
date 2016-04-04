from itertools import combinations

# This script was written to generate a complete graph with 12 nodes
# Doing it manually would've taken forever :)

users = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

# Write the nodes to party
party_users = open('party_users.txt', 'w')
for user in users:
	party_users.write(user + '\n')
party_users.close()

# Write the relations to party
pairs = list(combinations(users, 2))
party_relations = open('party_relations.txt', 'w')
for node, adjacent_node in pairs:
	party_relations.write(node + " coaches " + adjacent_node + '\n')
	party_relations.write(adjacent_node + " is coached by " + node + '\n')
party_relations.close()