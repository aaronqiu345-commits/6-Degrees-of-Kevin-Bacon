from grapher import Node, nodeStorage
from collections import deque
def breadth(start, target):
  queue = deque([start])
  visited = {start}
  prev = {}
  path = []
  while len(queue) != 0:
    layer = range(len(queue))
    print(f"finished layer. next up: {queue}")
    for i in layer:
      next = queue.popleft()
      visited.add(next)
      for neighbor in nodeStorage[next].neighbors:
        if neighbor.data not in prev and neighbor.data not in visited:
          prev[neighbor.data] = next
          print(prev)
        if neighbor.data == target:
          track = neighbor.data
          while track in prev:
            path.append(track)
            track = prev[track]
          path = path[::-1]
          print(f"Path: {path}")
          return f"Found {target} in {len(path)-1} steps"
        if neighbor.data not in visited and neighbor.data not in queue:
          queue.append(neighbor.data)
  return f"Could not find {target}"