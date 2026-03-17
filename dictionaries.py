from processor import lines
neighborStorage = {}
for movie in lines:
  neighborStorage[movie[0]] = movie[1:]

for movie in lines:
  for actor in movie[1:]:
    if actor not in neighborStorage:
      neighborStorage[actor] = [movie[0]]
    else:
      neighborStorage[actor].append(movie[0])