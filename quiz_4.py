# 학교에서 파이썬 코딩대회를 개최
# 참석률을 높이기 위해 댓글 이벤트 진행
# 댓글 작성자들 중에 추첨을 통해 1명 치킨, 3명 커피쿠폰
# 추첨 프로그램을 작성하시오

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하된 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용

# 출력예제
# --당점자 발료--
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]
# --축하합니다--

# 활용예제
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

from random import *
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(lst)
shuffle(lst)
# print(lst)
chiken=sample(lst,1)
# print(chiken)
coffee=sample(lst,3)
print("--당첨자 발표--")
print("치킨 당첨자 :",chiken)
print("커피 당첨자 :",coffee)
print("--축하합니다--")

#문제풀이
print("\n")
users = range(1,21)
print(type(users))
users=list(users)
# print(users)
shuffle(users)
# print(users)
winners=sample(users,4)
print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")
