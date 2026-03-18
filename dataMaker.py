import random
import string

def randomize(length, count):
  nums = string.digits
  digitCount = length
  times = count
  ids = set()
  line = []
  lines = []
  lastAct = None

  for x in range(times):
    digits = ''.join(random.choices(nums, k = digitCount))
    ids.add(digits)
  print(ids)

  while len(ids) != 0:
    id = ids.pop()
    print(f"processing id {id}")
    rng = random.randint(1, 5)
    print(rng)
    if rng == 1 and len(line) >= 3 or len(line) == 5:
      lines.append("|".join(line))
      print(f"adding line {line}")
      line = []
    else:
      if len(line) == 0:
        print(f"adding {id} as movie")
        line.append(f"Movie_{id}")
        if lastAct:
          line.append(lastAct)
      else:
        print(f"adding {id} as actor")
        line.append(f"Actor_{id}")
        lastAct = f"Actor_{id}"
  if len(line) != 0:
    id = "".join(random.choices(nums, k = digitCount))
    print(f"adding {id} as actor")
    line.append(f"Actor_{id}")
    line.append
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