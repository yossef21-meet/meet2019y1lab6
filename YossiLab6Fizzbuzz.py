n=int(input("enter a number "))
result=[]
for count in range(1,n):
    if count % 3 == 0:
        result.append("Fizz")
    else:
        result.append(count)
