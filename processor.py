lines = []
with open('data.txt') as data:
  for line in data:
    lines.append(line.strip().split("|"))
print(lines)