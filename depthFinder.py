from grapher import Node, nodeStorage
visited = []
def depth(start, target, path):
  global visited
  path = path
  path.append(start)
  if start in visited:
    return
  visited.append(start)
  if start == target:
      print(f"Found {target} in {len(path)-1} steps")
      print(f"Path: {path}")
      visited = []
      return True
  for neighbor in nodeStorage[start].neighbors:
    if neighbor.data not in visited:
      print(f"Searched {start}, rerunning its neighbor {neighbor.data}")
      if depth(neighbor.data, target, path):
        return True