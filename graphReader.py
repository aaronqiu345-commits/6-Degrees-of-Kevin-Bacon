from grapher import Node, nodeStorage
from collections import deque
visited = []
queue = deque([])
def read(node):
  for connect in nodeStorage[node].neighbors:
    print(f"{node} is connected to {connect.data}")
    visited.append(nodeStorage[node])
    if connect not in visited and connect.data not in queue:
      queue.append(connect.data)
  while len(queue) != 0:
    print(f"|| Queue moving to {queue[0]} ||")
    read(queue.popleft())

read("Movie1")