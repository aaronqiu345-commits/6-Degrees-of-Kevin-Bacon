#import zone
from breadthFinder import breadth
from depthFinder import depth
from customFinder import doubleBread
import time
import random
import string

#whats a node

class Node:
  def __init__(self, data):
    self.data = data
    self.neighbors = []
nodeStorage = {}

#function zone

def makeGraph():
  lines = []
  with open('data.txt') as data:
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

def default():
  with open('data.txt', 'w') as data:
    data.write('Movie1|Actor2|Actor3|Actor4|Actor5\n')
    data.write('Movie6|Actor5|Actor7\n')
    data.write('Movie8|Actor7|Actor9\n')
    data.write('Movie10|Actor9|Actor11|Actor12\n')
    data.write('Movie11|Actor7|Actor13|Actor14\n')
  print("Test case reset.")

def randomize(count):

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

  with open('data.txt', 'w') as data:
    for line in lines:
      data.write(f"{line}\n")

  file = []
  with open('data.txt') as data:
    for line in data:
      file.append(line.strip().split("|"))
  print(file)
  print("Test case randomized.")




#main zone

testCase = input("Would you like to randomize or reset the test case? Type RANDOM or RESET if so. ")
if testCase.upper() == "RANDOM":
  nodeCount = int(input("How many IDs should be generated? "))
  randomize(nodeCount)
if testCase.upper() == "RESET":
  default()

makeGraph()
while True:
  todo = input("DFS, BFS, or CUSTOM? ")
  if todo.upper() == "DFS":
    print("Depth-First-Search selected.")
    start = input("Where do you want to start from? ")
    target = input("Where do you want to end at? " )
    timeStart = time.perf_counter()
    depth(start, target)
    timeEnd = time.perf_counter()
    timeTotal = timeEnd - timeStart
    print(f"Time taken: {timeTotal:.2f}")
  elif todo.upper() == "BFS":
    print("Breadth-First-Search selected.")
    start = input("Where do you want to start from? ")
    target = input("Where do you want to end at? ")
    timeStart = time.perf_counter()
    breadth(start, target)
    timeEnd = time.perf_counter()
    timeTotal = timeEnd - timeStart
    print(f"Time taken: {timeTotal:.2f}")
  elif todo.upper() == "CUSTOM":
    print("Double-Breadth-Search selected.")
    start = input("Where do you want to start from? ")
    target = input("Where do you want to end at? ")
    timeStart = time.perf_counter()
    doubleBread(start, target)
    timeEnd = time.perf_counter()
    timeTotal = timeEnd - timeStart
    print(f"Time taken: {timeTotal:.2f}")
  elif todo.upper() == "READ":
    print("Graph reading selected.")
    start = input("Where do you want to start reading from? ")
    read(start)
