print("a"+"b")
print("a","b")

print("-방법1-")
print("나는 %d살입니다." %20) # %d는 정수
print("나는 %s을 좋아해요" %"파이선") # %s는 문자열
print("Apple은 %c로 시작해요" %"A") # %c는 한 문자만 받는다는 의미
print("-%s로 한번에-")
print("나는 %s살입니다." %20) # %d는 정수
print("나는 %s을 좋아해요" %"파이선") # %s는 문자열
print("Apple은 %s로 시작해요" %"A") # %c는 한 문자만 받는다는 의미
print("-두개 출력-")
print("나는 %s색과 %s색을 좋아해요" %("노란","빨간"))
print("-방법2-")
print("나는 {}살입니다. ".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","노란"))
print("나는 {0}색과 {2}색을 좋아해요".format("파란","노란","검정"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","노란","검정"))
print("-방법3-")
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20,color="노란"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="노란", age=20))
print("-방법4 v3.6이상-")
age=48
color="노란"
print(f"나는 {age}살이며, {color}색을 좋아해요")
