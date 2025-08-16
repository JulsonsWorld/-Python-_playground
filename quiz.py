import random 

kwestionariusz = {
    "Co niezwykłego jest w odchodach wombatów?": [
        ("Są zielone jak trawa", -0.5),
        ("Mają kształt kostki", +1),
        ("Świecą w ciemności", -0.5)
    ],          

    "Jak porusza się kangur, kiedy idzie powoli (nie skacze)?":[
        ("Chodzi wyłącznie na tylnych łapach",-0.5),
        ("Chodzi na czterech łapach jak pies", -0.5),
        ("Opiera się na ogonie jak na trzeciej nodze", +1)
    ],
    
    "Ile może żyć rekin arktyczny (grenlandzki)?": [
        ("Ponad 400 lat", +1),
        ("Około 150 lat",-0.5),
        ("Do 70 lat",-0.5)
                ],
    
    "Dlaczego kapibary są często pokazywane w towarzystwie innych zwierząt?": [
        ("Są niezwykle spokojne i towarzyskie", +1),
        ("Mają zapach, który przyciąga ptaki",-0.5),
        ("Mimo, że są bardzo hałaśliwe, ale lubią dzielić się jedzeniem z innymi gatunkami", -0.5)
                ],
    
    "Dlaczego kuoka nazywana jest „najsłodszym zwierzęciem świata' ": [
        ("Bo wygląda jakby ciągle się uśmiechała",+1),
        ("Bo ma miękkie futro i fioletowy język",-0.5),
        ("Bo daje się głaskać każdemu człowiekowi",-0.5)
                ],

    "Co pomaga panterze śnieżnej przetrwać w zimnym klimacie?": [
        ("Ma specjalne gruczoły ogrzewające krew",-0.5),
        ("Ma bardzo gęste, grube futro i szerokie łapy",+1),
        ("Zapada w sen zimowy na 3 miesiące",-0.5)
                ],
    
    "Dlaczego alpaki często plują?": [
        ("Aby wyrazić niezadowolenie lub pokazać dominację", +1),
        ("Bo mają za dużo śliny", -0.5),
        ("Bo to sposób, w jaki się porozumiewają z ludźmi", -0.5)
                ],  
   
    "Co wyróżnia żółwia słoniowego z Galapagos?": [
        ("Potrafi pływać z prędkością 20 km/h", -0.5),
        ("Ma miękki pancerz, który zmienia kolor", -0.5),
        ("Jest jednym z największych żółwi lądowych na świecie", +1)
                ], 

    "Jak słonie indyjskie okazują emocje?": [
        ("Przez dotyk, dźwięki i ruchy trąby", +1),
        ("Przez zmianę koloru skóry", -0.5),
        ("Poprzez machanie uszami w różne strony", -0.5)
                ],
    
    "Ile serc ma ośmiornica?" : [
        ("jedno", -0.5),
        ("osiem", -0.5),
        ("trzy", +1)
                ]
}

# Zapytanie o imię gracza
imie = str(input("\nPodaj swoje imię: ")).strip()
if True:
    print(f"\nWitaj, {imie}! Rozpoczynamy quiz.")


punkty = 0

# zamieniamy słownik na listę i tasujemy pytania
pytania = list(kwestionariusz.items())
random.shuffle(pytania)

for pytanie, warianty in pytania:
    print("\n", pytanie)

    # tasujemy odpowiedzi
    warianty = list(warianty)   # kopiujemy listę odpowiedzi (jeśli była krotką)
    random.shuffle(warianty)

    for indeks, wariant in enumerate(warianty, start=1):
        print(indeks, ".", wariant[0])

    wybor_gracza = input(f"{imie}, jaką odpowiedź wybierasz: ")

    while wybor_gracza not in ("1", "2", "3"):
        print("Zły nr odpowiedzi. Wpisz coś z zakresu 1-3")
        wybor_gracza = input("Twój wybór: ")

    indeks_odp = int(wybor_gracza) - 1
    punkty += warianty[indeks_odp][1]
    print("Twoje aktualne punkty:", punkty)