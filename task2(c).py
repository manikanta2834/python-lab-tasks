
num = int(input("Enter a number: "))

num = abs(num)

count = 0

while num != 0:
    num = num // 10  
    count += 1       

print("Total number of digits is:", count)
