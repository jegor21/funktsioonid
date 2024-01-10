from module1 import *

s=summa3(3.5,2,4.9)
print(s)
a=float(input("arv1: "))
b=float(input("arv2: "))
c=float(input("arv3: "))
s3=summa3=(a,b,c)



#ülesanne 1
v=arithmetic(float(input("arv1: ")),float(input("arv2: ")), input("tehing: "))
print("vastus = ",v)

#ülesanne 2
v=is_year_leap(int(input("sisestage aasta: ")))
print(v)

#ülesanne 3
s,p,d=square(4)
print("pindala",s)
print("ümbermõõt",p)
print("läbimõõt",d)

# #ülesanne 4
v=season(int(input("kuu: ")))
print(v)


#Ülesanne 5
v1=float(input("Sisestage algmakse: "))
v2=int(input("Palju aastad?: "))

t=bank(v1,v2)
print("Lõppsumm on ", round(t,2), "eurot")
#Ülesanne 6

s=is_prime()
print(s)




#Ülesanne 7

d=int(input("Sisestage päev: "))
m=int(input("Sisestage kuu: "))
y=int(input("Sisestage aasta: "))

v=date(d,m,y)

print(v)


#Ülesanne 8


