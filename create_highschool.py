from itertools import combinations

users = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# This script was created to generate the highschool graph
# It consists of complete graphs k = 3 to k = 8

# Generate the users file
highschool_users = open('highschool_users.txt', 'w')
for i in range(3, 9):
	for j in range(0, i):
		user = users[j] * (i - 2)
		highschool_users.write(user + '\n')

highschool_users.close()

# Generate relations file
highschool_relations = open('highschool_relations.txt', 'w')
for i in range(3, 9):
	users_set = []
	for j in range(0, i):
		user = users[j] * (i - 2)
		users_set.append(user)

	pairs = list(combinations(users_set, 2))

	for node, adjacent_node in pairs:
		highschool_relations.write(node + " coaches " + adjacent_node + '\n')
		highschool_relations.write(adjacent_node + " is coached by " + node + '\n')

highschool_relations.close()