#while 어떤 조건이 만족 할때까지 반복
from operator import index


# customer = "토르"
# index =5
# while index >=1:
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")


# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index))
#     index +=1

customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름을 입력하세요. ")