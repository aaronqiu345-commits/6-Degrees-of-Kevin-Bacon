class Node:
  def __init__(self, data):
    self.data = data
    self.neighbors = []
nodeStorage = {}

def makeGraph():
  lines = []
  with open('data.txt') as data:
    for line in data:
      lines.append(line.strip().split("|"))
  print(lines)

  neighborStorage = {}
  for movie in lines:
    neighborStorage[movie[0]] = movie[1:]

  for movie in lines:
    for actor in movie[1:]:
      if actor not in neighborStorage:
        neighborStorage[actor] = [movie[0]]
      else:
        neighborStorage[actor].append(movie[0])

  for node in neighborStorage:
    makeNode = Node(node)
    nodeStorage[node] = makeNode

  for node in nodeStorage:
    for connect in neighborStorage[node]:
      nodeStorage[node].neighbors.append(nodeStorage[connect])