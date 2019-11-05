import json

class LanguagePacket:
    def __init__(self, Archive="LanguagePacket.json"):
        self.NameLanguagePack = Archive
    def DictLanguage (self):
        PackLang = open(self.NameLanguagePack, 'r')
        UseLanguage=json.loads(PackLang.readline())
        PackLang.close()
        return UseLanguage