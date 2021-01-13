def palindrome(lista):
    wynik = list()
    for text in lista:
        if text[::-1] == text:
            wynik.append(True)
        else:
            wynik.append(False)
    return wynik
 
print(palindrome(["auto", "potop", "kawa", "kajak", "rower"]))
