#function2.py
def setValue(newValue):
    #지역변수
    x=newValue
    print(x)

#호출
#디버깅 중단점
retValue=setValue(10)
print(retValue)

#함수정의
def swap(x,y):
    return y,x

#호출
print(swap(3,4))