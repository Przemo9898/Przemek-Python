# a=6
# b=5
#
# if a > b:
#     print('liczba a wieksza od liczby b:')
# elif a < b:
#     print('liczba a mniejsza od liczby b:')
# else:
#     print('liczby są równe')
#a = input('wczytaj liczba: ')
# print(a)
# print(type(a))
# a = int(a)
# print(type(a))
# a = input('wczytaj pierwszy liczba: ')
# b = input('wczytaj drugi liczba: ')
# c = input('wczytaj trzeci liczba: ')
# d = input('wczytaj czwarty liczba: ')
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# if (a > b) & (c > d):
#     print('liczba a jest od liczby b i liczba c jest wieksza od liczby d')
# else:
#     print('liczba a jest mniejsza od liczby b lub liczba c jest mniejsza od liczby d')
# for a in range(0, 7, 1):
#     print(a)
# lista= ['a', 3, 4, 5.6]
# for a in lista:
#     print(a)
# else:
#     print('wyświetlone zostały elementy z listy')

# licznik = 0
# while licznik != 11:
#     print(licznik)
#     licznik += 1

# lista =[4, 6, 2, 5, 3, 9, 8, 7]
# a = input('Podaj liczbę: ')
# licznik = 0
# while licznik != len(lista):
#     if int(a) - lista[licznik] == 0:
#         print('liczba ' + str(a) + ' - ' + str(lista[licznik]) + ' = 0 ')
#         break
#     else:
#         licznik += 1
# else:
#     print('żadna z wartości nie dała odpowiedniego wyniku')

# lista1 = [4, 6, 3, 2, 7, 9, 5, 1]
# lista2 = [4, 7, 5, 3]
# suma = []
# for a in lista1:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)

# a = input('pierwsza liczba: ')
# b = input('druga liczba: ')
# try:
#     a = int(a)
#     b = int(b)
#     wynik =a / b
#     print(wynik)
# except ZeroDivisionError:
#     print('nie dzieli się przez 0')
# except ValueError:
#     print('nie wczytano liczby całkowitej')
#zad1
sport = {
    'pilka nozna': 1,
    'koszykowka': 2,
    'siatkowka': 3
}
a = input("Wpisz sport: ")
print(sport[a])
#zad2