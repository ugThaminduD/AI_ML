
total_sum = 0

print("Enter numbers: ")

while True:
  num = float(input())
  if num == -999:
    break
  total_sum = total_sum + num
    
print("Total sum: ", total_sum)  
  