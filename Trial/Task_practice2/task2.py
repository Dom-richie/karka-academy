#1
isPython=True
Date_Of_Birth="13-10-2001"
print(isPython)
print(Date_Of_Birth)
#2
a=5
b=10
print(a+b)
#3
r=5
n=3.14
area_of_a_circle=n*r**2
print(area_of_a_circle)
#4
l=10
w=50
area_of_a_rectangle=l*b
print(area_of_a_rectangle)
#5
b=5
h=20
area_of_a_triangle= 1/2 *b * h
print(area_of_a_triangle)
fruits=['apple','orange','mango']
print(fruits[0])
print(fruits[1])
fruits.append("pineapple")
print(fruits)
fruits.insert(1,"banana")
print(fruits)
fruits.remove("mango")
print(fruits)
#6
a=int(input("num1:"))
b=int(input("num2:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#7
a=30
b=20
c=10
d=50
a+=20
b-=10
c*=5
d/=10
print(a,b,c,d)
#8
a=30
b=20
a+=20
b-=10
print(a,b)
#9
a="john"
b="john"
c=5
d=10
print(a==b)
print(a!=b)
print(c>d)
print(c<d)
# 10
marks=20
if marks>40 and marks<60:
    print("average")
elif marks>60 or marks>30:
    print("GOOD")
else:
    print("fail")
#11
a=80
b=20
c=a
a=b
b=c 
print(a,b)
#12
count=0
num=[20,30,40,50,60]
for i in num:
    count+=i
    avg=count/len(num)
    print(avg)
#13
a=50
b=123
c=333
d=5
ee=a+b
ww=ee*c
final=ww/d
print(final) 
#14
tamil=int(input("tamil:"))
english=int(input("english:"))
maths=int(input("maths:"))
science=int(input("science:"))
social=int(input("social:"))
total=tamil+english+maths+science+social
avg=total/5
print(avg)
print(total)