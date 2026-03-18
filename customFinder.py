from grapher import Node, nodeStorage
from collections import deque

def constructPath(end1, prev1, end2, prev2):
  print(prev1, prev2)
  path = []
  track1 = end1
  track2 = end2
  while track1 in prev1:
    print(f"appending {track1} to {path}")
    path.append(track1)
    track1 = prev1[track1]
  path.append(track1)
  path = path[::-1]
  while track2 in prev2:
    print(f"appending {track2} to {path}")
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
    print(startVisited)
    print(targetVisited)
    timer += 1
    if timer % 2 == 0:
      startLayer = range(len(startQueue))
      startLayers += 1
      for i in startLayer:
        startNext = startQueue.popleft()
        startVisited.add(startNext)
        for neighbor in nodeStorage[startNext].neighbors:
          if neighbor.data in targetVisited:
            startPrev[neighbor.data] = startNext
            print(f"path from {node} to {target} found in {startLayers + targetLayers}")
            print(neighbor.data)
            print(constructPath(neighbor.data, startPrev, targetNext, targetPrev))
            return
          if neighbor.data not in startVisited:
            startPrev[neighbor.data] = startNext
            visitAndQueue(neighbor.data, startVisited, startQueue)
    if timer % 2 == 1:
      targetLayer = range(len(targetQueue))
      targetLayers += 1
      for i in targetLayer:
        targetNext = targetQueue.popleft()
        targetVisited.add(targetNext)
        for neighbor in nodeStorage[targetNext].neighbors:
          if neighbor.data in startVisited:
            targetPrev[neighbor.data] = targetNext
            print(f"path from {node} to {target} found in {startLayers + targetLayers}")
            print(neighbor.data)
            print(constructPath(startNext, startPrev, neighbor.data, targetPrev))
            return
          if neighbor.data not in targetVisited:
            targetPrev[neighbor.data] = targetNext
            visitAndQueue(neighbor.data, targetVisited, targetQueue)
  return f"could not find {target}"