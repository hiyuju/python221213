#web2.py
from bs4 import BeautifulSoup

#페이지 로딩: 메서드 체인(연속으로 함수, 메서드 호출)
page =open ("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체
soup=BeautifulSoup(page, "html.parser")
#전체
print(soup.prettify())

#<p>태그 전부
#print(soup.find_all("p"))
#print(soup.find("p"))


#print(soup.find_all("p", class_="outer-text"))

#컨텐츠만
for item in soup.find_all("p"):
    title=item.text.strip()
    title=title.replace("\n","")
    print(title)

    