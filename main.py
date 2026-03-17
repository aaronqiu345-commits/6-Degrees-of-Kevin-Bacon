from graphReader import read
from breadthFinder import breadth
from depthFinder import depth

while True:
  todo = input("DFS, BFS, or READ? ")
  if todo.upper() == "DFS":
    print("Depth-First-Search selected.")
    start = input("Where do you want to start from? ")
    target = input("Where do you want to end at? " )
    depth(start, target)
    break
  if todo.upper() == "BFS":
    print("Breadth-First-Search selected.")
    start = input("Where do you want to start from? ")
    target = input("Where do you want to end at? ")
    breadth(start, target)
    break
  if todo.upper() == "READ":
    print("Graph reading selected.")
    start = input("Where do you want to start from? ")
    read(start)
    break