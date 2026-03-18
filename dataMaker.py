import random
import string

def randomize(count):

  nums = string.digits
  times = count
  ids = set()
  line = []
  lines = []
  lastAct = None

  def addctor(id):
    nonlocal lastAct
    print(f"adding Actor{id}")
    line.append(f"Actor{id}")
    lastAct = f"Actor{id}"

  def addvie(id):
    print(f"adding Movie{id}")
    line.append(f"Movie{id}")

  for x in range(times):
    # digits = ''.join(random.choices(nums, k = digitCount))
    ids.add(x)
  print(ids)

  while len(ids) != 0:
    id = ids.pop() + 1
    print(f"processing id {id}")
    RNG = random.randint(1, 4)
    if len(line) == 0:
      addvie(id)
      if lastAct:
        line.append(lastAct)
    else:
      addctor(id)

    if RNG == 1 and len(line) >= 3 or len(line) == 5:
      lines.append("|".join(line))
      print(f"adding line {line}")
      line = []
      treeRNG = random.randint(1, 2)
      if treeRNG == 1 and len(ids) >= 3:
        print(f"making new branch")
        brancher = lastAct
        branchRNG = random.randint(1, 3)
        for i in range(branchRNG):
          if len(ids) != 0:
            id = ids.pop() + 1
            addvie(id)
            print(f" appending {brancher} to movie")
            line.append(f"{brancher}")
            leafRNG = random.randint(1, 2)
            for i in range(leafRNG):
              if len(ids) != 0:
                id = ids.pop() + 1
                addctor(id)

              else:
                print("ran out of ids while branching")
                print(line)
                lines.append("|".join(line))
                line = []
                break
            lines.append("|".join(line))
            line = []
          else:
            print("ran out of ids while branching")
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