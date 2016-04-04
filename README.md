# infection
The project based interview assignment for Khan Academy.

The web visualization can be accessed here:
https://infection-project-ka.herokuapp.com/

To perform a total infection, click the total infection button and select a node.

To perform a limited infection, first enter a number in the text field, then click limited infection.

From the drop-down menu you can choose from some given visualizations.

To use total_infection, and limited_infection with python code, take a look at infection.py.
The only functions you need to use are read_graph, total_infection, and limited_infection.

First you need to call read_graph:
G = read_graph(user_file, user_relations_file)

For the user file, just create a text file with a list of nodes, each node being on a separate line.
Like:
A
B
C
.
.
.
Z

For relations file, you need to specify the relationships between users so a proper graph can be generated.
The file will consist of lines like:
A coaches B
B is coached by A

So if A is a teacher, and B, C are the students your file will look like:
A coaches B
A coaches C
B is coached by A
C is coached by A

Once you have a read in a graph from the files, you just need to call total_infection, or limited_infection.
Everything put together, you should have something that looks like:

G = read_graph(user_file, user_relations_file)

S = total_infection(G, user) # Where user is some node in G
I = limited_infection(G, amount) # Where amount is an integer

S, I are sets containing the users that will be infected.

One thing to note about limited infection is that set I will be empty if there is no set of nodes fulfilling the criteria 
of only having amount nodes be infected.
