degree=int(input("Enter the degree:"))
if degree <=20:
    print("Cold Weather!")
elif degree >20 and degree <=38:
    print("Normal Weather!")
else:
    print("Hot Weather!")
fahernheit=((degree*1.8)+32)
print("The fahrenheit value is=", fahernheit)