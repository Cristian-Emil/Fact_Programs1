""" Factory Patterns """

class EnglishTranslator:
    translations = {
        "masina": "car",
        "casa": "house",
        "floare": "flower",
        "copac" : "tree",
        "fata": "girl"
    }

    @staticmethod
    def localize(word):
        return EnglishTranslator.translations.get(word, "Translation not available")

class FrenchTranslator:
    translations = {
        "masina": "voiture",
        "casa": "maison",
        "floare": "fleur",
        "gradina" : "jardine",
        "copac": "arbre",
        "fata" : "fille"

    }

    @staticmethod
    def localize(word):
        return FrenchTranslator.translations.get(word, "Translation not available")


class SpanishTranslator:
    translations = {
        "masina": "coche",
        "casa": "casa",
        "floare": "flor",
        "gradina" : "jardin",
        "fata" : "chica",

    }

    @staticmethod
    def localize(word):
        return SpanishTranslator.translations.get(word, "Translation not available")


class Factory:
    @staticmethod
    def get_translator(language):
        if language == "english":
            return EnglishTranslator()
        elif language == "french":
            return FrenchTranslator()
        elif language == "spanish":
            return SpanishTranslator()
        else:
            raise ValueError("Unsupported language")



translator = Factory.get_translator("english")
word = input("Introduceți un cuvânt în limba română: ")
translation = translator.localize(word)
print(f"Traducerea în limba engleză: {translation}")

translator2 = Factory.get_translator("french")
# word = input("Introduceți un cuvânt în limba română: ")
translation = translator2.localize(word)
print(f"Traducerea în limba franceza: {translation}")

translator3 = Factory.get_translator("spanish")
# word = input("Introduceți un cuvânt în limba română: ")
translation = translator3.localize(word)
print(f"Traducerea în limba spaniola: {translation}")

# translator = Factory()
#
# english_trans = translator.get_translator("english")
# spanish_trans = translator.get_translator("spanish")
#
# print(f'In engleza zicem {english_trans.localize("masina")}')
# print(f'In spaniola zicem {spanish_trans.localize("masina")}')


print( " " )