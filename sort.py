n = int(input("Enter the no. of Words:"))
lst = []
if n > 0:
  for i in range(n+1):
    lst.append(input("Enter the elements:"))
  lst.sort(key=len)
  print(lst)
else:
  print("Invalid Input")
