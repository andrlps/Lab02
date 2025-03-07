import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!
    if txtIn.isdigit():
        if int(txtIn)<1 or int(txtIn)>5:
            print("Input invalido\n")
    else:
        print("Input invalido\n")

    if int(txtIn) == 1:
        print()
        while(True):
            parola = input("Ok, quale parola devo aggiungere?\n")
            if parola.startswith("<") and parola.endswith(">") and "> <" in parola:
                break;
            print("Parola non conforme\n")
        t.handleAdd(parola)
        print("Parola aggiunta\n")
    if int(txtIn) == 2:
        print()
        while (True):
            parola = input("Ok, quale parola devo cercare?\n")
            if parola.startswith("<") and parola.endswith(">"):
                break;
            print("Parola non conforme\n")
        parola.lower()
        t.handleTranslate(parola)
    if int(txtIn) == 3:
        print()
        parola = input("Ok, quale parola devo cercare?\n")
        parola.lower()
        while (True):
            parola = input("Ok, quale parola devo cercare?\n")
            if parola.startswith("<") and parola.endswith(">"):
                break;
            print("Parola non conforme\n")
            if parola.count("?") <= 1:
                if parola.count("?") == 0:
                    print(t.handleTranslate(parola))
                else:
                    print(t.handleWildCard(parola))
                break;
            print("Non sono ammessi più di un ?")
    if int(txtIn) == 4:
        print()
        t.stampaDizionario()
    if int(txtIn) == 5:
        break