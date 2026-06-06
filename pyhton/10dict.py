# marks = {
#     "Harry": 100,
#     "Subh": 56,
#     "Rahul": 34
# }

# print(len(marks), type(marks))

# #Q3

# dict = {
#   "table" : ("a piece of furniture", "list of facts & figures"), 
#   "cat" : "a small animal"
# }
# print(dict)

#Q2

stu_marks = {
  
 }
marks1 = str(input("Physics = "))
stu_marks.update({"Physics": marks1})

marks2 = str(input("chemistry = "))
stu_marks.update({"Chemisty": marks2})

marks3 = str(input("maths = "))
stu_marks.update({"Maths": marks3})

print(stu_marks)
