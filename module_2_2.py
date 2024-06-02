first, second , third = int(input("enter first number:")), int(input("enter second number:")), int(input("enter third number:"))
if first == second and first == third: print(3)
elif first == second or first == third or second == third: print(2)
else: print(0)