#사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
#규칙1 : http:// 부분은 제외 => naver.com
#규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
#규칙3 : 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 'e' 갯수 + "!"로 구성
# nav + 5 + 1 + !
#생성된 비밀번호 nav51!

juso="http://daum.com"
slash=juso.index("/")
slash=juso.index("/",slash+1)
print(slash)
dot=juso.index(".")
print(dot)
pass1=juso[slash+1:dot]
print(pass1)
pass2=pass1[0:3]
print(pass2)
pass3=len(pass1)
print(pass3)
pass4=pass1.count("e")
print(pass4)
print("생성된 비밀번호 : {aaa}{bbb}{ccc}{ddd}".format(aaa=pass2,bbb=pass3,ccc=pass4,ddd="!"))

print("\n문제풀이")
url="http://daum.com"
my_str=url.replace("http://","") #규칙1
print(my_str)
my_str=my_str[:my_str.index(".")] #규칙2
print(my_str)
password=my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다.".format(url,password))

print("\n 복습")
juso="http://google.com"#변수선언
name=juso.replace("http://","")#replace로 http://를 공백으로 치환
name=name[:name.index(".")]#첫번째 (.) 앞의 글자까지만 
password=name[:3]+str(len(name))+str(name.count("e"))+"!"#첫세글자, name의 문자수, e의 갯수,
print("{0}의 비밀번호는 {1}입니다.".format(juso,password))
