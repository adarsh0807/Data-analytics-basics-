'''
x = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

n = int(input("Enter number = "))

i = 0

while i < len(x):
  if (x[i] == n):
    print("FOUND")
    break

  else:
    print("Finding.....")

  i += 1  

print("end of loop")

'''
i = 1
while i <= 10:
  if i % 2 != 0:
    i += 1
    continue
  print(i)
  i += 1