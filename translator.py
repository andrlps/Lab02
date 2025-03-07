from operator import index

from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.dizionario = Dictionary()

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        stringa = ""
        for i in range(30):
            stringa += "-"
        print(stringa+"\n   Translator Alien-Italian   \n"+stringa
            +"\n1. Aggiungi una nuova parola\n2. Cerca una traduzione\n3. Cerca con wild card\n4. Stampa tutto il Dizionario\n5. Exit\n"+stringa+"\n")

    def loadDictionary(self, dict):
        try:
            file = open(dict, "r")
        except FileNotFoundError:
            return
        for line in file:
            word_meaning = line.rstrip().lower().split(" ")
            word = word_meaning[0]
            meaning = word_meaning[1]
            self.dizionario.addWord(word, [meaning])
        file.close()

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parola = entry.lstrip("<").rstrip(">").lower().split("> <")
        word = parola[0]
        meaning = parola[1]
        if not word.isalpha():
            print("Parola non conforme")
            return
        else:
            if " " in meaning:
                meaning = meaning.split(" ")
                for m in meaning:
                    if not m.isalpha():
                        print("Parola non conforme")
                self.dizionario.addWord(word, meaning)
            else:
                self.dizionario.addWord(word, [meaning])

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        query = query.lstrip("<").rstrip(">")
        if not query.isalpha():
            print("Parola non conforme")
            return
        traduzione = self.dizionario.translate(query)
        if traduzione != None:
            for p in traduzione:
                print(p)
        else:
            print("Parola non trovata")

    def handleWildCard(self,query):
        query = query.lstrip("<").rstrip(">")
        traduzione = self.dizionario.translateWordWildCard(query)
        if traduzione != None:
            for p in traduzione:
                print(p)
        else:
            print("Parola non trovata")

    def stampaDizionario(self):
        self.dizionario.__str__()