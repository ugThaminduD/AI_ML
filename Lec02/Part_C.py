def get_grade(marks):
  if marks > 75:
     return "A"
  elif 75 >= marks >= 65:
     return "B"
  elif 64 >= marks >= 55:   
     return "C"
  elif 54 >= marks >= 45:
     return "S"
  else:
     return "F"


marks = []

for m in range(5):
  mark = float(input(f"Enter mark {m+1}: "))
  marks.append(mark)
  
print("Grades:")
for i, mark in enumerate(marks, 1):
   print(f"Mark {i}: {mark} → Grade: {get_grade(mark)}")
   
  