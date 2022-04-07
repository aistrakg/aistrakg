# print(len("dklsjlfls"))

# age="48"
# print(type(age))
# n_age=int(age)
# print(type(n_age))


# #define fuction = def
# def say_hello():
#     print("hello")
# say_hello()

# def test():
#     name=input("이름을 입력하세요 ")
#     print("당신의 이름은 {0}입니다.".format(name))
# test()

# def say_hello(who):
#     print("hello",who)

# say_hello("KG")


# def plus(a,b):
#     print(a+b)

# plus(2,6)

# def minus(a,b=0):
#     print(a-b)

# minus(6,2)

# def hello(name="anonymous"):
#     print("hello",name)

# hello()
# hello("KG")

#return
# def p_plus(a,b):
#     return (a+b)
# def r_plus(a,b):
#     return a+b

# p_result=p_plus(3,3)
# r_result=r_plus(2,3)

# print(p_result,r_result) 

# def plus(a,b):
#     return a+b

# result=plus(2,4)
# print(result)

def hello(name,age,nation,food):
    return f"이름은 {name} 이구요 나이는 {age} 입니다. {nation}에서 왔구 {food}를 좋아합니다."

hi=hello(name="KG",age=48,nation="한국",food="라면")
hi2=hello(name="teddy",age=48,nation="한국",food="오뎅")
print (hi)
print (hi2)
