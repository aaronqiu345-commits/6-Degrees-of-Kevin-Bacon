from grapher import makeGraph
from graphReader import read
from breadthFinder import breadth
from depthFinder import depth
from customFinder import doubleBread
from datamaker import randomize

import time

testCase = input("Would you like to randomize the test case? Type Y if so. ")
if testCase.upper() == "Y":
  digits = input("How many numbers long should movie/actor IDs be? (Duplicate IDs are deleted.) ")
  nodeCount = input("How many IDs should be generated? ")
  randomize(digits, nodeCount)

makeGraph()
while True:
  todo = input("DFS, BFS, CUSTOM, or READ? ")
  if todo.upper() == "DFS":
    print("Depth-First-Search selected.")
    start = input("Where do you want to start from? ")
    target = input("Where do you want to end at? " )
    timeStart = time.perf_counter()
    depth(start, target)
    timeEnd = time.perf_counter()
    break
  elif todo.upper() == "BFS":
    print("Breadth-First-Search selected.")
    start = input("Where do you want to start from? ")
    target = input("Where do you want to end at? ")
    timeStart = time.perf_counter()
    breadth(start, target)
    timeEnd = time.perf_counter()
    break
  elif todo.upper() == "CUSTOM":
    print("Double-Breadth-Search selected.")
    start = input("Where do you want to start from? ")
    target = input("Where do you want to end at? ")
    timeStart = time.perf_counter()
    doubleBread(start, target)
    timeEnd = time.perf_counter()
  elif todo.upper() == "READ":
    print("Graph reading selected.")
    start = input("Where do you want to start from? ")
    timeStart = time.perf_counter()
    read(start)
    timeEnd = time.perf_counter()
    break
timeTotal = timeEnd - timeStart
print(f"Time taken: {timeTotal:.2f}")