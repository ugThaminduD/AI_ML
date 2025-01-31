marks = []

for std in range(10):
  mark = float(input(f"Enter mark for student {std+1}: "))
  marks.append(mark)
  
max_mark = max(marks)
min_mark = min(marks)
avg_mark = sum(marks) / len(marks)

print(f"Max mark: {max_mark}")
print(f"Min mark: {min_mark}")
print(f"Average mark: {avg_mark}")
 