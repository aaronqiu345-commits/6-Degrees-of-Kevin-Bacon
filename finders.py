#import zone
from collections import deque

#whats a node

class Node:
  def __init__(self, data):
    self.data = data
    self.neighbors = []
nodeStorage = {}

#function zone
dVisited = []
dPrev = {}
dPath = []
def depth(start, target):
  global dVisited
  global dPath
  if len(dVisited) == 0:
    dPath.append(start)
  if start in dVisited:
    return
  dVisited.append(start)
  if start == target:
      track = target
      revPath = []
      while track in dPrev:
        revPath.append(track)
        track = dPrev[track]
      revPath = revPath[::-1]
      dPath = dPath + revPath
      print(f"Found {target} in {len(dPath)-1} steps")
      print(f"Path: {dPath}")
      dVisited = []
      return True
  for neighbor in nodeStorage[start].neighbors:
    if neighbor.data not in dVisited:
      print(f"Searched {start}, rerunning on its neighbor {neighbor.data}")
      dPrev[neighbor.data] = start
      if depth(neighbor.data, target):
        return True

def breadth(start, target):
  queue = deque([start])
  visited = {start}
  prev = {}
  path = []
  while len(queue) != 0:
    layer = range(len(queue))
    print(f"Finished layer. Next up: {queue}")
    for i in layer:
      next = queue.popleft()
      visited.add(next)
      for neighbor in nodeStorage[next].neighbors:
        if neighbor.data not in prev and neighbor.data not in visited:
          prev[neighbor.data] = next
        if neighbor.data == target:
          track = neighbor.data
          while track in prev:
            path.append(track)
            track = prev[track]
          path.append(track)
          path = path[::-1]
          print(f"Path: {path}")
          print (f"Found {target} in {len(path)-1} steps")
          return
        if neighbor.data not in visited and neighbor.data not in queue:
          queue.append(neighbor.data)
  return f"Could not find {target}."

def constructPath(end1, prev1, end2, prev2):
  path = []
  track1 = end1
  track2 = end2
  while track1 in prev1:
    path.append(track1)
    track1 = prev1[track1]
  path.append(track1)
  path = path[::-1]
  while track2 in prev2:
    path.append(track2)
    track2 = prev2[track2]
  path.append(track2)
  return f"Path: {path}"

def visitAndQueue(data, visit, queue):
  visit.add(data)
  queue.append(data)

def doubleBread(node, target):
  startQueue = deque([node])
  targetQueue = deque([target])
  startVisited = {node}
  targetVisited = {target}
  startPrev = {}
  targetPrev = {}
  startLayers = 0
  targetLayers = 0
  timer = -1
  startVisited.add(node)
  while len(startQueue) != 0 and len(targetQueue) != 0:
    timer += 1
    if timer % 2 == 0:
      print(f"Iterating from start location: {startQueue}")
      startLayer = range(len(startQueue))
      startLayers += 1
      for i in startLayer:
        startNext = startQueue.popleft()
        startVisited.add(startNext)
        for neighbor in nodeStorage[startNext].neighbors:
          if neighbor.data in targetVisited:
            startPrev[neighbor.data] = startNext
            print(f"Path from {node} to {target} found in {startLayers + targetLayers} steps")
            print(constructPath(neighbor.data, startPrev, targetNext, targetPrev))
            return
          if neighbor.data not in startVisited:
            startPrev[neighbor.data] = startNext
            visitAndQueue(neighbor.data, startVisited, startQueue)
    if timer % 2 == 1:
      print(f"Iterating from target location: {targetQueue}")
      targetLayer = range(len(targetQueue))
      targetLayers += 1
      for i in targetLayer:
        targetNext = targetQueue.popleft()
        targetVisited.add(targetNext)
        for neighbor in nodeStorage[targetNext].neighbors:
          if neighbor.data in startVisited:
            targetPrev[neighbor.data] = targetNext
            print(f"path from {node} to {target} found in {startLayers + targetLayers}")
            print(constructPath(startNext, startPrev, neighbor.data, targetPrev))
            return
          if neighbor.data not in targetVisited:
            targetPrev[neighbor.data] = targetNext
            visitAndQueue(neighbor.data, targetVisited, targetQueue)
  return f"Could not find {target}"
