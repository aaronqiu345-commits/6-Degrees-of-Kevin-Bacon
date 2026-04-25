6 Degrees of Kevin Bacon 

----------

config.txt

Holds the desired search type (line 1), file to search (line 2), start node, and target node (line 3).
It should read something like this:

DFS
data.txt
ActorStart|ActorFinish

Accepted methods for line 1 are DFS, BFS, and 2BFS.

----------

main.py

This is where you see your results and randomize the test case, if desired. Run in bash and type "python main.py" or "python3 main.py".
Reads the config file for the search type, file to search, and nodes to path between.

Upon opening, you will be asked if you would like to randomize the test case and with how large of a dataset. Type RANDOM if so, and anything else if not.

Builds the graph with information from the selected text file. After graph creation, the method in config line 1 is used to find a path between the 2 nodes indicated in config line 3.

----------

movie_data.txt

Holds movies and the actors that starred in them in a Movie|Actor|Actor|Actor (and so on) format.
Line break between movies.
If you want to change the data set, do it here.

----------

finders.py

depth()

Uses the (Node) class and (nodeStorage) dictionary from grapher.py.
Finds a path from the starting actor to the target actor in a depth-first-search format.


breadth()

Uses the (Node) class and (nodeStorage) dictionary from grapher.py.
Finds a path from the starting actor to the target actor in a breadth-first-search format.


doubleBread()

Uses the (Node) class and (nodeStorage) dictionary from grapher.py.
Starts breadth-first-search from two different points, then stops when their visited sets start overlapping.
