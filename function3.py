#function3.py
#가변형식
wordlist=["J","A","M"]

#함수 정의
def change(x):
    #복사본 생성
    x1=x[:]
    x1[0]="H"
    print("내부:", x1)

#호출
change(wordlist)
print(wordlist)

print("---global키워드---")
g=1
def testScope(a):
    #외부의 전역변수를 맵핑
    #global g
    g=2
    return g+a

#호출
testScope(1)
print("전역변수 g:", g)

#교집합 문자 리턴
def intersect(prelist,postlist):
    result=[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출
print(intersect("HAM","SPAM"))