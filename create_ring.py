# This script creates a ring of 30 users

# Write the nodes
ring_users = open('ring_users.txt', 'w')
for i in range(0, 30):
	ring_users.write(str(i) + '\n')
ring_users.close()

# Write the edges
ring_relations = open('ring_relations.txt', 'w')
for i in range(0, 30):
	node = i
	adjacent_node = (i + 1) % 30
	ring_relations.write(str(node) + " coaches " + str(adjacent_node) + '\n')
	ring_relations.write(str(adjacent_node) + " is coached by " + str(node) + '\n')
ring_relations.close()