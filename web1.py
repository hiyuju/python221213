#web1.py
from bs4 import BeautifulSoup

#페이지 로딩
page =open ("c:\\work\\test01.html", "rt", encoding="utf-8").open()
#검색이 용이한 객체
soup=BeautifulSoup(page, "html.parser")
#전체
print(soup.prettify())