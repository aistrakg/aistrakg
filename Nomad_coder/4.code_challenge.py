# code challenge
# plus, minus, times, dvision, negation, power, reminder

# a = int(input("숫자를 입력하세요"))
# b = int(input("숫자를 입력하세요"))
# def Calculato(a,b):
#     return a+b, a-b, a*b, a/b, -a, a**b, a%b

# print(Calculato(a,b))


def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def times(a,b):
    return a*b
def division(a,b): 
    return a/b
def negation(a,b):
    return -a,-b
def power(a,b):
    return a**b
def reminder(a,b):
    return a%b
print("\n")
print("Start Calculation")
print("\n")
print("1.plus, 2.minus, 3.times, 4.division, 5.negation, 6.power, 7.reminder")
cal=int(input("input type of Calculation :"))
print("\n")
a=int(input("input Number A : "))
print("\n")
b=int(input("input Number b : "))
print("\n")
if cal==1:
    a_result=plus(a,b)
    print(f"{a} Plus {b} is {a_result}") #just tried other way
elif cal==2:
    a_result=minus(a,b)
    print(a_result)
elif cal==3:
    a_result=times(a,b)
    print(a_result)
elif cal==4:
    a_result=division(a,b)
    print(a_result)
elif cal==5:
    a_result=negation(a,b)
    print(a_result)
elif cal==6:
    a_result=power(a,b)
    print(a_result)
elif cal==7:
    a_result=reminder(a,b)
    print(a_result)
