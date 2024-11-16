woordenboek = {
    "computer":"computer"
}

woord = input("Welk woord wil je vertalen? ")

if woord in woordenboek:
    print(woordenboek[woord])
else:
    print("Dit woord bestaat niet!")