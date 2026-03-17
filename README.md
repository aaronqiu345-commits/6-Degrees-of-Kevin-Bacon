6 Degrees of Kevin Bacon 

To use this program, run in bash and type "python main.py" or "python3 main.py".

----------

main.py

Lets you run depthFinder.py, breadthFinder.py, and graphReader.py.

----------

data.txt

Holds movies and the actors that starred in them in a Movie|Actor|Actor|Actor (and so on) format.
Line break between movies.
If you want to change the data set, do it here.

----------

grapher.py

Turns each line from data.txt and puts it into a list, named (lines).
Takes each list from (lines) and makes a list of dictionaries out of them, named (neighborStorage).
Dictionaries with movies as keys have values of the actors starring in them, and vice versa.
A key's value is used to determine its node's neighbors.

Holds the Node class and uses data from (neighborStorage) to construct and link nodes.
Nodes are passed into the (nodeStorage) dictionary as: Node.data:Node

----------

graphReader.py

Uses the (Node) class and (nodeStorage) dictionary from grapher.py.
Reads out the entire graph from a starting node in a breadth-first-search format.

----------

depthFinder.py

Uses the (Node) class and (nodeStorage) dictionary from grapher.py.
Finds a path from the starting actor to the target actor in a depth-first-search format.

----------

breadthFinder.py

Uses the (Node) class and (nodeStorage) dictionary from grapher.py.
Finds a path from the starting actor to the target actor in a breadth-first-search format.