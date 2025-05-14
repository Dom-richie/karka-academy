#1
test=int(input())
if test>0:
    print(test,"-positive")
else:
    print(test,"-negative")
#2
num=int(input())
if num%2==0:
    print(num,"[even]")
else:
    print(num,"[odd]")
#3
a=int(input("enter the number"))
b=int(input("enter the number"))
c=a**b
print(c)
#4
a=int(input("enter the number"))
b=int(input("enter the number"))
if a>b:
    print(a ,"is grater than" ,b)
elif a<b:
    print(b,"is grater than",a)
elif a==b:
    print(a,"is equal to",b)
#5
year=int(input("year"))
if year%4==0 and year%100!=0 or year%400==0:
    print(year,"it is a leap year")
else:
    print(year,"it is not a leap year")
#6
mark=int(input("mark-"))
if mark>=90:
    print(mark,"-A")
elif mark>=80 and mark<90:
    print(mark,"-B")
elif mark>=70 and mark<=79:
    print(mark,"-C")
elif mark<60:
    print(mark,"-fail")
#7
age=int(input("how old are you-"))
if age<16:
    print(age,"-you cant drive")
elif age>=16 and age<=17:
    print(age,"-you can drive but not vote")
elif age>17 and age<24:
    print(age,"-you can vote but rent a car")
elif age>=24:
    print(age,"-you can do pretty much anything")
#8
for i in range (1,101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print(i, "fizz")
    elif i%5==0:
        print(i, "buzz")
    else:
        print(i)
#9
year=int(input("year"))
if year%4==0 and year%100!=0 or year%400==0:
    print(year,"it is a leap year")
else:
    print(year,"it is not a leap year")