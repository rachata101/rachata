n = int(input("n:"))
for x in range(n):
  test =" "*(n-x)
  for y in range(2*n-1):
      if y<=2*x:
        test += "*"
  print(test)