#zadanie 1
# A = [1 - x for x in range(0,11)]
# print(A)
# B = [4 ** x for x in range(0,8)]
# print(B)
# C = [x for x in B if x % 2 == 0]
# print(C)

#zadanie 2
# import random
# lista = []
# for i in range(0,11):
#     lista.append(random.randint(0,20))
# print(lista)
# lista2 = [x for x in lista if x % 2 == 0]
# print(lista2)

#zadanie3
# słownik = {'cola': 'id', 'chleb': 'szt','ziemniaki': 'kg'}
# lista = [a for (a,b) in słownik.items() if b == 'szt']
# print(lista)

#zadanie 4
# def trojkat(a, b, c):
#     if ((a+b>c) and (a+c>b) and (b+c>a)):
#         if ((a*a+b*b==c*c) or (a*a+c*c==b*b) or (b*b+c*c==a*a)):
#             print("To jest trójkąt prostokątny")
#         else:
#             print("Nie można zbudować trójkata")
# trojkat(5, 2, 3)
# trojkat(2, 6, 10)
# trojkat(3, 7, 12)

#zadanie 5
# import math
# def trapez(a = 12, b = 5, h = 4):
#     return ((a + b) * h / 2)
# print(trapez())

#zadanie 6
# def ciąg(a = 1, b = 4, ile=10):
#     wynik = a
#     elementy = []
#     for x in range(ile):
#         x = a + x * b
#         elementy.append(x)
#         wynik *= x
#     print(elementy)
#     return wynik

#zadanie 7
import math
# def ciąg(* a):
#     if len(a) == 0:
#         return 0
#     else:
#         elementy = [x for x in a]
#         iloczyn = 1
#         for x in a:
#             iloczyn *= x
#         return iloczyn

#zadanie 8
# def funkcja(** produkty):
#     ilosc = 0
#     cena = 0
#     for x in produkty:
#         ilosc += 1
#         cena += produkty[x]
#     print('ilosc: ', ilosc)
#     print('cena: ', cena)
# funkcja(słodycze = 2.0, cola = 0.90, szynka = 3.00)

