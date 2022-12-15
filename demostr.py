#demoStr.py

print("--공백문자 제거--")
u="<<<spam and ham>>>"
result=u.strip("<>")
print(u)
print(result)

result=result.replace("spam","spam egg")
print(result)
lst=result.split()
print(lst)
print("---다시 합치기---")
print( ":)".join(lst))

#반복적인 문구
names=["전우치","이순신","박문수"]
for name in names:
    print("="*40)
    print("안녕하세요 {0}님 추운 겨울입니다".format(name))
    print("="*40)