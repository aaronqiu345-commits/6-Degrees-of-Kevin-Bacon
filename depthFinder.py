from grapher import Node, nodeStorage
visited = []
def depth(start, target):
  global visited
  if start in visited:
    return
  visited.append(start)
  for neighbor in nodeStorage[start].neighbors:
    if neighbor.data == target:
      print(f"found {target} as a neighbor of {start}")
      visited = []
      return True
    if neighbor.data not in visited:
      print(f"searched {start}, rerunning its {neighbor.data}")
      if depth(neighbor.data, target):
        return True