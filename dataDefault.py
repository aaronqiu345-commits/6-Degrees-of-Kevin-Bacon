def default():
  with open('data.txt', 'w') as data:
    data.write('Movie1|Actor2|Actor3|Actor4|Actor5\n')
    data.write('Movie6|Actor5|Actor7\n')
    data.write('Movie8|Actor7|Actor9\n')
    data.write('Movie10|Actor9|Actor11|Actor12\n')
    data.write('Movie11|Actor7|Actor13|Actor14\n')
  print("Test case reset.")