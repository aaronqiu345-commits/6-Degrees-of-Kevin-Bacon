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

  times = count
  ids = set()
  line = []
  lines = []
  lastAct = None
  uniqueActors = set()
  webRNG = random.randint(1, 4)
  freqRNG = random.randint(0, 2)

  def addctor(id):
    nonlocal lastAct
    line.append(f"Actor{id}")
    lastAct = f"Actor{id}"

  def addvie(id):
    line.append(f"Movie{id}")

  for x in range(times):
    ids.add(x)

  while len(ids) != 0:
    id = ids.pop() + 1
    lenRNG = random.randint(1, 4)
    if len(line) == 0:
      addvie(id)
      if lastAct:
        line.append(lastAct)
    else:
      addctor(id)
    if lenRNG == 1 and len(line) >= 4 or len(line) == 6:
      if len(uniqueActors) > 1:
        if (webRNG - freqRNG) > 0:
          totalWeb = random.randint(0, webRNG - freqRNG)
          if totalWeb < len(uniqueActors):
            print(f"rolled {totalWeb} webs")
            for x in range(totalWeb):
              randAct = random.choice(tuple(uniqueActors))
              while randAct in line:
                print(f"double web {randAct}, gotta reroll")
                randAct = random.choice(tuple(uniqueActors))
              print(f"webbing {randAct} to {line}")
              line.append(randAct)
      for actor in line[1:]:
        uniqueActors.add(actor)
      lines.append("|".join(line))
      print(f"adding line {line}")
      line = []
      
  if len(line) != 0:
    lines.append("|".join(line))
    line = []
  print(lines)

  with open(configFile, 'w', encoding="utf-8") as data:
    for line in lines:
      data.write(f"{line}\n")

  print("Test case randomized.")
  print("Final dataset:")
  for movie in lines:
    print(movie)


  if (webRNG - freqRNG) < 1:
    print(f"totalWeb rolled less than 1, no webs were made")
  else:
    print(f"totalWeb range was 0 to {webRNG - freqRNG}")



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
  reroll = "Y"
  while reroll.upper() == "Y":
    nodeCount = int(input("How many IDs should be generated? "))
    randomize(config, nodeCount)
    reroll = input("Do you want to generate another test case? If so, type Y.")
  if reroll != "Y":
    while True:
      display = input("Test case finalized. Modify config.txt with new starting and ending node." )

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
