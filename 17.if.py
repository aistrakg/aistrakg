weather ="비"
# weather = input("오늘 날씨는 어때요? ") input 사용시 string으로 입력됨
if weather == "비" or "눈":
# if weather == "비" or  weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp=int(input("기온이 어때요? ")) #숫자 입력시 int로 묶어줌
if 30<= temp:
    print("너무 더워요. 나가지 마세요")
elif 10<= temp and temp <30:
    print("괜찬은 날씨에요")
elif 0<= temp <10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지 마세요")
    10