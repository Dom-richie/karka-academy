#1
for i in range (1,11):
    print(i)
#2
for i in range (1,21):
    if i%2==0:
        print(i)
#3
for i in range(1,21):
    if i%2!=0:
        print(i)
#4
factorial=[]
for i in range(6):
    fact=1
    for j in range(1,i+1):
        fact*=j
    factorial.append(fact)
print (factorial)
#5
total=0
for i in range (1,101):
    total+=i
    print(total)
#6
marks=[74,45,86,59,92]
total=0
for i in marks:
    total+=i
    avg=total/len(marks)
    print(avg)
#7
n=5
w=30
for i in range(n):
    row=""
    for j in range(w):
      row+="*"
    print(row)
#8
for i in range (1,6):
    print(i)
#9
num=list(range(1,101))
for i in range(10):
    print(num[i])
#10
marks=[10,30,20,60,10]
if marks[0]==marks[-1]:
        print(True)
else:
        print(False)
#11
for i in range (1,450):
        if i%5==0:
                print(i)
#12
a="h"
if (a=="a" or a=="e" or a=="i" or a=="o" or a=="u"):
        print(a,"vowel")
else:
        print(a,"constant")
#13
even=[]
odd=[]
for i in  range (10,56):

    if i%2==0:
        even.append(i)
    else :
        odd.append(i)
print("even numbers-",len(even))
print("odd numbers-",len(odd))
print(even)
#14
for i in  range(1,26):
    if i%5!=0:
        print(i)
#15
n=[1,2,3,4,5]
factorial=[]
for i in n:
    fact=1
    for j in range(1,i+1):
        fact*=j
    factorial.append(fact)
print (factorial)
#16
n=1
for i in range(1,11):
    n*=i
    print(n)
n=0
for i in range (1,101):
    n+=i
    print(n)
#17
a=10
b=5
if a>b:
     print(a,"a is greater")
else:
     print(b,"is greater")
#18
a=10
b=2
c=5
if a>b and a>c:
    print(a,"is greater")
elif b>a and b>c:
    print(b,"is greater")
else:
    print(c,"is greater")
#19
positive_numbers=[]
negative_numbers=[]
list=[23,4,23,-9,21,3,-45,-8]
for i in list:
    if i>=0:
        positive_numbers.append(i)
    elif i<0:
        negative_numbers.append(i)
print("positive numbers",positive_numbers)
print("negative numbers",negative_numbers)
