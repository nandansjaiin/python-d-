a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
fn = input("Enter a function, you want to perform (+,-,*,/):")
sum1 = a+b
diff = a-b
multi = a*b
div = a/b
if "+":
    print(sum1)
elif "-":
    print(diff)
elif "*":
    print(multi)
elif "/":
    print(div)
else:
    print("Invalid function")