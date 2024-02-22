def loops():
  x = []
  y = 0
  n = int(input())
  while y < n:
    x.append(y)
    y = y+1
  for i in range(len(x)):
    j = x[i]**2
    print(j)

loops()