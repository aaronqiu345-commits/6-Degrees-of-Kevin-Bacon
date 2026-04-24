#import zone
from finders import depth, breadth, doubleBread, Node, nodeStorage
import time
import random
import string

#function zone

def makeGraph(file):
  lines = []
  with open(file, encoding="utf-8") as data:
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

def randomize(configFile, count):

  nums = string.digits
  times = count
  ids = set()
  line = []
  lines = []
  lastAct = None

  def addctor(id):
    nonlocal lastAct
    line.append(f"Actor{id}")
    lastAct = f"Actor{id}"

  def addvie(id):
    line.append(f"Movie{id}")

  for x in range(times):
    # digits = ''.join(random.choices(nums, k = digitCount))
    ids.add(x)
  print(ids)

  while len(ids) != 0:
    id = ids.pop() + 1
    RNG = random.randint(1, 4)
    if len(line) == 0:
      addvie(id)
      if lastAct:
        line.append(lastAct)
    else:
      addctor(id)

    if RNG == 1 and len(line) >= 3 or len(line) == 5:
      lines.append("|".join(line))
      line = []
      treeRNG = random.randint(1, 2)
      if treeRNG == 1 and len(ids) >= 3:
        brancher = lastAct
        branchRNG = random.randint(1, 3)
        for i in range(branchRNG):
          if len(ids) != 0:
            id = ids.pop() + 1
            addvie(id)
            line.append(f"{brancher}")
            leafRNG = random.randint(1, 2)
            for i in range(leafRNG):
              if len(ids) != 0:
                id = ids.pop() + 1
                addctor(id)

              else:
                print(line)
                lines.append("|".join(line))
                line = []
                break
            lines.append("|".join(line))
            line = []
          else:
            break

  if len(line) != 0:
    lines.append("|".join(line))
    line = []
  print(lines)

  with open(configFile, 'w', encoding="utf-8") as data:
    for line in lines:
      data.write(f"{line}\n")

  fileText = []
  with open(configFile, encoding="utf-8") as data:
    for line in data:
      fileText.append(line.strip().split("|"))
  print(fileText)
  print("Test case randomized.")




#main zone

mode = None
config = None
node1 = None
node2 = None
with open('config.txt') as data:
  for i, line in enumerate(data):
    if i == 0:
      mode = line.strip()
    if i == 1:
      config = line.strip()
    if i == 2:
      searchers = line.strip().split("|")
      node1 = searchers[0]
      node2 = searchers[1]

testCase = input("Would you like to randomize the config file? Type RANDOM if so. ")
if testCase.upper() == "RANDOM":
  nodeCount = int(input("How many IDs should be generated? "))
  randomize(config, nodeCount)

makeGraph(config)

timeStart = time.perf_counter()
if mode.upper() == "DFS":
  depth(node1, node2)
if mode.upper() == "BFS":
  breadth(node1, node2)
if mode.upper() == "2BFS":
  doubleBread(node1, node2)
timeEnd = time.perf_counter()
timeTotal = timeEnd - timeStart
print(f"Mode: {mode.upper()}")
print(f"Time taken: {timeTotal:.2f}")