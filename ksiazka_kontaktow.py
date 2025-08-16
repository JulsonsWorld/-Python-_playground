import json
import os

if os.path.exists("plik_z_danymi.json"):
    with open("plik_z_danymi.json", "r", encoding="utf8") as plik_json:
                kontakty = json.load(plik_json)
else:
     kontakty = {}



# Książka adresowa
# kontakty = {
#     "Kasia": "kasia@wp.pl",
#     "Basia": "basia@tolubi.pl",
#     "Brad" : "bradpitt@onet.pl"   
   
# }


while True:
    menu = '''
Menu
    1 - dopisanie pozycji do książki
    2 - aktualizacja pozycji książki
    3 - usunięcie pozycji z książki
    4 - wydruk imion z książki
    5 - wydruk całej książki z kontaktami
    6 - koniec programu
    7 - zapisanie kontaktów
'''
    print(menu)

    wybor = int(input("Podaj numer operacji, którą chcesz wykonać: "))
    if wybor == 1:
        imie = input("Podaj imię: ")
        if imie not in kontakty:
                email = input(f"Podaj email dla kontaktu {imie}: ")
                kontakty[imie] = email
                print("Dodano kontakt.")
        else:
                print("Ta pozycja już istnieje.")
        
    elif wybor == 2:
        imie = input("Podaj imię kontaktu do aktualizacji: ")
        if imie in kontakty:
            nowy_email = input("Podaj nowy e-mail: ")
            kontakty[imie] = nowy_email 
            print("Zaktualizowano kontakt.")
        else:
            print("Nie znaleziono takiego kontaktu.")
    
    elif wybor == 3:
        imie = input("Kogo chcesz usunąć? ")
        if imie in kontakty:
            del kontakty[imie]
            print(f"Usunięto kontakt: {imie}")
        else:
            print("Nie znaleziono takiego kontaktu.")
    
    elif wybor == 4:
        for imie in kontakty:
            print(imie, end=", ")
    
    elif wybor == 5:
        print(kontakty)
    
      
    elif wybor == 6:
        print("Dziękuję za skorzystanie z aplikacji. ")
        decyzja = int(input("Czy zapisać zmiany w pliku? Tak(1)/Nie(2)"))
        if decyzja ==  1:
            with open("plik_z_danymi.json", "w", encoding = "utf8") as plik_json:
                json.dump(
                kontakty,
                plik_json,
                indent=4,
                sort_keys=True,
                ensure_ascii=False,
                )
            print("Zapisano książkę adresową w pliku 'plik_z_danymi'.") 
            break
        else:
             break

    elif wybor == 7:
        with open("plik_z_danymi.json", "w", encoding = "utf8") as plik_json:
            json.dump(
        kontakty,
         plik_json,
        indent=4,
        sort_keys=True,
        ensure_ascii=False,
        )
            print("Zapisano książkę adresową w pliku 'plik_z_danymi'.")