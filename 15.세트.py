#집합(set)
#중복안됨, 순서없음

my_set ={1,2,3,3,3}
print(my_set)

print("\n")

java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

#교집합 - java와 python을 모두 할수 있는 사람
print(java&python)
print(java.intersection(python))

#합집합 -java도 할수 있고 python을 할수 있는 개발자
print(java|python)
print(java.union(python))
#순서가 보장되지 않는다

#차집합 java가능 python불가능자
print(java-python)
print(java.difference(python))

#python 할줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 까먹은사람
java.remove("김태호")
print(java)
