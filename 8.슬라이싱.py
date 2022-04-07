#필요한 정보 가져오기
jumin = "750912-1110312"
print("성별 : " + jumin[7])
print("연 : "+jumin[0:2]) #0부터 2직전까지
print("월 : "+jumin[2:4]) #2부터 4직전까지 
print("일 : "+jumin[4:6]) #4부터 6직전까지

print("생년월일 : "+jumin[0:6])
print("생년월일 : "+jumin[:6]) #처음부터 6직전까지

print("주민번호 뒷 7자리: "+jumin[7:14])
print("주민번호 뒷 7자리: "+jumin[7:])
print("주민번호 뒷 7자리(뒤에서) : "+jumin[-7:])

