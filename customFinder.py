from grapher import Node, nodeStorage
from collections import deque
startQueue = deque([])
targetQueue = deque([])
startVisited = set()
targetVisited = set()

def doubleBread(node, target):
  startQueue.append(node)
  targetQueue.append(target)
  timer = 0
  startVisited.add(node)
  while len(startQueue) != 0 and len(targetQueue) != 0:
    print(f"Visited 1: {startVisited}")
    print(f"Visited 2: {targetVisited}")
    if not startVisited.isdisjoint(targetVisited):
      print(f"path from {node} to {target} found")
      return
    while timer % 2 == 0:
      timer += 1
      startLayer = range(len(startQueue))
      for i in startLayer:
        startQue = [] # purely a debugging/console list
        for item in startQueue:
          startQue.append(item)
        print(f"Next up: {startQue}")
        startNext = startQueue.popleft()
        startNeigh = [] # purely a debugging/console list
        for neighbor in nodeStorage[startNext].neighbors:
          startNeigh.append(neighbor.data)
        print(f"Neighbors of {startNext}: {startNeigh}")
        startVisited.add(startNext)
        for neighbor in nodeStorage[startNext].neighbors:
          if neighbor.data not in startVisited and neighbor.data not in startQueue:
            startQueue.append(neighbor.data)
    while timer % 2 == 1:
      timer += 1
      targetLayer = range(len(targetQueue))
      for i in targetLayer:
        targetQue = [] # purely a debugging/console list
        for item in targetQueue:
          targetQue.append(item)
        print(f"Next up: {targetQue}")
        targetNext = targetQueue.popleft()
        targetNeigh = [] # purely a debugging/console list
        for neighbor in nodeStorage[targetNext].neighbors:
          targetNeigh.append(neighbor.data)
        print(f"Neighbors of {targetNext}: {targetNeigh}")
        targetVisited.add(targetNext)
        for neighbor in nodeStorage[targetNext].neighbors:
          if neighbor.data not in targetVisited and neighbor.data not in targetQueue:
            targetQueue.append(neighbor.data)
  return f"could not find {target}"