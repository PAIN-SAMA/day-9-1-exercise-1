student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
num = 0
#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  num = int(student_scores[key])
  
  # key = int(student_scores[key])
  if num >= 91 and num <= 100:
    student_grades[key] = "Outstanding"
    # print(key)
  elif num >= 81 and num <= 90:
    student_grades[key] = "Exceeds Expectations"
    # print(key)
  elif num >= 71 and num <= 80: 
    student_grades[key] = "Acceptable"
    # print(key)
  elif num <= 70:
    student_grades[key] = "Fail"
    # print(key)
    
# Hermione, Harry, Ron, Draco, Neville 
# 🚨 Don't change the code below 👇
print(student_grades)





