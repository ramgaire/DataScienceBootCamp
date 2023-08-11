for r in range(6):
  for c in range(5):
    if r ==0 and c in {0,1,2,3,4}:
      print("-", end=" ")

    elif r in {1,2,3,4,5} and c == 2:
      print("|", end=" ")
    else:
      print(" ", end=" ")
  print()
