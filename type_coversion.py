#float type to integer type conversion
float_1=float(input("enter the float value"))#the float value is given by user
int_1=int(float_1)#here we are converting float type value into integer value by using int(variable)
print(f"the float value given by user is{ float_1} this converted into integer value {int_1}")

#integer type to string type conversion
integer_1=int(input("enter the integer value"))#the integer value is given by user
str_1=str(integer_1)#here we are converting integer type value into string value by using str(variable)
print(f"the float value given by user is{ integer_1} this converted into string value {str_1}")
print(type(str_1))

#age as input conversion into integer and add5 and print the result
age=input("enter the age")
int_1=int(age)
result=int_1+5
print(f"age entered by user is{age} than that value is converted into integer that is{int_1}after adding 5 to result is{result}")