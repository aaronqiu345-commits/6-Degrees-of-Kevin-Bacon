from grapher import makeGraph
from graphReader import read
from breadthFinder import breadth
from depthFinder import depth
from customFinder import doubleBread
from dataMaker import randomize
from dataDefault import default

import time

testCase = input("Would you like to randomize or reset the test case? Type RANDOM or RESET if so. ")
if testCase.upper() == "RANDOM":
  nodeCount = int(input("How many IDs should be generated? "))
  randomize(nodeCount)
if testCase.upper() == "RESET":
  default()

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