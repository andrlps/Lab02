class Dictionary:
    def __init__(self):
        self.dizionario = {}

    def addWord(self, word, meaning):
        if not self.dizionario.__contains__(word):
            self.dizionario[word] = []
        for element in meaning:
            if element not in self.dizionario[word]:
                self.dizionario[word].append(element)


    def translate(self, word):
        if self.dizionario.__contains__(word):
            return self.dizionario[word]
        else:
            return None

    def translateWordWildCard(self, word):
        word = list(word.lower())
        posizione = word.index("?")
        word.pop(posizione)
        for key in self.dizionario.keys():
            if len(key) >= (posizione+1):
                lista = list(key)
                lista.pop(posizione)
                if lista == word:
                    return self.dizionario[key]
        print("Parola non trovata")
        return None

    def __str__(self):
        for key in self.dizionario.keys():
            stringa = key+": "
            for meaning in self.dizionario[key]:
                stringa = stringa+" "+meaning
            print(stringa)
        print()