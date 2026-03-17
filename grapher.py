from dictionaries import neighborStorage
class Node:
  def __init__(self, data):
    self.data = data
    self.neighbors = []
nodeStorage = {}

for node in neighborStorage:
  print(f"made node {node}")
  makeNode = Node(node)
  nodeStorage[node] = makeNode

print(nodeStorage)
for node in nodeStorage:
  for connect in neighborStorage[node]:
    nodeStorage[node].neighbors.append(nodeStorage[connect])
    print(f"connected {connect} to {node}.")