# This script creates a ring of 30 users

# Write the nodes
ring_users = open('ring_users.txt', 'w')
for i in range(0, 30):
	ring_users.write('A' + str(i) + '\n')
ring_users.close()

# Write the edges
ring_relations = open('ring_relations.txt', 'w')
for i in range(0, 30):
	node = 'A' + str(i) 
	adjacent_node = 'A' + str((i + 1) % 30)
	ring_relations.write(node + " coaches " + adjacent_node + '\n')
	ring_relations.write(adjacent_node + " is coached by " + node + '\n')
ring_relations.close()