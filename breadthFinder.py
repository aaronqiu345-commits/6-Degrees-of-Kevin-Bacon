from grapher import Node, nodeStorage
from collections import deque
queue = deque([])
visited = []
def breadth(start, target):
  queue = deque([start])
  visited = []
  while len(queue) != 0:
    layer = range(len(queue))
    for i in layer:
      que = [] # purely a debugging/console list
      for item in queue:
        que.append(item)
      print(f"Next up: {que}")
      next = queue.popleft()
      neigh = [] # purely a debugging/console list
      for neighbor in nodeStorage[next].neighbors:
        neigh.append(neighbor.data)
      print(f"Neighbors of {next}: {neigh}")
      visited.append(next)
      for neighbor in nodeStorage[next].neighbors:
        if neighbor.data == target:
          return f"found {target} as a neighbor of {nodeStorage[next].data}"
        if neighbor.data not in visited and neighbor.data not in queue:
          queue.append(neighbor.data)
  return f"could not find {target}"