python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index=python.index("n")
print(index)
index=python.index("n",index + 1)
print(index)

print(python.find("Java"))
print(python.find("is"))
print(python.find("Python"))
#print(python.index("Java"))
#index는 없는 문자열을 찾을때 오류가 발생한다. 

print(python.count("n"))