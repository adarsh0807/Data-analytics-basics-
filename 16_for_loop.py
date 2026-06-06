'''
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in x:
  print(val)


sen = "adarsh"

for char in sen:
  if (char == "d"):
    print("d found")
    break
  print(char) 


n = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for sqr in n:
    print(sqr)
'''

range = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 25]

x = 25
i = 0
for val in range:
  if (val == x):
    print("number found at indx", i)
  i += 1  
    