#Q1
# name = "Addy"
# age = 20

# print("my name is",name,"and I am",age,"years old")

# #Q2
# a = 5
# b = 10
# print(a,b)

# a = 10
# b = 5
# print(a,b)

# #3
# I = 5
# F = 10.5
# S = "Addy"
# B = True
# L = [20,30,40,50]

# print(type(I))
# print(type(F))
# print(type(S))
# print(type(B))
# print(type(L))

# #Q4
# Num = int(input("Enter Number:"))
# numf = float(Num)
# nums = str(Num)

# print(type(Num))
# print(type(numf))
# print(type(nums))


# #Q5
# s = "150"
# a = int(s)
# print(a+50)

# @Q6

# food = ["pizza", "burger", "vadapav", "paneer", "chole"]

# print(food[0])
# food.insert(1,"sevusar")
# food.pop(0)
# print(food)



# #Q7

# color = ("green", "yellow", "red")

# print(type(color))
# print(color[1])


# S = str(input("Enter your mane: "))

# print(S)

# print(S.upper())

# print(S.lower())

# print(S.replace(" ","_"))



# #Q9

# fruit = "banana"
# print(fruit.count("a"))

# #Q10

# S = "adarsh"

# R = S[::-1]

# print(R)


# #Q11

# num1 = int(input("Enter 1st number ="))
# num2 = int(input("Enter 2nd number ="))

# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)


# #Q12

# num = int(input("enter number ="))

# if num % 2 == 0:
#   print("even")

# else:
#   print("odd")

# #Q13

# num1 = int(input("1st number ="))
# num2 = int(input("2nd number ="))

# if num1 > num2:
#   print(num1,"is greater than", num2)

# elif num1 < num2:
#   print(num1,"is less than", num2)

# else:
#   print(num1,"is equal to", num2)



# #Q14

# name = str(input("Enter your name ="))
# college = str(input("Enter your college name ="))
# branch = str(input("Enter your branch ="))

# print("My name is",name,"I am studing in",college,"and my brach is",branch)


# #Q15

# x = int(input("Enter an integer ="))

# if x > 0:
#   print("The number",x,"is positive.")

# elif x < 0:
#   print("The number",x,"is negative.")

# else:
#   print("number is zero.")


# #Q16

# x = int(input("Enter marks ="))

# if x > 100:
#   print("Invalid") 

# elif x >= 90:
#   print("A Grade")

# elif x >= 75:
#   print("B Grade") 

# elif x >= 50:
#   print("C Grade") 

# elif x < 0:
#   print("Invalid")

# else:
#   print("Fail")


# #Q17 
# Username = str(input("Enter username: "))
# Password = int(input("Enter password: "))

# if Username == "admin" and Password == 1234:
#   print("Login successfull")

# else:
#   print("Invalid Username or password")


# #Q18

# def calcu_sum(a, b):
#   sum = a + b
#   print(sum)

# calcu_sum(2, 4)

# #Q18.1

# def calcu_avg(a, b, c):
#   sum = a+b+c
#   avg = sum / 3
#   print(avg)
#   return avg

# calcu_avg(11, 22, 33)

# #Q19

# dict = {
#   "table" : ("a piece of furniture", "list of facts "),
#   "cat" : "a small animal"
# }

# print(type("table"))


# sub = {"pyhton", "java", "C++", "pyhton", "javascript", "java", "pyhton", "java", "C++", "C"}

# print(len(sub))

# print(sub)

# #Q20

# Grade = {}

# subject1 = str(input("Subject name 1 ="))
# marks = int(input("Enter marks ="))
# Grade[subject1] = marks

# print(Grade)

# #Q20.1

# marks = {}

# subject1 = int(input("Physics marks = "))
# marks.update({"Physics" : subject1})

# subject2 = int(input("Chemistry marks = "))
# marks.update({"Chamistry" : subject1})

# subject3 = int(input("Maths marks = "))
# marks.update({"Maths" : subject1})

# print(marks)

# #Q21

# set = {("x",9), ("y",9.0)}
# print(set)

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# n = 36
# i = 0
# for val in list:
#   if val == n:
#     print("found at", i)
#   i += 1  

# for i in range(100,0,-1):
#   print(i)

n = 5

x = 0
for i in range(1, n+1):
  x += i

print(x)