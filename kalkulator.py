#kalkulator
print("KALKULATOR")
 
def dodawanie(x, y):
   return x + y
 
def odejmowanie(x, y):
   return x - y
 
def mnozenie(x, y):
   return x * y
 
def dzielenie(x, y):
   return x / y

wyjscie = False
while wyjscie == False:
 
    print("::Menu::")
    print("1 - dodawanie")
    print("2 - odejmowanie")
    print("3 - mnozenie")
    print("4 - dzielenie")
    print("5 - wyjscie")
    
 
    choice = input("Wybierz (1/2/3/4/5):")
 
    if choice == '5':
        pytanie = input("Wyjść z programu? (Tak/Nie): ")
        if pytanie == 'Tak':
            wyjscie = True
            print('Koniec programu!')
            exit()
        elif pytanie == 'Nie':
            wyjscie = False
            print('Powrót do programu')
            choice = input("Wybierz (1/2/3/4/5):")
 
    x= float(input("Podaj liczbe: "))
    y = float(input("Podaj liczbe: "))
 
    if choice == '1':
         print(x,"+",y,"=", dodawanie(x,y))
 
    elif choice == '2':
        print(x,"-",y,"=", odejmowanie(x,y))
 
    elif choice == '3':
         print(x,"*",y,"=", mnozenie(x,y))
 
    elif choice == '4':
         print(x,"/",y,"=", dzielenie(x,y))
 
    else:
     print("Wybraleś nieistniejącą opcje!")
