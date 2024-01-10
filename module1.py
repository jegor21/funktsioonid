from random import randint
def summa3(arv1: float, arv2: float, arv3:float)->float:
    """Tagastab kolme arvu summa
    
    :param float arv1: Esimene arv
    :param float arv2: Teine arv
    :param float arv3: Kolmas arv
    :rtype: float



    """
    summa=arv1+arv2+arv3
    return summa

#Ülesanne 1

def arithmetic(a1: float, a2: float, operation: str)->any:
    
    """Lihtne kalkulaator
    +
    -
    *
    /
    :param float a1: Esimene arv
    :param float a2: Teine arv
    :param str operation: aritmeetiline tehing
    :rtype: var Määramata tüüp(float or str)

    """

    if operation in ["+","-","*","/"]:
        if a2==0 and operation=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(a1)+operation+str(a2))
    else:
        vastus="Tundmatu operatsioon"
    return vastus


#Ülesanne 2

def is_year_leap (year: int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab loogilises formaadis tulemus

    """
    if year%4==0:
        v=True
    else:
        v=False
    return v


#Ülesanne 3

def square(a: float):
    """

    """
    S=a**2
    p=4*a
    d=(2)**(1/2)*a
    return "Pindala"+str(S),"Ümbermõõt"+str(p),"Läbimõõt"+str(d)

#Ülesanne 4

def season(aeg: int)->str:
    """

    """
    if aeg in [1,2,12]:
        v="Talv"
    elif aeg in [3,4,5]:
        v="Kevad"
    elif aeg in [6,7,8]:
        v="Suvi"
    elif aeg in [9,10,11]:
        v="Sügis"
    else:
        v="Vale andmed"
    return v


#Ülesanne 5

def bank(a: float, years: int)->float:
    """

    """
    for i in range(years):
        a*=1.1
    return a 



#Ülesanne 6
def is_prime(a=randint(0,1000))->bool:
    """

    """
    print(a)
    v=False
    for i in range(2,a):
        if a%i==0:
            y=True

    return v

#Ülesanne 7

def date(päev: int, kuu: int, aasta: int):
    """

    """

    if päev in range(1, 31) and kuu in [1,3,5,7,8,10,12]:
        v=True
    elif päev in range(1, 29) and kuu == 2 and is_year_leap:
        v=True
    elif päev in range(1, 30) and kuu in [2,4,6,9,11]:
        v=True
    else:
        v=False
    return v


#Ülesanne 8

def XOR_cipher(v, key):
    tet1 = ""
    for i in range(len(v)):
        
        tet11 = chr(ord(v[i]) ^ ord(key[i % len(key)]))
        tet1 += tet11
    
    return tet1

def XOR_uncipher(tet1, key):
    tet2 = ""
    for i in range(len(tet1)):
        
        tet22 = chr(ord(tet1[i]) ^ ord(key[i % len(key)]))
        tet2 += tet22
    
    return tet2



