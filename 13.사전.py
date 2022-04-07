cabinet={3:"유재석",100:"김태호"}#키는 3 / 밸류는 유재석
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))

#print(cabinet.[5]) 할당안된 키는 에러
print(cabinet.get(5)) #할당안된 키를 get으로 호출시 none 반환
print(cabinet.get(5,"사용가능")) #지정된 문구를 출력가능
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet2 = {"A-3":"유재석","B-100":"김태호"}
print(cabinet2["A-3"])
print(cabinet2["B-100"])

print("새 손님")
print(cabinet2)
cabinet2["C-20"]="조세호"
cabinet2["A-23"]="김종국"
print(cabinet2)

print("나간 손님")
del cabinet2["A-3"]
print(cabinet2)

print("Key만 출력")
print(cabinet2.keys())

print("value만 출력")
print(cabinet2.values())

print("key,value 출력")
print(cabinet2.items())

# 목욕탕 폐점
cabinet.clear()
cabinet2.clear()
print(cabinet)
print(cabinet2)
