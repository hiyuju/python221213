#demoFile.py

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---정렬을 변경---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(3))

print("---0채우기---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(3))

print("---서식변경---")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:2f}".format(4/3))
print("{0:,}".format(15000000))

#raw string notation 
f=open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()


