from main import Node, nodeStorage
visited = []
prev = {}
path = []
def depth(start, target):
  global visited
  global path
  if len(visited) == 0:
    print(path)
    path.append(start)
  if start in visited:
    return
  visited.append(start)
  if start == target:
      track = target
      revPath = []
      while track in prev:
        revPath.append(track)
        track = prev[track]
      revPath = revPath[::-1]
      path = path + revPath
      print(f"Found {target} in {len(path)-1} steps")
      print(f"Path: {path}")
      visited = []
      return True
  for neighbor in nodeStorage[start].neighbors:
    if neighbor.data not in visited:
      print(f"Searched {start}, rerunning on its neighbor {neighbor.data}")
      prev[neighbor.data] = start
      if depth(neighbor.data, target):
        return True
