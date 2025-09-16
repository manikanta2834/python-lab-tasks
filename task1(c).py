
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

print("\nUsing AND:")
print("Is a > b AND b > c?")
print((a > b) and (b > c))   

print("\nUsing OR:")
print("Is a > b OR b > c?")
print((a > b) or (b > c))    

print("\nUsing NOT:")
print("Is it NOT true that a > b?")
print(not (a > b))           
