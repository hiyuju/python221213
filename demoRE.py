#demoRE.py
import re

result=re.search("[0-9]*th","35th")
print(result)
print(result.group())

#result=re.match("[0-9]*th","35th")
#print(result)
#print(result.group())

result=re.search("apple","this is apple")
print(result.group())

# result=re.match("apple","this is apple")
# print(result.group())

#컴파일 함수 사용
s ="Apple is  big company and apple is very delicious"
#대소문자 구분 안함
c=re.compile("apple", re.I)
print(c.findall(s))

print("--연도 찾기--")
result=re.search("\d{4}","올해는 2022년")
print(result.group())
result=re.search("\d{5}","우리동네는 52300")
print(result.group())